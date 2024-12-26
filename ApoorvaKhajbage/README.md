# Text Summarization Model

## Overview
This project focuses on developing a **Text Summarization Model** capable of creating concise and informative summaries from large text documents. The system leverages advanced **Natural Language Processing (NLP)** techniques and state-of-the-art transformer models to support both **extractive** and **abstractive summarization** methods.

## Features
- **Abstractive Summarization**: Generates summaries by paraphrasing the content and creating novel sentences that retain the meaning of the source text.
- **Extractive Summarization**: Selects key sentences or phrases directly from the original text to construct summaries.
- **Support for Multiple Domains**: Handles various types of documents, including news articles, legal documents, academic papers, and more.
- **Evaluation Metrics**: Evaluates summary quality using industry-standard ROUGE metrics (ROUGE-1, ROUGE-2, and ROUGE-L).

## Dataset
The model is trained and evaluated on the **CNN-DailyMail News Text Summarization Dataset**, which contains over 300,000 unique English-language news articles.

## Key Components
### Models:
- **BART**: Used for abstractive summarization. It generates human-like summaries by understanding the context and paraphrasing.
- **BERT**: Used for extractive summarization. It identifies and extracts the most relevant parts of the text directly.

## Key Learnings
- Learned the importance of data preprocessing for improving model performance.
- Understood the differences and use cases of extractive vs. abstractive summarization.
- Gained experience with transformer architectures like BART and BERT.

## Conclusion
This project successfully implements a text summarization tool that delivers high-quality summaries using both extractive and abstractive methods. It demonstrates potential applications in media, education, and customer service domains while addressing key challenges in NLP model training and evaluation.

