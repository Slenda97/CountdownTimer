import time

def main():
    timer = 10

    for i in range(timer):
        print(timer)
        time.sleep(1)
        timer -= 1
    print("Time is up!")
        


main()