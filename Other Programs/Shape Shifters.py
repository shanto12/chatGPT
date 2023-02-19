import pygame

# initialize Pygame
pygame.init()

# define window size and title
WINDOW_SIZE = (600, 600)
pygame.display.set_caption("Shape Shifters")
screen = pygame.display.set_mode(WINDOW_SIZE)

# define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
TEAL = (0, 128, 128)
ORANGE = (255, 165, 0)

# define shapes
CIRCLE = 'circle'
SQUARE = 'square'
TRIANGLE = 'triangle'
STAR = 'star'
DIAMOND = 'diamond'
HEXAGON = 'hexagon'

# define board and player pieces
board = [
    [(0, 0, RED, CIRCLE), (1, 0, BLUE, SQUARE), (2, 0, GREEN, TRIANGLE)],
    [(0, 1, YELLOW, STAR), (1, 1, PURPLE, DIAMOND), (2, 1, ORANGE, HEXAGON)],
    [(0, 2, PINK, CIRCLE), (1, 2, BROWN, SQUARE), (2, 2, TEAL, TRIANGLE)]
]

player1_pieces = [
    (0, 0, RED, CIRCLE),
    (1, 0, BLUE, SQUARE),
    (2, 0, GREEN, TRIANGLE),
    (0, 1, YELLOW, STAR),
    (1, 1, PURPLE, DIAMOND),
    (2, 1, ORANGE, HEXAGON)
]

player2_pieces = [
    (0, 2, PINK, CIRCLE),
    (1, 2, BROWN, SQUARE),
    (2, 2, TEAL, TRIANGLE),
    (0, 1, GREEN, STAR),
    (1, 1, ORANGE, DIAMOND),
    (2, 1, PURPLE, HEXAGON)
]


# define game functions
def draw_board():
    square_size = 50
    for y in range(3):
        for x in range(3):
            square = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            pygame.draw.rect(screen, board[y][x][2], square)


