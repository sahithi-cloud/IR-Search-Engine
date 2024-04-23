import pickle
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


index_location = '/mnt/c/Users/DELL/Documents/IR/IR/spiders/index.pkl'

with open(index_location, 'rb') as f:
    index = pickle.load(f)

vector = TfidfVectorizer()
tfidf = vector.fit_transform([doc['document'] for doc in index.values()])

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    queryjson = request.json
    query = queryjson.get('query', '')

    queryvector = vector.transform([query])
    cosinesimilarities = cosine_similarity(queryvector, tfidf).flatten()
    k = min(5, len(cosinesimilarities))
    topk_indices = cosinesimilarities.argsort()[-k:][::-1]

    results = [{'cosine_similarity': cosinesimilarities[idx], 
                'document_name': index[idx]['document_name']} for idx in topk_indices]
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
