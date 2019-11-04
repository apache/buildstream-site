title: Install BuildBox
slug: buildbox_install

[TOC]

BuildStream master now depends on buildbox-casd to manage the local CAS cache
and communicate with CAS servers. buildbox-casd is still in development and
there is no stable release yet. Thus, it's not available yet in Linux distros
and it has to be manually installed.

## Install binary

Linux x86-64 users can download a statically linked binary: [buildbox-casd-x86_64-linux.tar.xz]<br/>
`sha256sum fa9b46ec50b6abb6177c53d78b0ebe4d2544f1131c2d962f13685fd736d34f09`

The tarball contains a single binary `buildbox-casd`, which should be extracted
into a directory in `PATH`, e.g., `~/.local/bin`.

## Build from source

### Installing dependencies

buildbox-casd depends on the following:

* C++ 14 compiler
* CMake
* libuuid
* OpenSSL
* protobuf
* gRPC

#### Debian and Ubuntu
    :::shell
    sudo apt install cmake uuid-dev libssl-dev \
        libprotobuf-dev protobuf-compiler libgrpc++-dev protobuf-compiler-grpc

On Debian 9 the stretch-backports repository is required for protobuf and gRPC.

On Ubuntu 18.04 LTS protobuf and gRPC have to be built from source.

#### Fedora and RHEL/CentOS 8
    :::shell
    sudo dnf install -y gcc-c++ cmake uuid-devel openssl-devel \
        protobuf-devel protobuf-compiler grpc-devel grpc-plugins

#### RHEL/CentOS 7
    :::shell
    sudo yum install -y cmake3 devtoolset-7 openssl-devel

protobuf and gRPC have to be built from source.

#### macOS
    :::shell
    brew install cmake protobuf grpc openssl pkgconfig

The path to OpenSSL has to be specified in the cmake commands with
`-DOPENSSL_ROOT_DIR=/usr/local/opt/openssl`.

### Building BuildBox components

The modules buildbox-common and buildbox-casd have to be built from source.
The master branches of these repositories are generally expected to work with
BuildStream master. However, as BuildBox is still in development, compatibility
can't be guaranteed yet. The commit SHAs below have been tested with BuildStream.

    :::shell
    git clone https://gitlab.com/BuildGrid/buildbox/buildbox-common.git
    cd buildbox-common
    git checkout 0.0.4
    cmake -DBUILD_TESTING=OFF -Bbuild
    make -C build
    make -C build install

    git clone https://gitlab.com/BuildGrid/buildbox/buildbox-casd.git
    cd buildbox-casd
    git checkout 0.0.4
    cmake -DBUILD_TESTING=OFF -Bbuild
    make -C build
    make -C build install

[buildbox-casd-x86_64-linux.tar.xz]: https://buildbox-casd-binaries.nyc3.cdn.digitaloceanspaces.com/buildbox-casd-x86_64-linux-20191104-598100dd.tar.xz
