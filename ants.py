import pygame
import os
import pygame.font

grey = (32, 32, 32)
p1_old = (139,10,80) #dark pink
p2_old = (0,139,139) # dark cyan
p1_new = (255, 0, 127) # pink
p2_new = (0,238,238) # light cyan
navy = (0, 0, 25)
white = (255, 255, 255)

class Ants:
	"""Class to draw ants"""
	def __init__(self, lv):
		"""init ants"""

		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings