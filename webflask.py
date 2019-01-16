import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template(f"{index.__name__}.html", name=index.__name__)
	
@app.route('/about')
def about():
    return render_template(f"{about.__name__}.html", name=about.__name__)

@app.route('/hello', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Please submit form"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)

@app.route('/form')
def form():
    return render_template(f"{form.__name__}.html")


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)