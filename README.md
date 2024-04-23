# Abstract

This project demonstrates a mechanism for retrieving web documents. Web crawling, document indexing, and query processing are all integrated using Python and specialized libraries. The objective is providing accurate and pertinent search results in a user-friendly manner.

## Overview

In this project, we are developing a search engine that utilizes TF-IDF (Term Frequency-Inverse Document Frequency) scoring to retrieve and rank web content. The solution outline and proposed system consists of 3 main components: a web crawler, indexing engine, and query processor. The development process encompasses several pivotal stages to ensure robust and precise search capabilities. Two separate APIs are developed to output top search results based on both standard and advanced indexing methods. This project is informed by Scikit-Learn documentation, recent research on semantic search and KNN methods.

## Design

### System Capabilities

The system has the following functionalities:

- **Web crawling:** The system uses a web crawler built on Scrapy to retrieve web documents from specified URLs while adhering to constraints like traversal depth and maximum page count.
  
- **Indexing:** The system uses a Scikit-Learn-based indexing approach to create an inverted index using TF-IDF scores. It also has advanced features like incorporating word embeddings and utilizing FAISS for improved similarity search.
  
- **Query Processing:** Using cosine similarity and TF-IDF scores, the Flask processor processes user queries, verifies them, and returns the best results. Spell check and query expansion options are also included.

### Interactions

- **Web Crawling to Indexing:** The indexing engine uses crawled web content to produce an inverted index with TF-IDF scores.
  
- **Indexing to Query Processing:** For the purpose of retrieving pertinent documents in response to user requests, the indexing engine generates an inverted index.
  
- **User Interaction:** By entering queries and obtaining search results, users communicate with the system via the Flask-based query processor.

### Integration

Two APIs handle search using standard and advanced indexing, connecting with the indexing engine and query processor. Web data goes to the indexing engine, then to the query processor, which interacts with both APIs. The modular design allows for future feature additions, ensuring an efficient system for accurate search results.

## Architecture

### Software components

1. **Web Crawler:** A Scrapy-based crawler for fetching web documents.
  
2. **Indexing Engine:** Scikit-Learn-based engine for TF-IDF indexing and optional advanced methods like word embeddings and FAISS.
  
3. **Query Processor:** Flask-based module for handling user queries, validation, and result retrieval.
  
4. **APIs:** Two separate APIs to serve search results based on standard and advanced indexing methods.

### Interfaces

- **API Interfaces:** RESTful APIs for search functionality.
  
- **Data Interface:** Interaction between the crawler, indexing engine, and query processor through data pipelines.

The architecture is designed to ensure seamless interaction between components, with clear interfaces for data flow and modular implementation for scalability and extensibility.

## Operation

### Installations

- Install Python and Linux on Windows: `wsl –install`
  
- Install required libraries:
  ```bash
  pip install scrapy
  pip install scikit-learn
  pip install beautifulsoup4
  pip install flask
  pip install requests
## Instructions to Run the Project

### Step 1
To run the project, navigate to the `spiders` folder in the terminal and enter the following command:
scrapy crawl <file name>
The TF-IDF scores and cosine similarity for the HTML documents will be calculated and stored in an `index.pkl` file.

### Step 2
To access the `index.pkl` file, navigate to the `access pickle` folder in the terminal and run the Python file. The content of the file will be displayed in the terminal.

### Step 3
To start the Flask server, navigate to the `Flask` folder in the terminal and run the Python file located in that folder.

### Step 4
Once the Flask server is initiated, open a new terminal and make a request to the Flask server with a query in the following format:
```bash
curl -X POST http://localhost:5000/query -H "Content-Type: application/json" -d '{"query": "DSA"}'
You will receive a JSON format response from the server which includes cosine similarity and document names of the top k results.
```
## Conclusion

The project demonstrates that both APIs return relevant documents as output. However, the ranking of the documents requires improvement. The Scikit-learn API also returns relevant documents for all queries; however, the precision could be enhanced. For certain additional inquiries, the results remain consistent across all three circumstances.
