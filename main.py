"""Homework lesson 4 Triangle Border"""
"""
       $       
      $ $      
     $   $     
    $     $    
   $       $   
  $         $  
 $           $ 
$$$$$$$$$$$$$$$

"""

rows = int(input("How many Rows: "))  # input rows
symbol = input("Please write symbol to draw: ")  # symbol to draw


def draw_triangle(n, s):
    for row in range(1, n + 1):  # draw rows
        for col in range(1, 2 * n):  # draw columns
            if row == n or row + col == n + 1 or col - row == n - 1:
                # row == n to print down side, row +col == n + 1 to print left side, col - row == n - 1 to print right side
                print(f"{s}", end='')
            else:
                print(end=" ")  # to print space
        print()  # print new row


draw_triangle(rows, symbol)
