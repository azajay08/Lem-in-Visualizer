import pygame
import os
import sys

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

	def read_ants(self):
		"""read the amount of ants"""
		self.line = sys.stdin.readline()
		self.ants = int(self.line)