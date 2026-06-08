# ChatAPP FastAPI Backend

This project is a robust Backend System for a real-time chat application and video management platform, built using **FastAPI**.

## 🚀 Key Features
* **Authentication**: Secure user authentication using OAuth2 and JWT (JSON Web Tokens).
* **Real-time Chat**: Full-duplex communication using **WebSockets**.
* **Matching System**: Automated pairing logic for users via `match_manager`.
* **Video Management**: Endpoints for uploading and managing video content associated with user profiles.
* **Clean Architecture**: Implemented the **Repository Pattern** to ensure separation of concerns and maintainability.

## 🛠 Tech Stack
* **Framework**: FastAPI
* **Database**: SQLite (via SQLAlchemy ORM)
* **Real-time**: WebSockets
* **Security**: Passlib (Bcrypt) for password hashing, PyJWT for tokens
* **Project Structure**: Modular design for scalability

## 📁 Project Structure
```text
.
├── repository/      # Database access and query logic
├── routers/         # API endpoint definitions
├── managers.py      # WebSocket connection and matching logic
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic models for data validation
└── main.py          # Application entry point
