import pygame
import os
import pygame.font

path = os.path.dirname(os.path.abspath(__file__))
ant_img_path = pygame.image.load(os.path.join(path, 'images', "ant_img.bmp"))
ant_img = pygame.transform.scale(ant_img_path, (50, 30))

class Title:
	"""A class to print the title and image"""

	def __init__(self, lv):
		"""Initialize title and image"""
		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings

		self.ant = ant_img
		self.ant_rect = self.ant.get_rect()
		self.ant_rect.top = self.screen.top + 20
		self.ant_rect.right = self.screen.right - 20
		

