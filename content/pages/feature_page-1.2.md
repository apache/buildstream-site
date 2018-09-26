title: Features
slug: feature
<!--
The latest feature page should have the slug `feature`
Other feature pages should follow the pattern `feature-x.y`
-->

[TOC]

## Release highlights

BuildStream 1.2 is the second Release delivered by the BuildStream project which incorporates a new CAS artifact cache based on bazel remote APIs. This new feature not just prevent files duplication but also opens the door to have remote execution which will significantly reduces build times. In addition, improved customisation through the tool's configuration file, together with new capabilities to fetch from multiple sources, increase the flexibility of BuildStream.

Over the last eight months, BuildStream has seen significant improvement, adding several minor features which provide a better onboarding experience to new users while still improving productivity in everyday workflows for application developers and integrators.

The technical documentation has been improved and extended accordingly with the code, the processes and practices to manage the project itself are more robust so we can maintain high levels of productivity while increasing the number of contributors and the project has taken the first step to have a website that help us to raise awareness about the project.

A sister project, [BuildGrid], has been created in order to allow BuildStream to "build at scale" and our association with [Freedesktop-SDK] has allowed BuildStream to test and improve the user experience and reliability.

### CAS Artifact Cache

As part of the preparatory work for Remote Execution BuildStream has moved from an OSTree-based artifact cache to a [Bazel CAS]-based artifact cache.

This should not affect users directly, but it has a few nice side-effects:

* BuildStream no longer depends on OSTree, making it easier to install
  * OSTree sources are of course still supported, and projects with
    such elements still require OSTree
* Artifact servers are now easier to set up, more robust, and support TLS
* CAS replaces the tar cache on non-Linux UNIX, drastically improving
  performance and allowing access to artifact servers

Jürg Billeter is the main developer of this feature.

More improvements will come as work on Remote Execution continues - watch this space!

### Source Mirroring

Source Mirroring is a way to ensure that sources can be pulled from multiple different URLs. This is useful to users in cases such as:

* The upstream repository is occasionally unreachable
* The upstream repository has low bandwidth
* The BuildStream user has a local mirror that doesn't necessarily hold the latest refs.

With source mirroring, as long as the source's URL uses an alias, fetching your sources from a different place is as simple as specifying a new mirror in project.conf.

Jonathan Maw is the main developer of this feature.

### Include directive

BuildStream is highly configurable and project confguration can become large. When using multiple subprojects, part of the configuration would need to be replicated. Maintaining changes could then be challenging. The include directive can be used to split project configuration into fragments which can be shared large across projects using junctions. Then only one file contains an aspect of configuration for multiple projects.

Elements can also use the include directive. For example, similar elements can be factorized. Or elements from subprojects can be imported and tweaked.

## What's new in BuildStream 1.2

New and updated features:

| Feature                                     | v1.0 | v1.2 | Notes                                                                                  |
|:-------------------------------------------:|:----:|:----:|:--------------------------------------------------------------------------------------:|
| [CAS] based artifact cache                  |      | New  | Switched to [CAS] based artifact cache from OSTree based cache                         |
| [Source Mirroring]                          |      | New  | Added functionality and configuration for providing multiple mirrors for any source.   |
| [Include directive]                         |      | New  | Elements can now include content from other files.                                     |
| Add junction support for subprojects        |      |      |                                                                                        |
| Workspace incremental builds                |      | New  | Up-to-date files will no longer be rebuilt for workspaced elements.                    |
| Element and source configuratrion overrides |      | New  | It is now possible to set and override global configuration options for plugins.       |
| Sanbox configuration                        |      | New  | The user/group ID of sandbox processes can now be set in `project.conf`.               |
| Reference storage                           |      | New  | Instead of inline declarations, an external file can now be used to store source refs. |

<br/>

New an updated software components:

