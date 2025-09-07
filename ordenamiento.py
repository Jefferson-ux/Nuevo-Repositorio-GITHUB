""" Python Sort Methods"""
import time
my_list = [4,2,6,9,10,1,3,8,5,7]

def bubble_sort(parameter_list):
    """ Funcion de ordenamiento burbuja"""
    n = len(parameter_list)
    for i in range(1,n):
        for j in range (0,n-1):
            if parameter_list[j]>parameter_list[j+1]:
                temp = parameter_list[j]
                parameter_list[j] = parameter_list[j+1]
                parameter_list[j+1]= temp
            time.sleep(.1)
    return parameter_list

bubble_sort(my_list)
print(my_list)

