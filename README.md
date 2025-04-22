# 🦜🔗 StreamlitSimpleChat

A simple interactive chatbot app built with [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/), using **Azure OpenAI** as the backend model.

---

## 🚀 Features

- 💬 Chat with GPT (via Azure OpenAI)
- 🔐 Secure API key entry via Streamlit sidebar
- ⚙️ Customize deployment name and endpoint
- 📦 Lightweight & easy to run

---

## 📦 Requirements

Install dependencies via `pip`:

```bash
pip install -r requirements.txt
```

> Note: You’ll also need an **Azure OpenAI account** with a deployed model (like `gpt-4o`).

---

## 🧪 Run the App

Make sure your virtual environment is activated, then:

```bash
streamlit run streamlit_app.py
```

---

## 🔐 Azure OpenAI Setup

When you launch the app, enter the following in the sidebar:

- **API Key** → Your Azure OpenAI API key
- **Endpoint** → Your Azure endpoint, e.g., `https://your-resource-name.openai.azure.com/`
- **Deployment Name** → The name of your deployed model (e.g., `gpt-4o`)

---

## 📁 Project Structure

```text
├── .venv/                 # Virtual environment (ignored)
├── streamlit_app.py       # Main Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # You are here!
```

---

## 🧠 Credits

Built using:
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)

---

## 📝 License

MIT – feel free to modify and share!
