class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.guess_board = Board()

    def setup_board(self):
        print(f"{self.name}, set up your board.")
        self.board.setup_ships()
        print("\n" * 50)

    def make_guess(self, opponent_board):
        print(f"{self.name}, it's your turn to make a guess.")
        row, column = opponent_board.setup_position()
        return row, column


class Board:
    def __init__(self):
        self.size = 10
        self.ships = 5
        self.board = [[' ']*self.size for _ in range(self.size)]
        self.rows_and_columns = {chr(i): i - ord('A') for i in range(ord('A'), ord('A') + self.size)}

    def setup_ships(self):
        for _ in range(self.ships):
            print("Where do you want to place the ship?")
            while True:
                row, column = self.setup_position()
                if self.board[row][column] == ' ':
                    self.board[row][column] = 'X'
                    break
                else:
                    print("That spot already has a battleship in it!")
            self.print_board()

    def setup_position(self):
        while True:
            column = input("Column (A to J): ").upper()
            if column in self.rows_and_columns:
                break
            else:
                print("Not a valid column.")

        while True:
            row = input("Row (1 to 10): ")
            if row.isdigit() and 1 <= int(row) <= self.size:
                break
            else:
                print("Not a valid row.")

        return int(row) - 1, self.rows_and_columns[column]

    def print_board(self):
        print("  " + " ".join(chr(i) for i in range(ord('A'), ord('A') + self.size)))
        print(" " + "-" * (self.size * 2))
        for i, row in enumerate(self.board, 1):
            print(str(i) + "|" + "|".join(row) + "|")
            print(" " + "-" * (self.size * 2))


class Game:
    def __init__(self, player1_name, player2_name):
        self.players = [Player(player1_name), Player(player2_name)]
        self.current_player = 0
        self.total_correct_guesses = 0

    def play(self):
        for player in self.players:
            player.setup_board()
        print("\n" * 100)

        while self.total_correct_guesses < 5:
            current_player = self.players[self.current_player]
            opponent_player = self.players[(self.current_player + 1) % len(self.players)]
            print(f"{current_player.name}'s turn:")
            row, column = current_player.make_guess(opponent_player.board)
            if opponent_player.board.board[row][column] == 'X':
                print("\nHIT!")
                opponent_player.guess_board.board[row][column] = '.'
                self.total_correct_guesses += 1
            else:
                if opponent_player.guess_board.board[row][column] == '.':
                    print("You have already guessed that place!")
                else:
                    print("\nMISS!")
                    opponent_player.guess_board.board[row][column] = '*'
            opponent_player.guess_board.print_board()
            self.current_player = (self.current_player + 1) % len(self.players)

        winner = self.players[(self.current_player - 1) % len(self.players)]
        print(f"\nGAME OVER! {winner.name} wins!")

def print_title():
    title = r"""
     ____        _   _   _      ____  _     _  ____           
    | __ )  __ _| |_| |_| | ___| __ )| |__ (_)|  _ \ 
    |  _ \ / _` | __| __| |/ _ \  _ \| '_ \| || |_) |  
    | |_) | (_| | |_| |_| |  __/ |_) | | | | ||  __/ 
    |____/ \__,_|\__|\__|_|\___|____/|_| |_|_||_|
    """
    print(title)


def main():
    print_title()
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")
    game = Game(player1_name, player2_name)
    game.play()

main()
