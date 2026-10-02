import json
docs=[('models/XBeach/raw/manuals/pdfs/XBeach_manual_kingsday.pdf',141,'XBeach_manual_kingsday'),
      ('models/XBeach/raw/manuals/pdfs/XBeach_manual_master.pdf',145,'XBeach_manual_master'),
      ('models/XBeach/raw/manuals/reports/non-hydrostatic_report_draft.pdf',69,'non-hydrostatic_report_draft'),
      ('models/XBeach/raw/manuals/reports/Parallellization_report.pdf',14,'Parallellization_report'),
      ('_staging/recovery/extract/XBeach/office/curvilinear grid properties.pdf',19,None),
      ('_staging/recovery/extract/XBeach/office/adapted_front_0.pdf',1,None)]
jobs=[]
for path,n,ext in docs:
    step=18
    a=1
    while a<=n:
        b=min(n,a+step-1)
        if n-b<6: b=n
        out='_staging/recovery/read/XBeach/'+path.split('/raw/')[-1] if '/raw/' in path else '_staging/recovery/read/XBeach/office-converted/'+path.split('/')[-1]
        jobs.append(dict(path=path,total=n,a=a,b=b,out=f'{out}/p{a:03d}-{b:03d}.md',ext=ext))
        a=b+1
json.dump(jobs,open('pdfjobs.json','w'),indent=0)
for i,j in enumerate(jobs,1): print(i,j['out'],j['a'],j['b'])
