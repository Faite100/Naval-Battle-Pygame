import random

def createShip(size, player1):
    while True:
        i = random.randint(0, 9)
        j = random.randint(0, 9)
        direction = random.choice(["horizontal", "vertical"])
        
        if direction == "horizontal":
            finalI = i
            finalJ = j + size - 1
            if finalJ > 9:
                continue
        else:
            finalI = i + size - 1
            finalJ = j
            if finalI > 9:
                continue
        
        collision = False
        for x in range(i, finalI + 1):
            for y in range(j, finalJ + 1):
                if player1[x][y] > 0:
                    collision = True
                    break
            if collision:
                break
        
        if not collision and not adjacentShip(player1, i, j, finalI, finalJ):
            for x in range(i, finalI + 1):
                for y in range(j, finalJ + 1):
                    player1[x][y] = size
            break

def adjacentShip(player1, i, j, finalI, finalJ):
    for x in range(i - 1, finalI + 2):
        for y in range(j - 1, finalJ + 2):
            if 0 <= x < 10 and 0 <= y < 10 and player1[x][y] > 0:
                return True
    return False

player1 = [[0] * 10 for _ in range(10)]

createShip(5, player1)
createShip(4, player1)
createShip(4, player1)
createShip(3, player1)
createShip(3, player1)
createShip(2, player1)
createShip(2, player1)
createShip(2, player1)
 
for i in range(0, 10):
    for j in range(0, 10):
        print(player1[i][j], end=' ')
    print()
