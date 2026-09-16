"""Check the generated research site without third-party Python dependencies."""
from html.parser import HTMLParser
from collections import Counter
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
    project_urls = {
        "/" + path.parent.relative_to(root).as_posix() + "/"
        for path in root.glob("portfolio/*/index.html")
    }
    homepage_links = set()
    if (root / "index.html").exists():
        homepage = Page((root / "index.html").read_text(encoding="utf-8"))
        homepage_links = {
            unquote(urlsplit(attrs.get("href", "")).path)
            for tag, attrs in homepage.tags if tag == "a"
        }
    for path in pages:
        if not path.exists():
            errors.append(f"Missing page: {path}")
            continue
        page = Page(path.read_text(encoding="utf-8"))
        if path in (root / "index.html", root / "portfolio/index.html"):
            cards = [attrs for _, attrs in page.tags if "data-project-url" in attrs]
            card_urls = Counter(unquote(attrs["data-project-url"]) for attrs in cards)
            if card_urls != Counter(project_urls):
                errors.append(f"Project browser must include every project once: {path.relative_to(root)}")
            topics = {
                attrs["data-project-filter"] for _, attrs in page.tags
                if "data-project-filter" in attrs and attrs["data-project-filter"] != "all"
            }
            for card in cards:
                assigned = set(card.get("data-project-topics", "").split())
                if not assigned or not assigned <= topics:
                    errors.append(f"Missing or unknown topics: {card['data-project-url']}")
        if sum(tag == "h1" for tag, _ in page.tags) != 1:
            errors.append(f"Expected one main heading: {path.relative_to(root)}")
        if path.parent.parent == root / "portfolio":
            project_url = "/" + path.parent.relative_to(root).as_posix() + "/"
            if project_url not in homepage_links:
                errors.append(f"Project missing from homepage: {project_url}")
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
