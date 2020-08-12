title: Welcome to the BuildStream project
slug: index

## What is BuildStream?

BuildStream is a powerful and flexible software integration toolset. It supports
multiple build-systems and can produce multiple outputs from the same project
(e.g. debian packages, flatpak runtimes, and system images).

BuildStream takes inspiration, lessons and use-cases from various projects
including OBS, Reproducible Builds, Yocto, Baserock, Buildroot, Aboriginal,
GNOME Continuous, JHBuild, Flatpak Builder and Android repo.

## Who is using BuildStream?

Our core users are application developers and system integrators who create
production-ready software systems that need to be maintained efficiently and
reliably in the long term.

Buildstream is currently used by multiple software projects, including:

<div style="display:flex; align-items:flex-end">
 <div style="margin:10px; margin-left:0; vertical-align:bottom; text-align:center">
  <a
href="https://gitlab.com/freedesktop-sdk/freedesktop-sdk">
    <img src="/images/Freedesktop-sdk_logo.png"
     width="100">
    <br>Freedesktop-sdk
  </a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://gitlab.gnome.org/GNOME/gnome-build-meta/">
    <img src="/images/Gnome-build-meta_logo.png"
     width="100">
    <br>Gnome-build-meta</a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://bitbucket.org/carbonOS/tree">
    <img src="/images/CarbonOS_logo.png"
     width="100">
   <br>CarbonOS
  </a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://gitlab.com/libreml/libreml">
    <img src="/images/Libreml_logo.png"
     width="100">
    <br>Libreml
  </a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://github.com/WebKit/webkit/tree/master/Tools/buildstream">
    <img src="/images/WebKitGTK_logo.png"
     width="100">
   <br> WebKitGTK SDK
  </a>
 </div>
</div>
<br>

## What can BuildStream do, and why should I use it?

* BuildStream is fast and predictable, powerful and robust.
* BuildStream can build complex systems at scale, in a continuous delivery
envrionment.
* BuildStream is extensible. You can adapt it to complex workflows, or to
support your favourite build-system.
* At the same time, BuildStream is simple enough to be installed locally to
build a simple change in an application that's under heavy development.
* BuildStream can create full systems and complete toolchains from scratch, for
a range of ISAs including x86\_32, x86\_64, ARMv7, ARMv8, MIPS.

Features:

* declarative build instructions & definitions
* builds in a controlled, reproducible sandboxed environment.
* provides traceability and reproducibility even for stacks of
hundreds/thousands of components.
* tracks changes and only rebuilds the things that have changed.


## How do I get BuildStream?

See our [install page]({filename}installation.md) for details.


## How do I get involved?

BuildStream is a welcoming Free Software project, which means your participation
is one of the project goals. The BuildStream project welcomes and promotes the
participation and contributions of any person.

The most obvious way to participate is to use BuildStream. If you do, then
please tell us about your experiences so we can learn from your feedback,
and tell other people about your exeriences too, so we can reach a larger user
base.

You can also install the latest development snapshots, and help us test new
features developed by the community.

#### How can I get involved with Buildstream Development?

First, request developer access to the [BuildStream Group] on Gitlab. The main
repository is called [buildstream] and development happens on the Master
branch. Following modern delivery practices, Master should always work.

We suggest starting with basic bug fixes, and working up to new feature
development. (New features should always be discussed on the mailing lists,
before being submitted as Merge Requests). See the project's
[contributing page] for details.

#### How can I get involved with the Community?

We have a [mailing list], and an [IRC channel] on the [GNOME IRC server].
Please also feel free to reach out to community members at conferences and at
events.

[BuildGrid]: https://gitlab.com/BuildGrid/buildgrid
[Freedesktop-SDK]: https://gitlab.com/freedesktop-sdk/freedesktop-sdk
[BuildStream docs]: https://docs.buildstream.build
[install page]: {filename}installation.md
[PyPi]: https://pypi.org/project/BuildStream/#history
[mailing list]: https://lists.apache.org/list.html?dev@buildstream.apache.org
[IRC channel]: irc://irc.gnome.org/#buildstream
[GNOME IRC server]: https://wiki.gnome.org/Community/GettingInTouch/IRC
[BuildStream Group]: https://gitlab.com/BuildStream
[buildstream]: https://gitlab.com/BuildStream/buildstream
[contributing page]: https://gitlab.com/BuildStream/buildstream/-/blob/master/CONTRIBUTING.rst
