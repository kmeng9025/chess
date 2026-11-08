import pygame
import chess
import time
import sys
from math import floor

pygame.init()

chessModuleBoard = chess.Board()

board_width = 512
board_height = 512

square_size = 64

white = (255, 255, 255)
black = (0, 0, 0)
window = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Chess Board")

wp = pygame.image.load("white_pawn.png")
wr = pygame.image.load("white_rook.png")
wn = pygame.image.load("white_knight.png")
wb = pygame.image.load("white_bishop.png")
wq = pygame.image.load("white_queen.png")
wk = pygame.image.load("white_king.png")
bp = pygame.image.load("black_pawn.png")
br = pygame.image.load("black_rook.png")
bn = pygame.image.load("black_knight.png")
bb = pygame.image.load("black_bishop.png")
bq = pygame.image.load("black_queen.png")
bk = pygame.image.load("black_king.png")
wp = pygame.transform.scale(wp, (62,62))
wr = pygame.transform.scale(wr, (62,62))
wn = pygame.transform.scale(wn, (62,62))
wb = pygame.transform.scale(wb, (62,62))
wq = pygame.transform.scale(wq, (62,62))
wk = pygame.transform.scale(wk, (62,62))
bp = pygame.transform.scale(bp, (62,62))
br = pygame.transform.scale(br, (62,62))
bn = pygame.transform.scale(bn, (62,62))
bb = pygame.transform.scale(bb, (62,62))
bq = pygame.transform.scale(bq, (62,62))
bk = pygame.transform.scale(bk, (62,62))

piece_images = {
    "wp": wp,
    "wr": wr,
    "wn": wn,
    "wb": wb,
    "wq": wq,
    "wk": wk,
    "bp": bp,
    "br": br,
    "bn": bn,
    "bb": bb,
    "bq": bq,
    "bk": bk
}

# Starting board
board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

def check_board_spots(spot):
    #print(spot.split(","))
    if board[int(spot.split(",")[0])][int(spot.split(",")[1])] != "--" :
        #print(board[int(spot.split(",")[0])][int(spot.split(",")[1])])
        return True
    return False

# Create a function to draw the board
def draw_board():
    for row in range(8):
        for col in range(8):
            if row % 2 == 0:
                if col % 2 == 0:
                    color = white
                else:
                    color = black
            else:
                if col % 2 == 0:
                    color = black
                else:
                    color = white
            pygame.draw.rect(window, color, (col * square_size, row * square_size, square_size, square_size))
            pygame.display.update()

# Create a function to draw the pieces on the board
def draw_pieces():
    for row in range(8):
        for col in range(8):
            a = board[row]
            if a[col] != "--":
                #print(a[col])
                #print(type(piece_images[a[col]]))
                window.blit(piece_images[a[col]],(col * square_size, row * square_size))
                pygame.display.update()

def closeEnoughToPushPawn(x1, x2):
    x1Number = 0
    x2Number = 0
    if str(x1) == str(x2):
        return true
    if str(x1) == "a":
        x1Number = 1
    elif str(x1) == "b":
        x1Number = 2
    elif str(x1) == "c":
        x1Number = 3
    elif str(x1) == "d":
        x1Number = 4
    elif str(x1) == "e":
        x1Number = 5
    elif str(x1) == "f":
        x1Number = 6
    elif str(x1) == "g":
        x1Number = 7
    elif str(x1) == "h":
        x1Number = 8
    if str(x2) == "a":
        x2Number = 1
    elif str(x2) == "b":
        x2Number = 2
    elif str(x2) == "c":
        x2Number = 3
    elif str(x2) == "d":
        x2Number = 4
    elif str(x2) == "e":
        x2Number = 5
    elif str(x2) == "f":
        x2Number = 6
    elif str(x2) == "g":
        x2Number = 7
    elif str(x2) == "h":
        x2Number = 8
    if x1Number + 1 == x2Number or x1Number - 1 == x2Number:
        return True
    else:
        return False



def flipNumber0_7(numberToFlip):
    return 7-numberToFlip
    # if numberToFlip == 1:
    #     return 6
    # if numberToFlip == 0:
    #     return 7
    # if numberToFlip == 2:
    #     return 5
    # if numberToFlip == 3:
    #     return 4
    # if numberToFlip == 4:
    #     return 3
    # if numberToFlip == 5:
    #     return 2
    # if numberToFlip == 6:
    #     return 1
    # if numberToFlip == 7:
    #     return 0


