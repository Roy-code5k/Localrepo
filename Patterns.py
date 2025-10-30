'''
*****
*****
*****
***** 
*****
'''

n = 5
for i in range(n):
    for j in range(n):
        print("*", end='')
    print() 


'''
*
**
***
****
*****
'''

n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print() 


'''
*****
****
***
**
*
'''

n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end='')
    print()


# n = int(input("Enter: "))
# for i in range(n):
#     if n < 0:
#         break
#     print("*"*(2*n - 2*i - 1))


'''
     *
    **
   ***
  ****
 *****
'''

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    for k in range(i+1):
        print("*", end='')
    print()


'''
    *
   ***
  *****
 *******
*********
'''

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print()

# n = int(input("Enter:"))
# for i in range(n):
#     print(" "*(n-i-1)+"*"*(2*i+1))



'''
*********
 *******
  *****
   ***
    *
'''

n = 5
for i in range(n):
    for j in range(i):
        print(" ", end='')
    for k in range(2*(n-i)-1):
        print("*", end='')
    print()

# n = 5
# for i in range(n-1, -1, -1):
#     print(" "*(n-i-1)+"*"*(2*i + 1))

'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''

n = int(input("Enter:"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i + 1))
for i in range(n-1, -1, -1):
    print(" "*(n-i-1)+"*"*(2*i + 1))


'''
1
12
123
1234
12345
'''

n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1, end='')
    print()


'''
12345
1234
123
12
1
'''

n = 5
for i in range(n):
    for j in range(n-i):
        print(j+1, end='')
    print()