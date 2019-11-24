import numpy as np

# Build 2 sample vectors
x = [i for i in range(1,5)]
y = [i for i in range(1,4)]
print("sample vector")
print(x)
print(y)
print("--------------------------")
# Build linear convolution by convolve() from numpy
def linear_convolution(vec1,vec2):
    return np.convolve(vec1,vec2,mode = 'full')

# Function convert a vector to a matrix for solve linear convolution
def convert_arr_to_custom_linear_matrix(vec1,vec2):   
    len1 = len(vec1)
    len2 = len(vec2)
    heightMatrix = len1 + len2 - 1
    widthMatrix = len2
    arr = [[0 for i in range(widthMatrix)] for i in range(heightMatrix)]
    countHeight = 0
    while(countHeight < heightMatrix):
        countWidth = 0
        while(countWidth < widthMatrix):
            if(((countHeight - countWidth) < len(vec1)) & ((countHeight - countWidth) >= 0)):
                arr[countHeight][countWidth] = vec1[countHeight - countWidth]
            else:
                arr[countHeight][countWidth] = 0
            countWidth+=1
        countHeight+=1
    return arr      

# Function solve linear convolution without convolve()
def solve_linear_convolution(vec1,vec2):
    arr = []
    len1 = len(vec1)
    len2 = len(vec2)
    if(len(vec1) > len(vec2)):
        arr1 = convert_arr_to_custom_linear_matrix(vec2,vec1)
        solve1 = [0 for i in range(len1 + len2 - 1)]
        countHeight = 0
        while(countHeight < len1 + len2 - 1):
            countWidth = 0
            while(countWidth < len1):
                solve1[countHeight] += arr1[countHeight][countWidth] * vec1[countWidth]               
                countWidth+=1
            countHeight+=1
        return solve1
    else: 
        arr2 = convert_arr_to_custom_linear_matrix(vec1,vec2)
        solve2 = [0 for i in range(len1 + len2 - 1)]
        countHeight = 0
        while(countHeight < len1 + len2 - 1):
            countWidth = 0
            while(countWidth < len2):
                solve2[countHeight] += arr2[countHeight][countWidth] * vec2[countWidth]               
                countWidth+=1
            countHeight+=1    
        return solve2

# Function convert a vector to a matrix for solve cyclic convolution
def convert_arr_to_custom_cyclic_matrix(vec1,vec2):   
    len1 = len(vec1)
    len2 = len(vec2)
    heightMatrix = len2
    widthMatrix = len2
    arr = [[0 for i in range(widthMatrix)] for i in range(heightMatrix)]
    countHeight = 0
    while(countHeight < heightMatrix):
        countWidth = 0
        while(countWidth < widthMatrix):
            if(((countHeight - countWidth) < len(vec1)) & ((countHeight - countWidth) >= 0)):
                arr[countHeight][countWidth] = vec1[countHeight - countWidth]
            else:
                if (countWidth >= len2 - len1 + 1 + countHeight):
                    arr[countHeight][countWidth] = vec1[len2 - countWidth + countHeight]
                else:
                    arr[countHeight][countWidth] = 0
            countWidth+=1
        countHeight+=1
    return arr

# Function solve cyclic convolution
def solve_cyclic_convolution(vec1,vec2):
    len1 = len(vec1)
    len2 = len(vec2)
    if(len(vec1) > len(vec2)):
        arr1 = convert_arr_to_custom_cyclic_matrix(vec2,vec1)
        solve1 = [0 for i in range(len1)]
        countHeight = 0
        while(countHeight < len1):
            countWidth = 0
            while(countWidth < len1):
                solve1[countHeight] += arr1[countHeight][countWidth] * vec1[countWidth]               
                countWidth+=1
            countHeight+=1
        return solve1
    else: 
        arr2 = convert_arr_to_custom_cyclic_matrix(vec1,vec2)
        solve2 = [0 for i in range(len2)]
        countHeight = 0
        while(countHeight < len2):
            countWidth = 0
            while(countWidth < len2):
                solve2[countHeight] += arr2[countHeight][countWidth] * vec2[countWidth]               
                countWidth+=1
            countHeight+=1    
        return solve2

# Function solve cyclic from linear
def solve_cyclic_from_linear(vec1,vec2):
    linear = solve_linear_convolution(vec1,vec2)
    lenLin = len(linear)
    i=0
    if len(vec1) > len(vec2):
        while(i<lenLin):
            linear[i] += linear[lenLin-len(vec2)+1+i]
            if i==len(vec2)-2:
                break
            i+=1
        k = lenLin - 1     
        while(k>=0):
            del linear[k]
            if k == lenLin - len(vec2) + 1: break
            k-=1
        return linear
    else:
        while(i<lenLin):
            linear[i] += linear[lenLin-len(vec1)+1+i]
            if i==len(vec1)-2:
                break
            i+=1
        k = lenLin - 1     
        while(k>=0):
            del linear[k]
            if k == lenLin - len(vec1) + 1: break
            k-=1
        return linear

    
#print result

print("linear convolution bằng hàm có sẵn")
print(linear_convolution(x,y))
print("lỉnear convolution bằng hàm tự code")
print(solve_linear_convolution(x,y))
print("cyclic convolution bằng hàm tự code")
print(solve_cyclic_convolution(x,y))
print("cyclic convolution tính từ linear convolution")
print(solve_cyclic_from_linear(x,y))
