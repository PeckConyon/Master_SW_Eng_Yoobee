# example 5
from random import randint



def add(a1, a2):
    return a1 + a2

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += randint(1, 3)
        new_item = add(new_item, item)
    b_list.append(new_item)

    print(b_list)
    
def main():
    a_demo_list = [1, 2, 3, 5, 1, 21, 4, 35]
    mutate(a_demo_list)

if __name__ == "__main__":
    main()