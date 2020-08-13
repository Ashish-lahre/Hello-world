import pathlib
import shutil
import time
from_path = pathlib.Path('C:/users/Durga/Downloads')
while True:
    for file in from_path.iterdir():
        file_in_string = str(file)
        if '.png' in file_in_string:
            time.sleep(0.005)
            shutil.move(str(file), "E:\png")




