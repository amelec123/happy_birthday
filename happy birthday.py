import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Feliz Cumpleaños")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (160, 32, 240)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)

# Fuente
font = pygame.font.Font(None, 26)

# Clase Globo
class Globo:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 15

    def move(self):
        self.y -= 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.radius), (self.x, self.y + self.radius + 10), 2)

# Lista de globos
balloons = []
colors = [RED, BLUE, YELLOW, GREEN, PURPLE]

# Variables de la carta
card_x, card_y = WIDTH // 2 - 100, HEIGHT // 2 - 10
card_width, card_height = 260, 120
message_y = card_y + 60
message_appear = False

# Bucle principal
running = True
clock = pygame.time.Clock()
frame_count = 0
while running:
    screen.fill(WHITE)

    # Dibujar carta
    pygame.draw.rect(screen, BLACK, (card_x, card_y, card_width, card_height), 2)
    pygame.draw.rect(screen, PINK, (card_x + 5, card_y + 5, card_width - 10, card_height - 10))
    
    # Mostrar mensaje después de unos segundos
    if frame_count > 100:
        message_appear = True
        text = font.render("  ¡Feliz Cumpleaños Eli Linda!", True, RED)
        screen.blit(text, (WIDTH // 2 - 100, message_y))
        
        # Crear globos
        if frame_count % 10 == 0:
            balloons.append(Globo(random.randint(card_x, card_x + card_width), card_y, random.choice(colors)))
    
    # Mover y dibujar globos
    for balloon in balloons:
        balloon.move()
        balloon.draw(screen)
    
    # Actualizar pantalla
    pygame.display.flip()
    
    # Control de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    frame_count += 1
    clock.tick(30)

pygame.quit()