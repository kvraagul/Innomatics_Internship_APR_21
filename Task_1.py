#!/usr/bin/env python
# coding: utf-8

# # INNOMATICS INTERNSHIP APRIL 2021
# 
# ## TASK 1
# 

# In[1]:


#Question 1

print("Hello, World!")


# In[2]:


#Question 2

n=int(input('enter a value = '))

if n%2==0:
    if n in range(2,5):
        print('Not Weird')
    elif n in range(6,21):
        print('Weird')
    elif n > 20:
        print('Not Weird')

else:
    print('Weird')


# In[3]:


#Question 3

a=int(input('enter value of a = '))
b=int(input('enter value of b = '))

print('{} \n{} \n{}'.format((a + b),(a - b),(a * b)))


# In[4]:


#Question 4

a=int(input('enter value of a = '))
b=int(input('enter value of b = '))

print("{} \n{}".format(a//b, a/b))


# In[5]:


#Question 5

n=int(input('enter a value = '))

for i in range(0,n):
    print(i*i)
    


# In[6]:


#Question 6

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input('enter the year'))
print(is_leap(year))


# In[7]:


#Question 7

n=int(input('enter a value = '))

for i in range(1,n+1):
  print(i,end='')


# In[ ]:




