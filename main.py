from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def promedio_notas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        if asistencia >= 75 and promedio >= 40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
        return render_template('ejercicio1.html', promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def calcular_mayor():
    if request.method == 'POST':
        nombres = []
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        if nombre1 != nombre2 and nombre1 != nombre3 and nombre2 != nombre3:
            nombres.append(nombre1)
            nombres.append(nombre2)
            nombres.append(nombre3)
            resultado = max(nombres, key=len)
            caracteres = len(resultado)
            return render_template('ejercicio2.html', resultado=resultado, caracteres=caracteres)
        else:
            return render_template('ejercicio2.html', error=error)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
