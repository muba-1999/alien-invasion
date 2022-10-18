class Settings:
	"""class to store settings for alien invasion"""

	def __init__(self):
		"""initializing the game seetings"""

		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		self.ship_speed = 1.5
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)