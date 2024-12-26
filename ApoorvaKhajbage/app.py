# import os
# import streamlit as st
# from transformers import BartForConditionalGeneration, BartTokenizer
# from summarizer import Summarizer
#
# # Set Streamlit page configuration (must be first)
# st.set_page_config(
#     page_title="Advanced Text Summarization Tool",
#     page_icon="📚",
#     layout="wide"
# )
#
# # Load the abstractive model and tokenizer
# abstractive_model_dir = './saved_model'  # Path to your saved abstractive model files
# abstractive_model = BartForConditionalGeneration.from_pretrained(abstractive_model_dir)
# abstractive_tokenizer = BartTokenizer.from_pretrained(abstractive_model_dir)
#
# # Load the extractive model from a local directory or fallback to pre-trained
# extractive_model_dir = './extractive_saved_model'  # Path to your saved extractive model files
# if os.path.exists(extractive_model_dir) and os.path.isdir(extractive_model_dir):
#     try:
#         # Try loading the custom extractive model from the local directory
#         extractive_model = Summarizer(model=extractive_model_dir)
#     except Exception as e:
#         st.error(f"Error loading custom extractive model: {e}")
#         extractive_model = None
# else:
#     st.warning(f"The directory {extractive_model_dir} does not exist. Falling back to pre-trained extractive model.")
#     extractive_model = Summarizer()
#
# # Custom CSS for improved UI
# st.markdown("""
#     <style>
#         .main {
#             background-color: #f0f8ff;
#             font-family: 'Helvetica', sans-serif;
#         }
#         .stButton>button {
#             background-color: #0073e6;
#             color: white;
#             font-size: 16px;
#             border-radius: 8px;
#             padding: 10px 15px;
#             transition: background-color 0.3s ease;
#         }
#         .stButton>button:hover {
#             background-color: #005bb5;
#             border-color: white;
#             color: white;
#         }
#         .summary-box {
#             background-color: #fff;
#             border: 1px solid #ddd;
#             border-radius: 8px;
#             padding: 15px;
#             font-size: 16px;
#             color: #000;
#             line-height: 1.5;
#             white-space: pre-wrap;
#             height: auto;
#         }
#         .column-left {
#             padding-right: 20px;
#         }
#         .column-right {
#             padding-left: 20px;
#         }
#     </style>
# """, unsafe_allow_html=True)
#
# # App title and description
# st.title("📚 Advanced Text Summarization Tool")
# st.markdown("""
#     Generate high-quality summaries from your text inputs or uploaded files. Choose between abstractive and extractive methods,
#     and select your desired summary style!
# """)
#
# # Create two columns: left for input, right for output
# col1, col2 = st.columns([1, 2])
#
# # Left Column (Input Section)
# with col1:
#     # Summarization type selection
#     summarization_type = st.radio(
#         "Select Summarization Type",
#         ["Abstractive", "Extractive"],
#         help="Choose between abstractive and extractive summarization methods."
#     )
#
#     # Summary style selection
#     summary_style = st.selectbox(
#         "Choose Summary Style",
#         ["Concise", "Detailed", "Headline"],
#         help="Select how you want the summary to be structured."
#     )
#
#     # Input options
#     uploaded_file = st.file_uploader("Upload a text file (TXT only):", type=['txt'], help="Upload a .txt file for summarization.")
#     input_text = st.text_area("Or, paste your text here:", height=300, placeholder="Paste your text here...")
#
#     # Generate summary button
#     generate_summary = st.button("Generate Summary")
#
# # Right Column (Summary Section)
# with col2:
#     if generate_summary:
#         # Load content from file if uploaded, otherwise from text input
#         if uploaded_file is not None:
#             content = uploaded_file.read().decode('utf-8')
#             input_text = content
#
#         if input_text.strip():
#             # Parameters for each summarization style
#             if summarization_type == "Abstractive":
#                 style_params = {"Concise": 300, "Detailed": 600, "Headline": 50}
#                 max_length = style_params[summary_style]
#             else:  # Extractive
#                 style_params = {"Concise": 0.2, "Detailed": 0.4, "Headline": 1}
#                 extractive_param = style_params[summary_style]
#
#                 # Ensure extractive_param is set to 1 for "Headline" style
#                 if summary_style == "Headline":
#                     extractive_param = 1
#                 else:
#                     extractive_param = int(extractive_param * len(input_text.split('.')))  # Number of sentences based on input text
#
#             # Generate the summary
#             if summarization_type == "Abstractive":
#                 # Abstractive summarization
#                 inputs = abstractive_tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512).to("cpu")
#                 summary_ids = abstractive_model.generate(
#                     inputs["input_ids"],
#                     max_length=max_length,
#                     min_length=max_length // 2,
#                     num_beams=4,
#                     early_stopping=True,
#                     length_penalty=2.0 if summary_style == "Detailed" else 1.0
#                 )
#                 summary = abstractive_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#
#             elif summarization_type == "Extractive":
#                 if extractive_model:
#                     # Extractive summarization using bert-extractive-summarizer
#                     summary = extractive_model(input_text, num_sentences=extractive_param)
#                 else:
#                     summary = "Error: Could not load extractive model."
#
#             # Display the summary in a box
#             st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
#
#             # Add download button
#             st.download_button(
#                 label="📥 Download Summary as Text",
#                 data=summary,
#                 file_name="summary.txt",
#                 mime="text/plain"
#             )
#         else:
#             st.warning("Please enter text or upload a file to summarize.")
#

