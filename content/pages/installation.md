title: Install
slug: install

<object style="vertical-align: middle" data="https://buildstream.gitlab.io/buildstream/_static/release.svg" type="image/svg+xml">
(your browser does not support SVG, please find releases at [https://download.gnome.org/sources/BuildStream/](https://download.gnome.org/sources/BuildStream/).
</object>
<object style="vertical-align: middle" data="https://buildstream.gitlab.io/buildstream/_static/snapshot.svg" type="image/svg+xml">
(your browser does not support SVG, please find releases at [https://download.gnome.org/sources/BuildStream/](https://download.gnome.org/sources/BuildStream/).
</object>

This page provides instructions for installing BuildStream on various
platforms, along with any installation related materials.

<div class="note">
<p>
BuildStream is currently only supported natively on Linux. Users of
Unix-like systems where OCI technology is available can still use BuildStream
by following the <a href="container_install.html">Container install</a> guide.
</p>
</div>


## From your Linux distribution

BuildStream is available on a limited number of Linux distributions already:

* BuildStream:

[![BuildStream](https://repology.org/badge/vertical-allrepos/buildstream.svg)](https://repology.org/metapackage/buildstream/versions)

* BuilsStream external plugins (bst-external):

[![BuildStream plugins](https://repology.org/badge/vertical-allrepos/bst-external.svg)](https://repology.org/metapackage/bst-external/versions)

[Instructions to install BuildStream for some of these distributions]({filename}package_installation.md)

## From source

If BuildStream is not available on your distribution of choice, or if your
distribution does not have a recent enough version of BuildStream yet, you will
need to install from source code.

- [Install the dependencies for your distribution]({filename}source_installation.md#installing_dependencies)

Then use one of the following techniques to install from source:

* [PyPI (recommended)]({filename}source_installation.md#install_pypi)
* [Tarball]({filename}source_installation.md#install_tarball)
* [Git]({filename}source_installation.md#install_git)

Then finish with the [post installation]({filename}source_installation.md#post_install).

## Using Containers (Toolbox, Docker)

The BuildStream project provides a container image which allows you to run
different versions of the BuildStream tool, without having to install any
dependencies.

- [Container install]({filename}container_install.md)
