from pathlib import Path
from zipfile import ZipFile


with ZipFile("files.zip", "w") as zip:
    for path in Path("modules_in_python/ecommerce").rglob("*.*"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("modules_in_python/ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
