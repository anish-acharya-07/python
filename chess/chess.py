import pygame

# Initialize Pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")

# Colors
WHITE = (255, 255, 255)
BROWN = (181, 136, 99)

# Board settings
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Function to draw chessboard
def draw_board(win):
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 != 0:
                pygame.draw.rect(win, BROWN, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Main loop
running = True
while running:
    draw_board(WIN)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
