from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Country  # Suponiendo que has definido la clase Country que representa la tabla "country"
import mysql.connector


# Configurar la conexión a la base de datos Sakila
engine = create_engine('mysql+mysqlconnector://root:rootserver@192.168.8.120:3306/sakila')

Session = sessionmaker(bind=engine)
session = Session()

# Realizar la consulta
countries = session.query(Country.country_id, Country.country).all()

# Imprimir los resultados
for country in countries:
    print(country.country_id, country.country)
