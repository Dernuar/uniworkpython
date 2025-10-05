from time import sleep
from datetime import *

def main():
    for i in range(5):
        print(datetime.now().strftime('%H:%M:%S'))
        sleep(1)

if __name__ == '__main__':
    main()