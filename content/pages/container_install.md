title: BuildStream inside a container
slug: container_install

If your system cannot provides the base requirements, it is possible to run
BuildStream within a container.  This gives you an easy way to get started
using BuildStream on any Unix-like platform where containers are available,
including macOS.

The BuildStream project provides [container images on Docker
Hub](https://hub.docker.com/r/buildstream/buildstream).

## Toolbox
[Toolbox](https://github.com/containers/toolbox) spawns interactive containers,
using podman.

You can create and enter a BuildStream toolbox with the following commands:

    ::shell
    toolbox create -i docker.io/buildstream/buildstream:dev
    toolbox enter buildstream-dev

## Docker
We recommend using the
[`bst-here` wrapper script](https://gitlab.com/BuildStream/buildstream/blob/master/contrib/bst-here)
which automates the necessary container setup. You can download it and make
it executable like this:

    ::shell
    mkdir -p ~/.local/bin
    curl --get https://gitlab.com/BuildStream/buildstream/raw/master/contrib/bst-here > ~/.local/bin/bst-here
    chmod +x ~/.local/bin/bst-here

Check if `~/.local/bin` appears in your `PATH` environment variable -- if it
doesn't, you should edit your `~/.bashrc` so that it does:

    ::shell
    export PATH="${PATH}:${HOME}/.local/bin"

Once the script is available in your `PATH`, you can run `bst-here` to open a
shell session inside a new container based off the latest version of the
`buildstream/buildstream` Docker image. The current working directory will be
mounted inside the container at `/src`.

You can also run individual BuildStream commands as `bst-here COMMAND`. For
example: `bst-here show systems/my-system.bst`. Note that BuildStream won't
be able to integrate with Bash tab-completion if you invoke it in this way.

Two Docker volumes are set up by the `bst-here` script:

 - `buildstream-cache --` mounted at `~/.cache/buildstream`
 - `buildstream-config --` mounted at `~/.config/`

These are necessary so that your BuildStream cache and configuration files
persist between invocations of `bst-here`.

By default, the `latest` tag of the `buildstream/buildstream` image will be
used. This tag tracks the latest stable release of BuildStream. You can choose
to use a different tag using the `-j` option.  For example, you can run the
nightly build of BuildStream like so:

    ::shell
    bst-here -j nightly

More details on image variants can be found
[here](https://hub.docker.com/r/buildstream/buildstream).
