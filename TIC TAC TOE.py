import numpy as np
# MENU

p=["P1","P2"]
while True:
   print("WELCOME TO TIC TAC TOE !")
   print("Press 0 to Start: ")
   print("Press 1 to Enter The Your Names : ")
   print("Press 2 for instructions: ")

   q=input("")
   if q=="0":
      break
   elif q=="1":
      p1=input("Enter the name of Player 1 : ")  
      p2=input("Enter the name of Player 2 : ") 
      p[0]=p1
      p[1]=p2
      print(f"Names set: {p[0]} (X) vs {p[1]} (O)") 
   elif q=="2":
      print("""
Welcome to Tic Tac Toe!

Grid positions are numbered 1 to 9 like this:

## 1 | 2 | 3

## 4 | 5 | 6

## 7 | 8 | 9

How to play:

* Player 1 is 'X', Player 2 is 'O'.    
* On your turn, enter the number (1-9) corresponding to the cell you want to mark.
*f The game checks for a winner after each move.
* First player to align 3 marks horizontally, vertically, or diagonally wins.
* If all cells are filled and no one wins, the game ends in a tie.

Example:

* To mark the middle cell, enter 5.
* To mark the bottom-right cell, enter 9.

Enjoy the game!
"""
)
      
# GAME LOGIC

#UI
def print_board(a):
    print("\n")
    for i in range(3):
        row = []
        for j in range(3):

            # expanded if-else
            if a[i][j] != "":
                row.append(a[i][j])
            else:
                row.append(" ")

        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")
 #Maths
a = np.full((3, 3), "", dtype=str)
t=0
winner=False
print_board(a)
for i in range(9):
    if t%2==0:
        pos = int(input(f"Enter position {p[0]} (1-9): "))
        x = (pos - 1) // 3
        y = (pos - 1) % 3
        v=True
        while v:
          if a[x][y]=="":
             a[x][y]="X"
             v=False
          else:
             pos = int(input(f"Please enter a VOID position {p[0]} (1-9): "))
             x = (pos - 1) // 3
             y = (pos - 1) % 3
    else:
        pos = int(input(f"Enter position {p[1]} (1-9): "))
        x = (pos - 1) // 3
        y = (pos - 1) % 3
        v=True
        while v:
          if a[x][y]=="":
             a[x][y]="O"
             v=False
          else:
             pos = int(input(f"Please enter a VOID position {p[1]} (1-9): "))
             x = (pos - 1) // 3
             y = (pos - 1) % 3
    t+=1
    print_board(a)
    if t>=5:
        if a[0][0]==a[1][1]==a[2][2] and a[0][0]!="":
          if a[0][0]=="X":
             print(f"The Winner is {p[0]}  !!!")
             winner=True
             break
          else:
             print(f"The Winner is {p[1]}  !!!")
             break
        elif a[0][2]==a[1][1]==a[2][0] and a[0][2]!="":
          if a[0][2]=="X":
             print(f"The Winner is {p[0]}   !!!")
             winner=True
             break
          else:
             print(f"The Winner is {p[1]}   !!!")
             winner=True
             break
        for j in range(3):
            if np.all(a[:, j] == "X"):
                print(f"Winner is {p[0]}  !!!")
                winner = True
                break
            if np.all(a[:, j] == "O"):
                print(f"Winner is {p[1]}  !!!")
                winner = True
                break

            if np.all(a[j, :] == "X"):
                print(f"Winner is {p[0]} !!!")
                winner = True
                break
            if np.all(a[j, :] == "O"):
                print(f"Winner is {p[1]} !!!")
                winner = True
                break
        if winner: 
           break
if not winner:
   print("TIE")