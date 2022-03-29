from flask import Flask, render_template, url_for
app = Flask(__name__)

post = [
    {
        'author': 'Jordi Sevilla',
        'title': 'Blog Post 1',
        'content':'Tonto quien lo lea',
        'date_posted': '22 Marzo, 2022'
    }
    ,
    {
        'author': 'Lluis Mayans',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted': '22 Marzo, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=post, title='Home')

@app.route("/about")
def about():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True)
