title: Installation
save_as: installation.html

BuildStream is available on some linux distributions, here are
some install instructions for the linux distributions which
have packaged BuildStream.

If your distribution is not listed in this page, please [install from source using PyPI](source_installation.html).

[TOC]

## Arch Linux

Packages for Arch exist in [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages).
Two different package versions are available:

 - Latest release: [buildstream](https://aur.archlinux.org/packages/buildstream)
 - Latest development snapshot: [buildstream-git](https://aur.archlinux.org/packages/buildstream-git)

## Fedora

BuildStream is not yet in the official Fedora repositories, but you can
install it from a Copr:

```
sudo dnf copr enable bochecha/buildstream
sudo dnf install buildstream
```

Optionally, install the `buildstream-docs` package to have the BuildStream
documentation in Devhelp or GNOME Builder.
