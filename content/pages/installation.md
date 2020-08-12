title: Install
slug: install

[TOC]

<object style="vertical-align: middle" data="https://buildstream.gitlab.io/buildstream/_static/release.svg" type="image/svg+xml">
(your browser does not support SVG, please find releases at [https://download.gnome.org/sources/BuildStream/](https://download.gnome.org/sources/BuildStream/).
</object>
<object style="vertical-align: middle" data="https://buildstream.gitlab.io/buildstream/_static/snapshot.svg" type="image/svg+xml">
(your browser does not support SVG, please find releases at [https://download.gnome.org/sources/BuildStream/](https://download.gnome.org/sources/BuildStream/).
</object>

This page provides instructions for installing BuildStream on various
platforms, along with any installation related materials.

BuildStream is currently only supported natively on Linux. Users of
Unix-like systems where OCI technology is available can still use BuildStream
by following the [Container Install] guide.


## From your Linux distribution

BuildStream is available on a limited number of Linux distributions already:

* BuildStream:

[![BuildStream](https://repology.org/badge/vertical-allrepos/buildstream.svg)](https://repology.org/metapackage/buildstream/versions)

* BuilsStream external plugins (bst-external):

[![BuildStream plugins](https://repology.org/badge/vertical-allrepos/bst-external.svg)](https://repology.org/metapackage/bst-external/versions)

## Instructions to install BuildStream for some of these distributions

<a id="arch"></a>

### Arch Linux

Packages for Arch exist in [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages).
Two different package versions are available:

 - BuildStream latest release: [buildstream](https://aur.archlinux.org/packages/buildstream)
 - BuildStream latest development snapshot: [buildstream-git](https://aur.archlinux.org/packages/buildstream-git)

The external plugins are available as well:

 - BuildStream-external plugins latest release: [bst-external](https://aur.archlinux.org/packages/bst-external)

<a id="fedora"></a>

### Debian

BuildStream is available in Debian Buster (testing) and Sid:

    :::shell
    apt install buildstream

The external plugins are available as well:

    :::shell
    apt install python3-bst-external

### Fedora

BuildStream is in the official Fedora repositories, starting with Fedora 28:

    :::shell
    sudo dnf install buildstream

Optionally, install the `buildstream-docs` package to have the BuildStream
documentation in Devhelp or GNOME Builder.

### Ubuntu

BuildStream is available in Ubuntu 19.04 and later:

    :::shell
    apt install buildstream

The external plugins are available as well:

    :::shell
    apt install python3-bst-external

## Advanced / Developer Installation Instructions

For other installation options (such as installing dependencies and building
BuildStream from source) visit the [BuildStream docs] and follow the
installation instructions there.

[Container Install]: https://gitlab.com/BuildStream/buildstream-docker-images/-/blob/master/USING.md
[BuildStream docs]: https://docs.buildstream.build
