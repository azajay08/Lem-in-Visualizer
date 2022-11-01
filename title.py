import pygame
import os
import pygame.font

path = os.path.dirname(os.path.abspath(__file__))
ant_img_path = pygame.image.load(os.path.join(path, 'images', 'ant_img.bmp'))
ant_img = pygame.transform.scale(ant_img_path, (170, 200))

class Title:
	"""A class to print the title and image"""

	def __init__(self, lv):
		"""Initialize title and image"""
		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings

		self.ant = ant_img
		self.ant_rect = self.ant.get_rect()
		self.ant_rect.right = self.screen_rect.right - 20
		self.ant_rect.top = self.screen_rect.top + 20
		
	def draw_image_title(self):
		"""Draw image and title"""
		self.screen.blit(self.ant, self.ant_rect)

