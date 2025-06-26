from os import path
from domain.dataset_tsv import DatasetTSV
from domain.dataset_ods import DatasetODS
from data.data_saver import DataSaver


tsv_path = path.join(path.dirname(__file__), "files/users.tsv")
ods_path = path.join(path.dirname(__file__), "files/clientes.ods")


tsv = DatasetTSV(tsv_path)
tsv.load_data()
tsv.validate_data()


ods = DatasetODS(ods_path)
ods.load_data()
ods.validate_data()

db = DataSaver()
db.save_dataframe(tsv.data, "users")
db.save_dataframe(ods.data, "ventas")