#Задание 1

def fact(x):
    if (x == 0 or x == 1):
        return 1
    else:
        return x * fact(x - 1)


#Задание 2

def filter_even(li):
    fil_li = list(filter(lambda x: x % 2 == 0, li))
    return fil_li


#Задание 3

def square(li):
    sq_li = list(map(lambda x: x ** 2, li))
    return sq_li


#Задание 4

def bin_search(li, element):
    for i in range(len(li)):
        if li[i] == element:
            return i
    return -1


    
