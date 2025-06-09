import pandas as pd
from domain.dataset import Dataset

class DatasetJSON(Dataset):
    def __init__(self, source):
        super().__init__(source)

    def load_data(self):
        try:
            df = pd.read_json(self.source)

            # Verificar si un vañor es una lista
            def es_lista(x):
               return isinstance(x, list)

            # Transformar todas las columnas tipo list a string
            def lista_a_string(x):
                if isinstance(x, list):
                    return ', '.join(map(str, x))

            for col in df.columns:
                if df[col].apply(es_lista).any():
                    df[col] = df[col].apply(lista_a_string)

            self.data = df
            
            print(self.data)
            print("JSON cargado")

            if self.validate_data():
                 print("Datos validados en el Json")
                 self.process_data()
        except Exception as e:
            print(f"Error cargando JSON: {e.__getstate__}")