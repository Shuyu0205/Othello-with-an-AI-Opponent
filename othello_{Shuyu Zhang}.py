# -*- coding: utf-8 -*-
""" A Python module for the Othello game. 

 
Full name: Shuyu Zhang 
StudentId: 10194589
Email: shuyu.zhang@student.manchester.ac.uk 
""" 
 
from copy import deepcopy # you may use this for copying a board 
 
def newGame(player1,player2):
     """      
     Make sure you write meaningful docstrings!
     """     
     game = {} 
     game['player1']=player1
     game['player2']=player2
     game['who']=1
     game['board']=[[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,2,1,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],]
     return game 
 
# TODO: All the other functions of Tasks 2-12 go here.
# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES! 
def printBoard(board):
    '''
    Task2
    '''
    print(' |a|b|c|d|e|f|g|h|')
    print(' +-+-+-+-+-+-+-+-+')
    lst=[]
    lstin=[]
    for r in range(8):
        for c in range(8):
            if board[r][c]==0:
                lstin.append(' ')
            if board[r][c]==1:
                lstin.append('X')
            if board[r][c]==2:
                lstin.append('O')
        lst.append(lstin)
        lstin=[]
    for r in range(8):
        print(str(r+1)+'|{0[0]}|{0[1]}|{0[2]}|{0[3]}|{0[4]}|{0[5]}|{0[6]}|{0[7]}|'.format(lst[r]))
    print(' +-+-+-+-+-+-+-+-+')
    return                  #useless, looks nicer

def strToIndex(s):
    '''
    Task3
    '''
    apht=['a','b','c','d','e','f','g','h']
    t=s.replace(' ','')
    t=t.casefold()
    if len(t)!=2:
        raise ValueError
    if not t.isalnum():
        raise ValueError
    if t.isalpha() or t.isdigit():
        raise ValueError
    try:
        t1=int(t[0])
        t2=t[1]
    except:
        t1=int(t[1])
        t2=t[0]
    if t1>8 or t1<1:
        raise ValueError
    if t2>'h' or t2<'a':
        raise ValueError
    c=apht.index(t2)
    r=t1-1
    return(r,c)

def indexToStr(t):
    '''
    Task4
    '''
    apht=['a','b','c','d','e','f','g','h']
    lst=list(t)
    r=lst[0]+1
    c=apht[lst[1]]
    s=str(c)+str(r)
    return s       

def loadGame():
    '''
    Task5
    '''
    try:
      f=open('game.txt','r')
    except:
      raise FileNotFoundError
    fr=f.readlines()
    lst=[]
    game={}
    try:
      if int(fr[2][:-1])>2 or int(fr[2][:-1])<1:
         raise ValueError
      game['player1']=fr[0][:-1]
      game['player2']=fr[1][:-1]
      game['who']=int(fr[2][:-1])
      for i in range(3,11):
          lst.append(fr[i].split(','))     
      for el in lst:
          if len(el[7])!=1:
              el[7]=el[7][:-1]          
          for j in range(8):
              el[j]=int(el[j])
    except:
      raise ValueError
    for el in lst:
        for j in range(8):
            if el[j]>2 or el[j]<0:
                raise ValueError
    game['board']=lst
    f.close()
    return game

def getLine(board,who,pos,dir):
    '''
    Task6
    '''
    line=[]
    pos=list(pos)
    dir=list(dir)
    dr=dir[0]
    dc=dir[1]
    r=pos[0]+dr
    c=pos[1]+dc
    if (r>7 or r<0) or (c>7 or c<0):
        return []
    if board[r][c]==0 or board[r][c]==who:
        return[]
    while board[r][c]!=who and r<=7 and c<=7 and r>=0 and c>=0 and board[r][c]!=0:
        line.append((r,c))
        r=r+dr
        c=c+dc
        if r>7 or r<0 or c>7 or c<0:
            return []
        if board[r][c]==0:
            line.remove((r-dr,c-dc))                 #useless but looks cool
            return []        
    return line

def getValidMoves(board,who):
    '''
    Task7
    '''
    list1=list2=list3=list4=list5=list6=list7=list8=[]
    moves=[]
    for r in range(8):
        for c in range(8):
            if board[r][c]==0:
              list1=getLine(board,who,(r,c),(0,1))
              list2=getLine(board,who,(r,c),(0,-1))
              list3=getLine(board,who,(r,c),(1,0))
              list4=getLine(board,who,(r,c),(-1,0))
              list5=getLine(board,who,(r,c),(1,1))
              list6=getLine(board,who,(r,c),(1,-1))
              list7=getLine(board,who,(r,c),(-1,-1))
              list8=getLine(board,who,(r,c),(-1,1))
            if list1!=[] or list2!=[] or list3!=[] or list4!=[] or list5!=[] or list6!=[] or list7!=[] or list8!=[]:
              moves.append((r,c))
              list1=list2=list3=list4=list5=list6=list7=list8=[]
    return moves
        
