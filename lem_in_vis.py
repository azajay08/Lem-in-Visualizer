from subprocess import ABOVE_NORMAL_PRIORITY_CLASS
import pygame
import sys
import os
from time import sleep

path = os.path.dirname(os.path.abspath(__file__))
ant_img_path = pygame.image.load(os.path.join(path, 'images', "ant_img.bmp"))
ant_img = pygame.transform.scale(ant_img_path, (50, 30))

class Lem_in:
	"""Class for lem_in visualizer"""

	def __init__(self):
		"""Initialize the visualizer"""