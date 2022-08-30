from flask import Flask, render_template, url_for, redirect,session, request

app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method=='POST':
    if request.form["boton"]=='registro':
      return redirect(url_for('registro'))
    elif request.form["boton"]=='logearse':
      session['nombre']= request.form['nombre']
      session['contraseña']=request.form['contraseña']
      return redirect(url_for('bienvenido'))
      
@app.route('/bienvenido')
def bienvenido():
  return render_template('pagina.html', name=session['nombre'])

@app.route('/registro')
def registro():
  return render_template("registro.html")

@app.route('/crearusuario',methods=['POST', 'GET'])
def crearusuario():
  if request.method=='POST':
    session['nombre']= request.form['nombre']
    session['contraseña']=request.form['contraseña']
    pais = request.form['pais']
    print(pais)
    return redirect(url_for('bienvenido'))
  
app.run(host='0.0.0.0', port=81)