title: feature page
slug: feature

<!-- Feature page. Check the content structure to better understand the relation with other pages: https://gitlab.com/BuildStream/nosoftware/alignment/blob/master/content_design/content_structure_proposal_description.md -->


[_TOC_]

## Release highlights

<!-- Text focused on those who can become users and current users, that is, we need to assume they have some technical knowledge. This text should mention and include a short description of the 2 or 3 features that makes a difference, that makes this release worth it. -->

Intro paragraph

Feature 1, Feature 2 and Feature 3 paragraph description

#### CAS Artifact Cache

<!-- TODO -->

#### Source Mirroring

<!-- TODO -->

#### Include directive

<!-- TODO -->

#### Summary
Why you should try it out. <!-- TODO -->

<!-- Table 1.0 vs 1.2 The idea is to reflect evolution and to inform about the updates in features, components and plugins or other elements   -->

### What's new - Feature table:

<!-- List key features for the general audience, then those for our target market and audience. Those who are only partially supported and will be fully supported in the next major version, too.   -->


|                                          Feature                                          |                                       Detail                                      |
|:-----------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
|                                            CAS                                            |                        Switched to CAS based artifact cache                       |
| [Source Mirroring](https://buildstream.gitlab.io/buildstream/format_project.html#mirrors) | Added functionality and configuration for providing multiple mirror for a source. |
|  [Include directive](https://buildstream.gitlab.io/buildstream/format_intro.html#include) |                 Elements can now include content from other files.                |

<br/>

### What's new software components table:

<!-- List key software components for the general audience, then those for our target market and audience. There are people that has installed in their machines software versions that might collide or not be appropiate for running BuildStream. We need to let them know here.   -->

<!-- TODO -->
| Component | v 1.1 | v 1.2 |
|:---------:|:-----:|:-----:|
|    v2.7   |  v2.8 |       |

<br/>

### What's new -  plugins and third party software table:

<!-- List key plugins and external software components that enable interesting or complementary features we partly or entirely rely on. for the general audience, then those for our target market and audience. Those who are only partially supported and will be fully supported in the next major version, too.   -->

|                                  Plugin                                  |                     Detail                     |
|:------------------------------------------------------------------------:|:----------------------------------------------:|
|  [remote](https://buildstream.gitlab.io/buildstream/sources/remote.html) |    Source for staging files from remote urls   |
|   [make](https://buildstream.gitlab.io/buildstream/elements/make.html)   |         BuildElement for using GNU make        |
|     [deb](https://buildstream.gitlab.io/buildstream/sources/deb.html)    |   Source for staging files from .deb packages  |
| [filter](https://buildstream.gitlab.io/buildstream/elements/filter.html) | Extract a subset of files from another element |

<br/>

## Try BuildStream 1.2 out!

If you want to try BuildStream 1.2 you must go through these two pages carefully:

* Until BuildStream gets official support from major distributions, the recommended way to [install BuildStream 1.2] is through [PyPI].
* All releases sources, including BuildStream 1.2, are available for [download].

The issues which may impact your experience early on are documented in the [Known Issues] page, with workarounds and links to the issue tickets, so you can keep up to date with developments.

Feel free to take a look at our [bug list] if you do not find a solution for the issue you have, join the #buildstream [IRC channel] to get immediate support or join the BuildStream [Community mailing list] and ask questions there if they need to be more elaborate.

## I have installed BuildStream 1.2, now what?

Have you already installed BuildStream 1.2 successfully? Then the next step should be to try the [Hello World! example] to get a sense of how the tool works. There are [more complex examples] you can try out next.

Find out more about BuildStream features, architecture and further technical details on the [BuildStream In Detail] page.

## Further resources

For further information about BuildStream check:

* [buildstream] repository includes the code of the core application.
* Check the [FAQ] for further questions.


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
