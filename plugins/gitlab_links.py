# gitlab_links.py: Support some gitlab style links in Markdown
# Copyright (C) 2018  Codethink Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import json

import urllib.parse
import urllib.request

import markdown.preprocessors
import markdown.extensions

issue_syntax = re.compile(r'(?P<project>[a-zA-Z0-9_./-]*)#(?P<issue>[0-9]+)')

class GitlabLinksPP(markdown.preprocessors.Preprocessor):
    def __init__(self, md):
        super(GitlabLinksPP, self).__init__(md)

    def _replace(self, m):
        project = urllib.parse.quote_plus(m.group('project'))
        issue = urllib.parse.quote_plus(m.group('issue'))
        path = '/api/v4/projects/{}/issues/{}'.format(project, issue)
        url = urllib.parse.urljoin('https://gitlab.com', path)

        with urllib.request.urlopen(url) as f:
            issue = json.loads(f.read().decode('utf-8'))
            web_url = issue.get('web_url')
            out = '#{}'.format(m.group('issue'))

            if issue.get('state') == 'closed':
                out = '{} (closed)'.format(out)

            if web_url:
                title = issue.get('title')
                if title:
                    web_url = '{} "{}"'.format(web_url, title)
                out = '[{}]({})'.format(out, web_url)

        return out

    def run(self, lines):
        try:
            return [issue_syntax.sub(self._replace, line) for line in lines]
        except:
            import traceback
            traceback.print_exc()
            raise

class GitlabLinks(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.preprocessors.add("gitlablinks", GitlabLinksPP(md), "_end")
