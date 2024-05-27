import pandas as pd

%%capture
!pip install bertopic
%%capture
!pip install git+https://github.com/MaartenGr/BERTopic.git@master

!pip install cudf-cu12 dask-cudf-cu12 --extra-index-url=https://pypi.nvidia.com
!pip install cuml-cu12 --extra-index-url=https://pypi.nvidia.com
!pip install cugraph-cu12 --extra-index-url=https://pypi.nvidia.com
!pip install cupy-cuda12x -f https://pip.cupy.dev/aarch64

!pip install safetensors
!pip install datasets
!pip install datashader
!pip install adjustText

import nltk
from nltk.corpus import stopwords
import string
from langdetect import detect
from sentence_transformers import SentenceTransformer
import collections
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups
from cuml.manifold import UMAP
from cuml.cluster import HDBSCAN


file_path = F://PreprocessedText.csv
data = pd.read_csv(file_path)

titles = []
Texts = []
timestamps = []

import re
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Extract title and content
        split_line = line.split(',', 2)  # Split only on the first two commas to preserve Text data format
        if len(split_line) < 3:
            continue  # Skip lines that do not contain enough data

        title = split_line[0]
        content = split_line[2]

        # Find all Text and timestamp matches
        matches = re.findall(pattern, content)
        for match in matches:
            titles.append(title)
            Texts.append(match[0])
            timestamps.append(pd.to_datetime(match[1], errors='coerce'))

data = pd.DataFrame({
    'Title': title
    'Text': Texts,
    'Timestamp': timestamps
})

label_data_filtered = label_data[['title, 'Park', 'Business_Center']].drop_duplicates()

merged_data = pd.merge(data, label_data_filtered, on='title', how='left')
merged_data['Park'].fillna(0, inplace = True)
merged_data['Business_Center'].fillna(0, inplace = True)

def preprocess_text(text):
    try:
        if detect(text) != 'en':
            return None
    except:
        return None

    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation and not char.isdigit()])
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

merged_data['Cleaned_Text'] = merged_data['Text'].apply(preprocess_text)
merged_data = merged_data.dropna(subset=['Cleaned_Text'])

business_Texts = merged_data[merged_data['Business_Center'] == 1]

business_Texts['Timestamp_business'] = pd.to_datetime(business_Texts['Timestamp'])
business_Texts = business_Texts.dropna(subset=['Timestamp_business'])  # Drop rows with NaT values
business_Texts['Timestamp_business_ordinal'] = business_Texts['Timestamp_business'].apply(lambda x: x.toordinal())

texts = business_Texts['Cleaned_Text'].tolist()
timestamps = business_Texts['Timestamp_business_ordinal'].tolist()
titles = business_Texts['title'].tolist()

from sentence_transformers import SentenceTransformer

# Create embeddings
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = embedding_model.encode(texts, show_progress_bar=True)

embeddings = np.load('F:/embeddings.npy')



vocab = collections.Counter()
tokenizer = CountVectorizer().build_tokenizer()
for doc in tqdm(texts):
    vocab.update(tokenizer(doc))
vocab = [word for word, frequency in vocab.items() if frequency >= 15]

umap_model = UMAP(n_components=5, n_neighbors=50, random_state=42, metric="cosine", verbose=True)
hdbscan_model = HDBSCAN(min_samples=20, gen_min_span_tree=True, prediction_data=True, min_cluster_size=20, verbose=True)
vectorizer_model = CountVectorizer(vocabulary=vocab
                                   
                                  
topic_model = BERTopic(
    embedding_model=embedding_model,
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    vectorizer_model=vectorizer_model,
    verbose=True,
    nr_topics = 11
).fit(texts, embeddings=embeddings))

topic_model.save("F:/bertopic_model")
topic_model = BERTopic.load("F:/bertopic_model")

docs_info = topic_model.get_document_info(docs=texts)
topic_8_docs = docs_info[docs_info['Topic'] == 8]

most_frequent_topic = 0
new_topics = [most_frequent_topic if topic == 8 else topic for topic in docs_info['Topic']]
topic_model.update_topics(docs=texts, topics=new_topics)

