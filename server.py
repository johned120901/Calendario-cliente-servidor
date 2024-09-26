from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Simulación de una base de datos (lista de recordatorios)
recordatorios = []

# Ruta para obtener todos los recordatorios
@app.route('/recordatorios', methods=['GET'])
def obtener_recordatorios():
    return jsonify(recordatorios)

# Ruta para agregar un nuevo recordatorio
@app.route('/recordatorios', methods=['POST'])
def agregar_recordatorio():
    data = request.json
    recordatorios.append(data)
    return jsonify({"message": "Recordatorio agregado", "recordatorio": data})

# Ruta para eliminar un recordatorio
@app.route('/recordatorios/<int:id>', methods=['DELETE'])
def eliminar_recordatorio(id):
    global recordatorios
    recordatorios = [rec for rec in recordatorios if rec['id'] != id]
    return jsonify({"message": "Recordatorio eliminado"})

# Ruta para modificar un recordatorio
@app.route('/recordatorios/<int:id>', methods=['PUT'])
def modificar_recordatorio(id):
    data = request.json
    for rec in recordatorios:
        if rec['id'] == id:
            rec.update(data)
            return jsonify({"message": "Recordatorio actualizado", "recordatorio": rec})
    return jsonify({"error": "Recordatorio no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
