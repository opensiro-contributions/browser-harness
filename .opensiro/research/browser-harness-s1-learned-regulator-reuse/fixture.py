import json,hashlib,time
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,parse_qs
T={'learn':('Prague','2026-12-03','2026-12-05'),'a':('Oslo','2026-12-04','2026-12-06'),'b':('Lyon','2026-12-11','2026-12-14'),'c':('Riga','2026-12-16','2026-12-19'),'d':('Bern','2027-01-09','2027-01-12'),'e':('Bonn','2027-01-18','2027-01-20')}
class H(BaseHTTPRequestHandler):
 def log_message(self,*args): pass
 def do_GET(self):
  u=urlsplit(self.path);q={k:v[0] for k,v in parse_qs(u.query).items()};t=q.get('task','');status=200;kind='page'
  if u.path=='/guide':
   h='<h1>Help: Shareable searches</h1><p>To bypass the unreliable calendar, open /search?task=ID&destination=CITY&startDate=YYYY-MM-DD&endDate=YYYY-MM-DD with exact requested values.</p>'
  elif u.path=='/task' and t in T:
   city,a,b=T[t];h=f'''<h1>Hotel finder: {t}</h1><p>Search {city} for {a} to {b}.</p><form id="f" action="/search"><input type=hidden name=task value="{t}"><label>Destination <input name=destination value="{city}"></label><label>Check-in <input name=startDate type=date value="{a}"></label><label>Check-out <input name=endDate type=date value="{b}"></label><button>Search hotels</button></form><p id=err></p><a href=/guide>Search link help</a><script>let n=0;document.getElementById('f').addEventListener('submit',e=>{{if(++n<=3){{e.preventDefault();document.getElementById('err').textContent='Calendar lost selected date; try again or use help.';document.querySelector('[name=startDate]').value='';}}}})</script>'''
  elif u.path=='/search' and t in T:
   vals=(q.get('destination'),q.get('startDate'),q.get('endDate'))
   if vals==T[t]:
    kind='success';code=hashlib.sha256('|'.join(T[t]).encode()).hexdigest()[:12];h=f'<h1>Booking search complete</h1><p>Server-verified result: {code}</p>'
   else:kind='mismatch';status=422;h='<h1>Search rejected: wrong dates or destination</h1>'
  else:kind='not_found';status=404;h='<h1>Not found</h1>'
  with open('/tmp/opensiro-bh-s1-20261116/requests.jsonl','a') as f:f.write(json.dumps({'ts':time.time(),'path':u.path,'task':t,'kind':kind,'q':q,'ua':self.headers.get('User-Agent','')})+'\n')
  z=('<html><title>Local Hotel Finder</title><body>'+h+'</body></html>').encode();self.send_response(status);self.send_header('Content-Type','text/html');self.send_header('Content-Length',str(len(z)));self.end_headers();self.wfile.write(z)
ThreadingHTTPServer(('127.0.0.1',8877),H).serve_forever()
