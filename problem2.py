import numpy as np
mat1=np.arange(100,200,5) #first and second argument gives the range og values..and third argument gives the space between them

final_mat=mat1[0:16].reshape(8,2)
print(final_mat)
