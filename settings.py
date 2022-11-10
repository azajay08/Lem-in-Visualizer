import pygame
import os
import sys

black = (0, 0, 0)
grey = (175, 175, 175)
navy = (0, 0, 25)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
orange = (255, 102, 0)
blue_bg = (15, 30, 50)
cyan_line = (0,139,139)

class Settings:
	"""Class to store settings variables"""

	def __init__(self):
		"""Initialize the settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = blue_bg

		self.delay = 200

		self.line = sys.stdin.read().splitlines()
		
	def read_ants(self):
		"""read the amount of ants"""
		self.ants = int(self.line[0])
		print(self.ants)

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
		for line in self.line:
			line_l = line.split('-')
			line = line.split(' ')
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
			if len(line_l) == 2:
				new_connect = {
					'l_1': line_l[0],
					'l_2': line_l[1],
				}
				self.connect.append(new_connect)

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

		self.source_img = pygame.Surface((self.grid_side, self.grid_side))
		self.source_img.fill(green)
		self.sink_img = pygame.Surface((self.grid_side, self.grid_side))
		self.sink_img.fill(red)
		self.room_img = pygame.Surface((self.grid_side, self.grid_side))
		self.room_img.fill(grey)
		self.midway = pygame.Surface((self.grid_side / 3, self.grid_side / 3))
		self.midway.fill(white)
		self.occupied = pygame.Surface((self.grid_side, self.grid_side))
		self.occupied.fill(orange)