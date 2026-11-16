#!/usr/bin/env python3
"""Local nonpayment form fixture for pre-code materiality screen. No external services."""
import json
import time
import threading
import hashlib
from pathlib import Path
from urllib.parse import urlsplit,parse_qs
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
ROOT=Path("/tmp/opensiro-bh-s1-action-20261116")
LOCK=threading.Lock()
LEDGER=ROOT/"ledger.json"
def read():
 return json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
class H(BaseHTTPRequestHandler):
 def log_message(self,*a):pass
 def send(self,status,obj,typ="application/json"):
  b=(json.dumps(obj) if typ=="application/json" else obj).encode()
  self.send_response(status);self.send_header("Content-Type",typ+"; charset=utf-8");self.send_header("Content-Length",str(len(b)));self.send_header("Cache-Control","no-store");self.end_headers();self.wfile.write(b)
 def do_GET(self):
  u=urlsplit(self.path);q=parse_qs(u.query);task=q.get("id",[""])[0]
  if not task.isalnum() or len(task)>40:return self.send(400,{"error":"invalid task"})
  if u.path=="/status":
   with LOCK: v=read().get(task,[])
   return self.send(200,{"id":task,"count":len(v),"receipts":v})
  if u.path=="/task":
   html=f"""<!doctype html><title>Task receipt demo</title><h1>Submit a task exactly once</h1><div id=task>{task}</div><button id=submit>Submit once</button><p id=status>Pending</p><script>
   document.getElementById("submit").onclick=()=>{{
     fetch("/commit?id={task}",{{method:"POST"}}).then(r=>r.json()).then(d=>document.getElementById("status").textContent="Committed "+d.receipt)
   }}</script>"""
   return self.send(200,html,"text/html")
  return self.send(404,{"error":"not found"})
 def do_POST(self):
  u=urlsplit(self.path);task=parse_qs(u.query).get("id",[""])[0]
  if u.path!="/commit" or not task.isalnum() or len(task)>40:return self.send(404,{"error":"not found"})
  if task.startswith("slow"): time.sleep(1.5)
  with LOCK:
   d=read(); items=d.setdefault(task,[])
   receipt=hashlib.sha256(f"{task}:{len(items)+1}".encode()).hexdigest()[:12]
   items.append(receipt)
   LEDGER.write_text(json.dumps(d,sort_keys=True))
   count=len(items)
  return self.send(200,{"id":task,"receipt":receipt,"count":count})
ThreadingHTTPServer(("127.0.0.1",8897),H).serve_forever()
