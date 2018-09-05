title: Install from source
slug: source_install

[TOC]

Until BuildStream is available in [your distro](#install_linux_distro), you will
need to install it yourself from source.

<a id="installing_dependencies"></a>
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

### Arch Linux

Install the dependencies with:

    :::shell
    sudo pacman -S python fuse2 bubblewrap python-pip


For the default plugins:

    :::shell
    sudo pacman -S bzr git lzip ostree patch python-gobject

The package *python-arpy* is required by the deb source plugin. This is not
obtainable via `pacman`, you must get
[python-arpy from AUR](https://aur.archlinux.org/packages/python-arpy/)

To install:

    :::shell
    wget https://aur.archlinux.org/cgit/aur.git/snapshot/python-arpy.tar.gz
    tar -xvf python-arpy.tar.gz
    cd python-arpy
    makepkg -si

### Debian

Install the dependencies with:

    :::shell
    sudo apt-get install \
        python3 fuse bubblewrap \
        python3-pip python3-dev

For the default plugins:

#### Stretch

With stretch, you first need to ensure that you have the backports repository
setup as described [here](https://backports.debian.org/Instructions).

By adding the following line to your sources.list:

    :::shell
    deb http://deb.debian.org/debian stretch-backports main

And then running:

    :::shell
    sudo apt update

At this point you should be able to get the system requirements for the default plugins with:

    :::shell
    sudo apt install \
        bzr git lzip patch python3-arpy python3-gi
    sudo apt install -t stretch-backports \
        gir1.2-ostree-1.0 ostree

#### Buster or Sid

For debian unstable or testing, only the following line should be enough
to get the system requirements for the default plugins installed::

    :::shell
    sudo apt-get install \
        lzip gir1.2-ostree-1.0 git bzr ostree patch python3-arpy python3-gi

### Fedora

For recent fedora systems, the following line should get you the system
requirements you need:

    :::shell
    dnf install -y \
        python3 fuse bubblewrap \
        python3-pip python3-devel

For the default plugins:

    :::shell
    dnf install -y \
        bzr git lzip patch ostree python3-gobject
    pip3 install --user arpy

### Ubuntu

#### Ubuntu 18.04 LTS or later

Install the dependencies with:

    :::shell
    sudo apt install \
        python3 fuse bubblewrap \
        python3-pip python3-dev

For the default plugins:

    :::shell
    sudo apt install \
        bzr gir1.2-ostree-1.0 git lzip ostree patch python3-arpy python3-gi

#### Ubuntu 16.04 LTS

On Ubuntu 16.04, neither [bubblewrap](https://github.com/projectatomic/bubblewrap/)
or [ostree](https://github.com/ostreedev/ostree) are available in the official repositories.
You will need to install them in whichever way you see fit. Refer the the upstream documentation
for advice on this.

## Installing

<a id="install_pypi"></a>

### Installing from PyPI

Once you have the base system dependencies, you can install the BuildStream
python package as a regular user.

Since we only ever publish [release versions](releases.html) on
PyPI, it is currently recommended to use this installation path. This will
ensure that you always have the latest recommended version of BuildStream that
we recommend.

To install from PyPI, you will additionally require:

 - pip for python3 (only required for setup)
 - Python 3 development libraries and headers

Simply run the following command:

    :::shell
    pip3 install --user BuildStream

This will install latest stable version of BuildStream and its pure python
dependencies into your user's homedir in `~/.local`.

Keep following the instructions below to ensure that the `bst`
command is in your `PATH` and to enable bash completions for it.

If you want a specific version of BuildStream, you can install it
using `pip install --user BuildStream==<version-number>`. Available
can be found versions in the [releases](releases.html). Note that some
of the oldest versions are not available on PyPI.

#### Upgrading from PyPI

Once you have already installed BuildStream from PyPI, you can later update
to the latest recommended version like so:

    :::shell
    pip install --user --upgrade BuildStream

<a id="install_git"></a>

### Installing from a git checkout

To install directly from the [git repository](https://gitlab.com/BuildStream/buildstream.git)
using python's `pip` package manager, you will additionally require:

- pip for python3 (only required for setup)
- Python 3 development libraries and headers
- git (to checkout BuildStream)

Before installing, please check the existing tags in the git repository
and determine which version you want to install, and whether you want
to install an official release version (recommended), or a development snapshot
to help us out testing the bleeding edge of development. Available versions can be found in the [releases](releases.html).

Run the following commands:

    :::shell
    git clone https://gitlab.com/BuildStream/buildstream.git
    cd buildstream
    git checkout <desired release tag>
    pip3 install --user -e .

This will install buildstream's pure python dependencies into
your user's homedir in `~/.local` and will run BuildStream directly
from the git checkout directory.

Keep following the instructions below to ensure that the `bst`
command is in your `PATH` and to enable bash completions for it.

We recommend the `-e` option because you can upgrade your
installation by simply updating the checked out git repository.

If you want a full installation that is not linked to your
git checkout, just omit the `-e` option from the above commands.

#### Upgrading from a git checkout

If you installed BuildStream from a local git checkout using `-e` option, all
you need to do to upgrade BuildStream is to update your local git checkout:

    :::shell
    cd /path/to/buildstream
    git pull --rebase

If you did not specify the `-e` option at install time or the dependancies
have changed, you will need to cleanly reinstall BuildStream:

    :::shell
    pip3 uninstall buildstream
    cd /path/to/buildstream
    git pull --rebase
    pip3 install --user .

If BuildStream has added any dependencies since the last upgrade,
you will need to uninstall and reinstall to ensure those dependencies
are met, regardless of whether you have used the `-e` option at
install time.

<a id="install_tarball"></a>

### Installing from tarball

Tarballs are available in the [releases](releases.html).

You will additionally require:

- pip for python3 (only required for setup)
- Python 3 development libraries and headers

Run the following commands from the unpacked tarball:

    :::shell
    pip3 install --user .

This will install buildstream's pure python dependencies into
your user's homedir in `~/.local` and will run BuildStream directly
from the git checkout directory.

Keep following the instructions below to ensure that the ``bst``
command is in your `PATH` and to enable bash completions for it.

<a id="post_install"></a>
## Post install setup

After having installed from source using any of the above methods, some
setup will be required to use BuildStream.


### Adjust `PATH`

Since BuildStream is now installed under your local user's install directories,
you need to ensure that `PATH` is adjusted.

A regular way to do this is to add the following line to the end of your `~/.bashrc`:

    :::shell
    export PATH="${PATH}:${HOME}/.local/bin"

You will have to restart your terminal in order for these changes to take effect.

### Bash completions

Bash completions are supported by sourcing the `buildstream/data/bst`
script found in the BuildStream repository. On many systems this script
can be installed into a completions directory but when installing BuildStream
without a package manager this is not an option.

To enable completions for an installation of BuildStream you
installed yourself from git, just append the script verbatim
to your `~/.bash_completion`:

    :::shell
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
