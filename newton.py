import math
tolerance = 0.000001

def newton(x):
    estimate = 1.0
    while True:
     estimate = (estimate + x / estimate) / 2
     difference = abs(x - estimate ** 2)
     if difference <= tolerance:
         break
    return estimate

def main():
    while True:
        x = input("Enter a positive number or press enter to quit: ")
        if x == "":
            break
        x = float(x)
        i = newton(x)
        ii = math.sqrt(x)
        print("The programs estimate of the square root of ", x, "is: %0.15f"% i)
        print("Python's estimate is: %0.15f"% ii)

if __name__ == '__main__':
    main()
