from sqlalchemy import create_engine, text

# Configurar la conexión a la base de datos Sakila
engine = create_engine('mysql+mysqlconnector://root:rootserver@localhost:3306/sakila')

# Ejecutar la consulta
with engine.connect() as connection:
    result = connection.execute(text('SHOW FULL TABLES;'))
    tables = result.fetchall()

# Imprimir los resultados
for table in tables:
    print(table)
