import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Force the browser to never cache HTML, JSON, CSS, or JS files
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

# Set up the server
Handler = NoCacheHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Server started at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    # Automatically open the default web browser
    webbrowser.open(f"http://localhost:{PORT}")
    
    try:
        # Keep the server running
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down server...")
        httpd.server_close()