import os
import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer, AutoTokenizer, AutoModelForSequenceClassification
import torch

# Set Streamlit page configuration
st.set_page_config(
    page_title="Advanced Text Summarization Tool",
    page_icon="📚",
    layout="wide"
)

# Load the abstractive model and tokenizer
abstractive_model_dir = './saved_model'  # Path to your saved abstractive model files
abstractive_model = BartForConditionalGeneration.from_pretrained(abstractive_model_dir)
abstractive_tokenizer = BartTokenizer.from_pretrained(abstractive_model_dir)

# Load the extractive model and tokenizer
extractive_model_dir = './extractive_saved_model'  # Path to your saved extractive model files
try:
    extractive_tokenizer = AutoTokenizer.from_pretrained(extractive_model_dir)
    extractive_model = AutoModelForSequenceClassification.from_pretrained(extractive_model_dir)
except Exception as e:
    extractive_tokenizer, extractive_model = None, None
    st.warning(f"Error loading extractive model: {e}")

# Custom CSS for UI enhancement
st.markdown("""
    <style>
        .main {background-color: #f0f8ff; font-family: 'Helvetica', sans-serif;}
        .stButton>button {background-color: #0073e6; color: white; font-size: 18px; border-radius: 8px; padding: 12px 18px; transition: background-color 0.3s ease;}
        .stButton>button:hover {background-color: #005bb5; border-color: white; color: white;}
        .summary-box {background-color: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 20px; font-size: 18px; color: #000; line-height: 1.8; white-space: pre-wrap; height: auto;}
        .section-title {font-size: 22px; font-weight: bold; margin-bottom: 15px; color: #333;}
        .preview-box {background-color: #f9f9f9; border: 1px solid #ccc; border-radius: 8px; padding: 15px; font-size: 16px; color: #555; margin-bottom: 20px; white-space: pre-wrap; height: auto; max-height: 200px; overflow-y: auto;}
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("📚 Advanced Text Summarization Tool")
st.markdown("""
    Generate high-quality summaries from your text inputs or uploaded files. Choose between **abstractive** and **extractive** summarization methods,
    and select your desired summary style!
""")

# Create input and output columns
col1, col2 = st.columns([1, 2])

# Left Column (Input Section)
with col1:
    summarization_type = st.radio("Select Summarization Type", ["Abstractive", "Extractive"])
    summary_style = st.selectbox("Choose Summary Style", ["Concise", "Detailed", "Headline"])
    uploaded_file = st.file_uploader("Upload a text file (TXT only):", type=['txt'])
    input_text = st.text_area("Or, paste your text here:", height=300, placeholder="Paste your text here...")

    # Preview uploaded file content
    if uploaded_file is not None:
        content = uploaded_file.read().decode('utf-8')
        st.markdown('<div class="section-title">Preview Uploaded File</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="preview-box">{content}</div>', unsafe_allow_html=True)
        input_text = content  # Use uploaded content as input

    generate_summary = st.button("Generate Summary")


# Function for extractive summarization
def extractive_summarize(text, num_sentences=3):
    if not extractive_model or not extractive_tokenizer:
        return "Error: Extractive summarization model could not be loaded."

    sentences = text.split('. ')
    inputs = extractive_tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

    with torch.no_grad():
        outputs = extractive_model(**inputs)
        scores = outputs.logits.squeeze(-1).tolist()

    ranked_sentences = sorted(zip(scores, sentences), reverse=True)[:num_sentences]
    ranked_sentences = [sent for _, sent in ranked_sentences]
    return '. '.join(ranked_sentences)


# Right Column (Output Section)
with col2:
    if generate_summary:
        if input_text.strip():
            # Abstractive summarization logic
            if summarization_type == "Abstractive":
                style_params = {"Concise": 300, "Detailed": 600, "Headline": 50}
                max_length = style_params[summary_style]

                inputs = abstractive_tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512).to(
                    "cpu")
                summary_ids = abstractive_model.generate(
                    inputs["input_ids"],
                    max_length=max_length,
                    min_length=max_length // 2,
                    num_beams=4,
                    early_stopping=True,
                    length_penalty=2.0 if summary_style == "Detailed" else 1.0
                )
                summary = abstractive_tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            # Extractive summarization logic
            elif summarization_type == "Extractive":
                style_params = {"Concise": 3, "Detailed": 5, "Headline": 1}
                num_sentences = style_params[summary_style]
                summary = extractive_summarize(input_text, num_sentences)

            # Display the summary
            st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)

            # Add space between summary and download button
            st.markdown("<br>", unsafe_allow_html=True)

            # Download button for the summary
            st.download_button(
                label="📥 Download Summary as Text",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )
        else:
            st.warning("Please enter text or upload a file to summarize.")
