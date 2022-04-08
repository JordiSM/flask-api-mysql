from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'aec68fbb762fe6d99d48c74290512f79'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created fr {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Logged in succesfully','success')
            return redirect(url_for('home'))
        else:
            flash(f'Failed to Log In', 'danger')
 
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
