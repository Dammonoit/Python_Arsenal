import random  
rand_list = []  
for i in range(0,10):  
    n = random.randint(1,50)  
    rand_list.append(n)  
print(rand_list)  


random_list_final = random.sample(range(10, 40), 6)  
print(random_list_final)  