def setChessFenUsingBoard(currentFen):
    print("Currect FEN = " + currentFen)
    currentFen = currentFen.split("/")
    currentFen = currentFen[7]
    currentFen = [*currentFen]
    print(currentFen)
    totalRuns = 0
    for i in range(8):
        # s = currentFen[i]
        print("outside of if = " + str(i))
       # if s == "q" or s == "k" or s == "r" or s == "b" or s == "n" or s == "p" or s == "Q" or s == "K" or s == "R" or s == "B" or s == "N" or s == "P":
        if currentFen[0] == " ":
            break

        currentFen.pop(0)
        totalRuns += 1
        print(i)
        #if s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8":
         #   currentFen.pop(i)
          #  totalRuns += int(s)-1
       # if totalRuns == 8:
        #    break

    print("\n\n\n\n")
    print(currentFen)
    print("\n\n\n")
#    currentFen.pop(0)
 #   currentFen.pop(1)
  #  currentFen.pop(2)
   # currentFen.pop(3)
    tailOfFen = ""

    for i in currentFen:
        tailOfFen = tailOfFen + str(i)
    print("Tail of Current FEN = " + tailOfFen)
    
    fenStringToSet = ""
    for i in range(8):
        NumberOfSpacesThatNeedToBeAppended = 0
        if i == 0:
            print("Promoting Pawn...")
        else:
            fenStringToSet = fenStringToSet + "/"
        for c in range(8):
            totalNumberOfFenAppended = 0
            if board[i][c] == "--":
                NumberOfSpacesThatNeedToBeAppended += 1
            elif board[i][c] == "wr":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "R"
            elif board[i][c] == "wb":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "B"
            elif board[i][c] == "wn":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "N"
            elif board[i][c] == "wq":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "Q"
            elif board[i][c] == "wk":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "K"
            elif board[i][c] == "wp":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "P"
            elif board[i][c] == "br":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "r"
            elif board[i][c] == "bb":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "b"
            elif board[i][c] == "bn":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "n"
            elif board[i][c] == "bq":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "q"
            elif board[i][c] == "bk":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "k"
            elif board[i][c] == "bp":
                if NumberOfSpacesThatNeedToBeAppended != 0:
                    fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                    NumberOfSpacesThatNeedToBeAppended = 0
                fenStringToSet = fenStringToSet + "p"
            if c == 7 and NumberOfSpacesThatNeedToBeAppended != 0:
                fenStringToSet = fenStringToSet + str(NumberOfSpacesThatNeedToBeAppended)
                NumberOfSpacesThatNeedToBeAppended = 0
    fenStringToSet = fenStringToSet + tailOfFen
    print(fenStringToSet)
                
            

def main():
    draw_board()
    draw_pieces()
    #print(chess.WHITE)
    #print(chess.BLACK)
    numberOfTurns = 0
