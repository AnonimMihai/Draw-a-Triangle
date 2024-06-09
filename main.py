import perimeter
import time

"""""""""
def runprogram():
    if perimeter.perimterCLI() == 532 or 432:
        print("Exited with error.")
        time.sleep(4.3)
        return 1
    else:
        perimeter.drawTriangle()
"""""""""
if __name__ == "__main__":
    perimeter.perimterCLI()
    perimeter.drawTriangle()
    time.sleep(4.3)