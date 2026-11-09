import os
os.chdir('/tmp/claude-0/-home-user/22a5d107-f852-5900-b5ed-f06b5ff6d492/scratchpad/site')
s = open('pam-en-sam.src.html').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a)); s = s.replace(a, b)
rep('family=IBM+Plex+Sans:wght@300;400&family=IBM+Plex+Serif:wght@300', 'family=Newsreader:opsz,wght@6..72,300..500&family=Courier+Prime&family=Hanken+Grotesk:wght@300;400')
rep('<meta name="theme-color" content="#2F2924">', '<meta name="theme-color" content="#F1F1EE">')
rep('<title>Pam &amp; Sam</title>', '<title>Pam &amp; Sam · Register</title>')
css = open('register.css').read(); i = s.index('</style>'); s = s[:i] + css + s[i:]
# kop: links de zin, rechts alleen Pam en Sam (openen direct het gesprek)
rep('''    <div class="hero-body">
      <p class="kicker">Iedereen worstelt weleens met zichzelf.</p>''', '''    <div class="hero-body"><div class="hero-left">
      <p class="kicker">Iedereen worstelt weleens met zichzelf.</p>''')
rep('''        <span class="small">6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers</span>
      </div>
    </div>''', '''        <span class="small">6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers</span>
      </div>
    </div>
    <div class="hero-right">
      <button class="reg-row pam" type="button" data-open="pam" aria-label="Begin een gesprek met Pam"><span class="n">(Pam)</span><span><b>Warm en empathisch</b><span class="d">Ze geeft eerst ruimte aan wat je voelt.</span></span><span class="go">begin →</span></button>
      <button class="reg-row sam" type="button" data-open="sam" aria-label="Begin een gesprek met Sam"><span class="n">(Sam)</span><span><b>Direct en nuchter</b><span class="d">Hij gaat zonder omweg naar de kern.</span></span><span class="go">begin →</span></button>
    </div></div>''')
rep('<div class="bar" id="bar">', '<span class="edge" aria-hidden="true"><i class="ep"></i><i class="es"></i></span>\n<div class="bar" id="bar">')
rep("bar.classList.toggle('in', scrollY > lim); };", "bar.classList.add('in'); bar.classList.toggle('glass', scrollY > 8); };")
rep("roomBg.style.borderRadius = `${16 / sx}px / ${16 / sy}px`;", "roomBg.style.borderRadius = '0';")
rep("n.style.setProperty('--dot', name === 'Pam' ? '#C9A15F' : '#4F6F92');", "n.style.setProperty('--dot', 'transparent');")
# markeerstift: elke gele markering een eigen, vaste variant
YEL = '''<script>(function(){var Y=['#F7F0A0','#F4E86E','#F1E15A','#F6EC86','#EFE36F'];
function rnd(s){return function(){s=(s*9301+49297)%233280;return s/233280}}
function mk(i){var r=rnd(i*7+3),c=Y.slice().sort(function(){return r()-.5}),a=84+Math.round(r()*28),s1=Math.round(r()*12),s2=38+Math.round(r()*20),s3=88+Math.round(r()*12);
return 'linear-gradient('+a+'deg,'+c[0]+' '+s1+'%,'+c[1]+' '+s2+'%,'+c[2]+' '+s3+'%)'}
function paint(){document.querySelectorAll('.btn.primary,.bar .nav .btn,.card span,.hl').forEach(function(el,i){if(!el.dataset.mk){el.dataset.mk=1;el.style.backgroundImage=mk(i+1)}})}
paint();new MutationObserver(paint).observe(document.body,{childList:true,subtree:true});})();</script>'''
s = s + YEL
open('../register/register.src.html', 'w').write(s)
b = open('../site-src/caren.b64').read().strip()
open('../register/pam-en-sam.html', 'w').write(s.replace('__CAREN__', b))
print('built')
