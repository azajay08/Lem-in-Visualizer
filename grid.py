import pygame
import os
import pygame.font

grey = (32, 32, 32)
p1_old = (139,10,80) #dark pink
p2_old = (0,139,139) # dark cyan
p1_new = (255, 0, 127) # pink
p2_new = (0,238,238) # light cyan
navy = (0, 0, 25)

class Grid:
	"""init grid"""
	def __init__(self, lv):
		"""Init grid"""

		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings

		self.width, self.height = 800, 400
		self.grid_colour = grey

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = 400
		self.rect.y = 300
		self.rect_img = pygame.Surface((self.width, self.height))
		self.rect_img.fill(grey)
		# self.screen.blit(self.rect_img, self.rect)


	def draw_grid(self):
		"""draws the map"""
		y_grid = self.rect.y
		x_grid = self.rect.x
		for room in self.settings.rooms:
			# for k, v in room.items():
			# 	print(f"{k}: {v}")
			x_grid += room['x'] * self.settings.grid_side
			y_grid += room['y'] * self.settings.grid_side
			if room['source'] == 1:
				self.screen.blit(self.settings.source_img, (x_grid, y_grid))
			elif room['sink'] == 1:
				self.screen.blit(self.settings.sink_img, (x_grid, y_grid))
			else:
				self.screen.blit(self.settings.room_img, (x_grid, y_grid))
			y_grid = self.rect.y
			x_grid = self.rect.x
		# self.screen.blit(self.rect_img, self.rect)


