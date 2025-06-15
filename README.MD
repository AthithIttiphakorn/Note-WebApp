pip install flask
pip install flask-login
pip install flask-sqlalchemy

if installed globally first then switch to venv these packages need to be installed again as venv s can be thought of as isolation where packages can have different versions. If global, all will have same version.

You can view the database in a more readable format by downloading DBeaver: https://dbeaver.io/download/


---INFORMATION ABOUT BLUEPRINTS---
    -object provided by Flask
Blueprints in Flask help organize your application by grouping related routes, views, and logic into separate modules, making the codebase easier to manage and scale. Instead of having all routes in a single file, Blueprints allow you to split functionality—for example, authentication routes (/login, /signup) can live in an auth Blueprint, while note-taking routes (/notes, /add_note) can be placed in a notes Blueprint. This modular approach improves readability and makes collaboration simpler since different team members can work on separate Blueprints without conflicts. Additionally, Blueprints enable cleaner URL routing by prefixing all routes in a Blueprint with a common URL segment if desired, such as /auth/login or /notes/view, helping keep URLs structured and intuitive. By registering Blueprints in the main application, Flask seamlessly links these modular components, allowing features like url_for('auth.login') to generate URLs dynamically across modules. Overall, Blueprints enhance maintainability, promote code reuse, and streamline development as your Flask app grows in complexity.

Structuring, like seperate meeting rooms

---INFORMATION ABOUT SQL---
PostgreSQL is a SQL database that is commonly used in production. PostgreSQL is an advanced relational database system and it supports both relational (SQL) and non-relational (JSON) queries.
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
