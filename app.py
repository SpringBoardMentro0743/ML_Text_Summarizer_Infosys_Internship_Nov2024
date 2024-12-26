import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
from sklearn.feature_extraction.text import TfidfVectorizer
import heapq
import nltk
from wordcloud import WordCloud

nltk.download('punkt')

# Load pre-trained models (cached for faster use)
@st.cache_data
def load_abstractive_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

def load_extractive_model():
    return TfidfVectorizer()

# Abstractive summarization function
def abstractive_summary(input_text, tokenizer, model, length_option, num_beams=4, length_penalty=2.0):
    length_mapping = {
        "Short": 30,
        "Medium": 60,
        "Long": 100
    }
    inputs = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs, 
        max_length=length_mapping[length_option], 
        min_length=10, 
        length_penalty=length_penalty, 
        num_beams=num_beams, 
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Extractive summarization function
def extractive_summary(input_text, vectorizer, length_option):
    length_mapping = {
        "Short": 3,
        "Medium": 5,
        "Long": 10
    }
    
    sentences = nltk.sent_tokenize(input_text)
    
    if len(sentences) < length_mapping[length_option]:
        return "Input text is too short for the selected summary length. Please provide more detailed text or select a shorter summary length."

    sentence_scores = {}
    vectorizer.fit(sentences)
    vectors = vectorizer.transform(sentences).toarray()

    for i, sentence in enumerate(sentences):
        sentence_scores[sentence] = vectors[i].sum()

    ranked_sentences = heapq.nlargest(length_mapping[length_option], sentence_scores, key=sentence_scores.get)
    return ' '.join(ranked_sentences)

# Streamlit app UI
st.set_page_config(page_title="Text Summarizer using NLP", page_icon="🔖", layout="wide")

# Sidebar for options
st.sidebar.title("Summarizer Options")
summary_type = st.sidebar.radio("Select Summary Type", ["Abstractive", "Extractive"])
length_option = st.sidebar.radio("Select Summary Length", ["Short", "Medium", "Long"])

# Additional options for customization
num_beams = st.sidebar.slider("Number of Beams (Abstractive Only)", min_value=1, max_value=10, value=4)
length_penalty = st.sidebar.slider("Length Penalty (Abstractive Only)", min_value=0.5, max_value=2.0, step=0.1, value=2.0)

st.title("Text Summarizer using NLP")
st.markdown("**Hello everyone, This project is part of my internship at Infosys Springboard, an app to summarize input text.**")

# Input text area
placeholder_text = "Enter your text here. For best results, input a few paragraphs of text."
input_text = st.text_area("Enter the text you want to summarize:", placeholder=placeholder_text, height=200)

# Sidebar features
uploaded_file = st.sidebar.file_uploader("Upload a text file", type=["txt", "docx"])
if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")

if st.button("Generate Summary"):
    if not input_text.strip():
        st.error("Please enter text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            if summary_type == "Abstractive":
                tokenizer, model = load_abstractive_model()
                summary = abstractive_summary(input_text, tokenizer, model, length_option, num_beams=num_beams, length_penalty=length_penalty)
            else:
                vectorizer = load_extractive_model()
                summary = extractive_summary(input_text, vectorizer, length_option)
        
        st.subheader("Summary")
        st.write(summary)

        # Additional features
        st.subheader("Summary Analysis")
        original_word_count = len(input_text.split())
        summary_word_count = len(summary.split())
        st.write(f"**Original Word Count:** {original_word_count}")
        st.write(f"**Summary Word Count:** {summary_word_count}")

        # Word cloud
        if summary_type == "Extractive":
            st.subheader("Word Cloud")
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(summary)
            st.image(wordcloud.to_array(), use_column_width=True)

# Add UI enhancements
st.sidebar.markdown("---")
st.sidebar.write("Developed with ❤️ using Streamlit and Transformers")
st.sidebar.write("[GitHub Repository](https://github.com/ANSH-PANT/Text_Summarization_using_NLP_Infosys_Internship_Oct2024)")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>Developed by ANSH PANT</div>", unsafe_allow_html=True)

# Add Dark Mode Option
st.sidebar.markdown("---")
dark_mode = st.sidebar.checkbox("Enable Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #2e2e2e;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
