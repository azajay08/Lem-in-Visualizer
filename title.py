import pygame
import os
import pygame.font

white = (255, 255, 255)

path = os.path.dirname(os.path.abspath(__file__))
ant_img_path = pygame.image.load(os.path.join(path, 'images', 'ant_img.bmp'))
ant_img = pygame.transform.scale(ant_img_path, (170, 200))
tfont = os.path.join(path, 'fonts', 'ant_font.ttf')


class Title:
	"""A class to print the title and image"""

	def __init__(self, lv):
		"""Initialize title and image"""
		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings

		self.title_font = pygame.font.Font(tfont, 180)

		self.ant = ant_img
		self.ant_rect = self.ant.get_rect()
		self.ant_rect.right = self.screen_rect.right - 20
		self.ant_rect.top = self.screen_rect.top + 20
		
		title_str = "Lem_in"
		self.title = self.title_font.render(title_str, True,
					white, self.settings.bg_colour)
		self.title_rect = self.title.get_rect()
		self.title_rect.left = self.screen_rect.left + 70
		self.title_rect.top = self.screen_rect.top + 40


	def draw_image_title(self):
		"""Draw image and title"""
		self.screen.blit(self.ant, self.ant_rect)
		self.screen.blit(self.title, self.title_rect)
		pygame.draw.line(self.screen, white, (100, 100), (400, 400))