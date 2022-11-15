import pygame
import os
import pygame.font

grey = (32, 32, 32)
dark_pink = (139,10,80) #dark pink
dark_cyan = (0,139,139) # dark cyan
light_pink = (255, 0, 127) # pink
light_cyan = (0,238,238) # light cyan
navy = (0, 0, 25)
white = (255, 255, 255)

class Ants:
	"""Class to draw ants"""
	def __init__(self, lv):
		"""init ants"""

		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings

	def draw_ants(self):
		"""functions for drawing the ants"""