"""Auditable SQLite registry. Unknowns remain NOT_MEASURED."""
from datetime import datetime, timezone
from pathlib import Path
import json, sqlite3

STATUSES={"NOT_MEASURED","DOCUMENTED","OBSERVED","REPRODUCED","INDEPENDENTLY_VERIFIED"}
EVIDENCE_TYPES={"DOCUMENTATION","DIRECT_OBSERVATION","REPRODUCIBLE_TEST","INDEPENDENT_REVIEW","INFERENCE"}
LICENSE_AREAS={"CODE","MODEL_WEIGHTS","DATASET","OUTPUTS","SERVICE_TERMS","OTHER"}
DOMAINS={"FULL_SONG","BEATMAKING","VOCALS","MIXING","MASTERING","VIDEO","GRAPHICS","ANIMATION","3D","OTHER"}
def now(): return datetime.now(timezone.utc).isoformat()
def required(v,k):
    if not isinstance(v,str) or not v.strip(): raise ValueError(f"{k} must be non-empty")
    return v.strip()
def connect(path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); db=sqlite3.connect(p); db.row_factory=sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.executescript('''CREATE TABLE IF NOT EXISTS capabilities(id TEXT PRIMARY KEY,name TEXT NOT NULL,domain TEXT NOT NULL,description TEXT NOT NULL DEFAULT '',source_url TEXT NOT NULL,source_version TEXT NOT NULL,source_revision TEXT NOT NULL DEFAULT '',implementation_status TEXT NOT NULL DEFAULT 'NOT_MEASURED',created_at TEXT NOT NULL,updated_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS evidence(id INTEGER PRIMARY KEY,capability_id TEXT NOT NULL REFERENCES capabilities(id),evidence_type TEXT NOT NULL,claim TEXT NOT NULL,artifact_uri TEXT NOT NULL DEFAULT '',artifact_sha256 TEXT NOT NULL DEFAULT '',test_environment TEXT NOT NULL DEFAULT '',result TEXT NOT NULL DEFAULT 'NOT_MEASURED',observed_at TEXT NOT NULL,reviewer TEXT NOT NULL DEFAULT '',notes TEXT NOT NULL DEFAULT '');
    CREATE TABLE IF NOT EXISTS licenses(id INTEGER PRIMARY KEY,capability_id TEXT NOT NULL REFERENCES capabilities(id),area TEXT NOT NULL,license_name TEXT NOT NULL DEFAULT 'UNKNOWN',license_url TEXT NOT NULL DEFAULT '',commercial_use TEXT NOT NULL DEFAULT 'NOT_MEASURED',redistribution TEXT NOT NULL DEFAULT 'NOT_MEASURED',notes TEXT NOT NULL DEFAULT '',observed_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS dependencies(capability_id TEXT NOT NULL REFERENCES capabilities(id),depends_on_id TEXT NOT NULL REFERENCES capabilities(id),dependency_type TEXT NOT NULL DEFAULT 'RUNTIME',notes TEXT NOT NULL DEFAULT '',PRIMARY KEY(capability_id,depends_on_id),CHECK(capability_id != depends_on_id));
    CREATE TABLE IF NOT EXISTS benchmarks(id INTEGER PRIMARY KEY,capability_id TEXT NOT NULL REFERENCES capabilities(id),benchmark_name TEXT NOT NULL,test_case TEXT NOT NULL DEFAULT '',hardware TEXT NOT NULL DEFAULT 'NOT_MEASURED',software_versions TEXT NOT NULL DEFAULT '',duration_ms REAL,quality_metrics TEXT NOT NULL DEFAULT '{}',outcome TEXT NOT NULL DEFAULT 'NOT_MEASURED',artifact_uri TEXT NOT NULL DEFAULT '',artifact_sha256 TEXT NOT NULL DEFAULT '',run_at TEXT NOT NULL,notes TEXT NOT NULL DEFAULT '');''')
    return db
def register_capability(db,x):
    cid=required(x.get('id'),'id'); name=required(x.get('name'),'name'); domain=required(x.get('domain'),'domain').upper()
    if domain not in DOMAINS: raise ValueError('invalid domain')
    url=required(x.get('source_url'),'source_url'); version=required(x.get('source_version'),'source_version'); status=x.get('implementation_status','NOT_MEASURED')
    if status not in STATUSES: raise ValueError('invalid implementation_status')
    t=now(); db.execute('''INSERT INTO capabilities VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET name=excluded.name,domain=excluded.domain,description=excluded.description,source_url=excluded.source_url,source_version=excluded.source_version,source_revision=excluded.source_revision,implementation_status=excluded.implementation_status,updated_at=excluded.updated_at''',(cid,name,domain,x.get('description',''),url,version,x.get('source_revision',''),status,t,t))
