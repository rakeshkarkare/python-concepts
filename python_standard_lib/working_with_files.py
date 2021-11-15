from pathlib import Path
from time import ctime
import shutil

source = Path("modules_in_python/ecommerce/__init__.py")

target = Path() / "__init__.py"
# path.exists()
# path.rename("init.txt")
# path.unlink()

# print(ctime(path.stat().st_ctime))

# with open("__init__.py", "r") as file:
#     ...

# print(path.read_text())  # internally calls opening and closing of files
# path.write_text("....")
# path.write_bytes()

# target.write_text(source.read_text())
shutil.copy(source, target)
