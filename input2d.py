import numpy as np
row=int(input("enter the number of rows:"))
col=int(input("enter the number of column:"))
print("Enter the entries in a single line(seperated by spaces):")

#user input of entries in single line seperated by spaces

entries=list(map(int, input().split()))
matrix=np.array(entries).reshape(row,col)
print(matrix)
 
np.savetxt('save_form',matrix,fmt='%s',delimiter=',',header='[',footer=']')

