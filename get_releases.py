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

def get_links(url):
    with urllib.request.urlopen(url) as f:
        parser = ExtractLinks()
        buffer = f.read()
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
    with urllib.request.urlopen(url) as f:
        lines = f.read().decode('ascii').splitlines()
        for line in lines:
            hash, name = line.split()
            yield hash, name

_get_version = re.compile('.*(?<=[-])(?P<version>[0-9.]*)(?=[.][^0-9])[.](?P<extension>.*)')
_root = 'https://download.gnome.org/sources/BuildStream/'

def get_versions():
    versions = {}
    for d in get_relative_directories(_root):
        for checksum in get_checksums(d):
            for hash, name in read_checksum(checksum):
                m = _get_version.match(name)
                if m:
                    url = urllib.parse.urljoin(d, name)
                    version = tuple(map(int, m.group('version').split('.')))
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

def make_link(url):
    shortname = os.path.basename(urllib.parse.urlparse(url).path)
    return '[{}]({})'.format(shortname, url)

for version, tarball, news in get_versions():
    env = {}
    env['v'] = '.'.join(map(str, version))
    env['tarball'] = make_link(tarball[0])
    env['tarball-hash'] = tarball[1]
    env['news'] = make_link(news[0]) if news else ''
    line = '| {v} | {tarball} | {tarball-hash} | {news} |'.format(**env)
    print(line)
