title: Known Issues
slug: known-issues

<!-- Known issues page page. Check the content structure to better understand the relation with other pages: https://gitlab.com/BuildStream/nosoftware/alignment/blob/master/content_design/content_structure_proposal_description.md#buildstream-in-detail -->

<!-- This page targets users, so they do not need to be familiar with the insides of the tool. Add a description about the impact of the bug, not about the technical details. The title does not need to match the bug one -->

<!-- Known issues should include in the ticket the workaround since we will route users to it -->

This page lists the issues that has been identified as harmful for those installing BuildStream or early on when using BuildStream. When available, a workaround is offered. In any case, the BuildStream community is working to fix them.

### BuildStream 1.2 known issue

* BuildStream/buildstream#609 Cache server running out of space
  * Impact Description:
    This affects only cache servers. Administrators should be aware of
    this issue.  The cache is cleaned up automatically. However at
    some point the cache continues to fill up and fails to clean older
    artifacts.  This issue is a priority for 1.2.

  * Workaround:
    Clean up manually the cache directory when disk resources get low.
    This directory is the one passed as parameter to `bst-artifact-server`.

* #XXX (Title) <!-- The title does not need to match the bug one. It needs to be easy to identify by its impact. Add the link to the issue tracker ticket so the state is updated here.  -->
   * Impact Description: <!-- Add a description about the impact of the bug, not about the technical details.  -->
   * Workaround: <!-- Remember to include the workaround on the ticket description. -->
* #XXX (Title) <!-- The title does not need to match the bug one. It needs to be easy to identify by its impact. Add the link to the issue tracker ticket so the state is updated here.  -->
   * Impact Description: <!-- Add a description about the impact of the bug, not about the technical details.  -->
   * Workaround: <!-- Remember to include the workaround on the ticket description. -->
* #XXX (Title) <!-- The title does not need to match the bug one. It needs to be easy to identify by its impact. Add the link to the issue tracker ticket so the state is updated here.  -->
   * Impact Description: <!-- Add a description about the impact of the bug, not about the technical details.  -->
   * Workaround: <!-- Remember to include the workaround on the ticket description. -->
* #XXX (Title) <!-- The title does not need to match the bug one. It needs to be easy to identify by its impact. Add the link to the issue tracker ticket so the state is updated here.  -->
   * Impact Description: <!-- Add a description about the impact of the bug, not about the technical details.  -->
   * Workaround: <!-- Remember to include the workaround on the ticket description. -->
