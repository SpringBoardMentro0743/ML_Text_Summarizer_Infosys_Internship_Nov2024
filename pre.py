import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from langdetect import detect
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

input_folder = "C:\\Users\\ANSH PANT\\Downloads\\data"
output_folder = "C:\\Users\\ANSH PANT\\Downloads\\preprocessing"

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_words = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_words)

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(lemmatized_words)

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

synonym_dict = {
    "NLP": "Natural Language Processing",
    "AI": "Artificial Intelligence"
}

def replace_synonyms(text):
    words = text.split()
    return ' '.join([synonym_dict.get(word, word) for word in words])

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)        
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_text = file.read()
        if is_english(raw_text):
            cleaned_text = clean_text(raw_text)
            cleaned_text = remove_stop_words(cleaned_text)
            cleaned_text = lemmatize_text(cleaned_text)
            cleaned_text = replace_synonyms(cleaned_text)
            output_path = os.path.join(output_folder, f"processed_{filename}")
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(cleaned_text)