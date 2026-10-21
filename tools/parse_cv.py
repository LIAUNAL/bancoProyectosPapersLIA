import re,json,sys,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
out={'articles':[],'projects':[]}
for c,(a0,a1,p0) in {'0001330950':(1451,3948,4434),'0000043222':(4782,9297,10875)}.items():
    L=open(f'raw/cv_{c}.txt').read().split('\n')
    arts='\n'.join(L[a0:a1]).split('Producción bibliográfica - Artículo')[1:]
    for a in arts:
        kind=a.split('\n')[0].strip(' -')
        t=re.search(r'"(.+?)"\s*\n',a,re.S)
        if not t: continue
        title=re.sub(r'\s+',' ',t.group(1)).strip()
        pre=a[:t.start()]; authors=[x.strip(' ,') for x in pre.split('\n')[1:] if x.strip(' ,')]
        post=a[t.end():].split('\n'); post=[x.strip() for x in post if x.strip()]
        journal=post[1] if len(post)>1 else ''
        yr=re.search(r',\s*((19|20)\d\d)\s*,',a); doi=re.search(r'DOI:\s*(\S+)',a)
        d=doi.group(1).strip() if doi else ''
        d=re.sub(r'^(https?://(dx\.)?doi\.org/|doi:)','',d,flags=re.I)
        out['articles'].append(dict(src=c,kind=kind,title=title,authors=authors,journal=journal,year=yr.group(1) if yr else '',doi=d))
    proj='\n'.join(L[p0:]).split(' Tipo de proyecto:')[1:]
    for p in proj:
        ls=[x.strip() for x in p.split('\n')]
        ptype=ls[0]; name=ls[1]
        ini=re.search(r'Inicio:\s*(\w+)?\s*\n\s*(\d{4})',p); fin=re.search(r'Fin( proyectado)?:\s*(\w+)?\s*\n\s*(\d{4})',p)
        res=p.split('Resumen',1)[1].strip() if 'Resumen' in p else ''
        out['projects'].append(dict(src=c,type=ptype,name=name,start=ini.group(2) if ini else '',end=fin.group(3) if fin else '',summary=res))
print(len(out['articles']),len(out['projects']))
# dedup
def dd(items,key):
    seen={};res=[]
    for it in items:
        k=norm(key(it))[:90]
        if k in seen:
            seen[k].setdefault('also_in',[]).append(it['src']); 
            if len(it.get('summary',''))>len(seen[k].get('summary','')): seen[k]['summary']=it['summary']
            if not seen[k].get('doi') and it.get('doi'): seen[k]['doi']=it['doi']
            continue
        seen[k]=it;res.append(it)
    return res
out['articles']=dd(out['articles'],lambda x:x['title']); out['projects']=dd(out['projects'],lambda x:x['name'])
print(len(out['articles']),len(out['projects']))
json.dump(out,open('cv.json','w'),ensure_ascii=False,indent=1)
