"""Run simple server for previewing."""

import http.server
import socketserver


class server(socketserver.TCPServer):
    """Allow address to be re-used so that server can be restarted immediately."""

    allow_reuse_address = True


def run_server(options, root_dir):
    """Run web server on specified port."""
    if not options.run:
        return

    class handler(http.server.SimpleHTTPRequestHandler):
        """Wrap the root directory."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=root_dir, **kwargs)

    with server(("", options.run), handler) as httpd:
        print(f"serving on port {options.run}...")
        httpd.serve_forever()
