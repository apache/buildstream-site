title: Known Issues
slug: known-issues

<!-- Known issues page page. Check the content structure to better understand the relation with other pages: https://gitlab.com/BuildStream/nosoftware/alignment/blob/master/content_design/content_structure_proposal_description.md#buildstream-in-detail -->

<!-- This page targets users, so they do not need to be familiar with the insides of the tool. Add a description about the impact of the bug, not about the technical details. The title does not need to match the bug one -->

<!-- Known issues should include in the ticket the workaround since we will route users to it -->

This page lists the issues that has been identified as harmful for those installing BuildStream or early on when using BuildStream. When available, a workaround is offered. In any case, the BuildStream community is working to fix them.

### BuildStream 1.2 known issue

* BuildStream/buildstream#624 BuildStream fails to view logs with utf-8 characters
  * Impact Description:
    When inspecting a build log that contains a utf-8 character using
    the BuildStream UI, BuildStream may crash.

  * Workaround:
    View the logs manually by opening the relevant file in
    `$HOME/.cache/buildstream/logs`.

* BuildStream/buildstream#622 `bst shell --build` will fail on only-pulled elements
  * Impact Description:
    BuildStream will fail to create a shell with the `--build` flag on
    an element that has only been pulled from a remote cache, and
    never been fetched locally.

  * Workaround:
    Manually fetch the sources for the element using `bst fetch --deps
    all <element>`. The `--deps all` flag is required since
    BuildStream will refuse to fetch sources for an element with an
    artifact.

* BuildStream/buildstream#609 Cache server running out of space
  * Impact Description:
    This affects only cache servers. Administrators should be aware of
    this issue.  The cache is cleaned up automatically. However at
    some point the cache continues to fill up and fails to clean older
    artifacts.  This issue is a priority for 1.2.

  * Workaround:
    Clean up manually the cache directory when disk resources get low.
    This directory is the one passed as parameter to `bst-artifact-server`.

* BuildStream/buildstream#551 BuildStream pushes just-pulled artifacts back
  * Impact Description:
    This affects users who push and pull to artifact servers. Under
    yet-undetermined circumstances, BuildStream will push an artifact
    that has just been pulled back to the server. This problem is
    rare, and mostly harmless. A fix will likely arrive at the same
    time as one for BuildStream/buildstream#609.

  * Workaround:
    None

* BuildStream/buildstream#525 The "quit" option does not work when interrupting a build
  * Impact Description:

    This affects all builds with the BuildStream client. When
    interrupting a build with `ctrl-C`, the "quit" option will not
    actually exit BuildStream, and the build will continue as normal.

  * Workaround:
    Wait until important jobs complete and use the "terminate" option instead.

* BuildStream/buildstream#524 Fetching from OSTree repos sometimes fails with "Too many open files"
  * Impact Description:
    This only affects projects with OSTree source elements. When
    fetching many elements simultaneously, BuildStream may
    occasionally fail with "too many open files".

  * Workaround:
    Fetch fewer elements before running the full pipeline.
