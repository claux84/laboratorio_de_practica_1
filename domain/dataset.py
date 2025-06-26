from abc import ABC, abstractmethod
import pandas as pd
from util.validationutils import validate_email, validate_phone_number

class Dataset(ABC):
    def __init__(self, source):
        self.__source = source
        self.__data = None

    @property
    def source(self):
        return self.__source
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        # validaciones
        self.__data = value

    @abstractmethod
    def load_data(self):
        pass

    def validate_data(self):
        
        if self.data is None:
            raise ValueError("Los datos no fueron cargados correctamente")
        else:
            df = self.data
        
        # Validaciones básicas: tipos, no nulos, duplicados
        if self.data.isnull().sum().sum() > 0:
            df = df.dropna()
            print("Datos nulos encontrados y eliminados.")
        if self.data.duplicated().sum() > 0:
            df = df.dropduplicates()
            print("Filas duplicadas detectadas y eliminadas.")

        if 'name' in df.columns:
            df['name'] = df['name'].astype(str)
        if 'email' in df.columns:
            df['email'] = df['email'].astype(str)
            #df = df[df['email'].apply(validate_email)]
        
        if 'phone_number' in df.columns:
            phone_number = df['phone_number'].apply(validate_phone_number)
            invalid_count = phone_number.isnull().sum().sum()
            print("Se han encontrado ", invalid_count , " numeros invalidos")
            #df = df[df['phone_number'].apply(validate_phone_number)]


        try:
            for col in df.columns:
                if df[col].dtype == 'object':
                    time_column = pd.to_datetime(df[col], errors = 'coerce', dayfirst= True)
                    nat_percentage = time_column.isnull().sum().sum()/len(df)
                    if nat_percentage < 0.1:
                        df[col] = time_column
        except Exception as e:
            print(f"Error validando fecha: {e}")


        df = df[(df['name'].notnull()) &  
                (df['email'].notnull())]
        
        
        
 
        

    



    