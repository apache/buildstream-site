title: feature page
slug: feature

[_TOC_]

## Release highlights

BuildStream 1.2 is the second Release delivered by the BuildStream project which incorporates a new CAS artifact cache based on bazel remote APIs. This new feature significantly reduces build times. In addition, a new structure of the tool's configuration file, together with new capabilities to fetch from multiple sources, increase BuildStream flexibility. 

Over the last eight months, BuildStream has seen significant improvement, adding several minor features which provide a better onboarding experience to new users while still improving productivity in everyday workflows for application developers and integrators.

The technical documentation has been improved and extended accordingly with the code, the processes and practices to manage the project itself are more robust so we can maintain high levels of productivity while increasing the number of contributors and the project has taken the first step to have a website that help us to raise awareness about the project.

A sister project, [BuildGrid], has been created in order to allow BuildStream to "build at scale" and our association with [Freedesktop-SDK] has allowed BuildStream to test and improve the user experience and reliability.

### CAS Artifact Cache

<!-- TODO -->

### Source Mirroring

Source Mirroring is a way to ensure that sources can be pulled from multiple different URLs. This is useful to users in cases such as:

* The upstream repository is occasionally unreachable
* The upstream repository has low bandwidth
* The BuildStream user has a local mirror that doesn't necessarily hold the latest refs.

With source mirroring, as long as the source's URL uses an alias, fetching your sources from a different place is as simple as specifying a new mirror in project.conf.

Jonathan Maw is the main developer of this feature.

### Include directive

<!-- TODO -->

## Features

<!-- List key features for the general audience, then those for our target market and audience. Those who are only partially supported and will be fully supported in the next major version, too.   -->


|      Feature             |  v1.0   |    v1.2   |               Notes               |
|:------------------------:|:-------:|:---------:|:---------------------------------:|
| [CAS] based artifact cache |         |   New   |  Switched to [CAS] based artifact cache from OSTree based cache  |
| [Source Mirroring]       |         |   New     |   Added functionality and configuration for providing multiple mirrors for any source. |
|  [Include directive]     |         |   New     |  Elements can now include content from other files.                |
| Add junction support for subprojects   |   |   |                                   |
|  Workspace incremental builds  |   |           |                                   |
|  Element and source configuratrion overrides   |   |   |                           |
| Sanbox configuration     |         |           |                                   |
|  Reference storage       |         |           |                                   |

<br/>


### Software components

<!-- List key software components for the general audience, then those for our target market and audience. There are people that has installed in their machines software versions that might collide or not be appropiate for running BuildStream. We need to let them know here.   -->

<!-- TODO -->
| Component | v 1.0 | v 1.2 |
|:---------:|:-----:|:-----:|
|   Python    |  v3.4+ |   v3.5+    |
|   Component b         |    |    |
|   Component c         |    |    |
|   Component d         |    |    |


<br/>

### Plugins and third party software

<!-- List key plugins and external software components that enable interesting or complementary features we partly or entirely rely on. for the general audience, then those for our target market and audience. Those who are only partially supported and will be fully supported in the next major version, too.   -->

|                                  Plugin                        |                     Detail                     |
|:--------------------------------------------------------------:|:----------------------------------------------:|
|  [remote] |        Source for staging files from remote urls   |                                                |
|  [make]   |             BuildElement for using GNU make        |                                                |
|  [deb]    |       Source for staging files from .deb packages  |                                                |
| [filter]  |     Extract a subset of files from another element |                                                |

<br/>

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
[CAS]: https://en.wikipedia.org/wiki/Content-addressable_storage
[Source Mirroring]: https://buildstream.gitlab.io/buildstream/format_project.html#mirrors
[Include directive]: https://buildstream.gitlab.io/buildstream/format_intro.html#include
[remote]: https://buildstream.gitlab.io/buildstream/sources/remote.html
[make]: https://buildstream.gitlab.io/buildstream/elements/make.html
[deb]: https://buildstream.gitlab.io/buildstream/sources/deb.html
[filter]: https://buildstream.gitlab.io/buildstream/elements/filter.html
[download]: https://buildstream.build/releases.html
[install BuildStream 1.2]: https://buildstream.build/install.html
[PyPI]: https://buildstream.build/source_install.html#install_pypi
[Known Issues]: https://buildstream.build/known-issues.html
[IRC channel]: irc://irc.gnome.org/#buildstream
[bug list]: https://gitlab.com/BuildStream/buildstream/boards/580462?=&label_name[]=Bug
[Community mailing list]: https://mail.gnome.org/mailman/listinfo/buildstream-list
[Hello World! example]: https://buildstream.gitlab.io/buildstream/tutorial/first-project.html
[more complex examples]: https://buildstream.gitlab.io/buildstream/using_examples.html
[BuildStream In Detail]: https://buildstream.build/detail.html
[buildstream]: https://gitlab.com/BuildStream/buildstream
