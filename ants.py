import pygame
import os
import pygame.font
import sys
import time

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
		self.line = self.settings.line
		self.grid = lv.grid
		self.rect = self.grid.rect
		self.rooms = self.settings.rooms

	def draw_ants(self):
		"""functions for drawing the ants"""
		
		for line in self.line:
			# line = line.split(' ')
			
			i = 0
			if line[:1] == 'L':
				line = line.rstrip("\n")
				line = line.rstrip(" ")
				line = line.split(' ')
				pygame.time.delay(1000)
				while i < len(line):
					y_grid = self.rect.y
					x_grid = self.rect.x
					line_l = line[i].split('-')
					r_name = str(line_l[-1])
					for room in self.rooms:
						if room['name'] == r_name:
							x_grid += ((room['x'] - self.settings.smallestx) * (self.settings.scale_x))
							y_grid += ((room['y'] - self.settings.smallesty) * (self.settings.scale_y))
							self.screen.blit(self.settings.occupied, (x_grid, y_grid))
						else:
							x_grid += ((room['x'] - self.settings.smallestx) * (self.settings.scale_x))
							y_grid += ((room['y'] - self.settings.smallesty) * (self.settings.scale_y))
							if room['source'] == 1:
								self.screen.blit(self.settings.source_img, (x_grid, y_grid))
							elif room['sink'] == 1:
								self.screen.blit(self.settings.sink_img, (x_grid, y_grid))
							else:
								self.screen.blit(self.settings.room_img, (x_grid, y_grid))
						y_grid = self.rect.y
						x_grid = self.rect.x
					i += 1
