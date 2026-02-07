# 🎓 University FAQ Assistant

An AI-powered University FAQ Assistant built using a Retrieval-Augmented Generation (RAG) architecture.  
The system enables students to ask natural language questions and receive accurate, document-grounded answers from official university documents.

---

## 🚀 Features
- Natural language question answering
- Document-based retrieval using vector search (FAISS)
- Source citation for transparency
- Scalable document ingestion pipeline
- Clean web-based chat interface

---

## 🧠 Architecture
The project follows a Retrieval-Augmented Generation (RAG) workflow:

1. University documents (PDFs) are ingested and processed.
2. Text chunks are converted into vector embeddings.
3. FAISS is used for efficient similarity search.
4. Relevant document chunks are retrieved for a user query.
5. A response is generated based on retrieved context.

---

## 🛠️ Tech Stack
- Python 3.10
- Streamlit (Frontend)
- FAISS (Vector Database)
- PyPDF (Document Parsing)
- NumPy
- Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure
university_faq_bot/
├── data/
│ ├── admission_policy.pdf
│ ├── fee_structure.pdf
│ └── hostel_rules.pdf
├── generate_pdfs.py
├── ingest.py
├── rag.py
├── app.py
├── requirements.txt
├── faiss.index
└── sources.pkl


---

## ▶️ How to Run
```bash
pip install -r requirements.txt
python generate_pdfs.py
python ingest.py
streamlit run app.py

📌 Example Queries

What is the eligibility for admission?

What is the hostel curfew time?

What is the B.Tech fee structure?

📈 Future Enhancements

Real LLM integration (OpenAI / Gemini)

Admin dashboard for document upload

Multilingual support

Authentication for students and staff


👨‍💻 Author

Avinash Raj
B.Tech IT, 3rd Year
