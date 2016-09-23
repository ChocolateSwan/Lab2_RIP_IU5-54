def min_arr (array):
 min_in_array = array[0]
 for m in array:
     if m<min_in_array:
       min_in_array=m
 print("Минимум в массиве:",min_in_array)
def sr_ar_arr(array):
 sum = 0
 for m in array:
     sum=sum+m
 sum=sum/len(array)
 print ("Средне арифметическое:",sum)
my_array_1 = [3, 4, 5, 1, 6]
my_array_2 = [30, 4643, 50, 135, 67]
print("Массив 1:")
min_arr(my_array_1)
sr_ar_arr(my_array_1)
print("Массив 2:")
min_arr(my_array_2)
sr_ar_arr(my_array_2)
