title: Frequently Asked Questions
slug: faq

[TOC]

## About BuildStream

#### What is BuildStream?

* **The Free Software project**: BuildStream is a Free Software project hosted by the [GNOME Foundation] focused on improving the continuous integration of complex systems and applications. The project aim to pay special attention to those developers and integrators who care about the maintainability of their projects during a long period of time.
* **BuildStream, the toolset**: BuildStream is a powerful and flexible software integration toolset. It has been designed to create different outputs out of a unique input and, at the same time, it is able to adapt to complex workflows, even when additional build tools are required. An important part of BuildStream is a sister project called BuildGrid, that allows BuildStream to build at scale.
* **BuildStream, the Gitlab Group**: the BuildStream project uses [Gitlab.com] service to host the repositories and to manage the project within a Gitlab [Group called BuildStream].
* **buildstream, the code repository**: within the BuildStream Group on [Gitlab.com] you can find a repository called [buildstream] where the core code of the application is hosted.

#### Who is BuildStream toolset for?

BuildStream targets application software developers and system integrators who require an integration tool which is simple enough to be installed locally to build a simple change in an application that is under heavy development and, at the same time, powerful and robust enough to build complex systems at scale as part of a Continuous Delivery based corporate service.

#### Why should I use BuildStream?

The motivation behind the development of BuildStream is to create a modern continuous integration tool suitable for corporate environments where applications and systems needs to be maintained for some for a long term. At the same time the daily usage of the tool needs to be cost effective, not just during development but also during maintenance stages so BuildStream combines flexibility and power through highly configurable features and good dosis of automation.

BuildStream might be an interesting option to those who like to build their systems and applications getting several outputs like packages, images or containers, from a single set of definitions and instructions, reducing maintenance efforts. BuildStream is also a tough contender in environments where complex integration workflows are required as well as in organizations that have adopted continuous delivery principles.

#### Which license is BuildStream using?

The BuildStream project creates and distribute the code and technical documentation under [LGPLv2.1] while the website content is published under the [CC-BY-SA 4.0] license.

The sister project [BuildGrid], which is not part of the GNOME Foundation, is published under [Apache v2.0] license.

#### Who is developing BuildStream?

BuildStream is developed by a community of professionals, several of which have prior experience in the development of Open Source integration tools. The BuildStream project is inclusive so people with different skills and levels of experience are welcome to participate. Visit our [Community] page to find out more.

## Use BuildStream

#### I want to give BuildStream a try. Where can I get it?

You will find all the versions of BuildStream accessible through the [Releases] page.

#### Which BuildStream version should I try?

**BuildStream releases** are created for those interested in using the tool. These releases are updated regularly with bug and security fixes. Make sure you consume the latest published Release.

**Development Snapshots** are created for those interested in evaluating BuildStream's new features and testing them. Again, it is important that you install the latest Snapshot.

Visit the [About BuildStream] page to know about these deliverables.

#### How do I install BuildStream?

BuildStream installation instructions can be found in the [Install] page. The recommended way of installing BuildStream is using [PyPI].

Make sure you also visit the [Known Issues] page if you find any problem. That page describes workarounds to some issues and allows you follow up the effort done by community members to fix those bugs.

#### I need help with BuildStream installation, where can I get it?

If after following the installation instructions from the [Install] guide and checking the [Known Issues] page, you still find problem during the installation process, subscribe to the BuildStream [Community mailing list], introduce yourself and describe the issue you have. You can do the same but using the #buildstream channel in [IRC] instead.

#### I have BuildStream installed, now what?

Take a look at our [tutorials and examples] to learn more about how to use BuildStream. If you are interesting in learning more about BuildStream capabilities, take a look at the [BuildStream In Detail] page.

## Contribute to BuildStream

#### I found a bug, how can I report it?

* BuildStream manages all the bugs though Gitlab.com which means that you will need an account there.
* Before opening a new [issue on gitlab], take a look at the already listed bugs in case your problem has been already reported.
* If that is not the case, you will need to become a Member of the [buildstream] repository in order to report a bug.
      * You can do that directly thorugh Gitlab
      * You can request becoming a Member through the [Community mailing list].
* Go back to the issue tracker and open a new ticket using the bug template.

#### Where can I get the development snapshot of BuildStream?

The latest Development Snapshot can be found on our [releases] page.

#### How do I install the development snapshot of BuildStream?

Installation of Development Snapshots must be done from sources. Check the [Install from source] section of the [Install] guide.

#### I would like to submit a patch, what should I do?

In the [Participate in the BuildStream project] section of our [Community] page, you will find the links to the information you need to follow in order to submit a patch and get it accepted.

#### I have a request to improve BuildStream, how can I present it to the BuildStream community?

The best way to request an enhancement to BuildStream is to present it the [Community mailing list] following the indications described in the [Features Addition] section of the [technical documentation].

[GNOME Foundation]: https://www.gnome.org/foundation/
[Gitlab.com]: https://gitlab.com
[Group called BuildStream]: https://gitlab.com/BuildStream
[buildstream]: https://gitlab.com/BuildStream/buildstream
[LGPLv2.1]: https://gitlab.com/BuildStream/buildstream/blob/master/COPYING
[CC-BY-SA 4.0]: https://creativecommons.org/licenses/by-sa/4.0/
[BuildGrid]: https://gitlab.com/BuildGrid/buildgrid
[Apache v2.0]: https://gitlab.com/BuildGrid/buildgrid/blob/master/LICENSE
[Community]: {filename}community.md
[Releases]: {filename}releases.md
[About BuildStream]: {filename}about.md
[Install]: {filename}installation.md
[PyPI]: {filename}source_installation.md#install_pypi
[Known Issues]: {filename}known_issues.md
[Community mailing list]: https://mail.gnome.org/mailman/listinfo/buildstream-list
[IRC]: irc://irc.gnome.org/#buildstream
[BuildStream In Detail]: {filename}buildstream_in_detail.md
[tutorials and examples]: https://buildstream.gitlab.io/buildstream/main_using.html
[issue on gitlab]: https://gitlab.com/BuildStream/buildstream/issues/new
[Install from source]: {filename}installation.md#install_from_source
[Participate in the BuildStream project]: {filename}community.md#participate-in-the-buildstream-project
[Features Addition]: https://buildstream.gitlab.io/buildstream/HACKING.html#feature-additions
[technical documentation]: https://buildstream.gitlab.io/buildstream/index.html
