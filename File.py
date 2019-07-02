#name = input("enter your name: ")

#print(name)

# f = open("name.txt", "r")
# print(f.readline())
#
# f = open("name.txt","r")
# for x in f:
#     print(x)
#
#     f = open("name.txt")
#     print(f.readline())
#     f.close()


reason=[]
reason =""

while reason != "reason":
    print('What is the reason')
    reason = input()


    with open("myreason.txt","a+") as file_object:
        file_object.write(reason)