# Flask Names

A small Flask app that saves names to a SQLite database and to a text file.

## 1. Clone the project

```
git clone https://github.com/maevlyn/basic-scaffold.git
cd basic-scaffold
```

## 2. Set up Python

Mac / Linux:

```
python3 -m venv venv
source venv/bin/activate
pip install flask
```

Windows:

```
python -m venv venv
venv\Scripts\activate
pip install flask
```

## 3. Run it

```
python app.py
```

Then open http://localhost:8000 in your browser.

## Pages

- `/`: enter a name
- `/names`: names saved in the database
- `/names-text-file`: names saved in the text file
