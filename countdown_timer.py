import time

my_time = int(input('Enter the number of seconds for countdown: '))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print("Time's Up!")