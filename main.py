#LIFE CALCULATOR
print("Welcome to Life Calculator. Make sure you read the instructions carefully.")
worktime = ""
tasks = []
traveltime = ""
fulltime=""
worktime = int(input("What time do you have to get to work for? Ex. ('8')>>>"))
worktime = worktime
print(f"You have to be at work for {worktime}:00")
traveltime = int(input("How many minutes does it take you to get from home to work? Ex. ('23')>>>"))

print(f"It takes {traveltime} minutes for you to get to work from home.")

print("Thank you. Just a few more questions")

to_dos = input("What do you do in the morning? Ex. ('This, That, This') >>> ")
tasks.append(to_dos)

print(f"When you wake up, you have to do the following: {tasks}")
tasks = to_dos.split(",")


total_time=0
each_time=[]
for x in tasks:
    task_time = input(f"How many minutes does it take you to {x}? ")
    each_time.append(task_time)
    total_time= total_time+ int(task_time)
#print(total_time)
print(each_time)
fulltime= total_time + traveltime
print(f"The total time for you to get ready and get to work is {fulltime} minutes" )

print("------------------------------")
print("This is your agenda for the day")

wake_up= worktime-fulltime
print(f"The time you need to wake up is {wake_up}")
#go_to_sleep=wake_up - 8
