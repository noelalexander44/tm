import sys
from pip._internal import main as pipmain
import subprocess


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

if __name__ == '__main__':
    with open(r'C:\Users\noel.alexander\Downloads\requirements.txt') as f:
        for line in f:
            print(line)
            install(line)

