import pygame

class Ship:
	"""Class that mmanages the ships behavior"""

	def __init__(self, ai_game):
		"""Initailize the ship and set its starting position"""

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#loading ship image and getting its rect
		self.image = pygame.image.load('./images/ship.bmp')
		self.rect = self.image.get_rect()

		#start each ship at the middle bottom
		self.rect.midbottom = self.screen_rect.midbottom

		self.moving_right = False
		self.moving_left = False

		self.settings = ai_game.settings

		self.x = float(self.rect.x)

	def update(self):
		"""updates the ships position base on the movement flag"""

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#updating rect object from self.x
		self.rect.x = self.x


	def blitme(self):
		#Draw the ship at its current position
		self.screen.blit(self.image, self.rect)