"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es otro metodo y no GET'

@app.route('/lele', methods=['GET', 'POST'])
def lele():
    #abort(403)
    #return redirect(url_for('lala', post_id=2))
    #print(request.form)
    #print(request.form['llave1'])
    #print(request.form['llave2'])
    return {
        "username": 'Chanchito feliz',
        "email": 'chanchito@feliz.com'
    }

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', mensaje='Hola Mundo')

if __name__ == '__main__':
    app.run(debug=True)