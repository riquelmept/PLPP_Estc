from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def ola_mundo():
    return "Teste Programa com Flask"
 
if __name__ == '__main__':
    app.run()