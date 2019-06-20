import os
from zipfile import ZipFile
import nmt

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def start():
    if os.path.isdir("pretrained_model"):
        return

    # print("START DOWNLOAD MODEL")
    # id_str = '1Y0u3V9Ml9m4vgEaylVy5xEgKzpkmZVfg'
    file_path = os.path.join(CURRENT_PATH, "pretrained_model.zip")
    # utils.download_file_from_google_drive(id_str, file_path)

    # Unzip model
    print("START UNZIP MODEL")
    with ZipFile(file_path, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall()


def translation(text=""):
    start()
    return nmt.translate(text)[0].decode("utf-8")
