import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
	"""class to manage game behavior"""

	def __init__(self):
		"""initializing the game and creating game resources"""

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

	def run_game(self):
		"""creating game loop"""

		while True:

			self._check_event()
			self._update_screen()

	def _check_event(self):
		#watching for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		#making the drawn screen visible
		pygame.display.flip()


if __name__ == '__main__':
	#making game instance and running game

	ai = AlienInvasion()
	ai.run_game()