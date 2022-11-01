import pygame
import os

black = (0, 0, 0)
navy = (0, 0, 25)

class Settings:
	"""Class to store settings variables"""

	def __init__(self):
		"""Initialize the settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = navy

		self.delay = 200