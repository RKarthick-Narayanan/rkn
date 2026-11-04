#!/usr/bin/env python3
"""Check source structure, links, metadata and publication completeness (not browser QA)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from collections import Counter
import json,re
ROOT=Path(__file__).resolve().parents[1]
VOID=set('area base br col embed hr img input link meta param source track wbr'.split())
errors=[]
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__(convert_charrefs=True);self.path=path;self.stack=[];self.tags=Counter();self.ids=[];self.links=[];self.attrs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags[tag]+=1;self.attrs.append((tag,a))
  if 'id' in a:self.ids.append(a['id'])
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
  if tag not in VOID:self.stack.append(tag)
  if tag=='section' and 'section' in self.stack[:-1]:errors.append(f'{self.path.name}: unexpectedly nested section')
  if tag=='a' and 'a' in self.stack[:-1]:errors.append(f'{self.path.name}: nested anchor')
 def handle_endtag(self,tag):
  if not self.stack or self.stack[-1]!=tag:errors.append(f'{self.path.name}: unexpected </{tag}> after {self.stack[-1:]}')
  elif self.stack:self.stack.pop()
 def handle_startendtag(self,tag,attrs):
  self.handle_starttag(tag,attrs)
  if tag not in VOID:self.handle_endtag(tag)
pages={}
for path in sorted(list(ROOT.glob('*.html'))+list(ROOT.glob('*.htm'))):
 p=Page(path);p.feed(path.read_text());pages[path.name]=p
 if p.stack:errors.append(f'{path.name}: unclosed tags {p.stack}')
 for tag in ['html','head','body','main','h1','title']:
  if p.tags[tag]!=1:errors.append(f'{path.name}: {p.tags[tag]} {tag} tags')
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{path.name}: duplicate IDs')
 if not any(t=='html' and a.get('lang')=='en' for t,a in p.attrs):errors.append(f'{path.name}: missing language')
 if not any(t=='meta' and a.get('name')=='description' and a.get('content') for t,a in p.attrs):errors.append(f'{path.name}: missing description')
 if not any(t=='a' and a.get('class')=='skip-link' for t,a in p.attrs):errors.append(f'{path.name}: missing skip link')
 if any(t=='img' and 'alt' not in a for t,a in p.attrs):errors.append(f'{path.name}: image alt missing')
 nav=[a.get('href') for t,a in p.attrs if t=='a' and a.get('href') in ['index.html','research.html','projects.html','publications.html','about.html','contact.html']]
 for n in ['index.html','research.html','projects.html','publications.html','about.html','contact.html']:
  if n not in nav:errors.append(f'{path.name}: missing navigation to {n}')
link_count=0;external=set()
for name,p in pages.items():
 for link in p.links:
  parsed=urlsplit(link)
  if parsed.scheme in ['https','http']:external.add(link);continue
  if parsed.scheme:continue
  link_count+=1
  if not link or link=='#':errors.append(f'{name}: empty link');continue
  if link.startswith('/'):errors.append(f'{name}: root-relative link breaks /rkn/: {link}')
  target=unquote(parsed.path) or name
  if not (ROOT/target).is_file():errors.append(f'{name}: missing target {link}');continue
  if parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:errors.append(f'{name}: missing fragment {link}')
ledger=json.loads((ROOT/'content/publications.json').read_text())
public=[a['data-publication'] for t,a in pages['publications.html'].attrs if 'data-publication' in a]
if len(public)!=16 or set(public)!={p['id'] for p in ledger}:errors.append('Publication ledger mismatch')
if Counter(p['id'][0] for p in ledger)!=Counter({'B':2,'J':5,'C':1,'P':5,'R':3}):errors.append('Publication categories mismatch')
if any('HOLD' in (ROOT/n).read_text() or 'CHECK' in (ROOT/n).read_text() for n in pages):errors.append('Editorial flags leaked into public HTML')
# Check actual palette values against WCAG normal-text contrast, independently of design claims.
def lum(hex):
 c=[int(hex[i:i+2],16)/255 for i in (1,3,5)]
 c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c]
 return .2126*c[0]+.7152*c[1]+.0722*c[2]
contrast={}
for fg in ['#1F2F35','#24675D','#586B70']:
 for bg in ['#F7F6F2','#FFFFFF']:
  a,b=sorted([lum(fg),lum(bg)]);ratio=(b+.05)/(a+.05);contrast[fg+' / '+bg]=round(ratio,2)
  if ratio<4.5:errors.append(f'Insufficient text contrast {fg} / {bg}: {ratio}')
result={'pages_checked':len(pages),'local_links_checked':link_count,'publication_count':len(public),'text_contrast':contrast,'errors':errors,'browser_qa':'SKIPPED — explicitly waived by user in VS Code session on 12 October 2026','external_urls':sorted(external)}
(ROOT/'docs/qa/static-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='external_urls'},indent=2))
raise SystemExit(bool(errors))
