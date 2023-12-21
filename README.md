# MDChat

![Tests](https://github.com/MykalMachon/NoteChat/actions/workflows/cicd.yml/badge.svg)

A CLI tool that allows you to chat with your markdown notes. MDChat uses a large language model (LLM) and a method called "Retrieval Augmented Generation" to allow you to have intelligent conversations with an expert on your content. 

The primary goal of this project is to be both easy to get started with and educational to what modern AI systems can achieve. There are lots of tools like this out there but, in my opinion, they get a bit too into the weeds on the tech or require too much setup.

## Getting started

To get started with MDChat you just need to install it, configure it, and get to chattin!

```bash
pip install mdchat
```

Then you can point mdchat at your notes through th interactive config and select a model (`GPT-4` is more accurate, `GPT-3.5-turbo` is much cheaper and faster)

```bash
mdchat config
```

After that's done, all you need to do is start a chat with your notes! You can start a new chat thread with the following command:

```bash
mdchat chat
```

Or if you want to chat with a specific note

```bash
mdchat chat --file "/path/to/your/file.md"
```

## Key Features 

- Allows you to "chat" with any folder of markdown files or a single markdown file.
- Answers will include "sources" to the notes used in generating them when possible.
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
