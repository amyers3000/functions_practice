def hello():
    print('Hello')
hello()

def pack(x, y, z):
    new_list = [x, y, z]
    print (new_list)
pack('ham', 'turkey', 'swiss')

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

eat_lunch([])
eat_lunch(['Sandwich'])
eat_lunch(["apple", "cake"])