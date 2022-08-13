"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = [1,11,4,23,95,5,55]

    for item1 in lista:
        if item1 >= 18:
            respuesta = "su edad es: " + str(item1) + ". Usted es mayor de edad "
            print("su edad es: ", str(item1), ". Usted es mayor de edad ")
        else:
            respuesta = "su edad es: " + str(item1) + ". Usted es menor de edad "
            print("su edad es: ", str(item1), ". Usted es menor de edad ")
    return render_template('index.html', lista=lista, item1=item1, respuesta=respuesta)

if __name__ == '__main__':
    app.run(debug=True)