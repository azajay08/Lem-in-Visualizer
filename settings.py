import pygame
import os
import sys

black = (0, 0, 0)
navy = (0, 0, 25)

class Settings:
	"""Class to store settings variables"""

	def __init__(self):
		"""Initialize the settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = navy

		self.delay = 200

		self.line = sys.stdin.read().splitlines()
		# for line in self.line:
		# 	print(line)

	def read_ants(self):
		"""read the amount of ants"""
		self.ants = int(self.line[0])
		print(self.ants)

	def read_rooms(self):
		"""read the rooms"""
		self.x_size = 0
		self.y_size = 0
		self.s_com = 0
		self.e_com = 0
		for line in self.line:
			line = line.split(' ')
			if len(line) > 1:
				if int(line[1]) > self.x_size:
					self.x_size = int(line[1])
				if int(line[2]) > self.y_size:
					self.y_size = int(line[2])
				if self.s_com == 1:
					self.source = line[0]
					self.s_com = 0
				if self.e_com == 1:
					self.sink = line[0]
					self.e_com = 0
			if '##start' in line:
				self.s_com = 1
			if '##end' in line:
				self.e_com = 1
		print(self.source)
		print(self.sink)
		print(self.x_size)
		print(self.y_size)


