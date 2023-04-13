import numpy as np


rand_ = np.round(np.random.rand(24),2)*100
rand_= rand_.reshape(6,4)

rand_   # 5th row with 1st and third index=(0,2) , 6th row with 2nd and 4th index=(1,3)

ran_1=rand_[0:3:2]   # sliced 1st and 3rd row
ran_2=rand_[1:4:2]   # sliced 2nd and 4th row  

rand_[4]= ran_1 [0] + ran_1[1]  
rand_[5]= ran_2 [0] + ran_2[1]    # summed the sliced rows mentioned in the assignment

rand_  # replaced successfully


