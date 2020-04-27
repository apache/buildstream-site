title: Install BuildBox
slug: buildbox_install

[TOC]

BuildStream master now depends on buildbox-casd to manage the local CAS cache
and communicate with CAS servers. buildbox-run is used for sandboxing. BuildBox
components are still in development and there are no stable releases yet.
Thus, they're not available yet in Linux distros and they have to be manually
installed.

## Install binaries

Linux x86-64 users can download statically linked binaries: [buildbox-x86_64-linux.tar.xz]<br/>
`sha256sum f938a187756ed2a919c2f66b911abb323acb2541035aeecee66b14e56dfe7673`

The tarball contains the binaries `buildbox-casd`, `buildbox-fuse`,
`buildbox-run-bubblewrap` and the symlink `buildbox-run`, which should be
extracted into a directory in `PATH`, e.g., `~/.local/bin`.

## Build from source

### Installing dependencies

BuildBox depends on the following:

* C++ 14 compiler
* CMake
* libuuid
* OpenSSL
* protobuf
* gRPC
* libfuse3

#### Debian and Ubuntu
    :::shell
    sudo apt install cmake uuid-dev libssl-dev \
        libprotobuf-dev protobuf-compiler libgrpc++-dev protobuf-compiler-grpc \
        libfuse3-dev

On Ubuntu 18.04 LTS protobuf and gRPC have to be built from source.

#### Fedora and RHEL/CentOS 8
    :::shell
    sudo dnf install -y gcc-c++ cmake uuid-devel openssl-devel \
        protobuf-devel protobuf-compiler grpc-devel grpc-plugins \
        fuse3 fuse3-devel

#### RHEL/CentOS 7
    :::shell
    sudo yum install -y cmake3 devtoolset-7 openssl-devel \
         fuse3 fuse3-devel

protobuf and gRPC have to be built from source.

#### macOS
    :::shell
    brew install cmake protobuf grpc openssl pkgconfig

The path to OpenSSL has to be specified in the cmake commands with
`-DOPENSSL_ROOT_DIR=/usr/local/opt/openssl`.

### Building BuildBox components

The modules buildbox-common, buildbox-casd, buildbox-fuse and buildbox-run-bubblewrap
have to be built from source. The master branches of these repositories are
generally expected to work with BuildStream master. However, as BuildBox is
still in development, compatibility can't be guaranteed yet. The tags below have
been tested with BuildStream.

    :::shell
    git clone https://gitlab.com/BuildGrid/buildbox/buildbox-common.git
    cd buildbox-common
    git checkout 0.0.7
    cmake -DBUILD_TESTING=OFF -Bbuild
    make -C build
    make -C build install

    git clone https://gitlab.com/BuildGrid/buildbox/buildbox-casd.git
    cd buildbox-casd
    git checkout 0.0.7
    cmake -DBUILD_TESTING=OFF -Bbuild
    make -C build
    make -C build install

    git clone https://gitlab.com/BuildGrid/buildbox/buildbox-fuse.git
    cd buildbox-fuse
    git checkout 0.0.7
    cmake -Bbuild
    make -C build
    make -C build install

    git clone https://gitlab.com/BuildGrid/buildbox/buildbox-run-bubblewrap.git
    cd buildbox-run-bubblewrap
    git checkout 0.0.7
    cmake -DBUILD_TESTING=OFF -Bbuild
    make -C build
    make -C build install

    # Configure buildbox-run-bubblewrap as default buildbox-run implementation
    ln -sv buildbox-run-bubblewrap /usr/local/bin/buildbox-run

[buildbox-x86_64-linux.tar.xz]: https://buildbox-casd-binaries.nyc3.cdn.digitaloceanspaces.com/buildbox-x86_64-linux-0.0.7-f938a187.tar.xz
