#run when starting web server
from website import create_app #get create_app func from __init__.py

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #turn debug off when running production server
    