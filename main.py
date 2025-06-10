from os import path
from domain.dataset_json import DatasetJSON
from domain.dataset_tsv import DatasetTSV
from data.data_saver import DataSaver

# Ruta de archivos
json_path = path.join(path.dirname(__file__), "files/friends.json")
tsv_path = path.join(path.dirname(__file__), "files/users.tsv")

# Cargar y transformar
tsv = DatasetTSV(tsv_path)
tsv.load_data()

json = DatasetJSON(json_path)
json.load_data()

db = DataSaver()
db.save_dataframe(tsv.data, "users")