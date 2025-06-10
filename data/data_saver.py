import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config 


class DataSaver:
    def __init__(self):
         user = config('DB_USER')
         password = config('DB_PASSWORD')
         host = config('DB_HOST')
         port = config('DB_PORT')
         database = config('DB_NAME')

         url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
         self.engine = create_engine(url)


    def save_dataframe(self, df, table_name):
        if df is None:
            print(f"No se puede guardar los datos porque la tabla {table_name} esta vacia")
            return

        if not isinstance(df, pd.DataFrame):
            print(f"Tipo inválido: se esperaba un DataFrame, se recibió {type(df)}.")
            return

        try:

            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)

            print(f"Datos guardados en tabla: {table_name}")

        except SQLAlchemyError as e:
            print(f"Error guardando datos: {e}")