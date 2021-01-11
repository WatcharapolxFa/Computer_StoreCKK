import numpy as np
import time

 a = np.random.rand(2000,2000)
 c = np.zeros(2000)
t1 = time.time()
for j in range(100) :
  for i in range(a.shape[0]):

    c += a[ i, :]

t2 = time.time()
print('TIME [ row vector ]:',(t2,t1)/100)


