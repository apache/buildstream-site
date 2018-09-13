title: Glossary
slug: glossary

<!-- Glossary page. Check the content structure to better understand the relation with other pages: https://gitlab.com/BuildStream/nosoftware/alignment/blob/master/content_design/content_structure_proposal_description.md#buildstream-in-detail -->

## BuildStream Glossary

[TOC]

### B

* build: <!-- vs integration -->
* BuildStream: The tool commonly executed through the use of the `bst` command. <!-- the tool -->
* buildstream: The [code repository] for the BuildStream tool. <!-- the repo -->
* BuildStream Project:
* BuildStream Community

### D

* Definitions: <!-- vs receipe -->

### E

* Element: A single component of a BuildStream project. Each `.bst` file is an element.
    * Various [element kinds] exist and new elements can be added as [plugins]

### I

* Integration: <!-- vs build -->

### M

* Master: Master is the bleeding edge version of BuildStream.
    * Note that no guarantees are made regarding the stability of master.

### P

* Pipeline:

### R

* Recipe:

### S

* Source: An input to an element.
    * Various [source kinds] exist and new sources can be added as [plugins]

### W

* Workspace: A controlled environment for developing buildstream projects.


[code repository]: https://www.gitlab.com/buildstream/buildstream
[source kinds]: https://buildstream.gitlab.io/buildstream/core_plugins.html#sources
[element kinds]: https://buildstream.gitlab.io/buildstream/core_plugins.html
[plugins]: https://buildstream.gitlab.io/buildstream/buildstream.plugin.html