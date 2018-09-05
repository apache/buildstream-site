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
Unix-like systems where Docker is available can still use BuildStream
by following the <a href="docker_install.html">Docker install guide</a>.
</p>
</div>


## From your Linux distribution

BuildStream is available on a limited number of Linux distributions already,
here are some simple instructions to install BuildStream for these distributions.

 * [Arch Linux]({filename}package_installation.md#arch)
 * [Fedora]({filename}package_installation.md#fedora)

## From source

If BuildStream is not available on your distribution of choice, or if your
distribution does not have a recent enough version of BuildStream yet, you will
need to install from source code.

First follow the [guide to install the dependencies for your distribution]({filename}source_installation.md#installing_dependencies), and then use
one of the following techniques to install from source:

* [PyPI (recommended)]({filename}source_installation.md#install_pypi)
* [Tarball]({filename}source_installation.md#install_tarball)
* [Git]({filename}source_installation.md#install_git)

Then finish with the [post installation]({filename}source_installation.md#post_install).

## Using Docker

BuildStream provides a docker image which allows you to easily run
BuildStream inside a Docker container. To use the Docker container
please follow [these instructions]({filename}docker_installation.md).
