import tempfile,unittest
from pathlib import Path
from manifex_cci.registry import connect,register_capability,add_evidence,add_license,add_benchmark,add_dependency,report
CAP={'id':'MUSIC-GEN-001','name':'Full-song generation','domain':'FULL_SONG','description':'Initial investigation target','source_url':'NOT_MEASURED','source_version':'NOT_MEASURED'}
class RegistryTests(unittest.TestCase):
 def setUp(self): self.tmp=tempfile.TemporaryDirectory(); self.db=connect(Path(self.tmp.name)/'test.sqlite3'); register_capability(self.db,CAP)
 def tearDown(self): self.db.close(); self.tmp.cleanup()
 def test_defaults_not_measured(self): self.assertEqual(self.db.execute('SELECT implementation_status FROM capabilities').fetchone()[0],'NOT_MEASURED')
 def test_invalid_domain_rejected(self):
  with self.assertRaises(ValueError): register_capability(self.db,{**CAP,'id':'BAD','domain':'INVALID'})
 def test_evidence_types_distinct(self):
  add_evidence(self.db,{'capability_id':CAP['id'],'evidence_type':'INFERENCE','claim':'Likely supports songs'}); add_evidence(self.db,{'capability_id':CAP['id'],'evidence_type':'REPRODUCIBLE_TEST','claim':'Test executed','result':'PASS'})
  self.assertEqual(self.db.execute('SELECT evidence_type FROM evidence ORDER BY id').fetchall()[0][0],'INFERENCE')
 def test_license_areas_separate(self):
  add_license(self.db,{'capability_id':CAP['id'],'area':'CODE','license_name':'MIT'}); add_license(self.db,{'capability_id':CAP['id'],'area':'MODEL_WEIGHTS'}); self.assertEqual(self.db.execute('SELECT COUNT(*) FROM licenses').fetchone()[0],2)
 def test_benchmark_unknowns(self):
  add_benchmark(self.db,{'capability_id':CAP['id'],'benchmark_name':'baseline'}); self.assertEqual(self.db.execute('SELECT outcome FROM benchmarks').fetchone()[0],'NOT_MEASURED')
 def test_dependency_and_report(self):
  register_capability(self.db,{**CAP,'id':'MASTER-001','name':'Mastering','domain':'MASTERING'}); add_dependency(self.db,'MASTER-001',CAP['id']); r=report(self.db); self.assertEqual(r['capability_count'],2); self.assertEqual(r['status_counts']['NOT_MEASURED'],2)
 def test_self_dependency_rejected(self):
  with self.assertRaises(Exception): add_dependency(self.db,CAP['id'],CAP['id'])
if __name__=='__main__': unittest.main()
