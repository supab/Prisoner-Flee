import pygame
from pygame.locals import *
import random
import math

class Player(object):
	def __init__(self, radius, color, pos):
		(self.x, self.y) = pos
		self.radius = radius
		self.color = color
		self.stat = 'front'
		self.frontimg = pygame.image.load("prisoner_front.png")
		self.backimg = pygame.image.load("prisoner_back.png")
		self.leftimg = pygame.image.load("prisoner_left.png")
		self.rightimg = pygame.image.load("prisoner_right.png")
	def move(self, delta_t, display, player):
		global score, game_over
		self.x += self.vx*delta_t
		self.y += self.vy*delta_t
		
	def move_up(self):
		self.y -= 5
		self.stat = 'back'

	def move_down(self):
		self.y += 5
		self.stat = 'front'
		
	def move_left(self):
		self.x -= 5
		self.stat = 'left'
	
	def move_right(self):
		self.x += 5
		self.stat = 'right'

	def render(self, surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.circle(surface, self.color, pos, self.radius, 0)
		if self.stat == 'front':
			surface.blit(self.frontimg,(self.x-15,self.y-15))
		if self.stat == 'back':
			surface.blit(self.backimg,(self.x-15,self.y-15))
		if self.stat == 'left':
			surface.blit(self.leftimg,(self.x-15,self.y-15))
		if self.stat == 'right':
			surface.blit(self.rightimg,(self.x-15,self.y-15))

#########################################

class Bullet(object):

	def __init__(self, radius, color, pos):
		self.radius = radius
		(self.x,self.y) = pos
		self.color = color
		
	def move(self):
		self.x += 5
		
	def render(self, surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.circle(surface, self.color, pos, self.radius, 0)
		
#########################################

class DirectionalBullet(object):
	def __init__(self, radius, color, pos,speed,dir):
		self.radius = radius
		(self.x,self.y) = pos
		(self.vx, self.vy) = speed
		self.color = color
		self.dir = dir
		
	def move(self):
		self.x += self.vx*float(math.cos(math.radians(self.dir)))
		self.y += self.vy* float(math.sin(math.radians(self.dir)))
		
	def render(self, surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.circle(surface, self.color, pos, self.radius, 0)
		
#########################################

class StarBullet(object):
	# b = [bullet() for x in range(50)]
	pass
	
#########################################
						
class Police1(object):
	def __init__(self, radius, color, pos,speed):
		self.radius = radius
		(self.x,self.y) = pos
		self.color = color
		(self.vx,self.vy) = speed
		self.stat = 'left'
		self.leftimg = pygame.image.load("police1_left.png")
		self.rightimg = pygame.image.load("police1_right.png")
		
	def move(self,player):
		if player.x >= self.x:
			self.stat = 'right'
			self.x += self.vx
			if player.y > self.y:
				self.y += self.vy
			else:
				self.y -= self.vy
		elif player.x < self.x:
			self.stat =  'left'
			self.x -= self.vx
			if player.y > self.y:
				self.y += self.vy
			else:
				self.y -= self.vy
	def render(self, surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.circle(surface, self.color, pos, self.radius, 0)
		if self.stat == 'left':
			surface.blit(self.leftimg,(self.x-15,self.y-15))
		if self.stat == 'right':
			surface.blit(self.rightimg,(self.x-15,self.y-15))
			
#########################################
class Police2(Police1):
	def __init__(self, radius, color, pos,speed):
		self.radius = radius
		(self.x,self.y) = pos
		self.color = color
		(self.vx,self.vy) = speed
		self.stat = 'left'
		self.leftimg = pygame.image.load("police2_left.png")
		self.rightimg = pygame.image.load("police2_right.png")
#########################################	
class Police3(Police1):
	def __init__(self, radius, color, pos,speed):
		self.radius = radius
		(self.x,self.y) = pos
		self.color = color
		(self.vx,self.vy) = speed
		self.stat = 'left'
		self.leftimg = pygame.image.load("police3_left.png")
		self.rightimg = pygame.image.load("police3_right.png")
#########################################	
class Police4(Police1):
	def __init__(self, radius, color, pos,speed):
		self.radius = radius
		(self.x,self.y) = pos
		self.color = color
		(self.vx,self.vy) = speed
		self.stat = 'left'
		self.leftimg = pygame.image.load("police4_left.png")
		self.rightimg = pygame.image.load("police4_right.png")
#########################################	
class Riot(Police1):
	def __init__(self, radius, color, pos,speed):
		self.radius = radius
		(self.x,self.y) = pos
		self.color = color
		(self.vx,self.vy) = speed
		self.stat = 'left'
		self.leftimg = pygame.image.load("riot_left.png")
		self.rightimg = pygame.image.load("riot_right.png")
#########################################	
class Captain(Police1):
	def __init__(self, radius, color, pos,speed):
		self.radius = radius
		(self.x,self.y) = pos
		self.color = color
		(self.vx,self.vy) = speed
		self.stat = 'left'
		self.leftimg = pygame.image.load("captain.png")
		self.rightimg = pygame.image.load("captain.png")
#########################################	

class RandomDirectionalBullet(DirectionalBullet):
	def move(self):
		self.x += self.vx*float(math.cos(math.radians(self.dir)))+(random.random()-0.5)*15
		self.y += self.vy* float(math.sin(math.radians(self.dir)))+(random.random()-0.5)*15
	def updateTrack(self):
			  trackX += self.vx*float(math.cos(math.radians(self.dir)))
			  trackY -= self.vx* float(math.sin(math.radians(self.dir)))

#########################################

