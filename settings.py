import pygame
import os
import sys

black = (0, 0, 0)
grey = (150, 150, 170)
navy = (0, 0, 25)
red = (200, 50, 50)
green = (100, 255, 100)
blue = (50, 100, 255)
white = (255, 255, 255)
# orange = (255, 102, 0)
blue_bg = (7, 30, 50)
cyan_line = (0,139,139)
light_blue = (116, 212, 205)

class Settings:
	"""Class to store settings variables"""

	def __init__(self):
		"""Initialize the settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = blue_bg

		self.delay = 500

		self.line = sys.stdin.read().splitlines()

		self.ant_col = 1
		
	def read_ants(self):
		"""read the amount of ants"""
		self.ants = int(self.line[0])
		# print(self.ants)

	def read_rooms(self):
		"""read the rooms"""
		self.rooms = []
		self.connect = []
		self.x_size = 0
		self.y_size = 0
		self.s_com = 0
		self.e_com = 0
		self.smallesty = 100000000;
		self.smallestx = 100000000;
		map_len = len(self.line)
		i = -1
		for line in self.line:
			line_m = line
			line_l = line.split('-')
			line = line.split(' ')
			i += 1
			if line_m[:1] == 'L':
				break
			if line_m[:1] == ' ':
				continue
			if len(line) == 3:
				if int(line[1]) > self.x_size:
					self.x_size = int(line[1])
				if int(line[2]) > self.y_size:
					self.y_size = int(line[2])
				if int(line[1]) < self.smallestx:
					self.smallestx = int(line[1])
				if int(line[2]) < self.smallesty:
					self.smallesty = int(line[2])
				new_room = {
					'name': line[0],
					'x': int(line[1]),
					'y': int(line[2]),
					'source': self.s_com,
					'sink': self.e_com,
					'used': 0,
				}
				if self.s_com == 1:
					self.source = line[0]
					self.s_com = 0
				if self.e_com == 1:
					self.sink = line[0]
					self.e_com = 0
				self.rooms.append(new_room)
			if '##start' in line:
				self.s_com = 1
			if '##end' in line:
				self.e_com = 1
			if '#' in line and self.e_com == 0 and self.s_com == 0:
				continue
			if len(line_l) == 2:
				new_connect = {
					'l_1': line_l[0],
					'l_2': line_l[1],
				}
				self.connect.append(new_connect)

		self.map_len = map_len
		self.i = map_len - i
		self.s_line = str(self.line[i]).rstrip(' ') + '\n'
		i += 1

		while i < map_len:
			self.s_line += str(self.line[i]).rstrip(' ') + '\n'
			# print(self.s_line)
			i += 1
		self.split_line = self.s_line.split('\n') 
		print(self.split_line[0])

		self.div = 400
		if (self.y_size < self.x_size):
			self.grid_scale = float(self.x_size)
		else:
			self.grid_scale = float(self.y_size)
		self.grid_side = float(self.div / self.grid_scale)
		self.scale_x = float(800 / self.x_size)
		self.scale_y = float(400 / self.y_size)
		if self.grid_side < 10:
			self.grid_side = 10

		# self.r = 255
		# self.g = 100
		# self.b = 0
		# self.orange = (self.r, self.g, self.b)
		self.source_img = pygame.Surface((self.grid_side, self.grid_side))
		self.source_img.fill(green)
		self.sink_img = pygame.Surface((self.grid_side, self.grid_side))
		self.sink_img.fill(red)
		self.room_img = pygame.Surface((self.grid_side, self.grid_side))
		self.room_img.fill(blue)
		self.midway = pygame.Surface((self.grid_side / 3, self.grid_side / 3))
		self.midway.fill(light_blue)
		# self.occupied = pygame.Surface((self.grid_side, self.grid_side))
		# self.occupied.fill(self.orange)