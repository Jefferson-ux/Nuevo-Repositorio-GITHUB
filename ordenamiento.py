""" Python Sort Methods"""
import time
my_list = [4,2,6,9,10,1,3,8,5,7]

def bubble_sort(parameter_list):
    """ Funcion de ordenamiento burbuja"""
    for i,elem in enumerate(parameter_list):
        actual = elem
        post = parameter_list[i+1] if i<len(parameter_list)-1 else actual
        temp = actual
        if actual > post:
            parameter_list[i]=post
            parameter_list[i+1]=temp
        time.sleep(.1)

bubble_sort(my_list)
print(my_list)
