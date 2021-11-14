from pathlib import Path

Path(r"C:\Program Files\Microsoft")  # r is raw string in this we don't have to give second \

# Path("/usr/local/bin")
# Path()
# Path("ecommerce/__init__.py")
# Path() / "ecommerce" / "__init__.py"
# Path.home()

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())
path = path.with_suffix("file.txt")
print(path)
