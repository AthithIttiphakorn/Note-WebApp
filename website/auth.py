#from flask import Blueprint
from flask import * 
#A blueprint for the project
#Blueprint define that this file has many URLS and Routes defined in it
#seperation is more easy - more organized

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #access data sent as part of a form
    #GET request to retrieve page (like when pressing link or refresh page), default send
    #POST if going to edit information, send into server, ect
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "hi"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = False
    if request.method == 'POST':
        email = request.form.get('email') #get specific value from 'name' of form component.
        firstName = request.form.get('firstName') #this is a POST function.
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2:
            flash('Passwords are not the same!', category='error')
            error = True
        if len(password1) < 7:
            flash('Password is too short!', category='error')
            error = True
        if len(firstName) < 2:
            error = True
            flash('First name must be greater than 2 characters!', category='error')

        if error == False:
            flash('Account created successfully!', category='success')
            
    return render_template("sign_up.html")