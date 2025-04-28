# SimpleEcommerce 🛒

A simple yet fully functional e-commerce website built with **Django**.

## Features ✨

- User authentication (signup, login, logout)
- Product listing and detailed view
- Add to cart and manage cart
- Checkout process

## Tech Stack 🛠️

- Backend: Django 5.x
- Database: SQLite (default) or MySQL/PostgreSQL
- Frontend: HTML5, Bootstrap 5 (optional)
- Deployment-ready (WSGI)

## Project Structure 📂


## Setup Instructions 🚀

### 1. Clone the repository

```bash
git clone https://github.com/Esmat434/SimpleEcommerce.git
cd SimpleEcommerce

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
