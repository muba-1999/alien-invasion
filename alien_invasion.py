import sys
import pygame

class AlienInvasion:
	"""class to manage game behavior"""

	def __init__(self):
		"""initializing the game and creating game resources"""

		pygame.init()

		self.screen = pygame.display.set_mode(1200, 800)
		pygame.display.set_caption("Alien Invasion")

		def run_game(self):
			"""creating game loop"""

			while True:

				#watching for keyboard and mouse events
				for event in pygame.event.get():
					if event.type == pygame.QUIT():
						sys.exit()

				#making the drawn screen visible
				pygame.display.flip()


if __name__ == 'main':
	#making game instance and running game

	ai = AlienInvasion()
	ai.run_game()