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
        pass

    def show_summary(self):
        pass
    



    