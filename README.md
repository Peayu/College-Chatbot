# 🤖 College FAQ Chatbot

An intelligent FAQ chatbot that answers common college-related questions using **TF-IDF vectorization and cosine similarity**. The chatbot compares a user's question with a predefined FAQ corpus and returns the answer associated with the most similar question.

🔗 **Live Demo:** [College FAQ Chatbot](https://college-chatbot-2be6.onrender.com/)

---

## 📌 Features

* 💬 Answers common college-related questions
* 🔎 Uses **TF-IDF vectorization** to represent questions numerically
* 📐 Uses **cosine similarity** to find the closest FAQ
* 📚 Contains a self-created FAQ corpus with 30+ questions
* 🎯 Uses a similarity threshold to determine whether a question is relevant
* 🚨 Provides a fallback response for unknown or unrelated questions
* 💻 Interactive chat interface built with Streamlit
* ☁️ Deployed on Render

---

## 🧠 How It Works

The chatbot follows a simple text-matching pipeline:

```text
             User Question
                   ↓
           TF-IDF Transformation
                   ↓
          Numerical Representation
                   ↓
          Cosine Similarity
                   ↓
       Compare with FAQ Corpus
                   ↓
          Find Highest Score
                   ↓
       Is Score ≥ 0.56?
          /          \
        YES           NO
         ↓             ↓
      Answer        Fallback
```

The chatbot does **not** use a trained language model or external AI API. Instead, it uses traditional NLP techniques to match the user's question with the most similar question in the FAQ corpus.

---

## 🔍 Question Matching

The chatbot uses **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert the FAQ questions into numerical vectors.

When a user enters a question, it is transformed using the same TF-IDF vectorizer.

The chatbot then calculates **cosine similarity** between the user's question and every question in the corpus.

The question with the highest similarity score is selected as the best match.

For example:

```text
User:
"When does the college open?"

        ↓

FAQ:
"What are the college timings?"

        ↓

Cosine Similarity

        ↓

Highest matching FAQ

        ↓

Return predefined answer
```

---

## 🚨 Fallback System

The chatbot uses a similarity threshold of **0.56**.

If the highest similarity score is at least `0.56`, the corresponding FAQ answer is returned.

If the score is below `0.56`, the chatbot returns a fallback response:

```text
Sorry, Ask a relevant question.
```

This prevents the chatbot from returning an unrelated answer when the user's question is outside the FAQ corpus.

---

## 📚 FAQ Corpus

The chatbot uses a self-created corpus containing questions and predefined answers.

Each FAQ follows this structure:

```python
{
    "question": "What are the college timings?",
    "answer": "The college operates from 9:00 AM to 4:00 PM, Monday to Friday."
}
```

The current corpus covers topics such as:

* College timings
* Working days
* Library timings
* Attendance requirements
* Examination schedules
* Leave policies
* Fee payments
* Student ID cards
* Courses
* Student support

---

## 🛠️ Technologies Used

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Core programming and chatbot logic |
| Scikit-learn | TF-IDF and cosine similarity       |
| Streamlit    | Interactive web interface          |
| Render       | Application deployment             |

---

## 📂 Project Structure

```text
college-chatbot/
│
├── app.py
├── Chatbot.py
├── requirements.txt
└── README.md
```

### `app.py`

Handles the Streamlit interface, user input, and chat history.

### `Chatbot.py`

Contains:

* FAQ corpus
* TF-IDF vectorizer
* FAQ vectorization
* Cosine similarity
* Question matching
* Similarity threshold
* Fallback response

---

## 💻 Running Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd college-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project requires:

```text
streamlit
scikit-learn
```

These can be installed using:

```bash
pip install -r requirements.txt
```

---

## ☁️ Deployment

The application is deployed on **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

### Live Application

**https://college-chatbot-2be6.onrender.com/**

---

## 📊 Evaluation

The chatbot can be evaluated using:

### Matching Accuracy

Measures how often the chatbot selects the correct FAQ for a known question.

### Answer Relevance

Measures whether the returned predefined answer appropriately addresses the user's question.

### Fallback Rate

Measures how frequently the chatbot cannot find a sufficiently similar question.

```text
Fallback Rate =
Number of fallback responses
----------------------------
Total questions
```

---

## 🔮 Future Improvements

Possible extensions include:

* Add more FAQ questions and alternative phrasings
* Add multilingual question support
* Add voice input
* Replace TF-IDF with semantic embeddings
* Add an LLM-based fallback
* Store FAQs in a database
* Add analytics for frequently asked questions
* Add human support escalation

---

## 🎯 Project Information

**Project:** Intelligent FAQ Chatbot
**Domain:** Artificial Intelligence
**Sub-Domain:** Conversational Systems
**Primary Technology:** TF-IDF-based question matching and cosine similarity

---

## 👨‍💻 Author

Developed as an Artificial Intelligence project demonstrating **Python programming, NLP fundamentals, text similarity, and Streamlit application development**.
