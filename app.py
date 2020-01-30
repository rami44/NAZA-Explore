from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       return render_template('index.html')
    else:
        email = request.form['email']

        database.save_to_database(email)        
        return render_template('index.html')


    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return logged_in()
    else:

        print("not right")
        return home()
# @app.route('/search', methods = ['POST'])
# def Search():
#     response = GenerateRestaurants(request.form['name'])
#     return render_template('index.html', restList = response)
# def GenerateRestaurants(name):
   
   
    return response

if __name__ == '__main__':
    app.run(debug=True)
