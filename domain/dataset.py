from abc import ABC, abstractmethod
import pandas as pd

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
            raise ValueError("Datos no cargados correctamente")
        
        try:
        
            for col in self.data.columns:
                pd.to_datetime(self.data[col], errors = 'coerce', format = 'd/%m/%Y')
                if self.data[col].dtype == 'datetime64[ns]':
                    print("La columna " + col + " es de tipo datetime64[ns]")
                else:
                    print("La columna " + col + " no es de tipo datetime64[ns]")
        except Exception as e:
            print(f"Error validando fecha: {e}")
        
 
        print(self.data.dtypes)

        if self.data.isnull().sum().sum() > 0:
            print("Datos faltantes detectados.")
        if self.data.duplicated().sum() > 0:
            print("Filas duplicadas detectadas.")

    



    