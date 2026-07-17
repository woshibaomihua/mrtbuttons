from __future__ import annotations

import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class CleanUrlHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
        ".js": "application/javascript",
        ".css": "text/css",
        ".xml": "application/xml",
        ".txt": "text/plain",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path: str) -> str:
        route = unquote(urlsplit(path).path).lstrip("/")
        if not route:
            return str(ROOT / "index.html")

        candidates = [ROOT / route]
        if not Path(route).suffix:
            candidates.extend([ROOT / f"{route}.html", ROOT / route / "index.html"])

        for candidate in candidates:
            resolved = candidate.resolve()
            if not (resolved == ROOT or ROOT in resolved.parents):
                continue
            if resolved.exists():
                return str(resolved)

        return str((ROOT / route).resolve())

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the static site with Vercel-style clean URLs.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=4175)
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), CleanUrlHandler)
    print(f"Serving {ROOT} at http://{args.host}:{args.port}/")
    print(f"Clean URL check: http://{args.host}:{args.port}/catalogue")
    server.serve_forever()


if __name__ == "__main__":
    main()
