import pygame

game_field = []
for i in range(16):
    game_field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


tile_size = 45

game_field_height = len(game_field)
game_field_width = len(game_field[0])

display_height = game_field_height * tile_size + 200
display_width = game_field_width * tile_size + 600

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Tetris")

pygame.init()

text_font = pygame.font.SysFont("Arial", 24)

score = 0

text = text_font.render(f"Score: {score}", True, (0, 0, 0))

display.fill((255, 255, 255))

for x in range(300, game_field_width * tile_size + 300, tile_size):
            for y in range(100, game_field_height * tile_size + 100, tile_size):
                    nelio = pygame.rect = (x, y, tile_size, tile_size)
                    pygame.draw.rect(display, (0, 0, 0), nelio, 1)
                    nelio2 = pygame.rect = (x+1, y+1, tile_size, tile_size)



text_x = game_field_width * tile_size + 370
text_y = 250
display.blit(text, (text_x, text_y))
pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        exit()