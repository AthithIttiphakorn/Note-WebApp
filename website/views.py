#store all routes or the URL endpoint.
#For the functioning of the front end
#virtual env to stop package conflicts
# If you install Flask 3.0.0, Project A might break.If you install Flask 2.1.0, Project B might break.
#They require different versions of Flask so they both need to be isolated with virtual environment so the versions can be used seperately.

#__name__ is a special variable that tells  whether the script is running directly or being imported as a module.
#if __name__ == "__main__": is used to run code when the file is executed directly, not imported.


from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
#Blueprint define that this file has many URLS and Routes defined in it
#seperation is more easy - more organized

views = Blueprint('views', __name__)

#- this is a decorator!-
@views.route('/', methods=['GET', 'POST']) #define homepage 
@views.route('/home')
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


