# notes_app
A very basic Flask App

Folowed [this tutorial](https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/).

To be used as demo for the [email-postponer](https://github.com/adinutzyc21/email-postponer) extension.

1. Create and activate a virtual environment using the following command:
```
python3 -m venv venv
. venv/bin/activate
```

2. Install Flask:
```
pip install flask
```

3. Install CORS
```
pip install -U flask-cors
```

4. Run the app:
```
export FLASK_APP=notes_app.py
flask run
```

5. App is running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

6. You can curl:
```
curl -X PATCH http://127.0.0.1:5000/notes -H 'Content-Type: application/json' -d '{"url":"url3","title": "Created", "content": "Created a new note"}
'
curl -X POST http://127.0.0.1:5000/notes -H 'Content-Type: application/json' -d '{"url":"url3"}'
curl -X POST http://127.0.0.1:5000/notes -H 'Content-Type: application/json' -d '{}'
```