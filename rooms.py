import pygame
import os
import pygame.font

grey = (32, 32, 32)
p1_old = (139,10,80) #dark pink
p2_old = (0,139,139) # dark cyan
p1_new = (255, 0, 127) # pink
p2_new = (0,238,238) # light cyan
navy = (0, 0, 25)

class Rooms:
	"""Class to read and print rooms"""

	def __init__(self, lv):
		"""Init rooms"""
		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings