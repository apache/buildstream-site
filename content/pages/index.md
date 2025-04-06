title: Welcome to the Apache BuildStream project
slug: index

## What is BuildStream?

BuildStream is a powerful software integration tool that allows developers to automate the
integration of software components including operating systems, and to streamline the software
development and production process.

Some key capabilities of BuildStream include:

* Defining software stacks in a declarative format: BuildStream allows users to define the steps
  required to build and integrate software components, including fetching source code and building
  dependencies.
* Integrating with version control systems: BuildStream can be configured to fetch source code from
  popular source code management solutions such as GitLab, GitHub, BitBucket as well as a range of
  non-git technologies.
* Supporting a wide range of build technologies: BuildStream supports a wide range of technologies,
  including key programming languages like C, C++, Python, Rust and Java, as well as many build tools
  including Make, CMake, Meson, distutils, pip and others.
* Ability to create outputs in a range of formats: e.g. debian packages, flatpak runtimes, sysroots,
  system images, for multiple platforms and chipsets.
* Flexible architecture: BuildStream is designed to be flexible and extensible, allowing users to
  customize their build and integration processes to meet their specific needs and tooling.
* Enabling fast and reliable software delivery: By extensibly use of sandboxing techniques and by
  its capability to distribute the build, BuildStream helps teams deliver high-quality software faster.

## Apache BuildStream 2 is now available

BuildStream 2 has been released and replaces BuildStream 1, which is now end-of-life, and no longer works with Python greater than Python 3.11.x.

Users are encouraged to follow the [porting guide](https://docs.buildstream.build/master/main_porting.html)
to port their projects to the new API, and distributions are encouraged to ship
BuildStream 2 in place of BuildStream 1.

For a period of transition, we understand that users will need to use both BuildStream 1
and BuildStream 2 in parallel, this can be done in various ways, such as using containers,
or installing these into separate python virtual environments, as explained in the
[install page](installation.html)

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
     alt="Freedesktop-SDK logo"
     width="100">
    <br>Freedesktop-sdk
  </a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://gitlab.gnome.org/GNOME/gnome-build-meta/">
    <img src="/images/Gnome-build-meta_logo.png"
     alt="GNOME logo"
     width="100">
    <br>Gnome-build-meta</a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://gitlab.com/carbonOS/build-meta">
    <img src="/images/CarbonOS_logo.png"
     alt="CarbonOS logo"
     width="100">
   <br>carbonOS
  </a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://gitlab.com/libreml/libreml">
    <img src="/images/Libreml_logo.png"
     alt="LibreML logo"
     width="100">
    <br>Libreml
  </a>
 </div>
 <br>
 <div style="margin:10px; vertical-align:bottom; text-align:center">
  <a href="https://github.com/WebKit/webkit/tree/master/Tools/buildstream">
    <img src="/images/WebKitGTK_logo.png"
     alt="WebKitGTK logo"
     width="100">
   <br> WebKitGTK SDK
  </a>
 </div>
</div>
<br>

## What can BuildStream do, and why should I use it?

See ["Why should I use BuildStream?"](https://docs.buildstream.build/master/main_about.html#why-should-i-use-buildstream)
for details.

## How do I get BuildStream?

See our [install page](installation.html) for details.

## How do I get involved?

BuildStream is a welcoming open source project, which means your participation
is one of the project goals. The BuildStream project welcomes and promotes the
participation and contributions of any person.

The most obvious way to participate is to use BuildStream. If you do, then
please tell us about your experiences so we can learn from your feedback,
and tell other people about your exeriences too, so we can reach a larger user
base.

You can also install the latest development snapshots, and help us test new
features developed by the community.

#### How can I get involved with Buildstream Development?

The main repository is [buildstream] and development happens on the default
branch. Following modern delivery practices, this branch should always work.

We suggest starting with basic bug fixes, and working up to new feature
development. New features should always be discussed on the mailing lists,
before being submitted as pull requests, see the project's [contributing page]
for details.

#### How can I get involved with the Community?

Please join our [mailing list].  When attending events or conferences please do
reach out to community members and introduce yourself.

[mailing list]: https://lists.apache.org/list.html?dev@buildstream.apache.org
[buildstream]: https://github.com/apache/buildstream
[contributing page]: https://github.com/apache/buildstream/tree/HEAD/CONTRIBUTING.rst
