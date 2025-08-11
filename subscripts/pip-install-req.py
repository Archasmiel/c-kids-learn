import subprocess
import sys

# Default commands to run if none given
CMD: str = './python-win/python.exe -m pip install -r ./requirements.txt --target=python-win/libs'

if __name__ == "__main__":
    subprocess.run(CMD.split(' '), check=False)
            