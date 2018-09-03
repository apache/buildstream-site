title: Installation
save_as: installation.html

[TOC]


<a id="install_linux_distro"></a>

# Installing from distro packages (recommended)

BuildStream is available on some linux distributions, here are
some install instructions for the linux distributions which
have packaged BuildStream.

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

# Installing from source

Until BuildStream is available in [your distro](#install_linux_distro), you will
need to install it yourself from source.

## Installing dependencies

Before installing BuildStream from source, it is necessary to first install
the system dependencies. Below are some linux distribution specific instructions
for installing these dependencies.

BuildStream requires the following base system requirements:

- python3 >= 3.5
- bubblewrap >= 0.1.2
- fuse2

BuildStream also depends on the host tools for the Source plugins.
Refer to the respective source plugin documentation for host tool
requirements of specific plugins.

The default plugins with extra host dependencies are:

- bzr
- deb
- git
- ostree
- patch
- tar

## Arch Linux

Install the dependencies with:

```
sudo pacman -S python fuse2 bubblewrap python-pip
```

For the default plugins:

```
sudo pacman -S bzr git lzip ostree patch python-gobject
```

The package *python-arpy* is required by the deb source plugin. This is not
obtainable via `pacman`, you must get *python-arpy* from AUR:
(https://aur.archlinux.org/packages/python-arpy/)[https://aur.archlinux.org/packages/python-arpy/]

To install:

```
wget https://aur.archlinux.org/cgit/aur.git/snapshot/python-arpy.tar.gz
tar -xvf python-arpy.tar.gz
cd python-arpy
makepkg -si
```

### Debian

Install the dependencies with:

```
sudo apt-get install \
    python3 fuse bubblewrap \
    python3-pip python3-dev
```

For the default plugins:

#### Stretch

With stretch, you first need to ensure that you have the backports repository
setup as described [here](https://backports.debian.org/Instructions).

By adding the following line to your sources.list:

```
deb http://deb.debian.org/debian stretch-backports main
```

And then running::

```
sudo apt update
```

At this point you should be able to get the system requirements for the default plugins with:

```
sudo apt install \
    bzr git lzip patch python3-arpy python3-gi
sudo apt install -t stretch-backports \
    gir1.2-ostree-1.0 ostree
```

#### Buster or Sid

For debian unstable or testing, only the following line should be enough
to get the system requirements for the default plugins installed::

```
sudo apt-get install \
    lzip gir1.2-ostree-1.0 git bzr ostree patch python3-arpy python3-gi
```

### Fedora

For recent fedora systems, the following line should get you the system
requirements you need:

```
dnf install -y \
    python3 fuse bubblewrap \
    python3-pip python3-devel
```

For the default plugins:

```
dnf install -y \
    bzr git lzip patch ostree python3-gobject
pip3 install --user arpy
```

### Ubuntu

#### Ubuntu 18.04 LTS or later

Install the dependencies with:

```
sudo apt install \
    python3 fuse bubblewrap \
    python3-pip python3-dev
```

For the default plugins:

```
sudo apt install \
    bzr gir1.2-ostree-1.0 git lzip ostree patch python3-arpy python3-gi
```

#### Ubuntu 16.04 LTS

On Ubuntu 16.04, neither [bubblewrap](https://github.com/projectatomic/bubblewrap/)
or [ostree](https://github.com/ostreedev/ostree) are available in the official repositories.
You will need to install them in whichever way you see fit. Refer the the upstream documentation
for advice on this.


## Installing

Once you have the base system dependencies, you can install the BuildStream
python package as a regular user.

### Installing from PyPI (recommended)

Since we only ever publish [release versions]({filename}faq.md#install_semantic_versioning) on
PyPI, it is currently recommended to use this installation path. This will
ensure that you always have the latest recommended version of BuildStream that
we recommend.

To install from PyPI, you will additionally require:

 - pip for python3 (only required for setup)
 - Python 3 development libraries and headers

Simply run the following command:

```
pip3 install --user BuildStream
```

This will install latest stable version of BuildStream and its pure python
dependencies into your user's homedir in `~/.local`.

Keep following the instructions below to ensure that the `bst`
command is in your `PATH` and to enable bash completions for it.

If you want a specific version of BuildStream, you can install it using
`pip install --user BuildStream==<version-number>`


#### Upgrading from PyPI

Once you have already installed BuildStream from PyPI, you can later update
to the latest recommended version like so:

```
pip install --user --upgrade BuildStream
```

<a id="install_git_checkout"></a>

## Installing from a git checkout

To install directly from the [git repository](https://gitlab.com/BuildStream/buildstream.git)
using python's `pip` package manager, you will additionally require:

- pip for python3 (only required for setup)
- Python 3 development libraries and headers
- git (to checkout BuildStream)

Before installing, please check the existing tags in the git repository
and determine which version you want to install, and whether you want
to install an official release version (recommended), or a development snapshot
to help us out testing the bleeding edge of development. Follow the
[semantic versioning]({filename}faq.md#install_semantic_versioning) to determine
which tag you intend to install.

Run the following commands:

```
git clone https://gitlab.com/BuildStream/buildstream.git
cd buildstream
git checkout <desired release tag>
pip3 install --user -e .
```

This will install buildstream's pure python dependencies into
your user's homedir in `~/.local` and will run BuildStream directly
from the git checkout directory.

Keep following the instructions below to ensure that the ``bst``
command is in your `PATH` and to enable bash completions for it.

We recommend the ``-e`` option because you can upgrade your
installation by simply updating the checked out git repository.

If you want a full installation that is not linked to your
git checkout, just omit the ``-e`` option from the above commands.

### Upgrading from a git checkout

If you installed BuildStream from a local git checkout using `-e` option, all
you need to do to upgrade BuildStream is to update your local git checkout:

```
cd /path/to/buildstream
git pull --rebase
```

If you did not specify the `-e` option at install time or the dependancies
have changed, you will need to cleanly reinstall BuildStream:

```
pip3 uninstall buildstream
cd /path/to/buildstream
git pull --rebase
pip3 install --user .
```

If BuildStream has added any dependencies since the last upgrade,
you will need to uninstall and reinstall to ensure those dependencies
are met, regardless of whether you have used the `-e` option at
install time.

## Post install setup

After having installed from source using any of the above methods, some
setup will be required to use BuildStream.


### Adjust `PATH`

Since BuildStream is now installed under your local user's install directories,
you need to ensure that `PATH` is adjusted.

A regular way to do this is to add the following line to the end of your `~/.bashrc`:

```
export PATH="${PATH}:${HOME}/.local/bin"
```

You will have to restart your terminal in order for these changes to take effect.

### Bash completions

Bash completions are supported by sourcing the `buildstream/data/bst`
script found in the BuildStream repository. On many systems this script
can be installed into a completions directory but when installing BuildStream
without a package manager this is not an option.

To enable completions for an installation of BuildStream you
installed yourself from git, just append the script verbatim
to your `~/.bash_completion`:

```
# BuildStream bash completion scriptlet.
#
# On systems which use the bash-completion module for
# completion discovery with bash, this can be installed at:
#
#   pkg-config --variable=completionsdir bash-completion
#
# If BuildStream is not installed system wide, you can
# simply source this script to enable completions or append
# this script to your ~/.bash_completion file.
#
_bst_completion() {
    local IFS=$'
'
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _BST_COMPLETION=complete $1 ) )
    return 0
}

complete -F _bst_completion -o nospace bst;
```

# BuildStream inside Docker

If your system cannot provide the base system requirements for BuildStream, then it is possible to run buildstream within a Docker image.

The BuildStream project provides
`Docker images <https://hub.docker.com/r/buildstream/buildstream-fedora>`_
containing BuildStream and its dependencies.
This gives you an easy way to get started using BuildStream on any Unix-like
platform where Docker is available, including Mac OS X.

We recommend using the
[`bst-here` wrapper script](https://gitlab.com/BuildStream/buildstream/blob/master/contrib/bst-here)
which automates the necessary container setup. You can download it and make
it executable like this:

```
mkdir -p ~/.local/bin
curl --get https://gitlab.com/BuildStream/buildstream/raw/master/contrib/bst-here > ~/.local/bin/bst-here
chmod +x ~/.local/bin/bst-here
```

Check if `~/.local/bin` appears in your `PATH` environment variable -- if it
doesn't, you should
[edit your `~/.profile` so that it does](https://stackoverflow.com/questions/14637979/).

Once the script is available in your `PATH`, you can run `bst-here` to open a
shell session inside a new container based off the latest version of the
buildstream-fedora Docker image. The current working directory will be mounted
inside the container at `/src`.

You can also run individual BuildStream commands as `bst-here COMMAND`. For
example: `bst-here show systems/my-system.bst`. Note that BuildStream won't
be able to integrate with Bash tab-completion if you invoke it in this way.

Two Docker volumes are set up by the `bst-here` script:

 - `buildstream-cache --` mounted at `~/.cache/buildstream`
 - `buildstream-config --` mounted at `~/.config/`

These are necessary so that your BuildStream cache and configuration files
persist between invocations of `bst-here`.
