# 37. Write a Python function to find the maximum and minimum numbers 
# in a list.


def max_min(a):
    minimun = min(lista)
    maximum = max(lista)
    return minimun, maximum


lista = [12,41,1,2,4,102,4124,34,12]

minimun, maximum = max_min(lista)


print(f"min: {minimun}")
print(f"max: {maximum}")
