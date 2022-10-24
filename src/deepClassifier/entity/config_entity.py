from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source",
    "local_data_file",
    "unzip_dir"
])