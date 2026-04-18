"""
AB Fluence HRMS — Dashboard launcher
Run this once. Opens Chrome to http://localhost:8585
Ollama connects cleanly (no file:// CORS issues).
"""
import os, subprocess, threading, time, webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8585
FOLDER = os.path.dirname(os.path.abspath(__file__))
URL = f'http://localhost:{PORT}/hr%20dashboard.html'

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=FOLDER, **kw)
    def log_message(self, *_):
        pass  # silence request logs

def open_browser():
    time.sleep(1.2)
    webbrowser.open(URL)

# Start Ollama if not running
env = os.environ.copy()
env['OLLAMA_ORIGINS'] = '*'
subprocess.Popen(['ollama', 'serve'], env=env,
                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f'Dashboard: {URL}')
print('Press Ctrl+C to stop.\n')

threading.Thread(target=open_browser, daemon=True).start()
HTTPServer(('localhost', PORT), Handler).serve_forever()
