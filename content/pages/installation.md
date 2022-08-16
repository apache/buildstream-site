title: Install
slug: install

[![Release](https://docs.buildstream.build/master/_static/release.svg)](https://docs.buildstream.build/master/_static/release.html) [![Snapshot](https://docs.buildstream.build/master/_static/snapshot.svg)](https://docs.buildstream.build/master/_static/snapshot.html)

This page is a "quick start" guide for installing BuildStream, with links
to detailed instructions found in the reference documentation.

BuildStream is currently only supported natively on Linux. Users of
Unix-like systems where OCI technology is available can still use BuildStream
by following the [Container Images](#container-images) guide.

## Do you need BuildStream 2 or BuildStream 1?

There are two major versions of BuildStream currently supported.

**BuildStream 2** is the latest version, stable since 2022 and recommended for
all new projects.

**BuildStream 1** is the "classic taste" version, stable and supported
since 2018. No new feature development is planned for BuildStream 1.

If you want to build a specific project, check its `project.conf` file for the
[`min-version` setting](https://docs.buildstream.build/master/format_project.html#minimum-version).
If the setting is `2.0` or above you need BuildStream 2, if the setting is
not present then you need BuildStream 1.

If you want BuildStream 1 and 2 on the same host, you'll need to use a
[venv] as they cannot share a single Python environment. See the
["Installing in virtual environments" guide](https://docs.buildstream.build/master/main_install.html#installing-in-virtual-environments)
for instructions.

## Installing BuildStream 2

If your distribution has an up-to-date `buildstream` package >= 2.0, use that.
[Repology] has a useful table of package versions.

Otherwise, try installing from [PyPI] into your home directory:

    pip3 install --user 'BuildStream == 2.*'

Note that:

  * Some host packages are required which Pip cannot provide, see the list in
    the reference manual's
    ["Installing Dependencies" section](https://docs.buildstream.build/master/main_install.html#installing-dependencies).

  * BuildStream 2 and its dependency `grpc` contain binary modules. The `pip
    install` command will work differently depending on whether [prebuilt
    'wheel' packages](https://pypi.org/project/BuildStream/#files) are
    available for your platform, and may fail if it can't build from source --
    if this happens, follow the full build + install procedure linked below.

The full build + install procedure for BuildStream 2 is documented in the
reference manual's ["Installing" section](https://docs.buildstream.build/master/main_install.html).

## Installing BuildStream 1

If your distribution has an up-to-date `buildstream` package < 2.0, use that.
[Repology] has a useful table of package versions.

Otherwise, install from [PyPI] into your home directory:

    pip3 install --user 'BuildStream == 1.*'

Some host packages are required beyond what Pip provides, see the list in
the reference manual's
["Installing dependencies" section](https://docs.buildstream.build/1.6/install_linux_distro.html#installing-dependencies)

The full build + install procedure for BuildStream 1 is documented in the
reference manual's
["Installing from source" section](https://docs.buildstream.build/1.6/install_linux_distro.html#installing-from-source).

## Container Images

BuildStream can run inside container tools such as Docker, Podman, and Toolbx.

Prebuilt images containing `bst` are available at
[docker.io/buildstream/buildstream] via the [buildstream-docker-images]
project. Please read that project's
[USING.md file](https://gitlab.com/BuildStream/buildstream-docker-images/-/blob/master/USING.md)
for usage instructions.

Note that the Docker `--privileged` flag is usually needed, as BuildStream runs
element build commands in a nested container.

## BuildStream Plugins

BuildStream is extensible via plugins written in Python. Projects should
provide their own setup instructions they require specific plugins from the
host.

Here are some common plugin sets:

Plugins for **BuildStream 2**:

 * **buildstream-plugins**:
   [documentation](https://apache.github.io/buildstream-plugins/),
   [PyPI package](https://pypi.org/project/buildstream-plugins/),
   [GitHub project](https://github.com/apache/buildstream-plugins/)
 * **bst-plugins-container**:
   [documentation](https://buildstream.gitlab.io/bst-plugins-container/),
   [PyPI package](https://pypi.org/project/bst-plugins-container/),
   [GitLab project](https://gitlab.com/BuildStream/bst-plugins-container)
 * **bst-plugins-experimental**:
   [documentation](https://buildstream.gitlab.io/bst-plugins-experimental),
   [PyPI package](https://pypi.org/project/bst-plugins-experimental/),
   [GitLab project](https://gitlab.com/BuildStream/bst-plugins-experimental)

Plugins for **BuildStream 1**:

  * **bst-external**:
    [documentation](https://buildstream.gitlab.io/bst-external/),
    [PyPI package](https://pypi.org/project/BuildStream-external/#history),
    [GitLab project](https://gitlab.com/BuildStream/bst-external)

[buildstream-docker-images]: https://gitlab.com/BuildStream/buildstream-docker-images/
[docker.io/buildstream/buildstream]: https://hub.docker.com/r/buildstream/buildstream
[BuildStream docs]: https://docs.buildstream.build
[Repology]: https://repology.org/project/buildstream/versions
[PyPI]: https://www.pypi.org/project/BuildStream/
[venv]: https://docs.python.org/3/library/venv.html
