import pandas as pd
from domain.dataset import Dataset

class DatasetTSV(Dataset):
    def __init__(self, source):
        super().__init__(source)

    def load_data(self):
        try:
            df = pd.read_table(self.source)
            self.data = df
            print(f"Archivo TSV cargado" )
        except Exception as e:
            print(f"Error cargando archivo TSV: {e}")