def add_evidence(db,x):
    typ=required(x.get('evidence_type'),'evidence_type').upper(); result=x.get('result','NOT_MEASURED').upper()
    if typ not in EVIDENCE_TYPES: raise ValueError('invalid evidence_type')
    if result not in STATUSES|{'PASS','FAIL','INCONCLUSIVE'}: raise ValueError('invalid evidence result')
    c=db.execute('INSERT INTO evidence(capability_id,evidence_type,claim,artifact_uri,artifact_sha256,test_environment,result,observed_at,reviewer,notes) VALUES(?,?,?,?,?,?,?,?,?,?)',(required(x.get('capability_id'),'capability_id'),typ,required(x.get('claim'),'claim'),x.get('artifact_uri',''),x.get('artifact_sha256',''),x.get('test_environment',''),result,x.get('observed_at') or now(),x.get('reviewer',''),x.get('notes',''))); return c.lastrowid
def add_license(db,x):
    area=required(x.get('area'),'area').upper()
    if area not in LICENSE_AREAS: raise ValueError('invalid license area')
    c=db.execute('INSERT INTO licenses(capability_id,area,license_name,license_url,commercial_use,redistribution,notes,observed_at) VALUES(?,?,?,?,?,?,?,?)',(required(x.get('capability_id'),'capability_id'),area,x.get('license_name','UNKNOWN'),x.get('license_url',''),x.get('commercial_use','NOT_MEASURED'),x.get('redistribution','NOT_MEASURED'),x.get('notes',''),x.get('observed_at') or now())); return c.lastrowid
def add_dependency(db,capability_id,depends_on_id,dependency_type='RUNTIME',notes=''):
    db.execute('INSERT INTO dependencies VALUES(?,?,?,?)',(required(capability_id,'capability_id'),required(depends_on_id,'depends_on_id'),required(dependency_type,'dependency_type'),notes))
def add_benchmark(db,x):
    outcome=x.get('outcome','NOT_MEASURED').upper(); duration=x.get('duration_ms')
    if outcome not in {'NOT_MEASURED','PASS','FAIL','INCONCLUSIVE'}: raise ValueError('invalid outcome')
    if duration is not None and (not isinstance(duration,(int,float)) or duration<0): raise ValueError('duration_ms must be non-negative or null')
    c=db.execute('INSERT INTO benchmarks(capability_id,benchmark_name,test_case,hardware,software_versions,duration_ms,quality_metrics,outcome,artifact_uri,artifact_sha256,run_at,notes) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(required(x.get('capability_id'),'capability_id'),required(x.get('benchmark_name'),'benchmark_name'),x.get('test_case',''),x.get('hardware','NOT_MEASURED'),x.get('software_versions',''),duration,json.dumps(x.get('quality_metrics',{}),sort_keys=True),outcome,x.get('artifact_uri',''),x.get('artifact_sha256',''),x.get('run_at') or now(),x.get('notes',''))); return c.lastrowid
def report(db):
    caps=[dict(r) for r in db.execute('SELECT * FROM capabilities ORDER BY id')]
    for c in caps:
        for key,sql in [('evidence','SELECT * FROM evidence WHERE capability_id=? ORDER BY id'),('licenses','SELECT * FROM licenses WHERE capability_id=? ORDER BY id'),('dependencies','SELECT depends_on_id,dependency_type,notes FROM dependencies WHERE capability_id=? ORDER BY depends_on_id'),('benchmarks','SELECT * FROM benchmarks WHERE capability_id=? ORDER BY id')]: c[key]=[dict(r) for r in db.execute(sql,(c['id'],))]
        for b in c['benchmarks']: b['quality_metrics']=json.loads(b['quality_metrics'])
    counts={s:0 for s in STATUSES}
    for r in db.execute('SELECT implementation_status,COUNT(*) n FROM capabilities GROUP BY implementation_status'): counts[r['implementation_status']]=r['n']
    return {'schema_version':'1.0','generated_at':now(),'capability_count':len(caps),'status_counts':counts,'capabilities':caps}
def export_report(db,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(report(db),indent=2,sort_keys=True)+'\n',encoding='utf-8')
