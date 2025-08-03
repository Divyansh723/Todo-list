# 📝 Django Todo List

A clean and minimal **Todo List web application** built with Django. This app allows users to create, track, and manage their personal tasks with ease. It's perfect for learning Django fundamentals and experimenting with CRUD operations, authentication, and basic UI styling.

---

## 🚀 Features

✅ User registration & login  
✅ Add, edit, and delete tasks  
✅ Mark tasks as completed  
✅ Fully responsive UI with Bootstrap  
✅ Built using Django’s built-in admin and auth system

---

## 🗂️ Project Structure

.
├── db.sqlite3 # SQLite database  
├── manage.py # Django's CLI management tool  
├── home/ # Core app handling task logic  
│   ├── views.py # View functions  
│   ├── models.py # Task model  
│   ├── urls.py # URL routing  
│   └── ...  
├── templates/ # HTML templates  
│   ├── base.html # Shared layout  
│   ├── home.html # Main dashboard  
│   ├── login.html # Login page  
│   ├── register.html # Registration page  
│   └── task.html # Individual task interface  
├── todo_list/ # Project configuration  
│   ├── settings.py # Project settings  
│   └── urls.py # Global URLs  
└── README.md  

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Divyansh723/Todo-list.git
cd Todo-list
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Start Development Server
```bash
python manage.py runserver
```

### 7. Open in Browser
Go to: http://127.0.0.1:8000/

---

✨ **How to Use**

- Sign up for a new account or log in if you already have one.  
- Add tasks by typing in the input field and clicking "Add".  
- Click a task to mark it as done, or edit/delete as needed.  
- Stay organized and on top of your goals!

---

📜 **License**  
This project is licensed under the MIT License.

👨‍💻 **Author**  
Made with ❤️ by [@Divyansh723](https://github.com/Divyansh723)
