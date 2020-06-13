import pygame,sys,random
from pygame.locals import *

boardw=8
boardh=2
tilesize=80
windoww=680
windowh=520
shufflemoves=30
fps=30
blank=None

"""
colorset1
background=(21,171,0)
tilecolor=(215,252,0)
textcolor=(0,59,174)
bordercolor=(254,169,119)
fontsize=20
msgcolor=(255,255,255)

colorset2
background=(97,0,161)
tilecolor=(255,172,0)
textcolor=(255,255,255) or (0,0,0)
bordercolor=(0,0,0)
fontsize=20
msgcolor=(236,253,18)
"""

background=(97,0,161)
tilecolor=(255,172,0)
textcolor=(255,255,255)
bordercolor=(73,186,0)
fontsize=20
msgcolor=(236,253,18)

boardx=int((windoww-(tilesize*boardw+boardw-1))/2)
boardy=int((windowh-(tilesize*boardh+boardh-1))/2)

up="up"
down="down"
left="lest"
right="right"

def main():
    global fpsclock,display,font,resetsurf,newsurf,solvesurf,resetrect,newrect,solverect
    pygame.init()
    fpsclock=pygame.time.Clock()
    display=pygame.display.set_mode((windoww,windowh))
    pygame.display.set_caption("Slide puzzle")
    font=pygame.font.SysFont("comicsansms", fontsize)
    resetsurf,resetrect=make_text(" Reset ",textcolor,tilecolor,windoww-120,windowh-90)
    newsurf,newrect=make_text(" New Game ",textcolor,tilecolor,windoww-120,windowh-60)
    solvesurf,solverect=make_text(" Solve ",textcolor,tilecolor,windoww-120,windowh-30)
    mainboard,solution=new_puzzle(shufflemoves)
    solvedboard=starting_board()
    allmoves=[]
    while True:
        slideto=None
        msg="Click tile or press arrow keys to slide."
        if mainboard==solvedboard:
            msg="Solved!"
            solution=[]
            allmoves=[]
        draw_board(mainboard,msg)
        quit_check()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP:
                spotx,spoty=spot_clicked(mainboard,event.pos[0],event.pos[1])
                if (spotx,spoty)==(None,None):
                    if resetrect.collidepoint(event.pos):
                        reset(mainboard,allmoves)
                    elif newrect.collidepoint(event.pos):
                        mainboard,solution=new_puzzle(shufflemoves)
                    elif solverect.collidepoint(event.pos):
                        reset(mainboard,solution+allmoves)
                    allmoves=[]
                else:
                    blankx,blanky=blank_position(mainboard)
                    if spotx==blankx and spoty==blanky+1:
                        slideto=up
                    elif spotx==blankx and spoty==blanky-1:
                        slideto=down
                    elif spotx==blankx+1 and spoty==blanky:
                        slideto=left
                    elif spotx==blankx-1 and spoty==blanky:
                        slideto=right
            elif event.type==KEYUP:
                if event.key in (K_UP,K_w) and is_valid_move(mainboard,up):
                    slideto=up
                elif event.key in (K_DOWN,K_s) and is_valid_move(mainboard,down):
                    slideto=down
                elif event.key in (K_LEFT,K_a) and is_valid_move(mainboard,left):
                    slideto=left
                elif event.key in (K_RIGHT,K_d) and is_valid_move(mainboard,right):
                    slideto=right
        if slideto:
            slide_animation(mainboard,slideto,"Click tile or press arrow keys to slide.",8)
            make_move(mainboard,slideto)
            allmoves.append(slideto)
        pygame.display.update()
        fpsclock.tick(fps)

def close_game():
    pygame.quit()
    sys.exit()

def quit_check():
    for event in pygame.event.get(QUIT):
        close_game()
    for event in pygame.event.get(KEYUP):
        if event.key==K_ESCAPE:
            close_game()
        pygame.event.post(event)

def starting_board():
    counter=1
    board=[]
    for i in range(boardw):
        column=[]
        for j in range(boardh):
            column.append(counter)
            counter+=boardw
        board.append(column)
        counter-=boardw*boardh-1
    board[boardw-1][boardh-1]=blank
    return board

def blank_position(board):
    for i in range(boardw):
        for j in range(boardh):
            if board[i][j]==blank:
                return (i,j)

def make_move(board,move):
    blankx,blanky=blank_position(board)
    if move==up:
        board[blankx][blanky],board[blankx][blanky+1]=board[blankx][blanky+1],board[blankx][blanky]
    elif move==down:
        board[blankx][blanky],board[blankx][blanky-1]=board[blankx][blanky-1],board[blankx][blanky]
    elif move==left:
        board[blankx][blanky],board[blankx+1][blanky]=board[blankx+1][blanky],board[blankx][blanky]
    elif move==right:
        board[blankx][blanky],board[blankx-1][blanky]=board[blankx-1][blanky],board[blankx][blanky]