#    for c in range(8):
     #   print(c)
    
    while 1:
        #print(chessModuleBoard.fen())
        #print(pygame.mouse.get_pressed())
        #time.sleep(1)
        if pygame.mouse.get_pressed() == (1,0,0):
           # setChessFenUsingBoard(chessModuleBoard.fen())
            x, y = pygame.mouse.get_pos()
            isTherePiece = check_board_spots(str(floor(y/64))+","+str(floor(x/64)))
          #  print("finished checking spot")
           # print("\n\n")
         #   time.sleep(1)
          #  print("Finished sleeping")
           # print("\n\n")
            #print(pygame.mouse.get_pressed())
            gotMouseUp=False
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        gotMouseUp = True
                        break
                if gotMouseUp == False:
                    continue
                gotMouseUp = False
                break

            if isTherePiece:
                firstClickX = floor(x/64)
                firstClickY = floor(y/64)
                # if floor(y/64) == 0:
                #     boardCoordsy = "8"
                # elif floor(y/64) == 1:
                #     boardCoordsy = "7"
                # elif floor(y/64) == 2:
                #     boardCoordsy = "6"
                # elif floor(y/64) == 3:
                #     boardCoordsy = "5"
                # elif floor(y/64) == 4:
                #     boardCoordsy = "4"
                # elif floor(y/64) == 5:
                #     boardCoordsy = "3"
                # elif floor(y/64) == 6:
                #     boardCoordsy = "2"
                # elif floor(y/64) == 7:
                #     boardCoordsy = "1"
                #
                # if floor(x/64) == 0:
                #     boardCoordsx = "a"
                # elif floor(x/64) == 1:
                #     boardCoordsx = "b"
                # elif floor(x/64) == 2:
                #     boardCoordsx = "c"
                # elif floor(x/64) == 3:
                #     boardCoordsx = "d"
                # elif floor(x/64) == 4:
                #     boardCoordsx = "e"
                # elif floor(x/64) == 5:
                #     boardCoordsx = "f"
                # elif floor(x/64) == 6:
                #     boardCoordsx = "g"
                # elif floor(x/64) == 7:
                #     boardCoordsx = "h"
                        
                if firstClickY == 0:
                    firstBoardCoordsY = "8"
                elif firstClickY == 1:
                    firstBoardCoordsY = "7"
                elif firstClickY == 2:
                    firstBoardCoordsY = "6"
                elif firstClickY == 3:
                    firstBoardCoordsY = "5"
                elif firstClickY == 4:
                    firstBoardCoordsY = "4"
                elif firstClickY == 5:
                    firstBoardCoordsY = "3"
                elif firstClickY == 6:
                    firstBoardCoordsY = "2"
                elif firstClickY == 7:
                    firstBoardCoordsY = "1"
                    
                if firstClickX == 0:
                    firstBoardCoordsx = "a"
                elif firstClickX == 1:
                    firstBoardCoordsx = "b"
                elif firstClickX == 2:
                    firstBoardCoordsx = "c"
                elif firstClickX == 3:
                    firstBoardCoordsx = "d"
                elif firstClickX == 4:
                    firstBoardCoordsx = "e"
                elif firstClickX == 5:
                    firstBoardCoordsx = "f"
                elif firstClickX == 6:
                    firstBoardCoordsx = "g"
                elif firstClickX == 7:
                    firstBoardCoordsx = "h"
                for i in range(8):
                    for c in range(8):
                        tryX = "0"
                        if c == 0:
                            tryX = "a"
                        elif c == 1:
                            tryX = "b"
                        elif c == 2:
                            tryX = "c"
                        elif c == 3:
                            tryX = "d"
                        elif c == 4:
                            tryX = "e"
                        elif c == 5:
                            tryX = "f"
                        elif c == 6:
                            tryX = "g"
                        elif c == 7:
                            tryX = "h"

                        if i == 0:
                            i = 7
                        elif i == 1:
                            i = 6
                        elif i == 2:
                            i = 5
                        elif i == 3:
                            i = 4
                        elif i == 4:
                            i = 3
                        elif i == 5:
                            i = 2
                        elif i == 6:
                            i = 1
                        elif i == 7:
                            i = 0
                        try:
                            chessModuleBoard.push_san(firstBoardCoordsx+str(firstBoardCoordsY)+tryX+str(i+1))
                            chessModuleBoard.pop()
                            if i == 1:
                                isub = 6
                            elif i == 2:
                                isub = 5
                            elif i == 3:
                                isub = 4
                            elif i == 0:
                                isub = 7
                            elif i == 4:
                                isub = 3
                            elif i == 5:
                                isub = 2
                            elif i == 6:
                                isub = 1
                           # print("Drawing rectangles")
                            #print(c)
                            #print(i)
                            pygame.draw.rect(window,(173, 216, 230),pygame.Rect(c*64,isub*64,64,64),5)
                            pygame.display.update()
                        except chess.IllegalMoveError:
                            continue
                
                #print("got past is there piece")
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            gotMouseUp = True
                            break
                    if gotMouseUp == False:
                        continue
                    gotMouseUp = False
                    break
                #print("Got second click")
                x, y = pygame.mouse.get_pos()
                boardCoordsx = "a"
                boardCoordsy = "0"
                if floor(y/64) == 0:
                    boardCoordsy = "8"
                elif floor(y/64) == 1:
                    boardCoordsy = "7"
                elif floor(y/64) == 2:
                    boardCoordsy = "6"
                elif floor(y/64) == 3:
                    boardCoordsy = "5"
                elif floor(y/64) == 4:
                    boardCoordsy = "4"
                elif floor(y/64) == 5:
                    boardCoordsy = "3"
                elif floor(y/64) == 6:
                    boardCoordsy = "2"
                elif floor(y/64) == 7:
                    boardCoordsy = "1"
                    
                if floor(x/64) == 0:
                    boardCoordsx = "a"
                elif floor(x/64) == 1:
                    boardCoordsx = "b"
                elif floor(x/64) == 2:
                    boardCoordsx = "c"
                elif floor(x/64) == 3:
                    boardCoordsx = "d"
                elif floor(x/64) == 4:
                    boardCoordsx = "e"
                elif floor(x/64) == 5:
                    boardCoordsx = "f"
                elif floor(x/64) == 6:
                    boardCoordsx = "g"
                elif floor(x/64) == 7:
                    boardCoordsx = "h"
                    
                if firstClickY == 0:
                    firstBoardCoordsY = "8"
                elif firstClickY == 1:
                    firstBoardCoordsY = "7"
                elif firstClickY == 2:
                    firstBoardCoordsY = "6"
                elif firstClickY == 3:
                    firstBoardCoordsY = "5"
                elif firstClickY == 4:
                    firstBoardCoordsY = "4"
                elif firstClickY == 5:
                    firstBoardCoordsY = "3"
                elif firstClickY == 6:
                    firstBoardCoordsY = "2"
                elif firstClickY == 7:
                    firstBoardCoordsY = "1"
                
                if firstClickX == 0:
                    firstBoardCoordsx = "a"
                elif firstClickX == 1:
                    firstBoardCoordsx = "b"
                elif firstClickX == 2:
                    firstBoardCoordsx = "c"
                elif firstClickX == 3:
                    firstBoardCoordsx = "d"
                elif firstClickX == 4:
                    firstBoardCoordsx = "e"
                elif firstClickX == 5:
                    firstBoardCoordsx = "f"
                elif firstClickX == 6:
                    firstBoardCoordsx = "g"
                elif firstClickX == 7:
                    firstBoardCoordsx = "h"
                #print(firstBoardCoordsx+str(firstBoardCoordsY)+boardCoordsx+str(boardCoordsy))
                try:
                    #print(chessModuleBoard)
                    chessModuleBoard.push_san(firstBoardCoordsx+str(firstBoardCoordsY)+boardCoordsx+str(boardCoordsy))
                    #print(chessModuleBoard)
                    board[0].clear()
                    board[1].clear()
                    board[2].clear()
                    board[3].clear()
                    board[4].clear()
                    board[5].clear()
                    board[6].clear()
                    board[7].clear()
                    parsableBoard = chessModuleBoard.fen()
                    parsableBoard = parsableBoard.split("/")
                  #  print(parsableBoard)
                    parsableBoard[0] = [*parsableBoard[0]]
                    parsableBoard[1] = [*parsableBoard[1]]
                    parsableBoard[2] = [*parsableBoard[2]]
                    parsableBoard[3] = [*parsableBoard[3]]
                    parsableBoard[4] = [*parsableBoard[4]]
                    parsableBoard[5] = [*parsableBoard[5]]
                    parsableBoard[6] = [*parsableBoard[6]]
                    parsableBoard[7] = [*parsableBoard[7]]
                   # print(parsableBoard)
                    for i in range(8):
                        completedRuns = 0
                        for c in range(8):
                            #print(i)
                            #print(c)
                            #print(parsableBoard)
                            if parsableBoard[i][c] == "8":
                                for d in range(8):
                                    board[i].append("--")
                                break
                            elif parsableBoard[i][c] == "7":
                                completedRuns += 7
                                for d in range(7):
                                    board[i].append("--")
                            elif parsableBoard[i][c] == "6":
                                completedRuns += 6
                                for d in range(6):
                                    board[i].append("--")
                            elif parsableBoard[i][c] == "5":
                                completedRuns += 5
                                for d in range(5):
                                    board[i].append("--")
                            elif parsableBoard[i][c] == "4":
                                completedRuns += 4
                                #print("\n\n\n Printing C")
                                #print(c)
                                for d in range(4):
                                    board[i].append("--")
                            elif parsableBoard[i][c] == "3":
                                completedRuns += 3
                                for d in range(3):
                                    board[i].append("--")
                            elif parsableBoard[i][c] == "2":
                                completedRuns += 2
                                board[i].append("--")
                                board[i].append("--")
                            elif parsableBoard[i][c] == "1":
                                board[i].append("--")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "p":
                                board[i].append("bp")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "r":
                                board[i].append("br")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "n":
                                board[i].append("bn")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "b":
                                board[i].append("bb")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "k":
                                board[i].append("bk")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "q":
                                board[i].append("bq")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "P":
                                board[i].append("wp")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "R":
                                board[i].append("wr")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "N":
                                board[i].append("wn")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "B":
                                board[i].append("wb")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "K":
                                board[i].append("wk")
                                completedRuns += 1
                            elif parsableBoard[i][c] == "Q":
                                board[i].append("wq")
                                completedRuns += 1
                            #print("\n\n\n\n\n")
                            #print(parsableBoard)
                            #print("\n")
                            #print(board)
                            if completedRuns == 8:
                                break
                    draw_board()
                    draw_pieces()
                    numberOfTurns += 1
                    if chessModuleBoard.is_checkmate():
                        print("Somebody got checkmated")
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()
                    elif chessModuleBoard.is_stalemate():
                        print("It is a draw by stalemate!!!")
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()
                    elif chessModuleBoard.is_insufficient_material():
                        print("This is amazing! It is a draw by insufficient material")
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()
                    elif chessModuleBoard.can_claim_fifty_moves():
                        print("This is unbelievable! It is a draw by fifty moves")
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()
                    elif chessModuleBoard.can_claim_threefold_repetition():
                        print("Booooooo!!! It is a draw by repetition")
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()

                    

                                
                            
    
                        
                    #print(parsableBoard)
                except chess.IllegalMoveError:
                    print(type(firstBoardCoordsY))
                    print(type(boardCoordsy))
                    if firstBoardCoordsY == "7" and boardCoordsy == "8":
                        print("Should be here")
                        if firstBoardCoordsx == boardCoordsx or closeEnoughToPushPawn(firstBoardCoordsx, boardCoordsx):
                            print("Should now be here")
                            if boardCoordsx == "a":
                                boardCoordssyyx = 0
                            elif boardCoordsx == "b":
                                boardCoordssyyx = 1
                            elif boardCoordsx == "c":
                                boardCoordssyyx = 2
                            elif boardCoordsx == "d":
                                boardCoordssyyx = 3
                            elif boardCoordsx == "e":
                                boardCoordssyyx = 4
                            elif boardCoordsx == "f":
                                boardCoordssyyx = 5
                            elif boardCoordsx == "g":
                                boardCoordssyyx = 6
                            elif boardCoordsx == "h":
                                boardCoordssyyx = 7
                            if 1 == 1:
                              #  print(str(flipNumber0_7(int(boardCoordsy)-1))+","+str(boardCoordssyyx))
                                print("Now im here")
                                if not chessModuleBoard.is_check():
                                    print("and here")
                                    if numberOfTurns%2==0:
                                        print("and then now here")
                                        print(firstBoardCoordsx+str(firstBoardCoordsY)+boardCoordsx+str(boardCoordsy)+"q")
                                        chessModuleBoard.push_san(firstBoardCoordsx+str(firstBoardCoordsY)+boardCoordsx+str(boardCoordsy)+"q")
                                        board[0].clear()
                                        board[1].clear()
                                        board[2].clear()
                                        board[3].clear()
                                        board[4].clear()
                                        board[5].clear()
                                        board[6].clear()
                                        board[7].clear()
                                        parsableBoard = chessModuleBoard.fen()
                                        parsableBoard = parsableBoard.split("/")
                                      #  print(parsableBoard)
                                        parsableBoard[0] = [*parsableBoard[0]]
                                        parsableBoard[1] = [*parsableBoard[1]]
                                        parsableBoard[2] = [*parsableBoard[2]]
                                        parsableBoard[3] = [*parsableBoard[3]]
                                        parsableBoard[4] = [*parsableBoard[4]]
                                        parsableBoard[5] = [*parsableBoard[5]]
                                        parsableBoard[6] = [*parsableBoard[6]]
                                        parsableBoard[7] = [*parsableBoard[7]]
                                       # print(parsableBoard)
                                        for i in range(8):
                                            completedRuns = 0
                                            for c in range(8):
                                                #print(i)
                                                #print(c)
                                                #print(parsableBoard)
                                                if parsableBoard[i][c] == "8":
                                                    for d in range(8):
                                                        board[i].append("--")
                                                    break
                                                elif parsableBoard[i][c] == "7":
                                                    completedRuns += 7
                                                    for d in range(7):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "6":
                                                    completedRuns += 6
                                                    for d in range(6):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "5":
                                                    completedRuns += 5
                                                    for d in range(5):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "4":
                                                    completedRuns += 4
                                                    #print("\n\n\n Printing C")
                                                    #print(c)
                                                    for d in range(4):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "3":
                                                    completedRuns += 3
                                                    for d in range(3):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "2":
                                                    completedRuns += 2
                                                    board[i].append("--")
                                                    board[i].append("--")
                                                elif parsableBoard[i][c] == "1":
                                                    board[i].append("--")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "p":
                                                    board[i].append("bp")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "r":
                                                    board[i].append("br")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "n":
                                                    board[i].append("bn")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "b":
                                                    board[i].append("bb")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "k":
                                                    board[i].append("bk")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "q":
                                                    board[i].append("bq")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "P":
                                                    board[i].append("wp")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "R":
                                                    board[i].append("wr")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "N":
                                                    board[i].append("wn")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "B":
                                                    board[i].append("wb")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "K":
                                                    board[i].append("wk")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "Q":
                                                    board[i].append("wq")
                                                    completedRuns += 1
                                                #print("\n\n\n\n\n")
                                                #print(parsableBoard)
                                                #print("\n")
                                                #print(board)
                                                if completedRuns == 8:
                                                    break
                                        #draw_board()
                                        #draw_pieces()
                                        numberOfTurns += 1

                                
                    elif firstBoardCoordsY == "2" and boardCoordsy == "1":
                        print("Should be here")
                        if firstBoardCoordsx == boardCoordsx or closeEnoughToPushPawn(firstBoardCoordsx, boardCoordsx):
                            print("Should now be here")
                            # if boardCoordsx == "a":
                            #     boardCoordssyyx = 0
                            # elif boardCoordsx == "b":
                            #     boardCoordssyyx = 1
                            # elif boardCoordsx == "c":
                            #     boardCoordssyyx = 2
                            # elif boardCoordsx == "d":
                            #     boardCoordssyyx = 3
                            # elif boardCoordsx == "e":
                            #     boardCoordssyyx = 4
                            # elif boardCoordsx == "f":
                            #     boardCoordssyyx = 5
                            # elif boardCoordsx == "g":
                            #     boardCoordssyyx = 6
                            # elif boardCoordsx == "h":
                            #     boardCoordssyyx = 7
                            if 1 == 1:
                              #  print(str(flipNumber0_7(int(boardCoordsy)-1))+","+str(boardCoordssyyx))
                                print("Now im here")
                                if not chessModuleBoard.is_check():
                                    print("and here")
                                    if numberOfTurns%2==1:
                                        print("and then now here")
                                        print(firstBoardCoordsx+str(firstBoardCoordsY)+boardCoordsx+str(boardCoordsy)+"q")
                                        chessModuleBoard.push_san(firstBoardCoordsx+str(firstBoardCoordsY)+boardCoordsx+str(boardCoordsy)+"q")
                                        board[0].clear()
                                        board[1].clear()
                                        board[2].clear()
                                        board[3].clear()
                                        board[4].clear()
                                        board[5].clear()
                                        board[6].clear()
                                        board[7].clear()
                                        parsableBoard = chessModuleBoard.fen()
                                        parsableBoard = parsableBoard.split("/")
                                      #  print(parsableBoard)
                                        parsableBoard[0] = [*parsableBoard[0]]
                                        parsableBoard[1] = [*parsableBoard[1]]
                                        parsableBoard[2] = [*parsableBoard[2]]
                                        parsableBoard[3] = [*parsableBoard[3]]
                                        parsableBoard[4] = [*parsableBoard[4]]
                                        parsableBoard[5] = [*parsableBoard[5]]
                                        parsableBoard[6] = [*parsableBoard[6]]
                                        parsableBoard[7] = [*parsableBoard[7]]
                                       # print(parsableBoard)
                                        for i in range(8):
                                            completedRuns = 0
                                            for c in range(8):
                                                #print(i)
                                                #print(c)
                                                #print(parsableBoard)
                                                if parsableBoard[i][c] == "8":
                                                    for d in range(8):
                                                        board[i].append("--")
                                                    break
                                                elif parsableBoard[i][c] == "7":
                                                    completedRuns += 7
                                                    for d in range(7):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "6":
                                                    completedRuns += 6
                                                    for d in range(6):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "5":
                                                    completedRuns += 5
                                                    for d in range(5):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "4":
                                                    completedRuns += 4
                                                    #print("\n\n\n Printing C")
                                                    #print(c)
                                                    for d in range(4):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "3":
                                                    completedRuns += 3
                                                    for d in range(3):
                                                        board[i].append("--")
                                                elif parsableBoard[i][c] == "2":
                                                    completedRuns += 2
                                                    board[i].append("--")
                                                    board[i].append("--")
                                                elif parsableBoard[i][c] == "1":
                                                    board[i].append("--")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "p":
                                                    board[i].append("bp")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "r":
                                                    board[i].append("br")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "n":
                                                    board[i].append("bn")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "b":
                                                    board[i].append("bb")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "k":
                                                    board[i].append("bk")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "q":
                                                    board[i].append("bq")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "P":
                                                    board[i].append("wp")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "R":
                                                    board[i].append("wr")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "N":
                                                    board[i].append("wn")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "B":
                                                    board[i].append("wb")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "K":
                                                    board[i].append("wk")
                                                    completedRuns += 1
                                                elif parsableBoard[i][c] == "Q":
                                                    board[i].append("wq")
                                                    completedRuns += 1
                                                #print("\n\n\n\n\n")
                                                #print(parsableBoard)
                                                #print("\n")
                                                #print(board)
                                                if completedRuns == 8:
                                                    break
                                        #draw_board()
                                        #draw_pieces()
                                        numberOfTurns += 1
                        
                    print("got illegal move")
                    time.sleep(0.1)
                    draw_board()
                    draw_pieces()
                    continue
                







