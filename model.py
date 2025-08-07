import ast
import pickle

import pandas as pd
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
credits = pd.read_csv("tmdb_5000_credits.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")

# Merge datasets
merged = movies.merge(credits, on="title")[['movie_id', 'genres', 'cast', 'crew', 'keywords', 'title', 'overview']]
merged.dropna(inplace=True)

# Helper functions
def convert(obj):
    return [i['name'] for i in ast.literal_eval(obj)]

def convert5(obj):
    L = []
    for i in ast.literal_eval(obj):
        if len(L) < 5:
            L.append(i['name'])
        else:
            break
    return L

def fetch_director(obj):
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            return [i['name']]
    return []

def stem(text):
    ps = PorterStemmer()
    return " ".join([ps.stem(i) for i in text.split()])

# Apply transformations
merged['genres'] = merged['genres'].apply(convert)
merged['keywords'] = merged['keywords'].apply(convert)
merged['cast'] = merged['cast'].apply(convert5)
merged['crew'] = merged['crew'].apply(fetch_director)
merged['overview'] = merged['overview'].apply(lambda x: x.split())

# Remove spaces in words
for feature in ['genres', 'keywords', 'cast', 'crew']:
    merged[feature] = merged[feature].apply(lambda x: [i.replace(" ", "") for i in x])

# Create tags
merged['tags'] = merged['overview'] + merged['cast'] + merged['crew'] + merged['keywords'] + merged['genres']
new_df = merged[['movie_id', 'title', 'tags']].copy()
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())
new_df['tags'] = new_df['tags'].apply(stem)

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(new_df, open('movies.pkl', 'wb'))
pickle.dump(new_df.to_dict(), open('movie_dict.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

if __name__ == "__main__":
    print("✅ Running model pipeline...")
    print(f"Movies data shape: {new_df.shape}")
    print("✅ Similarity matrix generated.")
    print("✅ Pickle files saved: movies.pkl, movie_dict.pkl, similarity.pkl")
