from pathlib import Path
path = Path("modules_in_python/ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

for p in path.iterdir():  # returns both files and directories
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]
print(paths)
print(py_files)
