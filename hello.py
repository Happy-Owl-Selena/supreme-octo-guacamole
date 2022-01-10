from flask import Flask, render_template


#Create a Flask Instance 
app = Flask(__name__)

#Create a route decorator 
@app.route('/')

#def index():
#    return "<h1>Hello World!</h1>"


# Filters
# safe - used to pass executable html
# capitalize
# lower
# upper
# title - capitalizes first letter of each word 
# trim - removes trailing spaces 
# striptags - removes all html tags




def index():
    first_name = "Selena"
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni", "Cheese","Mushrooms", 41]
    return render_template("index.html", first_name=first_name,
                            stuff=stuff,
                            favorite_pizza=favorite_pizza)

# localhost:5000/user/Selena
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)



# Create Custom Error Pages 

#Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error thing
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500