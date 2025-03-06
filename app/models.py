from app import db


class Activo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default="Disponible")
    fecha_adquisicion = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Activo {self.nombre}>"
