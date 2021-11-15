import subprocess

try:
    completed = subprocess.run(["python3", "python_standard_lib/other.py"],
                               capture_output=True,
                               text=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
