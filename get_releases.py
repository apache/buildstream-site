import urllib.request
import urllib.parse
import json
import re
import os
from html.parser import HTMLParser

class ExtractLinks(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.found = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.found.append(value)
                    break

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

url_cache = {}

def get_url(url):
    if url in url_cache:
        return url_cache[url]
    with urllib.request.urlopen(url) as f:
        url_cache[url] = f.read()
        return url_cache[url]

def get_links(url):
    buffer = get_url(url)
    parser = ExtractLinks()
    parser.feed(buffer.decode('utf-8'))
    for url in parser.found:
        yield urllib.parse.urlparse(url)

def get_relative_directories(url):
    for link in get_links(url):
        if link.scheme or link.netloc:
            continue
        if link.path.startswith('/'):
            continue
        if link.path.endswith('/'):
            yield urllib.parse.urljoin(url, link.path)

def get_checksums(url):
    for link in get_links(url):
        if link.scheme or link.netloc:
            continue
        if link.path.startswith('/'):
            continue
        if link.path.endswith('.sha256sum'):
            yield urllib.parse.urljoin(url, link.path)

def read_checksum(url):
    buf = get_url(url)
    lines = buf.decode('ascii').splitlines()
    for line in lines:
        hash, name = line.split()
        yield hash, name

_get_version = re.compile('.*(?<=[-])(?P<version>[0-9.]*)(?=[.][^0-9])[.](?P<extension>.*)')
_root = 'https://download.gnome.org/sources/BuildStream/'

def get_versions(stable=True):
    versions = {}
    for d in get_relative_directories(_root):
        for checksum in get_checksums(d):
            for hash, name in read_checksum(checksum):
                m = _get_version.match(name)
                if m:
                    url = urllib.parse.urljoin(d, name)
                    version = tuple(map(int, m.group('version').split('.')))
                    if len(version) >= 2 and bool(version[1] % 2) == stable:
                        continue
                    if version not in versions:
                        versions[version] = (None, None)
                    if m.group('extension') == 'tar.xz':
                        versions[version] = ((url, hash), versions[version][1])
                    elif m.group('extension') == 'news':
                        versions[version] = (versions[version][0], (url, hash))

    versions_found = list(versions.keys())
    versions_found = sorted(versions_found, reverse=True)
    for version in versions_found:
        tarball, news = versions[version]
        yield version, tarball, news

import markdown.preprocessors
import markdown.extensions

class DownloadTablePP(markdown.preprocessors.Preprocessor):
    def __init__(self, md):
        super(DownloadTablePP, self).__init__(md)

    def run(self, lines):
        output = []
        for line in lines:
            if line.startswith('_download_table_stable:') or line.startswith('_download_table_unstable:'):
                stable = line.startswith('_download_table_stable:')
                _, pattern = line.split(':', 1)
                for version, tarball, news in get_versions(stable=stable):
                    env = {}
                    env['version'] = '.'.join(map(str, version))
                    env['uri'] = tarball[0]
                    env['basename'] = os.path.basename(urllib.parse.urlparse(tarball[0]).path)
                    env['sha256'] = tarball[1]
                    if news:
                        env['news'] = news[0]
                        env['news-basename'] = os.path.basename(urllib.parse.urlparse(news[0]).path)
                    else:
                        env['news'] = ''
                        env['news-basename'] = ''
                    newline = pattern.format(**env)
                    newline = re.sub(r'[[](?P<txt>[^]]*)[]][(][)]', r'\g<txt>', newline)
                    output.append(newline)
            else:
                output.append(line)
        return output

class DownloadTable(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.preprocessors.add("downloadtable", DownloadTablePP(md), "_end")
