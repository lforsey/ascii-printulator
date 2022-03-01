## Written by Liam Forsey 2022
## This program will return the ascii art versions of the letters you enter in terminal
import string
## First, we'll store all the ascii art alphabet characters IN A 0 INDEXED LIST FOO!


list_of_chars = [("""\

      A  
     A A 
    A   A
    AAAAA
    A   A
    A   A
    A   A
    """), ("""\

    BBBB 
    B   B
    B   B
    BBBB
    B   B
    B   B
    BBBB
    """), ("""\

     CCC 
    C   C
    C    
    C    
    C    
    C   C
     CCC 
    """), ("""\

    DDDD 
    D   D
    D   D
    D   D
    D   D
    D   D
    DDDD 
    """), ("""\

    EEEEE
    E    
    E    
    EEE  
    E    
    E    
    EEEEE
    """), ("""\

    FFFFF
    F    
    F    
    FFF  
    F    
    F    
    F    
    """), ("""\
    
     GGG 
    G   G
    G    
    GGGGG
    G   G
    G   G
     GGG 
    """), ("""\

    H   H
    H   H
    H   H
    HHHHH
    H   H
    H   H
    H   H
    """), ("""\

    IIIII
      I  
      I  
      I  
      I  
      I  
    IIIII
    """), ("""\

    JJJJJ
      J  
      J  
      J  
    J J  
    J J  
     JJ
    """), ("""\

    K   K
    K  K
    K K
    KK
    K K
    K  K
    K   K
    """), ("""\

    L    
    L    
    L    
    L    
    L    
    L    
    LLLLL
    """), ("""\

    M   M
    MM MM
    MM MM
    M M M
    M   M
    M   M
    M   M
    """), ("""\
    
    N   N
    NN  N
    N N N
    N  NN
    N   N
    N   N
    N   N
    """), ("""\

     OOO 
    O   O
    O   O
    O   O
    O   O
    O   O
     OOO 
    """), ("""\

    PPPP 
    P   P
    P   P
    PPPP 
    P    
    P    
    P    
    """), ("""\

     QQQ 
    Q   Q
    Q   Q
    Q   Q
    Q   Q
    Q  Q 
     QQ Q
    """), ("""\

    RRRR 
    R   R
    R   R
    RRRR 
    R R  
    R  R 
    R   R
    """), ("""\

     SSS 
    S   S
    S    
     SSS 
        S
    S   S
     SSS
    """), ("""\

    TTTTT
      T  
      T  
      T  
      T  
      T  
      T  
    """), ("""\

    U   U
    U   U
    U   U
    U   U
    U   U
    U   U
     UUU
    """), ("""\

    V   V
    V   V
    V   V
    V   V
    V   V
     V V 
      V  
    """), ("""\

    W   W
    W   W
    W   W
    W W W
    WW WW
    WW WW
    W   W
    """), ("""\

    X   X
    X   X
     X X 
      X  
     X X 
    X   X
    X   X
    """), ("""\

    Y   Y
     Y Y 
      Y  
      Y  
      Y  
      Y  
      Y  
    """), ("""\

    ZZZZZ
        Z
       Z 
      Z  
     Z   
    Z
    ZZZZZ
    """)]



##Then, greet the user and ask for their initials in two different lines
print()
print("Hi, welcome to the ASCII generator")
print()
print("This program was written by Liam Forsey 2022")
print()


##There must be a more efficient way to write this -- Edit: Look how gosh darned efficient this is!


def get_index(initial):
  initial = initial.lower()
  initial = string.ascii_lowercase.index(initial)
  return initial


index_first = get_index(input("Enter your first initial here: "))

if index_first in range (0, 26):
    print(list_of_chars[index_first])

index_second = get_index(input("Enter your second initial here: "))

if index_second in range (0, 26):
    print(list_of_chars[index_second])

index_last = get_index(input("Enter your last initial (or your dogs initial) here: "))

if index_last in range (0, 26):
    print(list_of_chars[index_last])

print()
input("Hit enter to exit this program at any time")