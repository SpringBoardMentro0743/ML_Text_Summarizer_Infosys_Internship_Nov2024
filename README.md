
# Text Summarization

## Overview
- Developing an automated text summarization system that can accurately and efficiently condense large bodies of text into concise summaries is essential for enhancing business operations.
- This project aims to deploy NLP techniques to create a robust text summarization tool capable of handling various types of documents across different domains.
- The system should deliver high-quality summaries that retain the core information and contextual meaning of the original text.
- Text Summarization focuses on converting large bodies of text into a few sentences summing up the gist of the larger text.
- There is a wide variety of applications for text summarization including News Summary, Customer Reviews, Research Papers, etc.
- This project aims to understand the importance of text summarization and apply different techniques to fulfill the purpose.

## Features
  Abstractive Summarization: Generates summaries by paraphrasing the content and creating novel sentences that retain the meaning of the source text.
    Extractive Summarization: Selects key sentences or phrases directly from the original text to construct summaries.
    Support for Multiple Domains: Handles various types of documents, including news articles, legal documents, academic papers, and more.
    Evaluation Metrics: Evaluates summary quality using industry-standard ROUGE metrics (ROUGE-1, ROUGE-2, and ROUGE-L).


## Dataset
The model is trained and evaluated on the BBC News Text Summarization Dataset, which contains over 7,000 unique English-language news articles.
https://www.kaggle.com/datasets/pariza/bbc-news-summary

## Models
 BART: Used for abstractive summarization. It generates human-like summaries by understanding the context and paraphrasing.
 BERT: Used for extractive summarization. It identifies and extracts the most relevant parts of the text directly. 


### API Endpoints
- Developed using FastAPI framework for handling URLs, files, and direct text input.
    - **Source Code:** `app.py` 
- **Endpoints:**
  - Root Endpoint
  - Summarize URL
  - Summarize File
  - Summarize Text


## CI/CD Pipeline
- Developed a CI/CD pipeline using Docker, Azure and GitHub Actions.
- Utilized Azure Container Instance (ACI) for deploying the image, triggers for every push to the main branch.
- **Source Code:** `.github/workflows/azure.yml`
- **IPv4 Address:** [Text Summarizer](http://20.235.235.107:8000/) ( http://20.235.235.107:8000/ )
- **FQDN:** [Text Summarizer](http://text-summarizer.bqegenbyedfzhpa3.centralindia.azurecontainer.io:8000/) ( http://text-summarizer.bqegenbyedfzhpa3.centralindia.azurecontainer.io:8000/ )
- **Screenshots:** 
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1y0upt5MfiMXMrA5Ar6D0FV91EJ2FIb0p&export=download" border="0"></a>
</div><br>
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1F1agLXesw1XyLh7xBWAC2zxju3bGTaGc&export=download" border="0"></a>
</div><br>
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1M5aIP7_Q7eakyBQ-dSxSaJqJBsblGmzy&export=download" border="0"></a>
</div><br>
<div align="center">
    <a><img src="https://drive.usercontent.google.com/u/0/uc?id=1rrHoRdoJEk8VTyrG8Py2RirkXspZadBQ&export=download" border="0"></a>
</div><br>
</i>

----

### Conclusion
This project successfully implements a text summarization tool that delivers high-quality summaries using both extractive and abstractive methods. It demonstrates potential applications in media, education, and customer service domains while addressing key challenges in NLP model training and evaluation.