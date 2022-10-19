import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""class creates and controls alien behavior"""

	def __init__(self, ai_game):
		"""initializing an alien and setting its start position"""

		super().__init__()
		self.screen = ai_game.screen

		#loading the alien image and setting its rect
		self.image = pygame.image.load('./images/alien.bmp')
		self.rect = self.image.get_rect()

		#start each alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#storing the aliens horizontal position
		self.x = float(self.rect.x)