def makeMove(board,move,who):
    '''
    Task8
    '''
    lst=[]
    list1=list2=list3=list4=list5=list6=list7=list8=[]
    move=list(move)
    r=move[0]
    c=move[1]
    list1=getLine(board,who,(r,c),(0,1))
    list2=getLine(board,who,(r,c),(0,-1))
    list3=getLine(board,who,(r,c),(1,0))
    list4=getLine(board,who,(r,c),(-1,0))
    list5=getLine(board,who,(r,c),(1,1))
    list6=getLine(board,who,(r,c),(1,-1))
    list7=getLine(board,who,(r,c),(-1,-1))
    list8=getLine(board,who,(r,c),(-1,1))
    board[r][c]=who
    for el in list1:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    for el in list2:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    for el in list3:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    for el in list4:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    for el in list5:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    for el in list6:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    for el in list7:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    for el in list8:
        lst=list(el)
        r_1=lst[0]
        c_1=lst[1]
        board[r_1][c_1]=who
    return board  
 
def scoreBoard(board):
    '''
    Task9
    '''
    p1=0
    p2=0
    for r in range(8):
        for c in range(8):
            if board[r][c]==1:
                p1=p1+1
            if board[r][c]==2:
                p2=p2+1
    diff=p1-p2
    return diff  

def suggestMove1(board,who):
    '''
    Task10
    '''
    max=scoreBoard(deepcopy(board))
    min=scoreBoard(deepcopy(board))
    moves=getValidMoves(deepcopy(board),who)
    if moves==[]:
        return None
    if len(moves)==1:
        return moves[0]
    if who==1:        
        for el in moves:
            ___=makeMove(deepcopy(board),el,who)
            score=scoreBoard(___)
            if score>=max:
               choice=el
               max=score
            board=deepcopy(board)
        return choice
    if who==2:
        for el in moves:
            ___=makeMove(deepcopy(board),el,who)
            score=scoreBoard(___)
            if score<=min:
               choice=el
               min=score
            board=deepcopy(board)
        return choice
    

