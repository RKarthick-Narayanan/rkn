#!/usr/bin/env python3
"""Render committed static HTML using the standard library. No runtime build required."""
from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]
spec=(ROOT/'content/design-specification.md').read_text()
pubs=json.loads((ROOT/'content/publications.json').read_text())
EMAIL='karthick.narayanan@outlook.in'
BOOK='Multilinguality, Vitality, and Endangerment: Insights from the Lived Experiences of Multilingual India'
BOOK_URL='https://archive.cambridgescholars.com/product/978-1-0364-5464-7/'
ACL='https://aclanthology.org/2025.fieldmatters-1.7/'
NAV=[('index.html','Home'),('research.html','Research'),('projects.html','Projects & Archives'),('publications.html','Publications'),('about.html','About / CV'),('contact.html','Contact')]
THEMES=[('multilingualism','Multilingualism and language vitality','How multilingual communities organise language use, negotiate social change, and sustain linguistic practices under unequal conditions.'),('documentation','Documentation and verbal art','Recording and studying spoken language, oral traditions, and other forms of linguistic and cultural expression with attention to their social context.'),('digital-archives','Digital archives and data stewardship','Designing and evaluating archives as sites of preservation, access, responsibility, and participation rather than as neutral storage systems.'),('language-resources','Orthographies and language resources','Exploring how community participation, linguistic analysis, and digital tools can support language resources and writing-system choices.')]
def md(s):
 s=html.escape(s)
 s=re.sub(r'\*([^*]+)\*',r'<em>\1</em>',s)
 s=re.sub(r'(https?://[^\s<]+)',lambda m:'<a href="'+m[1].rstrip('.')+'">'+m[1].rstrip('.')+'</a>'+('.' if m[1].endswith('.') else ''),s)
 return s

def quoted_between(start,end):
 return re.findall(r'^> (.+)$',spec.split(start,1)[1].split(end,1)[0],re.M)
def paragraphs(lines): return '\n'.join('<p>'+md(p)+'</p>' for p in lines)
def link(url,label,cls='text-link'):return f'<a class="{cls}" href="{html.escape(url)}">{html.escape(label)} <span aria-hidden="true">↗</span></a>'
def intro(label,title,lead):return f'<header class="page-intro"><p class="eyebrow">{label}</p><h1>{title}</h1><p class="lead">{lead}</p></header>'
def section(title,body,id='',cls=''):
 return f'<section class="section {cls}"'+(f' id="{id}"' if id else '')+f'><h2>{title}</h2>{body}</section>'
def feature():
 return f'''<aside class="featured-book" aria-labelledby="featured-title"><div><p class="eyebrow">Featured scholarship · 2025</p><p class="book-type">Monograph</p><p class="small">Cambridge Scholars Publishing</p></div><div><h2 id="featured-title">{BOOK}</h2><p>Drawing on Toda and Kota experiences in the Nilgiris, this book questions approaches to language endangerment that overlook everyday multilingualism and the structural conditions shaping language choice.</p><p class="small">R. Karthick Narayanan · 2025</p>{link(BOOK_URL,'Book details at the publisher')}</div></aside>'''
def shell(file,title,desc,body,canonical=None,extra=''):
 nav=''.join(f'<li><a href="{url}"'+(' aria-current="page"' if file==url else '')+f'>{label}</a></li>' for url,label in NAV)
 url=canonical or ('https://rkarthick-narayanan.github.io/rkn/'+('' if file=='index.html' else file))
 return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{url}">
  <meta name="theme-color" content="#F7F6F2">
  <link rel="stylesheet" href="assets/css/site.css">
  <script src="assets/js/navigation.js" defer></script>
  {extra}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header"><div class="container header-inner">
  <a class="wordmark" href="index.html">R. Karthick Narayanan</a>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" hidden>Menu <span aria-hidden="true">☰</span></button>
  <nav id="primary-nav" aria-label="Primary"><ul>{nav}</ul></nav>
