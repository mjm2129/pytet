from matrix import *
import random


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:

                print("XX", end='')
        print()


###
### initialize variables
###


arrayBlk = [[ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ],
            [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 1 ]],
            [ [ 1,1],[1,1]],
            [ [ 0, 1, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ]],
            [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 1, 1, 0 ]],
            [ [ 0, 1, 1 ], [ 1, 1, 0 ], [ 0, 0, 0 ]],
            [ [ 1, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 0 ]]]


### transpose 함수(2차원 배열 오른쪽 회전)
def transpose(a):
    m = len(a)
    ret = [[0] * m for _ in range(m)]

    for r in range(m):
        for c in range(m):
            ret[c][m-1-r] = a[r][c]
    a=ret
    return a
    
    
### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)


abc=random.randrange(0,7)# 시작할때 abc라는 수를 뽑아서
currBlk = Matrix(arrayBlk[abc])# 시작할때의 현재 블록을 arrayblk [abc]인덱스로 정함. 
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

aaa=(arrayBlk[abc])#추가한거

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        currBlk = Matrix(transpose(aaa))
        aaa=transpose(aaa)

    
    elif key == ' ': # drop the block
        top+=15
        


    
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            
            for i in range(3):
                aaa=transpose(aaa)
            currBlk = Matrix((aaa))
            
        elif key == ' ':# undo: move up
            for p in range(20):
                if tempBlk.anyGreaterThan(1):
                        top-=1
                        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
                        tempBlk = tempBlk + currBlk
                        if tempBlk.anyGreaterThan(1)==False:
                            newBlockNeeded = True

                    




        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    if key!=' ':
        draw_matrix(oScreen); print()  

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False

        abc=random.randrange(0,7) #
        currBlk = Matrix(arrayBlk[abc])# 
        aaa=(arrayBlk[abc])#

        
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