| Component   | v 1.0 | v 1.2     |
|:-----------:|:-----:|:---------:|
| Python      | v3.4+ | v3.5+     |
| Bubblewrap  | Any   | v0.1.2+   |
| ruamel.yaml | Any   | v0.15.51- |
| blessings   | Any   | Removed   |
| jinja2      | Any   | v2.10-    |
| protobuf    | N/A   | v3.5-     |
| grpcio      | N/A   | v1.10-    |


<br/>

New and updated plugins and third party software:

|                                  Plugin                        |                     Detail                     |
|:--------------------------------------------------------------:|:----------------------------------------------:|
|  [remote] |        Source for staging files from remote urls   |                                                |
|  [make]   |             BuildElement for using GNU make        |                                                |
|  [deb]    |       Source for staging files from .deb packages  |                                                |
| [filter]  |     Extract a subset of files from another element |                                                |

<br/>

## Incompatibilities with BuildStream 1.0.x

If you already use 1.0.x in your project, take into account the following:

* Project configuration file (project.conf) does not push to cache servers by default anymore, you have to specify "push: true" (See https://gitlab.com/BuildStream/buildstream/issues/224)
* The cache-key has been changed (See https://gitlab.com/BuildStream/buildstream/issues/326)
* Changes in the default value of build-root (See https://gitlab.com/BuildStream/buildstream/issues/414)

## Try BuildStream 1.2 out!

If you want to try BuildStream 1.2 you must go through these two pages carefully:

* Until BuildStream gets official support from major distributions, the recommended way to [install BuildStream 1.2] is through [PyPI].
* All releases sources, including BuildStream 1.2, are available for [download].

The issues which may impact your experience early on are documented in the [Known Issues] page, with workarounds and links to the issue tickets, so you can keep up to date with developments.

Feel free to take a look at our [bug list] if you do not find a solution for the issue you have, join the #buildstream [IRC channel] to get immediate support or join the BuildStream [Community mailing list] and ask questions there if they need to be more elaborate.

## I have installed BuildStream 1.2, now what?

Have you already installed BuildStream 1.2 successfully? Then the next step should be to try the [Hello World! example] to get a sense of how the tool works. There are [more complex examples] you can try next.

Find out more about BuildStream features, architecture and further technical details on the [BuildStream In Detail] page.

## Further resources

For further information about BuildStream check:

* [buildstream] repository includes the code of the core application.
* Check the [FAQ] for further questions.

[BuildGrid]: https://buildgrid.gitlab.io/buildgrid/
[Freedesktop-SDK]: https://gitlab.com/freedesktop-sdk
[Bazel CAS]: https://docs.bazel.build/versions/master/remote-caching.html
[CAS]: https://en.wikipedia.org/wiki/Content-addressable_storage
[Source Mirroring]: https://buildstream.gitlab.io/buildstream/format_project.html#mirrors
[Include directive]: https://buildstream.gitlab.io/buildstream/format_intro.html#include
[remote]: https://buildstream.gitlab.io/buildstream/sources/remote.html
[make]: https://buildstream.gitlab.io/buildstream/elements/make.html
[deb]: https://buildstream.gitlab.io/buildstream/sources/deb.html
[filter]: https://buildstream.gitlab.io/buildstream/elements/filter.html
[download]: {filename}releases.md
[install BuildStream 1.2]: {filename}installation.md
[PyPI]: {filename}source_installation.md#install_pypi
[Known Issues]: {filename}known_issues.md
[IRC channel]: irc://irc.gnome.org/#buildstream
[bug list]: https://gitlab.com/BuildStream/buildstream/boards/580462?=&label_name[]=Bug
[Community mailing list]: https://mail.gnome.org/mailman/listinfo/buildstream-list
[Hello World! example]: https://buildstream.gitlab.io/buildstream/tutorial/first-project.html
[more complex examples]: https://buildstream.gitlab.io/buildstream/using_examples.html
[BuildStream In Detail]: {filename}buildstream_in_detail.md
[buildstream]: https://gitlab.com/BuildStream/buildstream
[FAQ]: {filename}faq.md