# ------------------- Main function -------------------- 
def play():
     """
     TODO in Task 11. Make sure to write meaningful docstrings!     
     """     
     print("*"*55)     
     print("***"+" "*8+"NOT WELCOME TO Shuyu'S OTHELLO GAME!"+" "*8+"***")     
     print("*"*55,"\n")     
     print("Enter the players' names, or type 'C' or 'L'.\n")     
     # TODO: Game flow control starts here 
     who=1
     sign=['(X)','(O)']
     player1=input('Name of player1:').capitalize()
     if player1!='L':
        while player1=='':
              player1=input('Name of player1:').capitalize()
        player2=input('Name of player2:').capitalize()
        while player2=='':
              player2=input('Name of player2:').capitalize()
        game=newGame(player1.capitalize(),player2.capitalize())
     else:
        game=loadGame()
        player2=game['player2']
        player1=game['player1']
        who=game['who']
     if player1!='C' and player2!='C':
        print('')
        print('Okay,let\'s play!')
        print('')
        printBoard(game['board'])
        valid=getValidMoves(game['board'],who)
        while valid!=[]:
              try:
               move=strToIndex(input(game['player'+str(who)].capitalize()+' '+str(sign[who-1])+':Which move to make?'))                          
               if move not in valid:
                  print('Invalid input.Try again!')
                  continue
              except:
                  print('Invalid input.Try again!')
                  continue
              print('')
              printBoard(makeMove(game['board'],move,who))
              if who==1:
                 who=2
              else:
                 who=1
              valid=getValidMoves(game['board'],who)
              if valid==[]:
                 print('')
                 print('No valid moves available for '+str(game['player'+str(who)]).capitalize()+' '+str(sign[who-1]))
                 print('Skip '+str(game['player'+str(who)]).capitalize())
                 print('')
                 if who==1:
                    who=2
                 else:
                    who=1
                 valid=getValidMoves(game['board'],who)
                 if valid==[]:
                    print('No valid moves available for both players, game over!') 
     if player1=='C' and player2!='C':
        game['player1']='Computer'
        print('')
        print('Okay,let\'s play!')
        print('')
        printBoard(game['board'])
        valid=getValidMoves(game['board'],who)
        while valid!=[]:
            if who==1:
             move=suggestMove1(game['board'],who)
             print('')
             print(str(game['player'+str(who)]).capitalize()+' '+str(sign[who-1])+' chose to move '+indexToStr(move))
             print('')
             printBoard(makeMove(game['board'],move,who))
             who=2
             valid=getValidMoves(game['board'],who)
            elif who==2:  
              try:
               move=strToIndex(input(game['player'+str(who)].capitalize()+' '+str(sign[who-1])+' :Which move to make? :'))                          
               if move not in valid:
                  print('Invalid input.Try again!')
                  continue
              except:
                  print('Invalid input.Try again!')
                  continue
              print('')
              printBoard(makeMove(game['board'],move,who))
              who=1
              valid=getValidMoves(game['board'],who)
            if valid==[]:
               print('')
               print('No valid moves available for '+str(game['player'+str(who)]).capitalize()+' '+str(sign[who-1]))
               print('Skip '+str(game['player'+str(who)]).capitalize())
               print('')
               if who==1:
                  who=2
               else:
                  who=1
               valid=getValidMoves(game['board'],who)
               if valid==[]:
                  print('No valid moves available for both players, game over!')
     if player1!='C' and player2=='C':
        game['player2']='Computer'
        print('')
        print('Okay,let\'s play!')
        print('')
        printBoard(game['board'])
        valid=getValidMoves(game['board'],who)
        while valid!=[]:
            if who==2:
             move=suggestMove1(game['board'],who)
             print('')
             print(str(game['player'+str(who)]).capitalize()+' '+str(sign[who-1])+' chose to move '+indexToStr(move))
             print('')
             printBoard(makeMove(game['board'],move,who))
             who=1
             valid=getValidMoves(game['board'],who)
            elif who==1:  
              try:
               move=strToIndex(input(game['player'+str(who)].capitalize()+' '+str(sign[who-1])+' :Which move to make? :'))                          
               if move not in valid:
                  print('Invalid input.Try again!')
                  continue
              except:
                  print('Invalid input.Try again!')
                  continue
              print('')
              printBoard(makeMove(game['board'],move,who))
              who=2
              valid=getValidMoves(game['board'],who)
            if valid==[]:
               print('')
               print('No valid moves available for '+str(game['player'+str(who)]).capitalize()+' '+str(sign[who-1]))
               print('Skip '+str(game['player'+str(who)]).capitalize())
               print('')
               if who==1:
                  who=2
               else:
                  who=1
               valid=getValidMoves(game['board'],who)
               if valid==[]:
                  print('No valid moves available for both players, game over!')
     if player1=='C' and player2=='C':
        game['player1']='Computer1'
        game['player2']='Computer2'
        print('')
        print('Okay,let\'s play!')
        print('')
        printBoard(game['board'])
        valid=getValidMoves(game['board'],who)
        while valid!=[]:
              move=suggestMove1(game['board'],who)                          
              print('')
              print(str(game['player'+str(who)]).capitalize()+' '+str(sign[who-1])+' chose to move '+indexToStr(move))
              print('')
              printBoard(makeMove(game['board'],move,who))
              if who==1:
                 who=2
              else:
                 who=1
              valid=getValidMoves(game['board'],who)
              if valid==[]:
                 print('')
                 print('No valid moves available for '+str(game['player'+str(who)]).capitalize()+' '+str(sign[who-1]))
                 print('Skip '+str(game['player'+str(who)]).capitalize())
                 print('')
                 if who==1:
                    who=2
                 else:
                    who=1
                 valid=getValidMoves(game['board'],who)
                 if valid==[]:
                    print('No valid moves available for both players, game over!')
     score=scoreBoard(game['board'])
     if score>0:
       print('--------------------------------------')
       print(game['player1'].capitalize()+' '+sign[0]+' wins '+'with a score of '+str(int(abs(score))))
     if score<0:
       print('--------------------------------------')
       print(game['player2'].capitalize()+' '+sign[1]+' wins '+'with a score of '+str(int(abs(score))))
     if score==0:
       print('--------------------------------------')
       print('Tie! Good luck next time!')
     return
            
                  
# the following allows your module to be run as a program 
if __name__ == '__main__' or __name__ == 'builtins': 
   play()
    

