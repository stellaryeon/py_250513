import numpy as np
d = np.array([[1,2,3,4,5,6],
              [7,8,9,10,11,12]])  
d1=d[:,::1]  # 홀수열만만
print(d1,d1.shape) 
