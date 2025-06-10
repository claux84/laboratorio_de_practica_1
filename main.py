from os import path
from domain.dataset_json import DatasetJSON
from domain.dataset_tsv import DatasetTSV
from domain.dataset_ods import DatasetODS
from data.data_saver import DataSaver

# Ruta de archivos
#json_path = path.join(path.dirname(__file__), "files/friends.json")
tsv_path = path.join(path.dirname(__file__), "files/users.tsv")
ods_path = path.join(path.dirname(__file__), "files/ventas.ods")

# Cargar y transformar
tsv = DatasetTSV(tsv_path)
tsv.load_data()

#json = DatasetJSON(json_path)
#json.load_data()

ods = DatasetODS(ods_path)
ods.load_data()

db = DataSaver()
db.save_dataframe(tsv.data, "users")
db.save_dataframe(ods.data, "ventas")