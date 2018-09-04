title: Alternative installation
save_as: alternative_installation.html

For alternative installation from source, you must first install
dependencies as described in [installation from source
page](source_installation.html)

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

## Installing from tarball

Tarballs are available on the [download page]({filename}download.md).

You will additionally require:

- pip for python3 (only required for setup)
- Python 3 development libraries and headers

Run the following commands from the unpacked tarball:

```
pip3 install --user .
```

This will install buildstream's pure python dependencies into
your user's homedir in `~/.local` and will run BuildStream directly
from the git checkout directory.

Keep following the instructions below to ensure that the ``bst``
command is in your `PATH` and to enable bash completions for it.
