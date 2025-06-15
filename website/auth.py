#from flask import Blueprint
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

import smtplib
import os


#A blueprint for the project
#Blueprint define that this file has many URLS and Routes defined in it
#seperation is more easy - more organized

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #access data sent as part of a form
    #GET request to retrieve page (like when pressing link or refresh page), default send
    #POST if going to edit information, send into server, ect
    #data = request.form
   # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get("password")

        #check if account exists
        user = User.query.filter_by(email=email).first()
        if user:  #if the user is in the database (already registered)
            if check_password_hash(user.password, password): #compare hashes to see if password is correct
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True) #remember stores users session. Will login automatically.
                return redirect(url_for('views.home'))
            else: 
                flash('Incorrect password, try again.')

        else: #user has nto signed up yet - not in database.
            flash("User does not exist. You may create a account by signing up.", category="error")

    return render_template("login.html", user=current_user)

@auth.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out successfully!", category='info')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = False
    if request.method == 'POST':
        email = request.form.get('email') #get specific value from 'name' of form component.
        first_name = request.form.get('firstName') #this is a POST function.
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists, use another one.', category="error")

        if password1 != password2:
            flash('Passwords are not the same!', category='error')
            error = True
        if len(password1) < 7:
            flash('Password is too short!', category='error')
            error = True
        if len(first_name) < 2:
            error = True
            flash('First name must be greater than 2 characters!', category='error')

        if error == False:                                                 #hash password so it is unreadable
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')

            #maybe migrate into a new seperate function so that it is reusable (if necessary) - North.
            smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

            smtp_object.ehlo()
            smtp_object.starttls()
            smtp_object.login( os.getenv("EMAIL"), os.getenv("APPWS"))

            subject = f"Hi, {first_name}!"
            msg = "Subject: " + subject + '\n' + "Thank you for trying out my website! :)"
            smtp_object.sendmail(os.getenv("EMAIL"), email, msg)
            smtp_object.quit()

            return redirect(url_for('views.home'))
            
    return render_template("sign_up.html", user=current_user)