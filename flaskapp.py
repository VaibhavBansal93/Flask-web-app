from flask import Flask , render_template, url_for, flash , redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

#this is a secret key  it protects against modifying cookies
#and cross site scripting attack
#ideally secret key should be a random set of characters
#so secrets module of python is used to generate a random key
app.config['SECRET_KEY'] = 'a3f14d55ce06de0ad04b2aef1ac782d6'

posts = [
    {
        'author' : 'Vaibhav Bansal',
        'title' : ' Blog Post 1',
        'content' : 'First post content',
        'date_updated' : 'July 10, 2019'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog post 2',
        'content' : 'Second post content',
        'date_updated' : 'June 9, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    #to pass variables use var1=var
    #var1 is the name that will be used by the html template
    #var is the name used in the python script
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register")
def register():
    form = RegistrationForm() #instance of the form that will be sent to the application
    return render_template('register.html',title='Register',form = form)

@app.route("/login")
def login():
    form = 'LoginForm()' #instance of the login form to be sent to the application
    return render_template('login.html',title='Login',form = form)

#runs the code
app.run(debug=True)