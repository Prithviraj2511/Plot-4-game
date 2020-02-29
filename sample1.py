import numpy as np
import pygame
import sys

purple = (102, 0, 102)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
r_count=6
c_count=7
def create_board():
    board=np.zeros((r_count,c_count))
    return board

def put_coin(board,select_row,select_col,piece):
    board[select_row][select_col]=piece

def is_valid(board,select_col):
    return board[r_count-1][select_col]==0

def get_next_open_row(board,select_col):
    for r in range(r_count):
        if board[r][select_col]==0:
            return r

def print_board(board):
    print(np.flip(board,0))

def win_move(board,piece,select_row,select_col):
    #checking horizontal locations
    for c in range(c_count-3):
        if board[select_row][c]==piece and board[select_row][c+1]==piece and board[select_row][c+2]==piece and board[select_row][c+3]==piece:
            return True
    #checking vertical locations
    for r in range(r_count-3):
        if board[r][select_col]==piece and board[r+1][select_col]==piece and board[r+2][select_col]==piece and board[r+3][select_col]==piece:
            return True
    #checking at slope /
    for c in range(c_count-3):
        for r in range(r_count-3):
            if board[r][c] == piece and board[r + 1][c+1] == piece and board[r + 2][c+2] == piece and board[r + 3][c+3] == piece:
                return True
    # checking at slope \
    for c in range(c_count-3):
        for r in range(3,r_count):
            if board[r][c] == piece and board[r -1][c+1] == piece and board[r - 2][c+2] == piece and board[r - 3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(c_count):
        for r in range(r_count):
            pygame.draw.rect(screen,purple,(c*sq_size,r*sq_size+sq_size,sq_size,sq_size))
            pygame.draw.circle(screen,black,(c*sq_size+(sq_size//2),r*sq_size+sq_size+(sq_size//2)),radius)
    for c in range(c_count):
        for r in range(r_count):
            if board[r][c]==1:
                pygame.draw.circle(screen,red,(c*sq_size+(sq_size//2),height-(r*sq_size+(sq_size//2))),radius)
            elif board[r][c]==2:
                pygame.draw.circle(screen,green,(c * sq_size + (sq_size // 2),height-( r * sq_size + (sq_size // 2))), radius)
    pygame.display.update()

board=create_board()
game_over=False
turn=0

pygame.init()

sq_size=100

width=c_count*sq_size
height=(r_count+1)*sq_size

size=(width,height)
radius=sq_size//2-5
screen=pygame.display.set_mode((size))
draw_board(board)
pygame.display.update()
f=pygame.font.SysFont("monospace", 45)

while not game_over:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            posx=event.pos[0]
            pygame.draw.rect(screen,black,(0,0,width,sq_size))
            if turn==0:
                pygame.draw.circle(screen,red,(posx,sq_size//2),radius)
            else:
                pygame.draw.circle(screen, green, (posx, sq_size // 2), radius)
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            # player 1 ip
            if turn == 0:
                posx=event.pos[0]
                select_col=posx//100
                #select_col = int(input("P1 make your selection(0 to 6)"))
                if is_valid(board, select_col):
                    select_row = get_next_open_row(board, select_col)
                    put_coin(board, select_row, select_col, 1)

                    if win_move(board, 1, select_row, select_col):
                        l1 = f.render("* * * Player 1 Wins * * *", 2, red)
                        game_over=True
                        screen.blit(l1, (40, 10))
                        #print("Player 1 wins")

            # player 2 ip
            else:
                posx = event.pos[0]
                select_col=posx//100
                #select_col = int(input("P2 make your selection(0 to 6)"))
                if is_valid(board, select_col):
                    select_row = get_next_open_row(board, select_col)
                    put_coin(board, select_row, select_col, 2)

                    if win_move(board, 2, select_row, select_col):
                        l1=f.render("* * * Player 2 Wins * * *",2,green)
                        game_over=True
                        screen.blit(l1,(40,10))
                        #print("Player 2 wins")
            draw_board(board)
            turn += 1
            turn = turn % 2
            if game_over:
                pygame.time.wait(4000)



