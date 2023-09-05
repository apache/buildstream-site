Title: BuildStream news and 2.0 planning
Date: 2019-03-13 12:00
Category: release
Tags: 2.0
Slug: buildstream-news-and-2.0-planning
Authors: Laurence
Summary: There will be no release version 1.4 and instead the project will focus on a new version of BuildStream: 2.0.

Please see Tristan's blog for the [original article].

## BuildStream 2.0 planning
As some may have noticed, we did not release any BuildStream 1.4 in the expected timeframes, and the big news is that we won’t be.

After much deliberation and hair pulling, we have decided to focus on a new BuildStream 2.0 API. The reasons for this are multifold, but mainly:

* The project has received much more interest and funding than anticipated, as such we currently have a staggering amount of contributors working full time on BuildStream & BuildGrid combined. Considering the magnitude of features and changes we want to make, committing to a 6 month stable release cycle for this development is causing too much friction.
* A majority of contributors would prefer to refine and perfect the command line interface than to commit to the interface we initially had, and indeed the result after adding new functionality will be more comprehensive and intuitive as a result. The result of these changes will not however be backwards compatible.
* With a long term plan to make it easier for external plugins to be developed, along with a plan to split out plugins into more sensible separate repositories, we also anticipate some API breakages to the format related to plugin loading which cannot be avoided.

To continue with the 1.x API while making the changes we want to make would be dishonest and just introduce unexpected breakages.

### What are we planning ?

Some highlights of what we are working on for future BuildStream 2.x include:

#### Remote execution support

A huge amount of the ongoing work is towards supporting distributed build scenarios and interoperability with other tooling on server clusters which implement the [remote execution API].

This means:

* Element builds which occur on distributed worker machines
* Ability to implement a Bazel element which operates on the same build servers and share the same caching mechanics
* Ability to use optimizations such as RECC which interact with the same servers and caching mechanics
* Optimizating for large scale projects

While performance of BuildStream 1.x is fairly acceptable when working with smaller projects with 500-1000 elements, it falls flat on its face when processing larger projects with ~50K elements or more.

#### New commands for interacting with artifacts

For practical purposes, we have been getting along well enough without the ability to list the artifacts in your cache or examine details about specific artifacts, but the overall experience will be greatly enriched with the ability to specify and manipulate artifacts (rather than elements) directly on the command line.

#### Stability of artifact cache keys

This is a part of BuildStream which was never stable (yet), meaning that any minor point upgrade (e.g. from 1.0 -> 1.2) would result in a necessary rebuild of all of a given project’s artifacts.

While this is not exactly on the roadmap yet, there is a growing interest in all contributing parties to make these keys stable, so I have an expectation that this will stabilize before any 2.0 release.

### Compatibility concerns
BuildStream 2.x will be incompatible with 1.x, as such we will need to guarantee safety to users of either 1.x or 2.x, probably in the form of ensuring parallel installability of BuildStream itself and ensuring that the correct plugins are always loaded for the correct version, and that 1.x and 2.x clients do not cross contaminate eachother in any way.

While there are no clear commitments about just how much the 2.x API will resemble the 1.x API, we are committed to providing a clear migration guide for projects which need to migrate, and we have a good idea what is going to change.

* The command line interface will change a lot. We consider this to be the least painful for users to adapt to, and as there are a lot of things which we want to enhance, we expect to take a lot of liberties in changing the command line interface.
* The Plugin facing Python API will change, we cannot be sure how much. One important change is that plugins will not interact directly with the filesystem but instead must use an abstract API. There are not that many plugins out in the wild so we expect that this migration will not be very painful to end users.
* The YAML format will change the least. We recognize that this is the most painful API surface to change and as such we will try our best to not change it too much. Not only will we ensure that a migration process is well documented, but we will make efforts to ensure that such migrations require minimal effort.

We have also made some commitment to testing BuildStream 2.x on a continuous basis and ensuring that we can build the freedesktop-sdk project with the new BuildStream at all times.

### Schedule
We have not committed to any date for the 2.0 release as of yet, and we explicitly do not have any intention to commit to a date until such a time that we are comfortable with the new API and that our distributed build story has sufficiently stabilized. I can say with confidence that this will certainly not be in 2019.

We will be releasing development snapshots regularly while working towards 2.0, and these will be released in the 1.90.x range.

In the mean time, as far as I know there are no features which are desperately needed by users at this time, and as long as bugs are identified and fixed in the 1.2.x line, we will continue to issue bugfix releases.

We expect that this will provide the safety required for users while also granting us the freedom we need to develop towards the new 2.0.


[original article]: https://blogs.gnome.org/tvb/2019/03/04/buildstream-news-and-2-0-planning/
[remote execution API]: https://github.com/bazelbuild/remote-apis
