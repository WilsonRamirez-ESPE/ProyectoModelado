from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pymongo
from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient

load_dotenv()


# Dirección IP pública de la máquina de tu amigo
mongo_host_amigo = "26.108.170.74"
mongo_port_amigo = 27017

# Tu configuración local de MongoDB
mongo_host_local = "localhost"
mongo_port_local = 27017  # Puerto mapeado en tu máquina host para MongoDB local
mongo_db = "AgenciaReclutamiento"

# Conexión a MongoDB de tu amigo
client_amigo = MongoClient(f"mongodb://{mongo_host_amigo}:{mongo_port_amigo}/")
baseDatos_amigo = client_amigo[mongo_db]

# Conexión a tu MongoDB local
client_local = MongoClient(f"mongodb://{mongo_host_local}:{mongo_port_local}/")
baseDatos_local = client_local[mongo_db]

#MONGO_URI = os.getenv("MONGO_URI")
#MONGO_BASEDATOS = "AgenciaReclutamiento"
#bdd = pymongo.MongoClient(MONGO_URI)
#baseDatos = bdd[MONGO_BASEDATOS]

app = Flask(__name__)


# Ruta y carga para documnetos estaticos
@app.route('/Proyecto/templates/recursos/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates/recursos', filename)

# Ruta y carga para la pagina de inicio
@app.route('/')
def inicio():
    return render_template('vistas/inicio.html')

# Ruta y carga para la pagina de candidatos
@app.route('/candidatos')
def candidatos():
    # Consulta en tu MongoDB local para obtener los candidatos
    candidatos = list(baseDatos_local.candidatos.find({}))
    
    # Consulta en MongoDB de tu amigo para obtener las habilidades
    habilidades = list(baseDatos_amigo.habilidades.find({}))
    
    # Convertir ObjectId a string para evitar problemas de serialización y combinar datos
    for candidato in candidatos:
        candidato['_id'] = str(candidato['_id'])
        candidato['habilidades'] = [
            habilidad for habilidad in habilidades 
            if str(habilidad.get('IDCandidato')) == candidato['_id']
        ]
    
    return render_template('vistas/candidatos.html', candidatos=candidatos)

# Ruta y carga para la pagina de empresas
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

# Ruta y carga para la pagina de entrevistas
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

#FUNCIONES PARA LA PAGINA DE CANDIDATOS
# Ruta y funciones para agregar un candidato
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

    baseDatos_local.candidatos.insert_one(nuevo_candidato)

    return redirect(url_for('candidatos'))

# Ruta y funciones para agregar una habilidad
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
    baseDatos_amigo.habilidades.insert_one(nueva_habilidad)
    return redirect(url_for('candidatos'))

# Ruta y funciones para eliminar un candidato/habilidad
@app.route('/eliminar_candidato', methods=['POST'])
def eliminar_candidato():
    candidato_id = int(request.form['id_candidatoE'])

    # Eliminar candidato por ID
    baseDatos_local.candidatos.delete_one({'_id': candidato_id})

    # Eliminar habilidades asociadas al candidato
    baseDatos_amigo.habilidades.delete_many({'IDCandidato': candidato_id})

    return redirect(url_for('candidatos'))

@app.route('/eliminar_habilidad', methods=['POST'])
def eliminar_habilidad():
    habilidad_id = int(request.form['id_habilidadE'])

    # Eliminar habilidad por ID
    baseDatos_amigo.habilidades.delete_one({'_id': habilidad_id})

    return redirect(url_for('candidatos'))


#FUNCIONES PARA LA PAGINA DE CANDIDATOS
@app.route('/agregar_empresa', methods=['POST'])
def agregar_empresa():
    empresa_id = int(request.form['id_empresa'])
    nombre = request.form['nombre']
    industria = request.form['industria']
    ubicacion = request.form['ubicacion']
    correo_contacto = request.form['correo']
    telefono_contacto = request.form['telefono']
    numero_empleados = int(request.form['numero_empleados'])
    facturacion_anual = int(request.form['facturacion_anual'])

    nueva_empresa = {
        "_id": empresa_id,
        "nombre": nombre,
        "industria": industria,
        "ubicacion": ubicacion,
        "correo_contacto": correo_contacto,
        "telefono_contacto": telefono_contacto,
        "numero_empleados": numero_empleados,
        "facturacion_anual": facturacion_anual
    }

    baseDatos.empresas.insert_one(nueva_empresa)
    return redirect(url_for('empresas'))

@app.route('/agregar_oferta', methods=['POST'])
def agregar_oferta():
    oferta_id = int(request.form['id_oferta'])
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    empresa = int(request.form['empresa'])
    salario = int(request.form['salario'])
    fecha_publicacion_str = request.form['fecha_publicacion']

    fecha_publicacion = datetime.strptime(fecha_publicacion_str, '%Y-%m-%d')

    nueva_oferta = {
        "_id": oferta_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "empresa": empresa,
        "salario": salario,
        "fecha_publicacion": fecha_publicacion
    }

    baseDatos.ofertas_trabajo.insert_one(nueva_oferta)
    return redirect(url_for('empresas'))


@app.route('/eliminar_empresa', methods=['POST'])
def eliminar_empresa():
    empresa_id = int(request.form['id_empresa'])
    baseDatos.empresas.delete_one({"_id": empresa_id})
    return redirect(url_for('empresas'))

@app.route('/eliminar_oferta', methods=['POST'])
def eliminar_oferta():
    oferta_id = int(request.form['id_oferta'])
    baseDatos.ofertas_trabajo.delete_one({"_id": oferta_id})
    return redirect(url_for('empresas'))

#FUNCIONES PARA LA PAGINA DE ENTREVISTAS
@app.route('/agregar_entrevistador', methods=['POST'])
def agregar_entrevistador():
    id_entrevistador = int(request.form['id_entrevistador'])
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    telefono = request.form['telefono']

    nuevo_entrevistador = {
        "_id": id_entrevistador,
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "telefono": telefono
    }

    baseDatos.entrevistador.insert_one(nuevo_entrevistador)
    return redirect(url_for('entrevistas'))

@app.route('/agregar_entrevista', methods=['POST'])
def agregar_entrevista():
    id_entrevista = int(request.form['id_entrevista'])
    candidato = int(request.form['candidato'])
    oferta = int(request.form['oferta'])
    fecha_hora = request.form['fecha_hora']
    ubicacion = request.form['ubicacion']
    entrevistador = int(request.form['entrevistador'])
    estado = request.form['estado']

    # Convertir la fecha_hora a formato de fecha de MongoDB
    fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%dT%H:%M')

    nueva_entrevista = {
        "_id": id_entrevista,
        "candidato": candidato,
        "oferta": oferta,
        "fecha_hora": fecha_hora,
        "ubicacion": ubicacion,
        "entrevistador": entrevistador,
        "estado": estado
    }

    baseDatos.entrevistas.insert_one(nueva_entrevista)
    return redirect(url_for('entrevistas'))

@app.route('/eliminar_entrevistador', methods=['POST'])
def eliminar_entrevistador():
    id_entrevistador = int(request.form['id_entrevistador'])
    baseDatos.entrevistador.delete_one({'_id': id_entrevistador})
    return redirect(url_for('entrevistas'))

@app.route('/eliminar_entrevista', methods=['POST'])
def eliminar_entrevista():
    id_entrevista = int(request.form['id_entrevista'])
    baseDatos.entrevistas.delete_one({'_id': id_entrevista})
    return redirect(url_for('entrevistas'))




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
