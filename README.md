# Online Clothing Store  

A full-featured **online clothing store** built with **Django**.  
This project is designed as a portfolio project to demonstrate backend development skills, covering authentication, product management, cart functionality, and order processing.  

---

## Features  

- **User Authentication**: Register, login, logout, profile management  
- **Product Management**: Add, edit, delete and browse clothing items  
- **Shopping Cart**: Add/remove items 
- **Order Processing**: Place and track orders   
- **Admin Panel**: Manage users, products, and orders via Django Admin 
- **Tests**:  Coverage for pages and user authentication using Django TestCase

---

## Tech Stack  

- **Backend**: Django 
- **Database**: SQLite (can be switched to PostgreSQL/MySQL)  
- **Frontend**: Django Templates (can be extended with React/Vue in the future)  
- **Other**: Python 3, Bootstrap/Tailwind (optional for styling)  
- **Testing**: Django `unittest.TestCase`
---

## Project Structure  

My_clothes_shop
│── manage.py
│── requirements.txt
│── README.md
├── users/ # User authentication and profiles
├── products/ # Clothing products
├── contact/ # Shopping cart logic, order placement and tracking
├── templates/ # HTML templates
└── static/ # Static files



---

## Installation  

1. Clone the repository  
```bash
git clone https://github.com/your-username/online-clothing-store.git
cd online-clothing-store

Create and activate virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies

pip install -r requirements.txt

Apply migrations

python manage.py migrate

Create superuser

python manage.py createsuperuser

Run the development server

python manage.py runserver
```

## Future Improvements 

- **Payment integration (Stripe/PayPal)**

- **Comments and reviews**

- **Frontend with React or Vue**

## Author

Developed by **Ivan Sotsenko** as a portfolio project.