import os
os.chdir('/tmp/claude-0/-home-user/22a5d107-f852-5900-b5ed-f06b5ff6d492/scratchpad/site')
s=open('pam-en-sam.src.html').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
rep('family=IBM+Plex+Sans:wght@300;400&family=IBM+Plex+Serif:wght@300','family=Literata:opsz,wght@7..72,300..500&family=Crimson+Pro:wght@400&family=Jost:wght@300;400')
rep('<meta name="theme-color" content="#2F2924">','<meta name="theme-color" content="#F9F6F0">')
rep('<title>Pam &amp; Sam</title>','<title>Pam &amp; Sam</title>')
css=open('couture.css').read(); i=s.index('</style>'); s=s[:i]+css+s[i:]
rep('<h1>Bespreek het met Pam of Sam.</h1>','<h1>Bespreek het <span>met Pam of Sam.</span></h1>')
rep("roomBg.style.borderRadius = `${16 / sx}px / ${16 / sy}px`;","roomBg.style.borderRadius = `${4 / sx}px / ${4 / sy}px`;")
rep("n.style.setProperty('--dot', name === 'Pam' ? '#C9A15F' : '#4F6F92');","n.style.setProperty('--dot', name === 'Pam' ? '#8A6849' : '#5F676D');")
open('../couture/couture.src.html','w').write(s)
b=open('../site-src/caren.b64').read().strip()
open('../couture/pam-en-sam.html','w').write(s.replace('__CAREN__',b))
print('built')
