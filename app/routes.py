from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Activo
from datetime import datetime


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/inventario")
def inventario():
    activos = Activo.query.all()
    return render_template("inventario.html", activos=activos)


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        estado = request.form["estado"]
        fecha_adquisicion = datetime.strptime(
            request.form["fecha_adquisicion"], "%Y-%m-%d"
        )

        nuevo_activo = Activo(
            nombre=nombre,
            categoria=categoria,
            estado=estado,
            fecha_adquisicion=fecha_adquisicion,
        )
        db.session.add(nuevo_activo)
        db.session.commit()
        return redirect(url_for("inventario"))

    return render_template("agregar.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    activo = Activo.query.get_or_404(id)
    if request.method == "POST":
        activo.nombre = request.form["nombre"]
        activo.categoria = request.form["categoria"]
        activo.estado = request.form["estado"]
        activo.fecha_adquisicion = datetime.strptime(
            request.form["fecha_adquisicion"], "%Y-%m-%d"
        )

        db.session.commit()
        return redirect(url_for("inventario"))

    return render_template("editar.html", activo=activo)


@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    activo = Activo.query.get_or_404(id)
    db.session.delete(activo)
    db.session.commit()
    return redirect(url_for("inventario"))


@app.route("/detalle/<int:id>", methods=["GET"])
def detalle(id):
    activo = Activo.query.get_or_404(id)
    return render_template("detalle.html", activo=activo)


@app.route("/confirmar_eliminar/<int:id>", methods=["GET", "POST"])
def confirmar_eliminar(id):
    activo = Activo.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(activo)
        db.session.commit()
        return redirect(url_for("inventario"))
    return render_template("confirmar_eliminar.html", activo=activo)
