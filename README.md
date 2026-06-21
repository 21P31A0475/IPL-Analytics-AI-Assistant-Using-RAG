# IPL Analytics AI Assistant Using RAG

## Project Overview

IPL Analytics AI Assistant is a Generative AI project that combines Retrieval-Augmented Generation (RAG) with Large Language Models (LLMs) to provide intelligent insights from Indian Premier League (IPL) cricket data.

The assistant allows users to ask natural language questions about IPL matches, teams, players, records, statistics, and historical performance, and receive accurate, context-aware responses grounded in IPL datasets.

---

## Problem Statement

IPL datasets contain large volumes of match statistics, player records, team performance metrics, and historical data.

Finding meaningful insights manually can be time-consuming and difficult for analysts, cricket enthusiasts, and decision-makers.

This project solves the problem by creating an AI-powered assistant capable of retrieving relevant IPL information and generating human-like responses instantly.

---

## Objectives

* Build an AI-powered IPL analytics chatbot.
* Enable natural language querying of IPL data.
* Retrieve relevant cricket statistics using vector search.
* Generate context-aware responses using LLMs.
* Improve answer accuracy through Retrieval-Augmented Generation (RAG).

---

## Technologies Used

* Python
* LangChain
* ChromaDB
* Grok / OpenAI / Gemini / LLM APIs
* Sentence Transformers
* Pandas
* NumPy
* Streamlit
* Jupyter Notebook

---

## Dataset

The project utilizes IPL historical datasets containing:

* Match Information
* Team Statistics
* Player Statistics
* Batting Records
* Bowling Records
* Venue Information
* Season-wise Performance
* Match Results

---

## Project Workflow

### 1. Data Collection

* Load IPL datasets.
* Combine multiple cricket-related data sources.
* Clean and preprocess records.

### 2. Data Preprocessing

* Format statistics.
* Convert structured data into textual documents.

### 3. Document Chunking

* Split large documents into smaller chunks.
* Optimize chunk size for retrieval performance.

### 4. Embedding Generation

* Convert text chunks into vector embeddings.
* Capture semantic meaning of IPL statistics.

### 5. Vector Database Creation

* Store embeddings in FAISS / ChromaDB.
* Enable similarity-based retrieval.

### 6. Retrieval-Augmented Generation (RAG)

* Retrieve the most relevant IPL information.
* Pass retrieved context to the LLM.
* Generate accurate answers grounded in the dataset.

### 7. User Interface

* Build an interactive chatbot using Streamlit.
* Accept natural language questions.
* Display responses in real time.

---

## Features

### Cricket Analytics Chatbot

Ask questions such as:

* Who scored the most runs in IPL history?
* Which team won the IPL in 2016?
* What is Virat Kohli's IPL performance?
* Which bowler has the most wickets?
  
### Context-Aware Responses

The assistant retrieves relevant information before generating answers.

### Fast Semantic Search

Uses vector similarity search to find relevant cricket records.

### Natural Language Interaction

No SQL queries or manual filtering required.

---

## Applications

* Cricket Analytics
* Sports Intelligence
* Fan Engagement Platforms
* Sports Journalism
* Fantasy Cricket Research
* Performance Analysis

---

## Future Enhancements

* Live IPL data integration.
* Real-time match analysis.
* Player performance prediction.
* Multi-language support.
* Voice-enabled AI assistant.
* Advanced visualization dashboards.

---

## Key Learning Outcomes

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Models
* Large Language Models (LLMs)
* Semantic Search
* Prompt Engineering
* Streamlit Deployment
* End-to-End Generative AI Development

---

## Project Outcomes

* Developed an AI-powered cricket analytics assistant.
* Implemented semantic retrieval using vector embeddings.
* Improved response accuracy using RAG architecture.
* Enabled natural language access to IPL statistics.
* Built an interactive Generative AI application.
