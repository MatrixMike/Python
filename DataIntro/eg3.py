#eg3   on python3

shopping_list =["milk", "bread", "three"]

def show_list():
    print()
    print("list looks like this now=>")
    for item in shopping_list:
        print(item)
        
def check_list():
    if "eggs" not in shopping_list:
        print("Well we can't have that!")
        shopping_list.append("eggs")

    show_list()
#    shopping_list[]


if "milk" in shopping_list:
    print("Delicious!")

show_list()


        
check_list()    
print ("second try")
check_list()
# now to remove the bread
shopping_list.remove("bread")
show_list()
#shopping_list.remove("water")
show_list()



