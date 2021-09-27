from flask_cors.core import parse_resources


game_board = []
orders = ["r"]
playing = True
no_win = True

for i in range(5):
    rows = []
    for j in range(5):
        rows.append(0)
    game_board.append(rows)

def print_matrix(game_board):
    for i in range(len(game_board)):
        print('-'*(len(game_board)*4))
        for j in range(len(game_board[0])):
            if game_board[i][j] != 0:
                print('|', game_board[i][j], end="|")
            else:
                print('|', ' ', end="|")
        print('')
    print()


class Game:
    def __init__(self, joueur, names):
        self.joueur = joueur
        self.names = names
        self.possibleDir = []
        self.posDirPerson = []

    def posTuple(self):
        asked_pos = input(f"{self.joueur} quelle position voulez-vous prendre?")
        pos_t = asked_pos.split(',')
        pos = tuple(int(x) for x in pos_t)
        return pos

    def askPos(self, pos):
        dir_list = self.checkPosition()
        valid_call = False
        if pos in dir_list:
            valid_call = True
            self.posDirPerson.append(pos[0])
            self.posDirPerson.append(pos[1])
        if valid_call and self.joueur == self.names[0]:
            game_board[pos[0]][pos[1]] = "y"
            return True
        elif valid_call and self.joueur == self.names[1]:
            game_board[pos[0]][pos[1]] = "r"
            return True
        else:
            return False


    def checkPosition(self):

        n = len(game_board)
        self.possibleDir = []
        index_row = 0

        for i in range(n):
            for j in range(n):
                if game_board[(n-1)-i][j] == 0:
                    self.possibleDir.append(((n-1) - i, j))
            if self.possibleDir != []:
                index_row = (n-1)-i
                break


        for i in range(n):
            for k in range(n):
                if (index_row - i > 0) and game_board[index_row - i][k] != 0 and game_board[index_row - (i + 1)][k] == 0:
                    self.possibleDir.append(((index_row - (i+1)), k))

        return self.possibleDir


    def checkWinCL(self):
        n = len(game_board)
        check_line = False
        check_column = False

        for i in range(n):
            counter_line = 0
            if game_board[i][0] == "y":
                for j in range(n):
                    if game_board[i][j] == "y":
                        counter_line += 1
                    else:
                        break
            if counter_line == 4:
                check_line = True
                break
            else:
                counter_line = 0
            if game_board[i][-1] == "y":
                for j in range(1,n-1):
                    if game_board[i][j] == "y":
                        counter_line += 1
                    else:
                        break
            if counter_line == 4:
                check_line = True
                break
            else:
                counter_line = 0
            if game_board[i][0] == "r":
                for j in range(n):
                    if game_board[i][j] == "r":
                        counter_line += 1
                    else:
                        break
            if counter_line == 4:
                check_line = True
                break
            else:
                counter_line = 0
            if game_board[i][-1] == "r":
                for j in range(1, n-1):
                    if game_board[i][j] == "r":
                        counter_line += 1
                    else:
                        break
            if counter_line == 4:
                check_line = True
                break

        for i in range(n):
            counter_column = 0
            if game_board[0][i] == "y":
                for j in range(n):
                    if game_board[j][i] == "y":
                        counter_column += 1
                    else:
                        break
            if counter_column == 4:
                check_column = True
                break
            else:
                counter_column = 0
            if game_board[-1][i] == "y":
                for j in range(n-1, 0, -1):
                    if game_board[j][i] == "y":
                        counter_column += 1
                    else:
                        break
            if counter_column == 4:
                check_column = True
                break
            else:
                counter_column = 0
            if game_board[0][i] == "r":
                for j in range(n):
                    if game_board[j][i] == "r":
                        counter_column += 1
                    else:
                        break
            if counter_column == 4:
                check_column = True
                break
            else:
                counter_column = 0
            if game_board[-1][i] == "r":
                for j in range(n-1, 0, -1):
                    if game_board[j][i] == "r":
                        counter_column += 1
            if counter_column == 4:
                check_column = True
                break

        if check_column or check_line:
            return True
        else:
            return False


    def checkWinDiago(self):
        n = len(game_board)-1
        for i in range(n, n-2, -1):
            for j in range(n+1):
                if (j < 2 and "y" == game_board[i][j] and "y" == game_board[i-1][j+1] and "y" == game_board[i-2][j+2] and "y" == game_board[i-3][j+3]):
                    return True
                if (j < 2 and "r" == game_board[i][j] and "r" == game_board[i-1][j+1] and "r" == game_board[i-2][j+2] and "r" == game_board[i-3][j+3]):
                    return True
                if (j > 2 and "y" == game_board[i][j] and "y" == game_board[i-1][j-1] and "y" == game_board[i-2][j-2] and "y" == game_board[i-3][j-3]):
                    return True
                if (j > 2 and "r" == game_board[i][j] and "r" == game_board[i-1][j-1] and "r" == game_board[i-2][j-2] and "r" == game_board[i-3][j-3]):
                    return True
        return False

# while playing:
#     name_1 = input("Quel est votre nom? ")
#     name_2 = input("Quel est votre nom? ")
#     names = ["felix", "victor"]
#     joueur1 = Game(names[0], names)
#     joueur2 = Game(names[1], names)

#     while no_win:
#         print(print_matrix(game_board))
#         print(joueur1.checkPosition())
#         posPlayer = joueur1.posTuple()
#         joueur1.askPos(posPlayer)

#         if joueur1.checkWinCL() or joueur1.checkWinDiago():
#             print(print_matrix(game_board))
#             print(f"Puissance4 {names[0]} t'es le plus fort")
#             break

#         print(print_matrix(game_board))
#         print(joueur2.checkPosition())
#         posPlayer = joueur2.posTuple()
#         joueur2.askPos(posPlayer)

#         if joueur2.checkWinCL() or joueur2.checkWinDiago():
#             print(print_matrix(game_board))
#             print(f"Puissance4 {names[1]} t'es le plus fort!")
#             break
#     playing = False

# names = ["felix", "victor"]
# joueur1 = Game(names[0], names)
# joueur2 = Game(names[0], names)

