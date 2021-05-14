# AI Ethics Tool Landscape

Open source and plain-text project providing a taxonomy for the existing tool landscape for ethical Artifical Intelligence.
Built with [Hugo](https://gohugo.io/).

Contributions via pull requests are welcome.

## Adding a tool

All content to this website is provided through a simple markdown file with some YAML metadata.
In order to contribute a tool, all you need to do is fork this repository, add a markdown file to `/content/tools/` and make a pull request.

An archetype for the [correct format](/content/archetypes/_default.md) is provided under `/archetypes`.
If you have `hugo` installed, you can use this archetype to easily add a tool to the content section with `hugo new tools/newtool.md`.

It is allowed that a tool addresses multiple values, categories, and design phases.
It is also possible that a tool is available in multiple languages.
Therefore these field values are provided as an array.

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

The fields are used to automagically create taxonomies, so there's nothing more to it!
