# AI Ethics Tool Landscape

Open source and plain-text project providing a taxonomy for the existing tool landscape for ethical Artificial Intelligence.
Built with [Hugo](https://gohugo.io/) and published on [GitHub pages](https://edwinwenink.github.io/ai-ethics-tool-landscape/).

Contributions via pull requests are welcome.

## Adding a tool

All content to this website is provided through a simple markdown file with some YAML metadata.
In order to contribute a tool, all you need to do is fork this repository, add a markdown file to `/content/tools/` and make a pull request to the `develop` branch.

An archetype for the [correct format](/archetypes/default.md) is provided under `/archetypes`.
If you have `hugo` installed, you can use this archetype to easily add a tool to the content section with `hugo new tools/newtool.md`.
You don't need `hugo` to contribute however.
All you need is a text editor and the know-how to make a pull request.
If you really don't know how to work with GitHub (and also really don't want to learn), there is always the back-up option of emailing me your contribution.
Using GitHub is preferred though, also because you will be recorded as a contributor in the git history.

It is allowed that a tool addresses multiple values, categories, and stages of AI development.
It is also possible that a tool is available in multiple languages.
Therefore these field values are provided as an array.

If you make a tool with spaces in the filename, replace the spaces with regular dashes to ensure that cross-referencing to this tool works.
This is because in the URL scheme of this project, spaces are replaced by dashes.

The fields are used to automagically create taxonomies, so there's nothing more to it!

### Multiple references

The format for listing (paper) references is slightly more complex.
The setup supports multiple references per tool.

The simplest syntax is as follows:

```
references:
- 'Paper 1, https://www.example.org'
- 'Paper 2, https://www.example.org'
```

However, it is preferable to provide the url separately and make the references hyperlinks.
For this situation, the following slightly more complex syntax is supported:

```
references: 
- 
    name: 'Paper 1'
    url: 'https://www.example.org'
- 
    name: 'Paper 2'
    url: 'https://www.example.org'
```

### Cross-references

A wiki-like syntax is supported to cross-link to other tools, categories, values etc.
In the markdown file for a tool, you can for example link to another tool with `{{< tool "Interpret-Text" >}}` or to another value with `{{< value "explainability" >}}`.

## Collaboration

This project is an open-ended work in progress.

Collaboration is invited through the addition of tools, refining of existing entries, but also for example conceptual contributions.
You can also refine descriptions of any of the taxonomy terms, for example the description of an [explanation type](https://edwinwenink.github.io/ai-ethics-tool-landscape/explanations/).
The concepts by which to categorize tools are up for discussion and some decisions were made to keep things simple enough.
However, if you have constructive suggestions, for example to adapt existing entry fields or maybe introduce a new one, feel free to open an issue.

If you want to contribute but do not know where to begin, have a look at the list of [candidates](./candidates.md).
