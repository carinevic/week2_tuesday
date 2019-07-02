import json
import todotask
import Todolist


list =[]

t1 = todotask.Todo_task("wash car","high")
list = Todolist.Todolist("mow lawn","low")

print("press 1 to add task: ")
print("press 2 to del task: ")
print("press 3 to view task: ")


task =[]

task=[ {"title": "wash car",
         "priority": "high"},

       {"title":"mow lawn" ,
         "priority":"low"}]



with open("tasklist.json", "w") as file_object:
     json.dump(task,file_object)