</div></header>
<main id="main" class="container" tabindex="-1">
{body}
</main>
<footer class="site-footer"><div class="container footer-inner"><div><p class="footer-name">R. Karthick Narayanan</p><a href="mailto:{EMAIL}">{EMAIL}</a></div><div class="footer-meta"><p>© <span data-year>2026</span> R. Karthick Narayanan</p><p>Katravai Patravai</p></div></div></footer>
</body>
</html>
'''
def write(file,title,desc,body,**kwargs):(ROOT/file).write_text('\n'.join(line.rstrip() for line in shell(file,title,desc,body,**kwargs).splitlines())+'\n')

hero_copy=quoted_between('### Hero introduction','### Hero links')[0]
# The full research introduction follows the compact above-the-fold statement.
hero=f'''<header class="hero"><div class="hero-identity"><p class="eyebrow">Linguist · Digital Archivist</p><h1>R. Karthick<br class="desktop-break"> Narayanan</h1><p class="hero-statement">Languages in society.<br>Knowledge in context.<br>Archives for the future.</p><div class="hero-actions">{link('research.html','Explore my research','primary-link')}{link('publications.html','Browse publications')}</div></div><div class="hero-note"><p class="eyebrow">Research & practice</p><p>Language, multilingualism,<br>and the social life of archives.</p><span class="annotation-line" aria-hidden="true"></span><p class="small">Sociolinguistics · Documentation<br>Community-centred stewardship</p></div></header>'''
themes='<div class="themes">'+''.join(f'<article><span class="index-number" aria-hidden="true">0{i}</span><h3><a href="research.html#{id}">{title}</a></h3><p>{text}</p></article>' for i,(id,title,text) in enumerate(THEMES,1))+'</div>'
selected='<div class="selected-list">'+''.join(f'<article><p class="eyebrow">{kind}</p><h3><a href="projects.html#{id}">{title}</a></h3><p>{text}</p></article>' for id,kind,title,text in [('toda-kota','Field research','Toda and Kota in the Nilgiris','Multilingual practices, language choice, and the structural conditions shaping language vitality.'),('sidhela','Archival practice','SiDHELA','Language collections and collaborative approaches to digital archiving in the Sikkim–Darjeeling Himalayas.'),('life-suite','Collaborative scholarship','Field to Model · LiFE Suite','Community-based data collection, linguistic annotation, and language-technology workflows.')])+'</div>'
shortbio=quoted_between('### Short formal identification','### Home research teasers')[0]
# Retain the existing excerpt verbatim; attribution is identified as inherited rather than newly verified.
quote='''<figure class="pullquote"><blockquote lang="ta">“ஏன் என்ற கேள்வி இங்கு கேட்காமல் வாழ்க்கை இல்லை...<br>...பகுத்தறிவு பிறந்ததெல்லாம் கேள்விகள் கேட்டதனாலே”</blockquote><figcaption>— Vaali <span lang="ta">(வாலி)</span></figcaption></figure>'''
body=hero+section('Research at a glance','<p class="reading">'+hero_copy+'</p>'+themes,'research-overview')+feature()+section('Selected work',selected+'<p>'+link('projects.html','Explore projects & archives')+'</p>','selected-work')+section('A research practice grounded in context','<p class="reading">'+shortbio+'</p><p>'+link('about.html','About & academic history')+'</p>','profile')+quote+section('Let’s keep the conversation going',f'<p class="reading">For academic correspondence, research discussions, or enquiries about potential collaborations, please get in touch.</p>{link("mailto:"+EMAIL,"Email me")}','correspondence','closing')
write('index.html','R. Karthick Narayanan | Linguist & Digital Archivist','Research in multilingualism, language vitality, documentation and community-centred digital archiving by linguist R. Karthick Narayanan.',body)

research=intro('Questions · Contexts · Methods','Research',quoted_between('## IV.3 Research page','### R1.')[0])
related=[ [('B01','2025 monograph'),('J05','Methodological review'),('C01','Gender differences and language shift')], [('B02','Toda oral literature'),('R01','Rongpo reports'),('J02','Toda acoustic research')], [('J03','SiDHELA'),('J01','Collaboratory model')], [('P01','LiFE Suite paper')]]
for i,(id,title,_) in enumerate(THEMES,1):
 source=spec.split(f'### R{i}.',1)[1].split('### ',1)[0]
 title=source.splitlines()[0].strip()
 text=re.findall(r'^> (.+)$',source,re.M)[0]
 refs='<p class="related"><strong>Related scholarship</strong><br>'+ ' · '.join(f'<a href="publications.html#{pid}">{label}</a>' for pid,label in related[i-1])+'</p>'
 research+=section(title,'<div class="reading"><p>'+text+'</p>'+refs+'</div>',id,'research-section')
research+=section('Languages and regions','<div class="reading"><p>My sustained research with Toda and Kota communities is grounded in the Nilgiris, Tamil Nadu. Documentary and archival appointments have also involved Rongpo and Spiti-related work in Himalayan contexts and language collections at Sikkim University. North-East Indian language-resource work connects to my prior orthography-development role at the Central Institute of Indian Languages.</p><p>These contexts encompass different kinds of engagement: sustained field research, institutional appointments, and collaborative support.</p></div>','languages')
research+=section('Methods and commitments','<ul class="commitments"><li>Sociolinguistic and ethnographic fieldwork</li><li>Language documentation and verbal-art analysis</li><li>Phonetic and phonological analysis; linguistic annotation</li><li>Archival design, metadata, and digital preservation</li><li>Collaborative language resources</li><li>Participation, attribution, and culturally appropriate access</li></ul><p class="reading">Documentation and preservation require care for the people and relationships through which knowledge is shared. This site presents scholarship and project descriptions; access to primary materials follows the arrangements of the relevant archive or project.</p>','methods')
write('research.html','Research | R. Karthick Narayanan','Research on multilingualism, language endangerment, verbal art, digital archiving and community-centred language resources.',research)

projects=intro('Fieldwork · Documentation · Stewardship','Projects & Archives','Research and archival practice connect linguistic questions with the responsibilities of documenting, describing, and sharing knowledge. The records below distinguish authored research, institutional archival work, and collaborative initiatives.')
def project(id,title,period,role,context,copy,source):
 return f'<article class="project" id="{id}"><div class="project-meta"><p class="eyebrow">{period}</p><p>{role}</p></div><div><h3>{title}</h3><p class="small">{context}</p>{paragraphs(copy)}<p>{source}</p></div></article>'
projects+=section('Selected research and completed work',
 project('toda-kota','Toda and Kota: multilingualism and language vitality','Field research · Book published 2025','Researcher and author','Nilgiris, Tamil Nadu',quoted_between('### P1. Toda and Kota','### P2.'),link(BOOK_URL,'Book details'))+
 project('sidhela','SiDHELA: endangered-language archiving','2019–2020 · Subsequent scholarship','Research associate and digital archivist','Centre for Endangered Languages, Sikkim University',quoted_between('### P2. SiDHELA','### P3.'),link('publications.html#J03','SiDHELA article')+' · '+link('publications.html#J01','Collaboratory model'))+
 project('life-suite','Collaborative language technology and LiFE Suite','Publication · 2025','Co-author and collaborator','Research and technology co-authors listed in the published paper',quoted_between('### P5. Collaborative','### P6.'),link(ACL,'Paper & collaborators at ACL Anthology')),'selected-research')
projects+=section('Current collaborations',
 project('tholkudi','Tholkudi digital archive','2025–2026','Digital repository collaboration','Digital heritage and archival infrastructure',['Contribution to the organisation, digitisation, description and long-term accessibility of linguistic and cultural heritage collections through a digital repository. This work concerns the practical relationship between archival metadata, preservation infrastructure and responsible access.'],link('contact.html','Enquire about this work'))+
 project('suvadugal','Suvadugal: performing-arts documentation','2026','Research and documentation collaboration through CoDIN','With Alternative Media Centre and participating artists and practitioners',['Suvadugal brings together documentation of performing-arts practices, artists, instruments, and associated material culture. Recent work has included documentation and 3D scanning of Silambam objects and a curated exhibition on Silambam material traditions. The initiative connects field documentation with questions of interpretation, attribution, digital representation and the continuity of artistic knowledge.','This is a collaborative initiative involving documentation and scanning teams, organisers, and community practitioners.'],link('contact.html','Discuss documentation collaborations')),'collaborations')
# HOLD programme stays in the private editorial ledger, not a public project.
write('projects.html','Projects & Archives | R. Karthick Narayanan','Selected research, language archives and collaborative documentation projects in multilingualism, cultural heritage and language technology.',projects)

publication=intro('Books · Articles · Chapters · Proceedings · Reports','Publications','Scholarly work in sociolinguistics, language documentation, verbal art, and digital archiving. The bibliography includes authored and collaborative publications, conference proceedings, and research reports.')+feature()
cats=[('books','Books','B'),('journal-articles','Journal articles','J'),('book-chapters','Book chapters','C'),('proceedings','Conference papers & proceedings','P'),('reports','Research reports & archival outputs','R')]
publication+='<nav class="category-nav" aria-label="Publication categories">'+''.join(f'<a href="#{id}">{title}</a>' for id,title,_ in cats)+'</nav>'
for id,title,prefix in cats:
 items=sorted([p for p in pubs if p['id'].startswith(prefix)],key=lambda p:-p['year'])
 body='<ol class="bibliography">'+''.join(f'<li id="{p["id"]}" data-publication="{p["id"]}"><span class="publication-year">{p["year"]}</span><div><p>{md(p["citation"])}</p>'+ (f'<p>{link(BOOK_URL,"Book details")}</p>' if p['id']=='B01' else '')+'</div></li>' for p in items)+'</ol>'
 publication+=section(title,body,id)
write('publications.html','Publications | R. Karthick Narayanan','Complete bibliography of books, journal articles, chapters, conference papers and reports by R. Karthick Narayanan and collaborators.',publication)

bio=quoted_between('### Full professional biography','**Copy edit safeguards:**')
about=intro('Biography · Education · Academic practice','About','R. Karthick Narayanan — linguist, digital archivist, and Executive Director of the Council for Diversity and Innovation.')+'<div class="reading biography">'+paragraphs(bio)+'</div>'
about+='<nav class="category-nav" aria-label="About sections"><a href="#education">Education</a><a href="#appointments">Appointments</a><a href="#early-research">Early research</a><a href="#teaching">Teaching</a><a href="#awards">Awards & service</a></nav>'
def chronology(rows):return '<ol class="chronology">'+''.join(f'<li><p class="date">{date}</p><div><h3>{title}</h3><p>{inst}</p>'+ ('<p class="small">'+detail+'</p>' if detail else '')+'</div></li>' for date,title,inst,detail in rows)+'</ol>'
about+=section('Education',chronology([
 ('Awarded 2021','PhD, Linguistics','Jawaharlal Nehru University, New Delhi','Doctoral research on language maintenance among Toda and Kota in the Nilgiris. Supervisors: Anvita Abbi and Ayesha Kidwai.'),
 ('2012–2014','MPhil, Linguistics','Jawaharlal Nehru University, New Delhi','Research on the vitality of languages spoken by fewer than 10,000 speakers in India.'),
 ('2010–2012','MA, Linguistics','Jawaharlal Nehru University, New Delhi','Dissertation research on Shekhawati phonetics and phonology.'),
 ('2009–2010','BEd, English Language Teaching','Tamil Nadu Teacher Education University, Chennai',''),
 ('2006–2009','BA, English','Loyola College, Chennai / University of Madras','')]),'education')
about+=section('Professional appointments',chronology([
 ('June 2026–present','Executive Director','Council for Diversity and Innovation (CoDIN)',''),
 ('2024–2026','Chief Community and Data Officer','UnReaL-TecE LLP, Agra, Uttar Pradesh',''),
 ('2022–2024','Post-Doctoral Fellow','Moturi Satyanarayana Centre for Advanced Study in the Humanities and Social Sciences, Krea University, Sricity, Andhra Pradesh',''),
 ('2021–2022','Senior Resource Person','Central Institute of Indian Languages, Ministry of Education, Mysuru, Karnataka','Orthography Development for Languages of North-East India.'),
 ('2021','Teaching Faculty','Department of Linguistics, Central University of Karnataka, Kalaburagi, Karnataka',''),
 ('2019–2020','Research Associate and Digital Archivist','Centre for Endangered Languages, Sikkim University, Gangtok, Sikkim','')]),'appointments')
about+=section('Early research',chronology([
 ('2016','Junior Resource Person','Jawaharlal Nehru University, New Delhi','Scheme of Protection and Preservation of Endangered Languages; Rongpo and Spiti-related documentation (Rongpa in the original appointment list).'),
 ('2015–2016','Research Assistant','Centre for Oral and Tribal Literature, Sahitya Akademi, New Delhi','Toda Oral Literature Project.'),
 ('2014','Junior Resource Person','Central Institute of Indian Languages, Mysuru, Karnataka','Scheme of Protection and Preservation of Endangered Languages.')]),'early-research')
about+=section('Teaching',chronology([
 ('2016','Field Methods and Data Digitisation Tutor','MA Field Methods, Jawaharlal Nehru University, New Delhi',''),
 ('2015','Course Teacher','BA Introduction to Phonetics, Jawaharlal Nehru University, New Delhi',''),
 ('2015','Field Methods and Data Digitisation Tutor','MA Field Methods, Jawaharlal Nehru University, New Delhi','')]),'teaching')
about+=section('Awards & scholarly service','<div class="reading"><p><strong>2024 · SPARROW-R Thyagarajan Literary Award</strong><br>In recognition of work on Toda verbal art in Tamil and English.</p><p>Academic memberships include the Linguistic Society of India and the Society of Endangered Languages.</p></div>','awards')
write('about.html','About & CV | R. Karthick Narayanan','Biography, education, academic appointments, teaching and awards of linguist and digital archivist R. Karthick Narayanan.',about)
contact=intro('Academic correspondence','Contact','For academic correspondence, research discussions, or enquiries about potential collaborations, please get in touch by email.')+f'<section class="contact-panel" aria-labelledby="email-title"><p class="eyebrow">Email</p><h2 id="email-title"><a href="mailto:{EMAIL}">{EMAIL}</a></h2><p>Research · Documentation · Digital archiving</p></section>'+section('Explore the work','<div class="contact-links">'+link('research.html','Research questions')+link('projects.html','Projects & archives')+link('publications.html','Publications')+'</div>','explore')
write('contact.html','Contact | R. Karthick Narayanan','Contact R. Karthick Narayanan for academic correspondence, research discussions and potential collaborations.',contact)
for file,title,target in [('education.html','Education','about.html#education'),('experience.html','Experience','about.html#appointments'),('1-about.htm','About','about.html'),('1-index.htm','Academic profile','index.html'),('O-index.htm','Academic profile','index.html')]:
 write(file,title+' | R. Karthick Narayanan','Continue to the updated academic website.',intro('Academic history',title,'This material is available on the updated website.')+'<p>'+link(target,'Continue to '+title.lower())+'</p>',canonical='https://rkarthick-narayanan.github.io/rkn/'+target.split('#')[0])
print('Rendered six primary pages and five compatibility pages.')
