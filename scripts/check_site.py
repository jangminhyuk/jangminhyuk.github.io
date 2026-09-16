"""Check the generated research site without third-party Python dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.heading = []
        self.in_heading = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
        if tag == "h1":
            self.in_heading = True

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_heading = False

    def handle_data(self, data):
        if self.in_heading:
            self.heading.append(data)


def main():
    root = Path(__file__).resolve().parents[1] / "_site"
    pages = [
        root / "index.html",
        root / "publications/index.html",
        root / "portfolio/index.html",
        *root.glob("portfolio/*/index.html"),
    ]
    errors = []
    for path in pages:
        if not path.exists():
            errors.append(f"Missing page: {path}")
            continue
        page = Page(path.read_text(encoding="utf-8"))
        if sum(tag == "h1" for tag, _ in page.tags) != 1:
            errors.append(f"Expected one main heading: {path.relative_to(root)}")
        if path.parent.parent == root / "portfolio":
            expected_title = next(
                (attrs.get("content", "") for tag, attrs in page.tags
                 if tag == "meta" and attrs.get("property") == "og:title"), ""
            )
            heading = " ".join("".join(page.heading).split())
            if not expected_title or heading != " ".join(expected_title.split()):
                errors.append(
                    f"Wrong project heading: {path.relative_to(root)}: "
                    f"expected {expected_title!r}, got {heading!r}"
                )
        ids = [attrs["id"] for _, attrs in page.tags if "id" in attrs]
        if len(ids) != len(set(ids)):
            errors.append(f"Duplicate anchors: {path.relative_to(root)}")
        for _, attrs in page.tags:
            for name in ("href", "src", "poster"):
                value = attrs.get(name, "")
                url = urlsplit(value)
                if url.scheme or url.netloc or not url.path:
                    continue
                local_path = unquote(url.path)
                target = (
                    root / local_path.lstrip("/")
                    if local_path.startswith("/")
                    else path.parent / local_path
                )
                if not target.exists():
                    errors.append(f"{path.relative_to(root)}: missing {value}")
    for name in ("_reference", "website_reference", ".claude", ".codex", ".agents"):
        if (root / name).exists():
            errors.append(f"Private/local directory in build: {name}")
    if errors:
        raise SystemExit("\n".join(sorted(set(errors))))
    print(f"Checked {len(pages)} pages: local links, media, project titles, headings, and anchors pass.")


if __name__ == "__main__":
    main()