def draw_pieces():
    piece_size = 40
    for piece in player1_pieces:
        piece_rect = pygame.Rect(piece[0] * 50 + 5, piece[1] * 50 + 5, piece_size, piece_size)
        pygame.draw.rect(screen, piece[2], piece_rect)
        if piece[3] == CIRCLE:
            pygame.draw.circle(screen, (255, 255, 255), (piece[0] * 50 + 25, piece[1] * 50 + 25), 15)
        elif piece[3] == SQUARE:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(piece[0] * 50 + 17, piece[1] * 50 + 17, 25, 25))
            # draw triangle shape
        elif piece[3] == TRIANGLE:
            triangle_points = [(piece[0] * 50 + 25, piece[1] * 50 + 15), (piece[0] * 50 + 10, piece[1] * 50 + 35),
                               (piece[0] * 50 + 40, piece[1] * 50 + 35)]
            pygame.draw.polygon(screen, (255, 255, 255), triangle_points)
        elif piece[3] == STAR:
            star_points = [(piece[0] * 50 + 25, piece[1] * 50 + 5), (piece[0] * 50 + 35, piece[1] * 50 + 45),
                           (piece[0] * 50 + 5, piece[1] * 50 + 20), (piece[0] * 50 + 45, piece[1] * 50 + 20),
                           (piece[0] * 50 + 15, piece[1] * 50 + 45)]
            pygame.draw.polygon(screen, (255, 255, 255), star_points)
        elif piece[3] == DIAMOND:
            diamond_points = [(piece[0] * 50 + 25, piece[1] * 50 + 5), (piece[0] * 50 + 45, piece[1] * 50 + 25),
                              (piece[0] * 50 + 25, piece[1] * 50 + 45), (piece[0] * 50 + 5, piece[1] * 50 + 25)]
            pygame.draw.polygon(screen, (255, 255, 255), diamond_points)
        elif piece[3] == HEXAGON:
            hexagon_points = [(piece[0] * 50 + 10, piece[1] * 50 + 25), (piece[0] * 50 + 25, piece[1] * 50 + 5),
                              (piece[0] * 50 + 40, piece[1] * 50 + 25), (piece[0] * 50 + 40, piece[1] * 50 + 45),
                              (piece[0] * 50 + 25, piece[1] * 50 + 65), (piece[0] * 50 + 10, piece[1] * 50 + 45)]
            pygame.draw.polygon(screen, (255, 255, 255), hexagon_points)

    for piece in player2_pieces:
        piece_rect = pygame.Rect(piece[0] * 50 + 5, piece[1] * 50 + 5, piece_size, piece_size)
        pygame.draw.rect(screen, piece[2], piece_rect)
        if piece[3] == CIRCLE:
            pygame.draw.circle(screen, (255, 255, 255), (piece[0] * 50 + 25, piece[1] * 50 + 25), 15)
        elif piece[3] == SQUARE:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(piece[0] * 50 + 17, piece[1] * 50 + 17, 25, 25))
            # draw triangle shape
        elif piece[3] == TRIANGLE:
            triangle_points = [(piece[0] * 50 + 25, piece[1] * 50 + 15), (piece[0] * 50 + 10, piece[1] * 50 + 35),
                               (piece[0] * 50 + 40, piece[1] * 50 + 35)]
            pygame.draw.polygon(screen, (255, 255, 255), triangle_points)
        elif piece[3] == STAR:
            star_points = [(piece[0] * 50 + 25, piece[1] * 50 + 5), (piece[0] * 50 + 35, piece[1] * 50 + 45),
                           (piece[0] * 50 + 5, piece[1] * 50 + 20), (piece[0] * 50 + 45, piece[1] * 50 + 20),
                           (piece[0] * 50 + 15, piece[1] * 50 + 45)]
            pygame.draw.polygon(screen, (255, 255, 255), star_points)
        elif piece[3] == DIAMOND:
            diamond_points = [(piece[0] * 50 + 25, piece[1] * 50 + 5), (piece[0] * 50 + 45, piece[1] * 50 + 25),
                              (piece[0] * 50 + 25, piece[1] * 50 + 45), (piece[0] * 50 + 5, piece[1] * 50 + 25)]
            pygame.draw.polygon(screen, (255, 255, 255), diamond_points)
        elif piece[3] == HEXAGON:
            hexagon_points = [(piece[0] * 50 + 10, piece[1] * 50 + 25), (piece[0] * 50 + 25, piece[1] * 50 + 5),
                              (piece[0] * 50 + 40, piece[1] * 50 + 25), (piece[0] * 50 + 40, piece[1] * 50 + 45),
                              (piece[0] * 50 + 25, piece[1] * 50 + 65), (piece[0] * 50 + 10, piece[1] * 50 + 45)]
            pygame.draw.polygon(screen, (255, 255, 255), hexagon_points)


def get_piece_at(x, y):
    for piece in player1_pieces:
        if piece[0] == x and piece[1] == y:
            return piece
    for piece in player2_pieces:
        if piece[0] == x and piece[1] == y:
            return piece
    return None


def is_valid_move(piece, new_x, new_y):
    if new_x < 0 or new_x > 2 or new_y < 0 or new_y > 2:
        return False
    if get_piece_at(new_x, new_y) is not None:
        return False
    if piece[0] == new_x and piece[1] == new_y:
        return False
    return True


def get_player_pieces(player):
    if player == 1:
        return player1_pieces
    else:
        return player2_pieces


def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1


def play_game():
    game_over = False
    current_player = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                break
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                square_x = x // 50
                square_y = y // 50
                piece = get_piece_at(square_x, square_y)
                if piece is not None:
                    current_piece = piece
                elif is_valid_move(current_piece, square_x, square_y):
                    get_player_pieces(current_player).remove(current_piece)
                    current_piece = (square_x, square_y, current_piece[2], current_piece[3])
                    get_player_pieces(current_player).append(current_piece)
                    current_player = switch_player(current_player)

        screen.fill((255, 255, 255))
        draw_board()
        draw_pieces()
        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()



play_game()
