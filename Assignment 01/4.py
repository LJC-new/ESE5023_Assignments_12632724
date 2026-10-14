x = int(input("请输入一个0-100的整数 ："))
def Least_moves(x):
    n = x          
    moves = 0    
    while n > 1:               
        if n % 2 == 0:         
            n = n // 2
        else:                  
            n = n - 1
        moves = moves + 1      
    print(moves)  
Least_moves(x)