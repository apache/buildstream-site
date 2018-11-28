title: Install from packages
slug: package_install

BuildStream is available on some linux distributions, here are
some install instructions for the linux distributions which
have packaged BuildStream.

[TOC]

<a id="arch"></a>

## Arch Linux

Packages for Arch exist in [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages).
Two different package versions are available:

 - BuildStream latest release: [buildstream](https://aur.archlinux.org/packages/buildstream)
 - BuildStream latest development snapshot: [buildstream-git](https://aur.archlinux.org/packages/buildstream-git)

The external plugins are available as well:

 - BuildStream-external plugins latest release: [bst-external](https://aur.archlinux.org/packages/bst-external)

<a id="fedora"></a>

## Fedora

BuildStream is not yet in the official Fedora repositories, but you can
install it from a Copr:

    :::shell
    sudo dnf copr enable bochecha/buildstream
    sudo dnf install buildstream

Optionally, install the `buildstream-docs` package to have the BuildStream
documentation in Devhelp or GNOME Builder.
