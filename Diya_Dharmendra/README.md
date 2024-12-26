# Text Summarization Project

## Overview
This project implements text summarization using T5 and BART models. It automates the process of generating concise summaries from large texts.

## Features
- Abstractive summarization with state-of-the-art models.
- User-friendly Streamlit app for input and summary generation.
- Performance evaluation using ROUGE and BLEU scores.

## Workflow
1. Preprocessed dataset by cleaning and tokenizing text.
2. Fine-tuned T5-small and BART models with optimized configurations.
3. Evaluated model performance using standard metrics.
4. Deployed a Streamlit app for user interaction.

## Technologies
- Python, HuggingFace Transformers, PyTorch, Streamlit.

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
3. Input text or upload a file to generate summaries.

## Results
- ROUGE-1: 0.4, ROUGE-L: 0.4
- BLEU: 0.0 (improvement possible).
