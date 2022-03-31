"""
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * * """
n = 5
for row in range(1, n+1):
    for col in range(1,n+1):
        print("*", end=' ')
    print()


""" *
      *
        *
          *
            *
"""
n = 5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row == col:
            print("*", end=' ')
        else:
            print(" ", end =' ')
    print()

"""      *
      *
    *
  *
*     """
n = 4
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col ==  n+1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

"""*
    * *
    * * *
    * * * * """
n = 5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row > col:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

"""   * * * *
        * * *
          * *
            * """
n = 5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row < col:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()


""" * * * *   
    * * *     
    * *       
    *  """

n = 5
for row in range(1, n+1):
    for col in range(1,n+1):
        if row + col <= n:
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()

"""       * 
        * * 
      * * * 
    * * * * 
  * * * * * """
n= 6
for row in range(1,n+1):
    for col in range(1,n+1):
        if n+2<= row + col<= n+n :
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

n = 10
for row in range(1, n+1):
    for col in range(1, n+1):
        if (row==col or row+col == n+1):
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print()

print()
""" * * * * * * 
    *         * 
    *         * 
    *         * 
    *         * 
    * * * * * * 
"""
n = 6
for row in range(1, n+1):
    for col in range(1, n+1):
        if row == 1 or row == n or col == 1 or col == n:
            print("*", end =' ')
        else:
            print(" ", end=' ')
    print()

""" A B C D 
    E F G H 
    I J K L 
    M N O P """
n = 4
i = 0
for row in range(n):
    for col in range(n):
        print(chr(ord('A')+i), end=' ')
        i += 1
    print()

print()
""" A B C D 
    B C D E 
    C D E F 
    D E F G """
n = 4
i = 0
for row in range(n):
    for col in range(n):
        print(chr((ord('A')+i)+col), end=' ')
    i += 1
    print()


""" 1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 """
n = 5
i = 0
for row in range(1,n+1):
    for col in range(1, n+1):
        print(col+i, end=' ')
    print()

print()

""" 1 2 3 4 5 
    2 3 4 5 6 
    3 4 5 6 7 
    4 5 6 7 8 
    5 6 7 8 9 """
n = 5
i = 0
for row in range(1,n+1):
    for col in range(1, n+1):
        print(col+i, end=' ')
    i += 1
    print()

""" 6 5 4 3 2 1 
    6 5 4 3 2 1 
    6 5 4 3 2 1 
    6 5 4 3 2 1 
    6 5 4 3 2 1 
    6 5 4 3 2 1 """
n=6
for row in range(1, n+1):
    for col in range(n, 0, -1):
        print(col, end=' ')
    print()
print()

""" 4 3 2 1 
    3 2 1 0 
    2 1 0 -1 
    1 0 -1 -2 """
n=4
i = 0
for row in range(1, n+1):
    for col in range(n, 0, -1):
        print(col-i, end=' ')
    i += 1
    print()

"""1           
    2 3         
    4 5 6       
    7 8 9 10     
    11 12 13 14 15   
"""
n = 6
i = 1
for row in range(1, n+1):
    for col in range(1, n+1):
        if row > col:
            print(i, end=' ')
            i += 1
        else:
            print(" ", end=' ')
    print()
print()

"""  1 2 3 4 
        5 6 7 
          8 9 
            10 """
n = 5
i = 1
for row in range(1, n+1):
    for col in range(1, n+1):
        if row < col:
            print(i, end=' ')
            i += 1
        else:
            print(" ", end= ' ')
    print()

""" 1 2 3 4   
    5 6 7     
    8 9       
    10  """
n = 5
i = 1
for row in range(1, n+1):
    for col in range(1, n+1):
        if row+col <= n:
            print(i, end=' ')
            i += 1
        else:
            print(" ", end=' ')
    print()

"""   1 
    2 3 
  4 5 6 
7 8 9 10"""
n = 5
i = 1
for row in range(1, n+1):
    for col in range(2, n+1):
        if n+2 <= row+col <= n+n:
            print(i, end=' ')
            i += 1
        else:
            print(' ', end=' ')
    print()