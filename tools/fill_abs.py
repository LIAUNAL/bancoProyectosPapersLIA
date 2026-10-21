import json,urllib.request,urllib.parse,time,re,sys,difflib
d=json.load(open('merged.json'))
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'bancoLIA/1.0'}),timeout=30))
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            time.sleep(3)
        except Exception: time.sleep(3)
n=0
for a in d['articles']:
    if a.get('abstract'): continue
    ab=''
    if a.get('doi','').startswith('10.'):
        r=get('https://api.crossref.org/works/'+urllib.parse.quote(a['doi']))
        if r: ab=re.sub(r'<[^>]+>',' ',r['message'].get('abstract','') or '')
    if not ab:
        q='https://api.semanticscholar.org/graph/v1/paper/'+('DOI:'+a['doi'] if a.get('doi','').startswith('10.') else 'search/match?query='+urllib.parse.quote(a['title'][:200]))
        r=get(q+('&' if '?' in q else '?')+'fields=title,abstract,tldr')
        if r:
            if 'data' in r: r=r['data'][0] if r['data'] else {}
            ab=r.get('abstract') or ((r.get('tldr') or {}).get('text') or '')
        time.sleep(1.1)
    if ab: a['abstract']=re.sub(r'\s+',' ',ab).strip(); n+=1
print('filled',n,'total',sum(1 for a in d['articles'] if a.get('abstract')),len(d['articles']))
json.dump(d,open('merged.json','w'),ensure_ascii=False,indent=1)
