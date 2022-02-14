# Notebook-Annotations-API

This is a basic notebook api that you can build many notes, any annotation have one or more tags, for  organisation proupose.

### How to setup?
```console
virtualenv .venv -p python3.10
source .venv/bin/activate
pip install -e .
```

### How to run the api?
* Using main file executor
```console
python src/main.py
```
* Using Uvicorn
```console
uvicorn src.main:app --host=0.0.0.0 --port=8000
```

### Where`s the api documentation?
* Here you can see all endpoints and more: https://notebook-anotations.herokuapp.com/docs
