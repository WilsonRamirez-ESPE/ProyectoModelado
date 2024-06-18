from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_BASEDATOS = "AgenciaReclutamiento"
bdd = pymongo.MongoClient(MONGO_URI)
baseDatos = bdd[MONGO_BASEDATOS]

app = Flask(__name__)

@app.route('/Proyecto/templates/recursos/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates/recursos', filename)

@app.route('/')
def inicio():
    return render_template('vistas/inicio.html')

@app.route('/candidatos')
def candidatos():
    pipeline = [
        {
            '$lookup': {
                'from': 'habilidades',
                'localField': '_id',
                'foreignField': 'IDCandidato',
                'as': 'habilidades'
            }
        }
    ]
    candidatos = list(baseDatos.candidatos.aggregate(pipeline))
    return render_template('vistas/candidatos.html', candidatos=candidatos)

@app.route('/empresas')
def empresas():
    pipeline = [
        {
            '$lookup': {
                'from': 'ofertas_trabajo',
                'localField': '_id',
                'foreignField': 'empresa',
                'as': 'ofertas'
            }
        }
    ]
    empresas = list(baseDatos.empresas.aggregate(pipeline))
    return render_template('vistas/empresas.html', empresas=empresas)


@app.route('/entrevistas')
def entrevistas():
    pipeline = [
        {
            '$lookup': {
                'from': 'entrevistas',
                'let': { 'entrevistador_id': '$_id' },
                'pipeline': [
                    {
                        '$match': {
                            '$expr': { '$eq': ['$entrevistador', '$$entrevistador_id'] }
                        }
                    },
                    {
                        '$lookup': {
                            'from': 'candidatos',
                            'localField': 'candidato',
                            'foreignField': '_id',
                            'as': 'candidato_info'
                        }
                    },
                    {
                        '$unwind': '$candidato_info'
                    },
                    {
                        '$project': {
                            '_id': 0,
                            'candidato': {'nombre':'$candidato_info.nombre', 
                                          'apellido': '$candidato_info.apellido'
                            },  # Nombre del candidato
                            'fecha_hora': 1,
                            'ubicacion': 1,
                            'estado': 1
                        }
                    }
                ],
                'as': 'entrevistas'
            }
        }
    ]
    entrevistadores = list(baseDatos.entrevistador.aggregate(pipeline))
    return render_template('vistas/entrevistas.html', entrevistadores=entrevistadores)



@app.route('/agregar_candidato', methods=['POST'])
def agregar_candidato():
    candidato_id = request.form['id_candidato']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    telefono = request.form['telefono']
    nivel_estudio = request.form['nivel_estudio']
    puestos = request.form.getlist('puesto[]')
    empresas = request.form.getlist('empresa[]')
    anios_experiencia = request.form.getlist('anio_experiencia[]')

    experiencia_laboral = []
    for i in range(len(puestos)):
        experiencia = {
            "puesto": puestos[i],
            "empresa": int(empresas[i]),
            "anio_experiencia": int(anios_experiencia[i])
        }
        experiencia_laboral.append(experiencia)

    nuevo_candidato = {
        "_id": int(candidato_id),
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "telefono": telefono,
        "nivel_estudio": nivel_estudio,
        "experiencia_laboral": experiencia_laboral
    }

    baseDatos.candidatos.insert_one(nuevo_candidato)

    return redirect(url_for('candidatos'))


@app.route('/agregar_habilidad', methods=['POST'])
def agregar_habilidad():
    habilidad_id = request.form['id_habilidad']
    habilidad_nombre = request.form['habilidad_nombre']
    habilidad_descripcion = request.form['habilidad_descripcion']
    nivel_experiencia = request.form['nivel_experiencia']
    habilidad_candidato = request.form['id_candidato']

    nueva_habilidad = {
        "_id":int(habilidad_id),
        "nombre": habilidad_nombre,
        "descripcion": habilidad_descripcion,
        "nivel_experiencia": nivel_experiencia,
        "IDCandidato": int(habilidad_candidato)
    }
    # Insertar la nueva habilidad en la colección habilidades
    baseDatos.habilidades.insert_one(nueva_habilidad)
    return redirect(url_for('candidatos'))

if __name__ == "__main__":
    app.run(debug=True)
