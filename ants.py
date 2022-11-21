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
		self.ants = []

	def choose_colour(self, x_co, y_co, col):
		"function that chooses which colour to print ant in"
		print(col)
		self.r = 255
		self.g = 100
		self.b = 0
		if col == 1:
			self.g = 100
			self.b = 0
		elif col == 2:
			self.g = 150
			self.b = 50
		elif col == 3:
			self.g = 200
			self.b = 100
		orange = (self.r, self.g, self.b)
		occupied = pygame.Surface((self.settings.grid_side, self.settings.grid_side))
		occupied.fill(orange)

		self.screen.blit(occupied, (x_co, y_co))


	def draw_ants(self, line_s):
		"""functions for drawing the ants"""
		i = 0
		line = line_s.split(' ')
		self.settings.ant_col += 1
		# print(line)
		while i < len(line):
			y_grid = self.rect.y
			x_grid = self.rect.x
			line_l = line[i].split('-')
			r_name = str(line_l[-1])
			a_num = int(line_l[0].strip('L'))
			add_ant = 1
			for ants in self.ants:
				if a_num == ants['ant_num']:
					add_ant = 0
					col_print = ants['ant_col']
			if add_ant == 1:
				new_ant = {
					'ant_num': int(a_num),
					'ant_col': self.settings.ant_col,
				}
				self.ants.append(new_ant)
				col_print = self.settings.ant_col
			for room in self.rooms:
				if room['name'] == r_name:
					room['used'] = 1
					x_grid += ((room['x'] - self.settings.smallestx) * (self.settings.scale_x))
					y_grid += ((room['y'] - self.settings.smallesty) * (self.settings.scale_y))
					if room['source'] == 1:
						self.screen.blit(self.settings.source_img, (x_grid, y_grid))
					elif room['sink'] == 1:
						self.screen.blit(self.settings.sink_img, (x_grid, y_grid))
					else:
						self.choose_colour(x_grid, y_grid, col_print)
				elif room['used'] == 0:
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

		for room in self.rooms:
			room['used'] = 0
		if self.settings.ant_col == 3:
				self.settings.ant_col = 0
