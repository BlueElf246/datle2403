from time import time
start_time=time()
k=0
for i in range(0,100000000):
    k+=i
end_time=time()
elapsed= end_time-start_time
print(elapsed)