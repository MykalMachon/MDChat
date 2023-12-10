# MDChat

![Tests](https://github.com/MykalMachon/NoteChat/actions/workflows/tests.yml/badge.svg)

A CLI tool that allows you to chat with your markdown notes. MDChat uses a large language model (LLM) and a method called "Retrieval Augmented Generation" to allow you to have intelligent conversations with an expert on your content. 

The primary goal of this project is to be both easy to get started with and educational to what modern AI systems can achieve. There are lots of tools like this out there but, in my opinion, they get a bit too into the weeds on the tech or require too much setup.

## Getting started

TODO: write this after you have the package up on pypi

## Key Features 

- Allows you to "chat" with any folder of markdown files.
- Answers will include "sources" to the notes used in generating them.
- summarizing the most recent notes on a certain topic (given your notes are dated)
- summarizing what you've been working on in the last day, or week (given your notes are dated)
- Making novel connections on topics you previously hadn't thought were related

## Contributing 

MDChat is open-source and open to contributions! if you're looking to contribute to this project please: 

* Create an issue to discuss your idea
* Fork this repo
* Create a new branch for your change 
* Make the chnage discussed in your issue 
* Send a pull request

### Installing dependencies

```bash
poetry lock
poetry install
```

### Running the CLI during development

```bash
poetry run mdchat <your-command>
```

### Running tests

```bash
poetry run pytest
```

## License 

MDChat is released under the [MIT License]([https://gi](https://github.com/MykalMachon/NoteChat/blob/main/LICENSE))
