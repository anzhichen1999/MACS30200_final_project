import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
import torch
from torch.nn.functional import softmax
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
import torch
from torch.nn.functional import softmax

class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_len=512):
        self.tokenizer = tokenizer
        self.texts = texts
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = str(self.texts[item])
        inputs = self.tokenizer.encode_plus(
            text,
            None,
            add_special_tokens=True,
            max_length=self.max_len,
            padding='max_length',
            return_token_type_ids=False,
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        return {
            'input_ids': inputs['input_ids'].flatten(),
            'attention_mask': inputs['attention_mask'].flatten()
        }



# Instantiate tokenizer and model from Hugging Face
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Check if CUDA is available and move the model to the GPU if possible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
model = model.to(device)

# Prepare your DataLoader
dataset = TextDataset(df['selftext'].tolist(), tokenizer)
loader = DataLoader(dataset, batch_size=16)

# Define your predict_sentiment function
def predict_sentiment(data_loader, model):
    model.eval()
    probabilities = []
    total_batches = len(data_loader)
    with torch.no_grad():
        for batch_num, d in enumerate(data_loader, start=1):
            input_ids = d["input_ids"].to(device)
            attention_mask = d["attention_mask"].to(device)
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            batch_probs = softmax(outputs.logits, dim=1)
            probabilities.extend(batch_probs.cpu().numpy())
            print(f'Processing batch {batch_num}/{total_batches}...')
    return probabilities

# Apply your sentiment prediction function
df['selftext_sentiment_probabilities'] = predict_sentiment(loader, model)
df['selftext_predicted_rating'] = df['selftext_sentiment_probabilities'].apply(lambda x: x.argmax() + 1)


# tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
# model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# model = model.to('cuda')

# # Prepare DataLoader
# dataset = TextDataset(df['selftext'].tolist(), tokenizer)
# loader = DataLoader(dataset, batch_size=16)


# def predict_sentiment(data_loader, model):
#     model.eval()
#     probabilities = []
#     total_batches = len(data_loader)
#     with torch.no_grad():
#         for batch_num, d in enumerate(data_loader, start=1):
#             input_ids = d["input_ids"].to('cuda')
#             attention_mask = d["attention_mask"].to('cuda')
#             outputs = model(input_ids=input_ids, attention_mask=attention_mask)
#             batch_probs = softmax(outputs.logits, dim=1)
#             probabilities.extend(batch_probs.cpu().numpy())
#             print(f'Processing batch {batch_num}/{total_batches}...')
#     return probabilities


# df['selftext_sentiment_probabilities'] = predict_sentiment(loader, model)
# df['selftext_predicted_rating'] = df['selftext_sentiment_probabilities'].apply(lambda x: x.argmax() + 1)

import numpy as np

def calculate_expected_value(probabilities):
    ratings = np.array([1, 2, 3, 4, 5])
    expected_value = np.sum(probabilities * ratings)
    return expected_value

def normalize_to_scale(value, scale_min=1, scale_max=5, target_min=-1, target_max=1):
    normalized_value = ((value - scale_min) / (scale_max - scale_min)) * (target_max - target_min) + target_min
    return normalized_value


new_scale_ratings = []
for probs in df['sentiment_probabilities']:
    expected_value = calculate_expected_value(np.array(probs))
    normalized_value = normalize_to_scale(expected_value)
    new_scale_ratings.append(normalized_value)


df['normalized_sentiment'] = new_scale_ratings