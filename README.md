# Apache Buildstream Website (buildstream.apache.org)

This repository provides the source for the main website of The Apache Software Foundation.

- [Production website](https://buildstream.apache.org/)

- [Content](content)
  - **md** pages in GitHub Flavored Markdown (GFM), which can include HTML.
  - **ezmd** pages in a combination of [ezt](https://github.com/gstein/ezt/blob/wiki/Syntax.md) and GFM.
  - **html** files are treated as static files.
  - Static assets of all types.
  - .htaccess files for redirection and rewrite rules.

- [Issues](https://github.com/apache/buildstream-site/issues)

- [Branches](https://github.com/apache/buildstream-site/branches). The `staging`
branch is served on https://buildstream.staged.apache.org/.
Note that [.asf.yaml](./.asf.yaml) is set up for autopreview. A branch named `preview/mytest` for example is automatically staged at https://buildstream-mytest.staged.apache.org/.

- [Pull requests](https://github.com/apache/buildstream-site/pulls)
  - [Creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request#creating-the-pull-request)

## Documentation

Read the [ASF-Pelican Getting started guide](https://infra.apache.org/asf-pelican-gettingstarted.html) and the pages it links to.

## Notes

The website is built with [Pelican](https://blog.getpelican.com).

Continuous Integration / Continuous Deployment (CI/CD) is via the [.asf.yaml file](https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features)
mechanism, which runs [Buildbot](https://ci2.apache.org/#/builders/3/).

- [Pelican Configuration](pelicanconf.yaml) -- Pelican configuration.
- [ASF Data Load](asfdata.yaml) -- ASF metadata to be used by ezt and Pelican. See [asfdata.py](https://github.com/apache/infrastructure-pelican/blob/master/plugins/asfdata.py).
- [ASF YAML Pelican Build](.asf.yaml) -- ASF infrastructure instructions.

## Local development and testing

If you wish to update and test the site locally, there is a Docker build script you can use.
You will also need Git, and familiarity with working in a command-line shell.

**The following instructions should work for Unix, Linux, and macOS, but will need adjustment for Windows.**

- Install [Docker](https://www.docker.com/get-started).
- Change to a suitable directory.
- Get the Infra Pelican setup: `git clone https://github.com/apache/infrastructure-pelican`.
- Change to the checkout: `cd infrastructure-pelican`.
- Build the container: `docker build -t pelican-asf .`. This will take a while the first time.
- Change to a suitable directory.
- Get the ASF website source: `git clone https://github.com/apache/buildstream-site`.
- Change to the website checkout: `cd buildstream-site`.
- Start the continuous builder: `docker run -it -p8000:8000 -v $PWD:/site pelican-asf`. This will generate a lot of output, but will eventually stop. [N.B. Pelican calls the data generation plugins 3 times before generating the pages.]
- If you want to add some additional debug output, add the following line to `pelicanconf.yaml`: `debug: true`
- Browse to http://localhost:8000/ .

If you make changes to the local copy of buildstream-site, these will be automatically built, and should
appear in the browser when you refresh the page.

## Previewing proposed changes

Any branch in the buildstream-site repository that is named preview/* will
auto-build and stage to buildstream-*.staged.apache.org.

If you need to test your changes, create a branch such as preview/_your-asf-id_

Commits to it will be staged at buildstream-_your-asf-id_.staged.apache.org

**Note:** the branch name must not include any "." characters,
or browsers will refuse to display the site due to an invalid SSL certificate.
The underscore character should not be used either, as it is disallowed in host names.
