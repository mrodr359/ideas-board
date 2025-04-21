# 🧠 Ideas Board API

A simple Flask-based API to submit, retrieve, and delete ideas — like startup ideas, reminders, or project concepts.  
Data is stored locally using SQLite, and the project is containerized with Docker.

---

## 🚀 Features

- Submit new ideas
- Retrieve all submitted ideas
- Retrieve a single idea by ID
- Delete an idea by ID
- Lightweight and fast
- No external API or payment required

---

## 🛠️ Tech Stack

- Python 3.12
- Flask
- SQLAlchemy (ORM)
- SQLite (Database)
- Docker

---

## 📦 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR-USERNAME/ideas-board.git
    cd ideas-board
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application locally:
    ```bash
    python app.py
    ```

4. Access the API at:
    ```
    http://localhost:5000
    ```

---

## 🐳 Run with Docker

1. Build the Docker image:
    ```bash
    docker build -t ideas-board .
    ```

2. Run the container:
    ```bash
    docker run -p 5000:5000 ideas-board
    ```

---

## 📋 API Endpoints

| Method | Endpoint | Description |
|:---|:---|:---|
| POST | `/ideas` | Submit a new idea |
| GET | `/ideas` | Get all ideas |
| GET | `/ideas/{id}` | Get a single idea by ID |
| DELETE | `/ideas/{id}` | Delete an idea by ID |

---

## ✨ Future Improvements

- Add user authentication
- Add categories/tags for ideas
- Add pagination for large lists
- Deploy to a public cloud platform

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧑‍💻 Author

Created by [Manny Rodriguez](https://github.com/mrodr359)

