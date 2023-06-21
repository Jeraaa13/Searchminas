import sqlite3

def crear_tabla_jugadores():
    with sqlite3.connect("bd_btf.db") as conexion:
        try:
            sentencia = ''' create table jugadores
                            (
                                id integer primary key autoincrement,
                                nombre text,
                                tiempo real
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla jugadores")
        except sqlite3.OperationalError:
            print("La tabla jugadores ya esta creada")

def leer_tabla_jugadores():
    with sqlite3.connect("bd_btf.db") as conexion:
        cursor = conexion.execute("SELECT nombre, tiempo FROM jugadores ORDER BY tiempo ASC LIMIT 10")
        resultados = cursor.fetchall()
    
    return resultados

def modificar_tabla_jugadores(nombre, tiempo):
    with sqlite3.connect("bd_btf.db") as conexion:
        cursor = conexion.cursor()
        
        cursor.execute("SELECT nombre FROM jugadores WHERE nombre = ?", (nombre,))
        registro_existente = cursor.fetchone()

        if registro_existente:
            cursor.execute("UPDATE jugadores SET tiempo = ? WHERE nombre = ?", (tiempo, nombre))
        else:
            cursor.execute("INSERT INTO jugadores (nombre, tiempo) VALUES (?, ?)", (nombre, tiempo))

        conexion.commit()
