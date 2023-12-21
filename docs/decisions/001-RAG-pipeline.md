# Initial RAG Pipeline

Date: 2023-12-19

Status: proposed

## Context

At the time of writing MDChat uses [LangChain](https://www.langchain.com/) and [FAISS](https://github.com/facebookresearch/faiss) for the majority of it's AI pipeline to create a [retrieval augmented generation or (RAG)](https://python.langchain.com/docs/use_cases/question_answering/#what-is-rag) pipeline. This pipeline gives LLMs access to each user's specific notes and all of the information within them.

Here's a rundown of how we're currently using these tools:

- **FAISS for indexing**: is a similarity search tool that "vectorizes" the content you feed into it as and allows you to store it as a database. Essentially this means FAISS converts your "text" into "vectors" (like arrays) of numbers that can then be compared to eachother for word/word-pairing similarity. MDChat uses FAISS to vectorize the notes you provide it so they can be relatively easily compared computationally.
- **LangChain for RAG**: is a tool that simplifies working with multiple LLMs via the same interface. Specifically, MDChat uses LangChain to prepare our FAISS vectors by splitting them into more digestible pieces, converting them to embeddings that LLMs can inteface with and finally wrapping those embeddings up in a nice package with the LLM via [`RetrievalQAWithSourcesChain`](https://api.python.langchain.com/en/latest/chains/langchain.chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain.html?highlight=retrievalqawithsourceschain#).

### Successes with this approach

In my testing, I've found this method to be pretty good at referencing specific singular notes and finding information and "connecting dots" that I hadn't considered previously.

### Issues with this approach 

We've had some good success with this method in general, but: 
- it seems to have troulbe with more "general" questions about your notes overall; it can answer questions about one note but struggles with answering questions about your notes as a whole
-  Another issue with this approach is speed and compatability; FAISS in particular requires a dGPU and is *very slow* and hard to serialized (currently it's stored in memory). This makes initial prompts slow even on expensive computers.

## Decision

We will continue to use this approach until we can find a more effective pipeline, but experimentation and testing should be encouraged! 

## Consequences

Issues with more comprehensive understanding of notes will continue until either prompt engineering, better embeddings, or other changes to the pipeline yield better results. 