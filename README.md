# FastAPI Practice Lab

This repository contains practice assignments built using FastAPI to strengthen backend development and REST API design skills.

---

## Tech Stack

- Python 3
- FastAPI
- Pydantic
- Uvicorn

---

## Topics Covered

- REST API Design
- FastAPI Routing
- Request/Response Validation
- Query & Path Parameters
- CRUD Operations
- Interactive API Documentation

---

## Requirements

Project dependencies are listed in the `requirements.txt` file.

Main dependencies:

- fastapi
- uvicorn
- pydantic

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/UrvishAhir1/fastapi-practice-lab.git
cd fastapi-practice-lab
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

Navigate to any folder and run:

```bash
uvicorn main:app --reload
```

Example:

```bash
cd "assignment 1"
uvicorn main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

**Author:** Urvish Ahir