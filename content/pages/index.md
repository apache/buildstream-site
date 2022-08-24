title: Welcome to the BuildStream project
slug: index

## What is BuildStream?

BuildStream is a Free Software tool for building/integrating software stacks.
It takes inspiration, lessons and use-cases from various projects including
[OBS](https://openbuildservice.org/),
[Reproducible Builds](https://reproducible-builds.org/),
[Yocto](https://www.yoctoproject.org/),
[Baserock](https://baserock.org/),
[Buildroot](https://buildroot.org/),
[Aboriginal](https://www.landley.net/aboriginal/),
[GNOME Continuous](https://wiki.gnome.org/Attic/GnomeContinuous),
[JHBuild](https://www.freedesktop.org/wiki/Software/jhbuild/),
[Flatpak Builder](https://docs.flatpak.org/en/latest/flatpak-builder.html) and
[Android repo](https://gerrit.googlesource.com/git-repo/).

BuildStream supports multiple build-systems (e.g. autotools, cmake, cpan,
distutils, make, meson, qmake), and can create outputs in a range of formats
(e.g. debian packages, flatpak runtimes, sysroots, system images) for multiple
platforms and chipsets.

## BuildStream 2 pre-releases are now available

BuildStream 2 is now in beta. BuildStream 2 will effectively replace
BuildStream 1, which will soon enter maintenance mode and will no longer be
actively developed.

Users are encouraged to test the beta releases. See the [install page](install.html)
for how to install them. Consult the [porting guide](https://docs.buildstream.build/master/main_porting.html)
for information on how to port your projects to the new API.

For a period of transition, we understand that users will need to use both BuildStream 1
and BuildStream 2 in parallel, this can be done in various ways, such as using containers,
or installing these into separate python virtual environments, as explained in the
[install page](install.html)

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

The main repository is [buildstream] and development happens on the master
branch. Following modern delivery practices, master should always work.

We suggest starting with basic bug fixes, and working up to new feature
development. New features should always be discussed on the mailing lists,
before being submitted as pull requests, see the project's [contributing page]
for details.

#### How can I get involved with the Community?

We have a [mailing list], and an [IRC channel] on the [GNOME IRC server].
Please also feel free to reach out to community members at conferences and at
events.

[mailing list]: https://lists.apache.org/list.html?dev@buildstream.apache.org
[IRC channel]: irc://irc.gnome.org/#buildstream
[GNOME IRC server]: https://wiki.gnome.org/Community/GettingInTouch/IRC
[buildstream]: https://github.com/apache/buildstream
[contributing page]: https://github.com/apache/buildstream/tree/master/CONTRIBUTING.rst
