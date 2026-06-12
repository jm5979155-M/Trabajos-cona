from flask import Flask, render_template, request, jsonify
from chatbot import obtener_respuesta

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/mensaje', methods=['POST'])
def mensaje():

    datos = request.get_json()

    texto = datos['mensaje']

    respuesta = obtener_respuesta(texto)

    return jsonify({
        'respuesta': respuesta
    })

if __name__ == '__main__':
    app.run(debug=True)