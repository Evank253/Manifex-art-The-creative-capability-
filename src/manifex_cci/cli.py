import argparse,json,sqlite3
from pathlib import Path
from .registry import connect,register_capability,add_evidence,add_license,add_benchmark,add_dependency,export_report
def main():
 p=argparse.ArgumentParser(prog='cci'); p.add_argument('--db',default='data/cci.sqlite3'); s=p.add_subparsers(dest='cmd',required=True)
 for n in ('register','evidence','license','benchmark'):
  q=s.add_parser(n); q.add_argument('json_file')
 q=s.add_parser('dependency'); q.add_argument('capability_id'); q.add_argument('depends_on_id'); q.add_argument('--type',default='RUNTIME'); q.add_argument('--notes',default='')
 q=s.add_parser('report'); q.add_argument('--output',default='reports/cci-report.json')
 a=p.parse_args(); db=connect(a.db)
 try:
  if a.cmd=='register': register_capability(db,json.loads(Path(a.json_file).read_text()))
  elif a.cmd=='evidence': add_evidence(db,json.loads(Path(a.json_file).read_text()))
  elif a.cmd=='license': add_license(db,json.loads(Path(a.json_file).read_text()))
  elif a.cmd=='benchmark': add_benchmark(db,json.loads(Path(a.json_file).read_text()))
  elif a.cmd=='dependency': add_dependency(db,a.capability_id,a.depends_on_id,a.type,a.notes)
  elif a.cmd=='report': export_report(db,a.output); print('Report written:',a.output)
  db.commit()
  if a.cmd!='report': print(a.cmd+': recorded')
 except (ValueError,sqlite3.IntegrityError,json.JSONDecodeError,OSError) as e: db.rollback(); p.exit(2,'cci: error: '+str(e)+'\n')
 finally: db.close()
if __name__=='__main__': main()
