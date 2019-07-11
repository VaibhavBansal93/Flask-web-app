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
    return render_template("home.html",title="Home", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods = ['GET', 'POST']) 
def register():
    form = RegistrationForm() #instance of the form that will be sent to the application
    if form.validate_on_submit(): #what to do submit
    #we use an f here because we need to pass a variable also to the string
        flash(f'Account created for { form.username.data }!', 'success') 
        #a message will be flahed 
        #different types of alerts should have different types of flash messages for them
        #flash accepts a second arguement
        # in the second arguement we pass a bootstrap class success
        #we also need to update the layout page to show this flash message
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form = form)

@app.route("/login", methods = ['GET', 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#runs the code
if __name__ == '__main__':
    app.run(debug=True)