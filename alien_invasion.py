import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet 
from alien import Alien


class AlienInvasion:
	"""class to manage game behavior"""

	def __init__(self):
		"""initializing the game and creating game resources"""

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		#self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()


	def run_game(self):
		"""creating game loop"""

		while True:

			self._check_event()
			self.ship.update()
			self.bullets.update()
			self._update_bullets()
			self._create_fleet()
			self._update_screen()


	def _create_fleet(self):
		"""creates an alien fleet"""
		#spacing between aliens is one alien width
		alien = Alien(self)
		alien_width = alien.rect.width
		availabe_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = availabe_space_x // (2 * alien_width)

		#creating the first row of aliens
		for alien_number in range(number_aliens_x):
			self._create_alien(alien_number)


	def _create_alien(self, alien_number):
		#creates an alien
		alien = Alien(self)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		self.aliens.add(alien)

	def _check_event(self):
		#watching for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_event(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_event(event)


	def _check_keydown_event(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_event(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False


	def _fire_bullet(self):
		"""creating a new bullet and adding it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _update_bullets(self):
		"""updates position of bullets and gets rid of old bullets"""

		#getting rid of the bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)



	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet( )

		self.aliens.draw(self.screen)

		#making the drawn screen visible
		pygame.display.flip()



if __name__ == '__main__':
	#making game instance and running game

	ai = AlienInvasion()
	ai.run_game()