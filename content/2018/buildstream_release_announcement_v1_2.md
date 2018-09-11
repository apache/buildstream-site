Title: BuildStream 1.2 is out!
Date: 2018-09-05 12:00
Category: release
Tags: 1.2,
Slug: buildstream-1.2-is-out
Authors: toscalix
Summary: BuildStream 1.2 has been released with new features and siginificant improvements.

The BuildStream project is happy to announce the release of the latest version of its integration toolset, **[BuildStream 1.2]({filename}../pages/releases.md)**. This version represents a remarkable step forward with the inclusion of several new features required in production environments. Almost every previously available feature has been improved and many bugs have been fixed during the development cycle that led to this 1.2 release.

Among the most relevant news we highlight a new [CAS] artifact cache based on [bazel remote APIs]. This new feature not just prevent files duplication but also opens the door to have remote execution which will significantly reduces build times. This new version also comes with a new structure of the tool's configuration file which together with new capabilities to fetch from multiple sources increase BuildStream flexibility and various minor features and improvement that provides a better onboarding experience to those using BuildStream for the very first time as well as a raise in productivity to BuildStream veterans.

Read more about **[what's new]({filename}../pages/feature_page.md)** on BuildStream 1.2 and **[install or update]({filename}../pages/source_installation.md#install_pypi)** to this new version.

## Who is BuildStream for?

BuildStream aims to be the default integration solution for integrators of complex systems and applications that will remain in production for a long time, which requires that the toolset is not just powerful, scalable, flexible and efficient, among other qualities, but also reliable and cost effective in the mid term. The project also desires to meet strict requirements coming from safety critical environments.

## About BuildStream

BuildStream is a Free Software project. You can learn more about what it is by visiting the [Frequently Asked Questions]({filename}../pages/faq.md) page and the [BuildStream Project]({filename}../pages/community.md) page. If you are interested in learning more about what BuildStream delivers, please visit our [About BuildStream]({filename}../pages/about.md) page.


[CAS]: https://en.wikipedia.org/wiki/Content-addressable_storage
[bazel remote APIs]: https://github.com/bazelbuild/remote-apis