#you can just parse e8e6 or something like that.



                
#            while True:
 #               print("Started while loop")
  #              print("\n\n\n\n\n")
   #             print(pygame.mouse.get_pressed())
    #            time.sleep(0.1)
   #            print("started while loop")
    #           # mouseState = pygame.mouse.get_pressed()
     #           #print("finished getting mouseState")
      #         if pygame.mouse.get_pressed()==(1,0,0):
       #            print("Got to if mouseState == (1,0,0)")
        #           print(pygame.mouse.get_pressed())
         #          time.sleep(0.1)
          #         print("finished sleeping for 0.1 seconds")
           #    else:
            #       print("Propably not going to happen but got to break")
             #      break;
              # print("about to continue in the loop")
                
#               check_board_spots("0,0")
 #               pygame.time.wait(100)
  #          if 64 < x < 128 and 0 < y < 64:
   #             check_board_spots("0,1")
    #            pygame.time.wait(100)
     #       if 128 < x < 192 and 0 < y < 64:
      #          check_board_spots("0,2")
       #         time.sleep(1)
        #    if 192 < x < 256 and 0 < y < 64:
         #       check_board_spots("0,3")
          #      time.sleep(1)
           # if 256 < x < 320 and 0 < y < 64:
            #    check_board_spots("0,4")
             #   time.sleep(1)
#            if 320 < x < 384 and 0 < y < 64:
 #               check_board_spots("0,5")
  #              time.sleep(1)
   #         if 384 < x < 448 and 0 < y < 64:
    #            check_board_spots("0,6")
     #           time.sleep(1)
      #      if 448 < x < 512 and 0 < y < 64:
       #         check_board_spots("0,7")
        #        time.sleep(1)


    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
main()
            
