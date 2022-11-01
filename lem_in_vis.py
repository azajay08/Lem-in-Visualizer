import pygame
import sys
import os
from title import Title
from time import sleep
from settings import Settings

class Lem_in:
	"""Class for lem_in visualizer"""

	def __init__(self):
		"""Initialize the visualizer"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Lem_in Visualizer")

		self.title = Title(self)

	def run_vis(self):
		"""Loops through program"""
		self.screen.fill(self.settings.bg_colour)
		self.title.draw_image_title()
		while True:
			self._check_events()
			
			pygame.display.flip()

	def _check_events(self):
		"""Function that check events in the program"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				#check buttons or speed
				if event.key == pygame.K_1:
					self.settings.delay = 300
				if event.key == pygame.K_2:
					self.settings.delay = 200
				if event.key == pygame.K_3:
					self.settings.delay = 100
				if event.key == pygame.K_4:
					self.settings.delay = 75
				if event.key == pygame.K_5:
					self.settings.delay = 50
				if event.key == pygame.K_6:
					self.settings.delay = 25
				if event.key == pygame.K_7:
					self.settings.delay = 10
				if event.key == pygame.K_8:
					self.settings.delay = 1
				if event.key == pygame.K_9:
					self.settings.delay = 0.000001

if __name__ == '__main__':
	lv = Lem_in()
	lv.run_vis()