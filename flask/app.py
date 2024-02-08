from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

data = [
    {"id": 1, "nombre": "JAVA"},
    {"id": 2, "nombre": "PHP"},
    {"id": 3, "nombre": "Swift"},
    {"id": 4, "nombre": "Kotlin"}
]

@app.route('/')
def index() :
    return render_template("index.html", datos=data)

# Create - Para añadir un nuevo elemento
@app.route('/add', methods=['POST'])
def add_element():
    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        nuevo_id = max(dato['id'] for dato in data) + 1
        data.append({"id": nuevo_id, "nombre": nuevo_nombre})
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)