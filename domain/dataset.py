from abc import ABC, abstractmethod

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
            raise ValueError("Datos no cargados")
        
        print(self.data.dtypes)

        if self.data.isnull().sum().sum() > 0:
            print("Datos faltantes detectados.")
        if self.data.duplicated().sum() > 0:
            print("Filas duplicadas detectadas.")
        return True

    def process_data(self):
        if self.data is not None:
            self.__data.columns = self.data.columns.str.lower().str.replace(" ", "_")
            self.__data = self.data.drop_duplicates()
            for col in self.data.select_dtypes(include="object").columns:
                self.__data[col] = self.data[col].astype(str).str.strip()
            print("Transformaciones aplicadas")
        else:
            print("No hay datos para transformar.")

    def show_summary(self):
        return print(self.data.describe(include='all') if self.data is not None else "No hay Datos")
    



    