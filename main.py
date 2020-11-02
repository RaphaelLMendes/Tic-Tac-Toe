import pygame
import time



pygame.init()

# creating screen size

winx = 300
winy = 300

# creating winodw
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("Tic Tac Toe")

# Tie cenario when board = tie

tie = [[1,1,1],
       [1,1,1],
       [1,1,1]]

# creating board class
class Board:
    def __init__(self):
        self.board=[[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        self.board1 = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.board2 = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def changeBoard(self,y,x,team):
        if self.board[y-1][x-1] == 0:
            if team == 1:
                self.board[y - 1][x - 1] = 1
                self.board1[y - 1][x - 1] = team
            elif team == 2:
                self.board[y - 1][x - 1] = 1
                self.board2[y - 1][x - 1] = team
            else:
                print("error")
            return False
        else:
            return True

    def checkWin(self):

        #Checking player 1 win

        # horizontal
        i=0
        for item in self.board1:
            if item[1] == 1 and item[2] == 1 and item[0] == 1:
                self.reset(1)
            i+=1
        # Vertical
        j=0
        while j<3:
            if self.board1[0][j] == 1 and self.board1[1][j] == 1 and self.board1[2][j] == 1:
                self.reset(1)
            j+=1
        # Diagnal

        if self.board1[0][0] == 1 and self.board1[1][1] == 1 and self.board1[2][2] == 1:
            self.reset(1)
        if self.board1[0][2] == 1 and self.board1[1][1] ==1 and self.board1[2][0] ==1 :
            self.reset(1)

        # Checking player 2 win
        # horizontal
        i = 0
        for item in self.board2:
            if item[1] == 2 and item[2] == 2 and item[0] == 2:
                self.reset(2)
            i += 1
        # Vertical
        j = 0
        while j < 3:
            if self.board2[0][j] == 2 and self.board2[1][j] == 2 and self.board2[2][j] == 2:
                self.reset(2)
            j += 1

        # Diagnal

        if self.board2[0][0] == 2 and self.board2[1][1] == 2 and self.board2[2][2]== 2:
            self.reset(2)
        if self.board2[0][2] == 2 and self.board2[1][1] == 2 and self.board2[2][0]== 2:
            self.reset(2)


        if self.board == tie:
            print('tie')
            self.reset(0)

    def draw(self,win):
        win.fill((255,255,255))
        i=0
        for item in self.board:
            j=0
            for subitem in item:
                pygame.draw.rect(win,(0,0,0),(j*100,i*100,100,100),1)
                j+=1
            i+=1
        i=0
        for item in self.board1:
            j=0
            for subitem in item:
                if subitem != 0:
                    # pygame.draw.rect(win,(0,0,0),(j*100+20,i*100+20,60,60))
                    pygame.draw.circle(win,(0,0,255),(j*100+50,i*100+50),30,4)
                j+=1
            i+=1
        i = 0
        for item in self.board2:
            j = 0
            for subitem in item:
                if subitem != 0:
                    # pygame.draw.rect(win, (255, 0, 0), (j * 100 + 20, i * 100 + 20, 60, 60))
                    pygame.draw.line(win,(255,0,0),(j*100+20,i*100+20),(j*100+80,i*100+80),5)
                    pygame.draw.line(win, (255, 0, 0), (j * 100 + 20, i * 100 + 80), (j * 100 + 80, i * 100 + 20), 5)
                j += 1
            i += 1

    def reset(self, winner):
        if winner == 1:
            print('o wins')
            show('      O wins      ',1)
        elif winner == 2:
            print('X wins')
            show('      X wins      ',2)
        else:
            print('TIE')
            show('      TIE      ',0)
        time.sleep(3)

        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.board1 = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
        self.board2 = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

#
def draw():
    b.draw(win)
    pygame.display.update()

def turn1():
    run = True
    while run:
        draw()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if pygame.mouse.get_pressed()==(1,0,0):
            if pos[0]<100:
                if pos[1] < 100:
                    run = b.changeBoard(1,1,1)
                elif 100 < pos[1] < 200:
                    run = b.changeBoard(2,1,1)
                elif pos[1] > 200:
                    run = b.changeBoard(3, 1, 1)
            elif 100<pos[0]<200:
                if pos[1] < 100:
                    run = b.changeBoard(1, 2, 1)
                elif 100 < pos[1] < 200:
                    run = b.changeBoard(2, 2, 1)
                elif pos[1] > 200:
                    run = b.changeBoard(3, 2, 1)
            elif pos[0]>200:
                if pos[1] < 100:
                    run = b.changeBoard(1, 3, 1)
                elif 100 < pos[1] < 200:
                    run = b.changeBoard(2, 3, 1)
                elif pos[1] > 200:
                    run = b.changeBoard(3, 3, 1)

def turn2():
    run = True
    while run:
        draw()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if pygame.mouse.get_pressed()==(1,0,0):
            if pos[0]<100:
                if pos[1] < 100:
                    run = b.changeBoard(1,1,2)
                elif 100 < pos[1] < 200:
                    run = b.changeBoard(2,1,2)
                elif pos[1] > 200:
                    run = b.changeBoard(3, 1, 2)
            elif 100<pos[0]<200:
                if pos[1] < 100:
                    run = b.changeBoard(1, 2, 2)
                elif 100 < pos[1] < 200:
                    run = b.changeBoard(2, 2, 2)
                elif pos[1] > 200:
                    run = b.changeBoard(3, 2, 2)
            elif pos[0]>200:
                if pos[1] < 100:
                    run = b.changeBoard(1, 3, 2)
                elif 100 < pos[1] < 200:
                    run = b.changeBoard(2, 3, 2)
                elif pos[1] > 200:
                    run = b.changeBoard(3, 3, 2)
            b.checkWin()

def show(text,winner):
    f = pygame.font.SysFont('arial',70,True)
    if winner == 1:
        onscreenText = f.render(text,False,(255,255,255),(0,0,255))
    elif winner ==2:
        onscreenText = f.render(text,False,(255,255,255),(255,0,0))
    else:
        onscreenText = f.render(text, False, (255, 255, 255), (133, 133, 133))
    win.blit(onscreenText,(winx/2-onscreenText.get_width()/2,winy/2-onscreenText.get_height()/2))
    pygame.display.update()

def mainLoop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
        turn1()
        turn2()



    pygame.quit()

b = Board()

mainLoop()