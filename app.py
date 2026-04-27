from flask import Flask, render_template,request,flash,url_for,redirect,session
import requests

from GestorTareas import GestorTareas
app = Flask(__name__)
app.secret_key = "Ali091903."

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route('/ValidaSesion', methods=['GET', 'POST'])
def ValidaSesion():
    if request.method == "POST":
        email = request.form.get('Email', '').strip()
        contra = request.form.get('Contra', '').strip()

        if not email or not contra:
            flash('Por favor ingresa email y contraseña', 'error')
            return redirect(url_for('login'))

        gestor = GestorTareas()
        usuario = gestor.obtener_usuario2(email, contra)

        if not usuario:
            flash('Usuario o contraseña incorrectos', 'error')
            return redirect(url_for('login'))

        session['usuario_email'] = email
        session['usuario'] = usuario['nombre']
        session['loggeado'] = True

        flash(f"Bienvenido {usuario['nombre']}!", 'success')
        return redirect(url_for('inicio'))

    return redirect(url_for('login'))

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("Nombre")  
        apellido = request.form.get("Apellido")      
        email = request.form.get("Email")      
        contra = request.form.get("Contra")     
        contraConfirm = request.form.get("ContraConfirm") 

        if contra != contraConfirm:
            flash("La contraseña no coincide", "error")
            return render_template("registro.html")
        
        session['usuario_email'] = email
        session['usuario'] = nombre
        session['loggeado'] = True

        flash(f"Cuenta creada correctamente para el usuario:{nombre} {apellido}", "success")
        return redirect(url_for("inicio"))

    return render_template("registro.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/logout")
def logout():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)