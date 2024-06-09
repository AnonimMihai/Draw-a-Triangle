import turtle
import math
import time
import sys
def perimterCLI():
    global side1
    global side2
    global base
    # global angle1
    # global angle2
    # global angle3
    global perimetr
    global p
    global aria
    global angleA
    global angleB
    global angleC
    try:
        side1 = int(input("Right Side (px): "))
        side2 = int(input("Left side (px): "))
        base = int(input("Base (px): "))
    except:
        print("Sorry but you entered something wrong.")
        time.sleep(4)
        sys.exit("Error code: 432")
    # angle1 = int(input("Top angle (degrees): "))
    # angle2 = int(input("Left angle (degrees): "))
    # angle3 = int(input("Right angle (degrees): "))
    perimetr = side1+side2+base
    try:
        p = perimetr/2
        aria = math.sqrt(p*(p-side1)*(p-side2)*(p-base))

        angleA = math.asin((2*aria) / (side1 * side2)) # formula for angle A
        angleB = math.asin((2*aria) / (side2 * base)) # formula for angle B
        angleC = math.asin((2*aria) / (base * side1)) # formula for angle C
        angleA = math.degrees(angleA)
        angleB = math.degrees(angleB)
        angleC = math.degrees(angleC)
        print("The perimeter of the triangle is:", round(perimetr), "(px)", sep=" ")
        print(f"The angles are: {round(angleA)}, {round(angleB)}, {round(angleC)}.")
        if angleA + angleB + angleC > 178 and angleA + angleB + angleC < 182:
            print("The sum of all the angles in the triangle is:", round(angleA + angleB + angleC), "(degrees)", sep=" ")
            return 0
        else:
            print("The sum of the angles isn't 180 degrees.")
            time.sleep(4)
            sys.exit("Error code: 532.")
            # return 532
    except:
        print("Sorry but you entered something wrong.")
        time.sleep(4)
        sys.exit("Error code: 432")
        # return 432

def drawTriangle():
    canvas = turtle.Turtle()
    canvas.forward(base)
    canvas.left(180 - angleC)
    canvas.forward(side1)
    canvas.left(180 - angleA)
    canvas.forward(side2)
    turtle.done()
