import nltk
from nltk.tokenize import sent_tokenize
from heapq import nlargest
import streamlit as st

# Download the NLTK punkt tokenizer
nltk.download('punkt')

def nltk_summarize(text, num_sentences=3):
    # Tokenize sentences
    sentences = sent_tokenize(text)
    
    # Create a frequency table of words
    words = nltk.word_tokenize(text.lower())
    word_frequencies = {}
    for word in words:
        if word.isalnum():
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Normalize frequencies
    max_freq = max(word_frequencies.values())  # Changed variable name from 'max' to 'max_freq'
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    # Score sentences based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Select top N sentences
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

# Streamlit UI components
st.set_page_config(page_title='📝 Text Summarization App')
st.title('📝 Text Summarization App')

text_input = st.text_area('Enter text to summarize', height=300)
max_sentences_input = st.text_input('Enter the maximum number of sentences to summarize to:', value="3")

try:
    # Convert max_sentences_input to an integer
    max_sentences = int(max_sentences_input)
except ValueError:
    max_sentences = 3  # Default value if input is invalid
    st.warning("Please enter a valid integer for the maximum number of sentences.")

num_sentences = st.slider('Number of sentences in summary', min_value=1, max_value=max_sentences, value=min(3, max_sentences))

if st.button('Summarize'):
    if text_input.strip():
        summary = nltk_summarize(text_input, num_sentences)
        st.subheader('Summary:')
        st.write(summary)
    else:
        st.warning('Please enter some text to summarize.')