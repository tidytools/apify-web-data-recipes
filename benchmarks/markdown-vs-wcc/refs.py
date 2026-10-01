"""Reference "main content" of a page, taken from its static HTML with the standard library only.

The page's main container is found (role=main, <main>, <article>, Sphinx div.body, else <body>) and its headings,
paragraphs, code blocks (<pre>) and tables are listed. Navigation, footers, sidebars, scripts and buttons inside the
container are ignored. These lists are the ground truth for the recall metrics in metrics.py.
"""
import html, re, urllib.request
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
SKIP = {"script", "style", "noscript", "svg", "template", "nav", "footer", "aside", "button", "form", "iframe", "dialog"}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.children, self.parent = tag, dict(attrs), [], parent

    def text(self, skip=SKIP):
        out = []

        def walk(n):
            for c in n.children:
                if isinstance(c, str):
                    out.append(c)
                elif c.tag not in skip and not hidden(c):
                    if c.tag == "br":
                        out.append("\n")
                    walk(c)
        walk(self)
        return "".join(out)

    def iter(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.iter()


def hidden(n):
    cls = n.attrs.get("class") or ""
    return (n.attrs.get("aria-hidden") == "true" or "hidden" in n.attrs or "headerlink" in cls or "hash-link" in cls
            or re.search(r"\b(sr-only|visually-hidden|screen-reader-text|copybutton|copy-button)\b", cls) is not None)


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse(html_text):
    t = Tree()
    t.feed(html_text)
    return t.root


def main_container(root):
    nodes = list(root.iter())
    def size(n):
        return len(n.text().strip())
    for test in (lambda n: n.attrs.get("role") == "main", lambda n: n.tag == "main", lambda n: n.tag == "article",
                 lambda n: n.tag == "div" and "body" in (n.attrs.get("class") or "").split()):
        cands = [n for n in nodes if test(n) and size(n) > 200]
        if cands:
            return max(cands, key=size)
    body = [n for n in nodes if n.tag == "body"]
    return body[0] if body else root


def clean(s):
    s = html.unescape(s).replace("¶", "").replace("​", "").replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()


def extract(html_text):
    root = parse(html_text)
    main = main_container(root)
    headings, paragraphs, code, tables = [], [], [], 0

    def inside_skipped(n):
        p = n.parent
        while p is not None and p is not main:
            if p.tag in SKIP or hidden(p):
                return True
            p = p.parent
        return False
    for n in main.iter():
        if inside_skipped(n) or hidden(n) or n.tag in SKIP:
            continue
        if re.fullmatch(r"h[1-6]", n.tag):
            t = clean(n.text())
            if t:
                headings.append(t)
        elif n.tag == "p":
            t = clean(n.text())
            if len(t) >= 40:
                paragraphs.append(t)
        elif n.tag == "pre":
            t = html.unescape(n.text(skip=SKIP - {"button"})).strip("\n")
            if t.strip():
                code.append(t)
        elif n.tag == "table":
            rows = [r for r in n.iter() if r.tag == "tr"]
            if len(rows) >= 2:
                tables += 1
    return {"headings": headings, "paragraphs": paragraphs, "code": code, "tables": tables}


def fetch(url):
    req = urllib.request.Request(url, headers={"user-agent": UA, "accept-language": "en-US,en;q=0.9"})
    r = urllib.request.urlopen(req, timeout=30)
    raw = r.read()
    enc = r.headers.get_content_charset() or "utf-8"
    return raw.decode(enc, "replace")
