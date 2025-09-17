from waitress import serve
from app import app  # app — это имя вашего файла с приложением

if __name__ == '__main__': 
    serve(app, host='0.0.0.0', port=8000, threads=4)