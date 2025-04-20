#store all routes or the URL endpoint.
#For the functioning of the front end
#virtual env to stop package conflicts
# If you install Flask 3.0.0, Project A might break.If you install Flask 2.1.0, Project B might break.
#They require different versions of Flask so they both need to be isolated with virtual environment so the versions can be used seperately.

#__name__ is a special variable that tells  whether the script is running directly or being imported as a module.
#if __name__ == "__main__": is used to run code when the file is executed directly, not imported.


from flask import Blueprint, render_template
#Blueprint define that this file has many URLS and Routes defined in it
#seperation is more easy - more organized

views = Blueprint('views', __name__)

#- this is a decorator!-
@views.route('/') #define homepage 
@views.route('/home')
def home():
    return render_template("home.html")


