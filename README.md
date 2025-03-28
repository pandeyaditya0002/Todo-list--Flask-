# Flask Project Setup Guide

## Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (3.x recommended)
- [pip](https://pip.pypa.io/en/stable/)
- [Visual Studio Code](https://code.visualstudio.com/) (or any preferred code editor)

---

## Installation & Setup

### 1. Clone or Download the Repository

- If using Git:
  ```sh
  git clone https://github.com/pandeyaditya0002/Todo-list--Flask-
  cd Todo-list--Flask-
  ```
- Or manually **download the ZIP**, extract it, and navigate to the folder.

### 2. Open in VS Code

Open the extracted folder in **Visual Studio Code**.

### 3. Create & Activate a Virtual Environment

Open the **terminal** in VS Code and run the following commands:

```powershell
python -m venv env  # Create virtual environment
Set-ExecutionPolicy Unrestricted -Scope Process  # Allow scripts temporarily
env\Scripts\Activate  # Activate virtual environment
```

*(For macOS/Linux, use **`source env/bin/activate`** instead of the last command.)*

### 4. Install Dependencies

```sh
pip install -r requirements.txt
```

### 5. Run the Flask App

```sh
python app.py
```

### 6. Access the Web App

Once the app starts, open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## Project Structure

```
Todo-list--Flask-/
│── env/                     # Virtual environment (generated after setup)
│── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── style.css        # Stylesheet
│   ├── js/
│   │   ├── test.js          # JavaScript file
│── templates/               # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── update.html
│── app.py                   # Main Flask application
│── List of Commands.txt      # List of useful commands
│── Procfile                  # Deployment process file (if using Heroku)
│── README.md                # Setup guide
│── requirements.txt         # Project dependencies
│── todo.db                  # SQLite database file
```

---

## 🖼️ Screenshots

Below is a screenshot of the project structure for reference:

![ToDo list UI](./Screenshot%202025-03-19%20175823.png) 
---

![ToDo list Update UI](./Screenshot%202025-03-21%20185607.png) 

---

## Deactivating the Virtual Environment

To exit the virtual environment, run:

```sh
deactivate
```

---

## Additional Notes

- If `env\Scripts\Activate` gives an error, try running PowerShell as administrator.
- If you get a **port conflict**, change the port in `app.py` like this:
  ```python
  app.run(port=5001)  # Change 5001 to any available port
  ```

Happy coding! 🚀

