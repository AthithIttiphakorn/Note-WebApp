#run when starting web server
from website import create_app #get create_app func from __init__.py
from waitress import serve

app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000) #turn debug off when running production server
    