
# coding: utf-8

# In[13]:


def Sub_Array_Max_Sum(arr, l, h) : 
      
    if (l == h) : 
        return arr[l] 
    
    m = (l + h) // 2
  
    return max(Sub_Array_Max_Sum(arr, l, m), Sub_Array_Max_Sum(arr, m+1, h), Sum_Array_Cross_Sum(arr, l, m, h)) 

def Sum_Array_Cross_Sum(arr, l, m, h) :  

    sum_one = 0; l_sum = -10000
      
    for i in range(m, l-1, -1) : 
        sum_one += arr[i] 
        l_sum = max(l_sum,sum_one)  

    sum_two = 0; r_sum = -10000
    
    for i in range(m + 1, h + 1) : 
        sum_two += arr[i]  
        r_sum = max(r_sum,sum_two) 
        
    return l_sum + r_sum;   

arr = [1,-3,2,-5,7,6,-1,-4,11,-23] 
n = len(arr) 
  
max_sum = Sub_Array_Max_Sum(arr, 0, n-1) 
print("Maximum SubArray sum is ", max_sum) 


# In[14]:


# Can we design a divide-and-conquer solution with a linear running time? 
# Yes it can be done as follows
def large_cont_sum(arr):
    
    if len(arr) == 0:
        return 0
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum,max_sum)
    return max_sum

arr = [1,-3,2,-5,7,6,-1,-4,11,-23] 
max_sum = large_cont_sum(arr) 
print("Maximum SubArray sum is ", max_sum) 

