from flask import Flask , render_template
app = Flask(__name__)


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


#runs the code
app.run(debug=True)