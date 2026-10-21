import re,json,difflib,unicodedata,urllib.request,urllib.parse,time,sys
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
cv=json.load(open('cv.json')); sch=json.load(open('scholar.json'))
def fuzzy_dedup(items,key):
    res=[]
    for it in items:
        n=norm(key(it)); dup=None
        for r in res:
            if (it.get('doi') and it.get('doi','').lower()==r.get('doi','').lower()) or difflib.SequenceMatcher(None,n,norm(key(r))).ratio()>=0.85:
                dup=r;break
        if dup:
            dup.setdefault('also_in',[]).append(it['src'])
            for f in ('summary','doi'):
                if len(it.get(f,'') or '')>len(dup.get(f,'') or ''): dup[f]=it[f]
        else: res.append(it)
    return res
arts=fuzzy_dedup(cv['articles'],lambda x:x['title'])
projs=fuzzy_dedup(cv['projects'],lambda x:x['name'])
# Scholar journal-only additions
for t in ['Transformer-Based Modeling of Directed Transfer Entropy','Identificación automática de perturbaciones en calidad de energía','Estimación de características relevantes para el monitoreo de condición de motores']:
    r=next(x for x in sch if x['title'].startswith(t))
    if max(difflib.SequenceMatcher(None,norm(r['title']),norm(a['title'])).ratio() for a in arts)<0.85:
        arts.append(dict(src='scholar',kind='Publicado en revista especializada',title=r['title'],authors=[r['authors']],journal=r['venue'],year=r['year'],doi=''))
# scholar citations
for a in arts:
    best=max(sch,key=lambda r:difflib.SequenceMatcher(None,norm(r['title']),norm(a['title'])).ratio())
    if difflib.SequenceMatcher(None,norm(best['title']),norm(a['title'])).ratio()>=0.85: a['scholar_cites']=best['cites']; a['in_scholar']=True
print(len(arts),len(projs),file=sys.stderr)
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'bancoLIA/1.0'}),timeout=30))
        except Exception as e: time.sleep(2)
def inv(ix):
    if not ix: return ''
    w=[(p,k) for k,ps in ix.items() for p in ps]; return ' '.join(k for p,k in sorted(w))
for i,a in enumerate(arts):
    w=None
    if a['doi'] and a['doi'].startswith('10.'):
        w=get('https://api.openalex.org/works/doi:'+urllib.parse.quote(a['doi']))
    if not w:
        r=get('https://api.openalex.org/works?per-page=3&search='+urllib.parse.quote(a['title'][:200]))
        if r and r.get('results'):
            c=r['results'][0]
            if difflib.SequenceMatcher(None,norm(c.get('title') or ''),norm(a['title'])).ratio()>=0.85: w=c
    if w:
        a['abstract']=inv(w.get('abstract_inverted_index')); a['openalex']=w.get('id')
        if not a['doi'] and w.get('doi'): a['doi']=w['doi'].replace('https://doi.org/','')
        a['concepts']=[t['display_name'] for t in (w.get('topics') or [])[:3]]
        a['keywords']=[k['display_name'] for k in (w.get('keywords') or [])[:6]]
        a['cited_by']=w.get('cited_by_count')
        a['all_authors']=[x['author']['display_name'] for x in w.get('authorships',[])]
        src=(w.get('primary_location') or {}).get('source') or {}
        if src.get('display_name'): a['journal_oa']=src['display_name']
    if i%25==0: print(i,file=sys.stderr)
    time.sleep(0.12)
json.dump(dict(articles=arts,projects=projs),open('merged.json','w'),ensure_ascii=False,indent=1)
print('abstracts',sum(1 for a in arts if a.get('abstract')),'/',len(arts),file=sys.stderr)
