import time

def main():
    timer = int(input("Enter the time in seconds: "))

    for i in range(timer):
        print(timer)
        time.sleep(1)
        timer -= 1
    print("Time is up!")
        


main()