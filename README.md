
# 📘 **Multilingual FAQ System (Django + React)**
A **full-stack** multilingual FAQ management system built with **Django REST Framework** and **React.js**. This project supports **WYSIWYG content editing**, **automatic translations**, **Redis caching**, and is **Dockerized** for easy deployment.

## 🚀 **Features**
✅ **Django REST API** with multilingual FAQ support  
✅ **WYSIWYG Editor** using `django-ckeditor` for formatting FAQ answers  
✅ **Automatic Translations** using `googletrans` for Hindi and Bengali  
✅ **Caching with Redis** for faster responses  
✅ **Admin Panel** to manage FAQs (CRUD operation) 
✅ **Unit Tests** using `pytest` for models and API validation  
✅ **Linting** with `flake8` (Python) and `ESLint` (JavaScript)  
✅ **Docker & Docker Compose** for easy deployment  


---

## 📦 **Installation Guide**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/AmishaKumari18/BharatFD-FAQ-Backend.git
cd BharatFD-FAQ-Backend

```

### **2️⃣ Backend (Django) Setup**
#### **🔹 Navigate to the Backend Directory**
```sh
cd FAQ_Backend
```
#### **🔹 Install Python Dependencies**
```sh
pip install -r requirements.txt
```

#### **🔹 Apply Migrations**
```sh
python manage.py migrate
```

#### **🔹 Create a Superuser**
```sh
python manage.py createsuperuser
```

#### **🔹 Run the Django Server**
```sh
python manage.py runserver
```
Access the API at:  
📌 **`http://127.0.0.1:8000/api/faqs/`**  
📌 **Admin Panel:** `http://127.0.0.1:8000/admin/`

---

### **3️⃣ Frontend (React) Setup**
#### **🔹 Navigate to the Frontend Directory**
```sh
cd faq-frontend
```

#### **🔹 Install Dependencies**
```sh
npm install
```

#### **🔹 Start React Frontend**
```sh
npm start
```
📌 **React App Runs on:** `http://localhost:3000/`

---

### **4️⃣ Run with Docker (Recommended)**
Ensure **Docker & Docker Compose** are installed.

#### **🔹 Build and Run Containers**
```sh
docker-compose up --build
```

#### **🔹 Verify Running Containers**
```sh
docker ps
```
Services:
- **Django Backend** (`http://127.0.0.1:8000/`)
- **React Frontend** (`http://localhost:3000/`)
- **Redis Cache**

---

## 🛠 **API Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/faqs/` | Fetch all FAQs (default: English) |
| `GET` | `/api/faqs/?lang=hi` | Fetch FAQs in Hindi |
| `GET` | `/api/faqs/?lang=bn` | Fetch FAQs in Bengali |
| `POST` | `/api/faqs/` | Create a new FAQ |

### **Example: Create an FAQ**
```sh
curl --location 'http://127.0.0.1:8000/api/faqs/' \
--header 'Content-Type: application/json' \
--data '{"question": "What is Django?", "answer": "Django is a web framework for Python."}'
```

---

## ✅ **Testing**
Run all **unit tests**:
```sh
pytest -v
```
Tests include:
- **Model Tests** (FAQ creation & translation)
- **API Tests** (CRUD operations)
- **Cache Tests** (Redis validation)

---

## ✨ **Code Quality & Linting**
### **Python (PEP8)**
```sh
flake8 .
```

### **JavaScript (ESLint)**
```sh
cd faq-frontend
npx eslint src/
```

---
