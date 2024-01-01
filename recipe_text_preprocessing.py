import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pandas as pd

# Load your data
recipes = pd.read_csv('RAW_recipes.csv')

# Initialize NLP tools
nltk.download('stopwords')
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Define a preprocessing function
def preprocess_text(text):
    if not isinstance(text, str):
        text = str(text)
    # Tokenization
    tokens = nltk.word_tokenize(text)
    # Lowercasing
    tokens = [word.lower() for word in tokens]
    # Stop words elimination
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # Stemming
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# Apply preprocessing to each column and exclude all RAW columns
processed_columns = []
for column in recipes.columns:
    recipes[column] = recipes[column].apply(preprocess_text)
    processed_columns.append(column)

# Write the processed data to a new file, excluding all RAW columns
result_df = recipes[processed_columns]
result_df.to_csv('processed_recipes.csv', index=False)
