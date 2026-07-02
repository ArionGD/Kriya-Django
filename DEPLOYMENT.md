# Deployment Guide: Project Kriya on PythonAnywhere

This guide provides simple, step-by-step instructions to host Project Kriya on **PythonAnywhere.com** using the built-in SQLite database and without requiring any complex environment variable files.

---

## Prerequisites

1. Create a free account on [PythonAnywhere.com](https://www.pythonanywhere.com).
2. Note down your username (referred to as `yourusername` below).

---

## Step 1: Open a Console and Clone the Repository

1. Log in to PythonAnywhere.
2. Go to the **Consoles** tab and start a new **Bash** console.
3. Clone your GitHub repository by running:
   ```bash
   git clone https://github.com/ArionGD/Kriya-Django.git
   ```
4. Move into the project directory:
   ```bash
   cd Kriya-Django
   ```

---

## Step 2: Set Up a Virtual Environment & Install Dependencies

1. While inside the `Kriya-Django` folder in the console, create a Python virtual environment:
   ```bash
   python3 -m venv ~/.virtualenvs/kriya-venv
   ```
2. Activate the virtual environment:
   ```bash
   source ~/.virtualenvs/kriya-venv/bin/activate
   ```
   *(You will see `(kriya-venv)` prefixing your console prompt).*
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Step 3: Run Database Migrations & Collect Static Files

1. Apply the database migrations to create the SQLite tables:
   ```bash
   python manage.py migrate
   ```
2. Create an admin superuser account so you can access the NGO panel:
   ```bash
   python manage.py createsuperuser
   ```
   *(Enter a username, email, and password. Remember these credentials!)*
3. Compile all static styles and files into a single directory:
   ```bash
   python manage.py collectstatic
   ```
   *(Type `yes` when prompted).*

---

## Step 4: Configure the Web App on PythonAnywhere

1. Open a new tab in your browser and go to the **Web** tab on PythonAnywhere.
2. Click **Add a new web app**.
3. Choose **Manual configuration** (do NOT choose Django, as we want to use our virtual environment).
4. Select **Python 3.10**.
5. After creating the app, configure the following paths under the Web tab:
   * **Source code**: `/home/yourusername/Kriya-Django`
   * **Working directory**: `/home/yourusername/Kriya-Django`
   * **Virtualenv**: `/home/yourusername/.virtualenvs/kriya-venv`

---

## Step 5: Configure the WSGI File

1. In the **Web** tab under the **Code** section, click on the **WSGI configuration file** link (it looks like `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
2. Delete everything inside that file.
3. Paste the following configuration, making sure to replace `yourusername` with your actual PythonAnywhere username:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/Kriya-Django'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Start the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

4. Click **Save** at the top right.

---

## Step 6: Serve Static Files

To ensure styles, layouts, and icons load correctly, map the static files path under the **Static files** section of the **Web** tab:

1. Under the **Static files** header, click **Add a new entry**.
2. Set the fields to:
   * **URL**: `/static/`
   * **Path**: `/home/yourusername/Kriya-Django/staticfiles`
3. Click the checkmark to save.

---

## Step 7: Reload and Test!

1. Scroll to the top of the **Web** tab page.
2. Click the green **Reload yourusername.pythonanywhere.com** button.
3. Open a new browser window and visit:
   👉 `http://yourusername.pythonanywhere.com/`

*You are all set! You can log in using the superuser credentials you created to verify the dashboards and platform.*
