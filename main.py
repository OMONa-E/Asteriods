import pygame
from constants import (
	SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, 
	ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
)

def main():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen, (0,0,0)) # cover the display window with specified color here -- black
		pygame.display.flip() # refresh the screen  -- .update() refresh entire or partial 

	print("Starting asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
	main()
