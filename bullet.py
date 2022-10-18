import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""create bullet and controls bullet behavior"""

	def __init__(self, ai_game):
		"""create a bullet object at the ships posistion"""
		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = settings.bullet_color

		#creating a bullet rect and setting its position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)