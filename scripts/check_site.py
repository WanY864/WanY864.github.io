#!/usr/bin/env python3
"""Check generated Hugo HTML for broken local paths, anchors, and missing alt text."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs, self.ids, self.problems = [], set(), []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        ident = attrs.get("id")
        if ident:
            if ident in self.ids:
                self.problems.append("duplicate id: " + ident)
            self.ids.add(ident)
        if tag == "img" and "alt" not in attrs:
            self.problems.append("img missing alt")
        fields = {"a": "href", "img": "src", "script": "src",
                  "link": "href", "iframe": "src"}
        if tag in fields and attrs.get(fields[tag]):
            self.refs.append((tag, attrs[fields[tag]]))

def target(root, page, uri):
    parsed = urlsplit(uri)
    if parsed.scheme or parsed.netloc:
        return None
    loc = unquote(parsed.path or "")
    if not loc and not parsed.fragment:
        return None
    file_path = root / loc.lstrip("/") if loc.startswith("/") else page.parent / loc
    if not loc:
        file_path = page
    if file_path.is_dir() or not file_path.suffix:
        file_path = file_path / "index.html"
    return file_path, parsed.fragment

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    if not (root / "index.html").is_file():
        raise SystemExit("Missing generated homepage")
    documents, problems = {}, []
    for page in root.rglob("*.html"):
        doc = Document()
        doc.feed(page.read_text(encoding="utf-8"))
        documents[page.resolve()] = doc
        problems.extend((page.relative_to(root), issue) for issue in doc.problems)
    for page, doc in documents.items():
        for tag, href in doc.refs:
            dest = target(root, page, href)
            if dest is None:
                continue
            dest_path, fragment = dest
            if not dest_path.is_file():
                problems.append((page.relative_to(root), f"{tag}: missing {href}"))
            elif tag == "a" and fragment and dest_path.suffix == ".html":
                target_doc = documents.get(dest_path.resolve())
                if target_doc and unquote(fragment) not in target_doc.ids:
                    problems.append((page.relative_to(root), f"missing anchor {href}"))
    for page, issue in problems[:40]:
        print(f"{page}: {issue}")
    print(f"Validated {len(documents)} HTML pages; {len(problems)} issues.")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
