from flask import Flask, render_template
import GestorTareas 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login")
def login():
    gestor= GestorTareas()
    if gestor:
        gestor.obtener_usuario2("hola@gmail.com", "123")
        return render_template("login.html")
    else:
        return render_template("error.Conection.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/logout")
def logout():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)