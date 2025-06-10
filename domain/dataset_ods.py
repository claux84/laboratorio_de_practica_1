import pandas as pd
from domain.dataset import Dataset
from pandas_ods_reader import read_ods

class DatasetODS(Dataset):
    def __init__(self, source):
        super().__init__(source)

    def load_data(self):
        try:
            df = read_ods(self.source)
            self.data = df
            print("ODS cargado.")
            print(self.data)
            if self.validate_data():
                print("Datos validados en el ODS")
                self.process_data()
        except Exception as e:
            print(f"Error cargando ODS: {e}")