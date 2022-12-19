import Personalizacion as p
from Trabajador import Persona


def grabaTrabajador(nuevo, id, nombre, apellidos, email, sexo):
    correcto = False

    try:
        conn = p.mysql_connect()  # Conectar a la base de datos
        cursor = conn[0].cursor()  # Crear un cursor
        query = None
        val = None

        if nuevo:
            query = ("INSERT INTO trabajador (nombre, apellidos, email, sexo) VALUES (%s, %s, %s, %s)")
            val = (nombre, apellidos, email, sexo)

            cursor.execute(query, val)  # Ejecutar una consulta
            id = conn.insert_id()

        else:
            query = "UPDATE trabajador SET nombre = %s, apellidos = %s, email = %s, sexo = %s WHERE idTrabajador = %s;"
            val = (nombre, apellidos, email, sexo, id)
            cursor.execute(query, val)  # Ejecutar una consulta

        conn[0].commit()
        cursor.close()  # Cerrar el cursor
        conn[0].close()  # Cerrar la conexión MYSQL
        conn[1].close()  # Cerrar la conexión SSH

        correcto = True
    except Exception as e:
        correcto = "Exeception occured:{}".format(e)

    return correcto, id


def listaTrabajador():
    try:
        conn = p.mysql_connect()  # Conectar a la base de datos
        cursor = conn[0].cursor()  # Crear un cursor

        query = "SELECT * FROM trabajador;"
        cursor.execute(query)  # Ejecutar una consulta

        data = cursor.fetchall()  # Traer los resultados de un select
        lista = []

        if data:
            for j in data:
                lista.append(cargaTrabjador(j))

        cursor.close()  # Cerrar el cursor
        conn[0].close()  # Cerrar la conexión MYSQL
        conn[1].close()  # Cerrar la conexión SSH

    except Exception as e:
        data = "Exeception occured:{}".format(e)

    return lista


def listaTrabajadorWhere(where):
    try:
        conn = p.mysql_connect()  # Conectar a la base de datos
        cursor = conn[0].cursor()  # Crear un cursor

        query = "SELECT * FROM trabajador WHERE " + where + ";"
        cursor.execute(query)  # Ejecutar una consulta

        data = cursor.fetchall()  # Traer los resultados de un select
        users = []

        if data:
            for j in data:
                users.append(cargaTrabjador(j))

        cursor.close()  # Cerrar el cursor
        conn[0].close()  # Cerrar la conexión MYSQL
        conn[1].close()  # Cerrar la conexión SSH

    except Exception as e:
        data = "Exeception occured:{}".format(e)

    return users


def leeTrabajador(where):
    try:
        conn = p.mysql_connect()  # Conectar a la base de datos
        cursor = conn[0].cursor()  # Crear un cursor

        query = "SELECT * FROM trabajador WHERE " + where + ";"
        cursor.execute(query)  # Ejecutar una consulta

        data = cursor.fetchone()  # Traer los resultados de un select
        users = None

        if data:
            users = cargaTrabjador(data)

        cursor.close()  # Cerrar el cursor
        conn[0].close()  # Cerrar la conexión MYSQL
        conn[1].close()  # Cerrar la conexión SSH

    except Exception as e:
        data = "Exeception occured:{}".format(e)

    return users


def cargaTrabjador(obj):
    persona = Persona(
        obj[0],  # id
        obj[1],  # nombre
        obj[2],  # apellidos
        obj[3],  # email
        obj[4]  # sexo
    )
    return persona


def grabaTrabajadorNO(nuevo, id, nombre, apellidos, email, sexo):
    correcto = False

    try:
        conn = p.mongodb_connect()
        mydb = conn[0]["Empresa"]
        mycol = mydb["Trabajador"]

        if nuevo:
            mydict = {
                "idTrabajador": id,
                "nombre": nombre,
                "apellidos": apellidos,
                "email": email,
                "sexo": sexo
            }

            x = mycol.insert_one(mydict)
            id = x.inserted_id

        else:
            a = "update"

        conn[0].close()  # Cerrar la conexión MongoDB
        conn[1].close() # Cerrar la conexión SSH

        correcto = True
    except Exception as e:
        correcto = "Exeception occured:{}".format(e)

    return correcto, id


def listaTrabajadorNo():
    try:
        conn = p.mongodb_connect()
        mydb = conn[0]["Empresa"]
        mycol = mydb["Trabajador"]

        data = mycol.find()
        users = []

        if data:
            for j in data:
                users.append(cargaTrabjadorNo(j))

        conn[0].close()  # Cerrar la conexión MongoDB
        conn[1].close()  # Cerrar la conexión SSH

    except Exception as e:
        data = "Exeception occured:{}".format(e)

    return users


def cargaTrabjadorNo(obj):
    persona = Persona(
        obj["idTrabajador"],  # id
        obj["nombre"],  # nombre
        obj["apellidos"],  # apellidos
        obj["email"],  # email
        obj["sexo"],  # sexo

    )
    return persona
