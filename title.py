import pygame
import os
import pygame.font

white = (255, 255, 255)
black = (0, 0, 0)
navy = (0, 0, 25)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 102, 0)

path = os.path.dirname(os.path.abspath(__file__))
# ant_img_path = pygame.image.load(os.path.join(path, 'images', 'ant_img.bmp'))
# ant_img = pygame.transform.scale(ant_img_path, (170, 200))
tfont = os.path.join(path, 'fonts', 'ant_font.ttf')
ifont = os.path.join(path, 'fonts', 'Pluto.ttf')

class Title:
	"""A class to print the title and image"""

	def __init__(self, lv):
		"""Initialize title and image"""
		self.screen = lv.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = lv.settings

		self.title_font = pygame.font.Font(tfont, 180)
		self.instructions_font = pygame.font.Font(ifont, 30)

		# self.ant = ant_img
		# self.ant_rect = self.ant.get_rect()
		# self.ant_rect.right = self.screen_rect.right - 20
		# self.ant_rect.top = self.screen_rect.top + 20
		
		title_str = "Lem_in"
		self.title = self.title_font.render(title_str, True,
					white, self.settings.bg_colour)
		self.title_rect = self.title.get_rect()
		self.title_rect.left = self.screen_rect.left + 70
		self.title_rect.top = self.screen_rect.top + 40

		self.start_box = pygame.Surface((25, 25))
		self.start_box.fill(green)
		self.sink_box = pygame.Surface((25, 25))
		self.sink_box.fill(red)
		self.empty_room = pygame.Surface((25, 25))
		self.empty_room.fill(blue)
		self.occupied_f = pygame.Surface((25, 25))
		self.occupied_f.fill(orange)

		start_str = "Starting room"
		self.start = self.instructions_font.render(start_str, True,
					white, self.settings.bg_colour)
		sink_str = "Sink room"
		self.sink = self.instructions_font.render(sink_str, True,
					white, self.settings.bg_colour)
		empty_str = "Empty room"
		self.empty = self.instructions_font.render(empty_str, True,
					white, self.settings.bg_colour)
		occ_str = "Occupied room"
		self.occ = self.instructions_font.render(occ_str, True,
					white, self.settings.bg_colour)

	def draw_title_instructions(self):
		"""Draw instructions and title"""
		# self.screen.blit(self.ant, self.ant_rect)
		self.screen.blit(self.title, self.title_rect)
		self.screen.blit(self.start_box, (800, 50))
		self.screen.blit(self.sink_box, (800, 100))
		self.screen.blit(self.empty_room, (800, 150))
		self.screen.blit(self.occupied_f, (800, 200))
		self.screen.blit(self.start, (850, 50))
		self.screen.blit(self.sink, (850, 100))
		self.screen.blit(self.empty, (850, 150))
		self.screen.blit(self.occ, (850, 200))
		