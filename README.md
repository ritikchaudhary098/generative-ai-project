# 🤖 AI Chatbot using LangChain + Mistral

An interactive AI chatbot built using **LangChain**, **Mistral AI**, and **Streamlit**.
This project demonstrates how to integrate Large Language Models (LLMs) into a real-time web application.

---

## 🚀 Features

* 💬 ChatGPT-like interactive UI
* ⚡ Real-time AI responses
* 🧠 Session-based chat memory
* 🖥️ Clean and responsive interface
* 🔄 Easy to extend with RAG (PDF, docs, etc.)

---

## 🛠️ Tech Stack

* Python
* LangChain
* Mistral AI
* Streamlit
* uv (package manager)

---

## 📂 Project Structure

```
generative-ai/
│
├── app.py                # Streamlit UI
├── chatmodels/
│   └── chat.py          # CLI chatbot (backend testing)
├── pyproject.toml       # Dependencies
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-chatbot-langchain.git
cd ai-chatbot-langchain
```

---

### 2️⃣ Install dependencies

```
uv sync
```

---

### 3️⃣ Add API Key

Create a `.env` file in the root folder:

```
MISTRAL_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the application

```
uv run streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🧪 Run CLI Chatbot (Optional)

```
uv run python chatmodels/chat.py
```

---

## 📸 Demo

*Add a screenshot or screen recording here*

---

## 💡 Future Improvements

* 📄 PDF-based Q&A (RAG)
* 🎤 Voice input
* 🌍 Deploy on cloud (Streamlit Cloud / Render)
* 🗄️ Database for persistent chat history

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 👨‍💻 Author

**Ritik Chaudhary**

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
