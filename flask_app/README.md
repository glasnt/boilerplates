# Basic Flask app

Read more: [Flask Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)

## Start your website

```shell
flask run
```

⚠️🎩: This command only works because by default, Flask will run `wsgi.py` or `app.py`. If you name your app anything else, you need to tell Flask what to run: 

```shell
$ export FLASK_APP=site.py
$ flask run
```

## View your website

Go to a brower and open `localhost:5000` (Flask should tell you this URL)

## Custom Ports

```shell
$ flask run --port 1337
```
