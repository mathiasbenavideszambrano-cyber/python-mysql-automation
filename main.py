import mysql.connector
from datetime import datetime

def conectar_db():
    """Conecta a MySQL y automatiza gestión de datos"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="automatizacion_db"
        )
        print(f"[{datetime.now()}] Conexión exitosa a MySQL")
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def automatizar_proceso():
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT PRIMARY KEY, mensaje VARCHAR(255), fecha DATETIME)")
        cursor.execute("INSERT INTO logs (mensaje, fecha) VALUES (%s, %s)", ("Proceso automatizado ejecutado", datetime.now()))
        conn.commit()
        print("Proceso automatizado completado")
        conn.close()

if __name__ == "__main__":
    automatizar_proceso()
