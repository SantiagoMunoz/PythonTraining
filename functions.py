def convert_to_uppercase(str_in):
    return str_in.upper()

def greeter(name,rude=False):
    """Displays greeting""" #docstring
    if(not rude):
        print("Hello " + convert_to_uppercase(name) + "!")
    else:
        print(name + " sucks")
#Arbitraty no of args get packed into a tuple
def arbitraty_no_args(text,*args):
    print(text)
    print(args)
#Arbitrary no of keyword arguments get packed into a dictionary
def arbitrary_pos_args(text, **args):
    print(args)

#Alterations to lists are permanent, unless you pass a copy
def add_item_to_list(m_list):
    m_list.append("Extra!")

greeter(input("What is your name? "))
greeter(input("What is your name? "),rude=True)
m_list = []
add_item_to_list(m_list)
print(m_list)
#By passing a copy, m_list is not modified
add_item_to_list(m_list[:])
arbitrary_pos_args("hey", key1="cat", key2="dog")