def is_valid_move(board,move):
    blankx,blanky=blank_position(board)
    return (move==up and blanky!=len(board[0])-1) or\
           (move==down and blanky!=0) or\
           (move==left and blankx!=len(board)-1) or\
           (move==right and blankx!=0)

def random_move(board,prmove=None):
    validmoves=[up,down,left,right]
    if prmove==up or not is_valid_move(board,down):
        validmoves.remove(down)
    if prmove==down or not is_valid_move(board,up):
        validmoves.remove(up)
    if prmove==left or not is_valid_move(board,right):
        validmoves.remove(right)
    if prmove==right or not is_valid_move(board,left):
        validmoves.remove(left)
    return random.choice(validmoves)

def top_left_of_tile(tilex,tiley):
    left=boardx+tilex*tilesize+tilex-1
    top=boardy+tiley*tilesize+tiley-1
    return (top,left)

def spot_clicked(board,x,y):
    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            top,left=top_left_of_tile(tilex,tiley)
            tile=pygame.Rect(left,top,tilesize,tilesize)
            if tile.collidepoint(x,y):
                return (tilex,tiley)
    return (None,None)

def draw_tile(tilex,tiley,number,adjx=0,adjy=0):
    top,left=top_left_of_tile(tilex,tiley)
    pygame.draw.rect(display,tilecolor,(left+adjx,top+adjy,tilesize,tilesize))
    textsurf=font.render(str(number),True,textcolor)
    textrect=textsurf.get_rect()
    textrect.center=left+int(tilesize/2)+adjx,top+int(tilesize/2)+adjy
    display.blit(textsurf,textrect)

def make_text(text,color,background,top,left):
    textsurf=font.render(text,True,color,background)
    textrect=textsurf.get_rect()
    textrect.topleft=(top,left)
    return (textsurf,textrect)

def draw_board(board,msg):
    display.fill(background)
    if msg:
        textsurf,textrect=make_text(msg,msgcolor,background,5,5)
        display.blit(textsurf,textrect)
    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                draw_tile(tilex,tiley,board[tilex][tiley])
    top,left=top_left_of_tile(0,0)
    width=boardw*tilesize
    height=boardh*tilesize
    pygame.draw.rect(display,bordercolor,(left-5,top-5,width+8+boardw,height+8+boardh),4)
    display.blit(resetsurf,resetrect)
    display.blit(newsurf,newrect)
    display.blit(solvesurf,solverect)

def slide_animation(board,direction,msg,speed):
    blankx,blanky=blank_position(board)
    if direction==up:
        movex=blankx
        movey=blanky+1
    elif direction==down:
        movex=blankx
        movey=blanky-1
    elif direction==left:
        movex=blankx+1
        movey=blanky
    elif direction==right:
        movex=blankx-1
        movey=blanky
    draw_board(board,msg)
    basesurf=display.copy()
    movetop,moveleft=top_left_of_tile(movex,movey)
    pygame.draw.rect(basesurf,background,(moveleft,movetop,tilesize,tilesize))
    for i in range(0,tilesize,speed):
        quit_check()
        display.blit(basesurf,(0,0))
        if direction==up:
            draw_tile(movex,movey,board[movex][movey],0,-i)
        elif direction==down:
            draw_tile(movex,movey,board[movex][movey],0,i)
        elif direction==left:
            draw_tile(movex,movey,board[movex][movey],-i,0)
        elif direction==right:
            draw_tile(movex,movey,board[movex][movey],i,0)
        pygame.display.update()
        fpsclock.tick(fps)

def new_puzzle(slides):
    sequence=[]
    board=starting_board()
    draw_board(board,"")
    pygame.display.update()
    pygame.time.wait(500)
    prmove=None
    for i in range(slides):
        move=random_move(board,prmove)
        slide_animation(board,move,"Generating new puzzle...",speed=int(tilesize/3))
        make_move(board,move)
        sequence.append(move)
        prmove=move
    return (board,sequence)

def reset(board,allmoves):
    reversedmoves=allmoves[:]
    reversedmoves.reverse()
    for move in reversedmoves:
        if move==up:
            oppositemove=down
        elif move==down:
            oppositemove=up
        elif move==left:
            oppositemove=right
        elif move==right:
            oppositemove=left
        slide_animation(board,oppositemove,"",speed=int(tilesize/2))
        make_move(board,oppositemove)

if __name__=="__main__":
    main()
