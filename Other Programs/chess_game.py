import pygame
import chess
import chess.engine

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 480
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chess Game')

# Load the chess board image
board_image = pygame.image.load('chess_board.png').convert()

# Set the font and font size
font = pygame.font.SysFont('Arial', 20)

# Initialize the chess board and engine
board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("stockfish.exe")

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define a function to draw the chess board and pieces
def draw_board():
    screen.blit(board_image, (0, 0))
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            x = (i % 8) * 60 + 30
            y = (i // 8) * 60 + 30
            piece_image = pygame.image.load('pieces/' + chess.piece_name(piece.piece_type, piece.color) + '.png').convert_alpha()
            screen.blit(piece_image, (x, y))

# Define a function to draw the status of the game
def draw_status():
    text = font.render('Turn: ' + ('White' if board.turn == chess.WHITE else 'Black'), True, black)
    screen.blit(text, (10, 10))
    text = font.render('Result: ' + str(board.result()), True, black)
    screen.blit(text, (10, 30))

# Define a function to get the move from the engine
def get_engine_move():
    result = engine.play(board, chess.engine.Limit(time=2.0))
    return result.move

# Set the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if board.turn == chess.WHITE:
                x, y = event.pos
                file = (x - 30) // 60
                rank = (y - 30) // 60
                if file >= 0 and file < 8 and rank >= 0 and rank < 8:
                    square = chess.square(file, 7 - rank)
                    moves = list(board.legal_moves)
                    for move in moves:
                        if move.from_square == square:
                            board.push(move)
                            break
        elif board.turn == chess.BLACK:
            move = get_engine_move()
            board.push(move)

    draw_board()
    draw_status()
    pygame.display.flip()

# Quit the engine and Pygame
engine.quit()
pygame.quit()
