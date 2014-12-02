import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import Bullet, Player, DirectionalBullet , StarBullet, RandomDirectionalBullet,Police1,Police2,Police3,Police4,Riot
import random

class MainGame(SimpleGame):
	BLACK = pygame.Color('black')
	BLUE = pygame.Color('blue')
	WHITE = pygame.Color('white')
	def __init__(self):
		super(MainGame, self).__init__('Squash', MainGame.BLACK)
		self.player = Player(radius=10, \
						color=MainGame.WHITE, \
						pos=(self.window_size[0]/2, \
						self.window_size[1]/2), )
		self.bullet = Bullet(radius=10, \
						color=MainGame.BLUE, \
						pos=(self.window_size[0]/2, \
						self.window_size[1]/2), )
		
		self.directionalbullettops =[]
		for i in range(1000):
			directionalbullettop = DirectionalBullet(radius=4, \
						color=MainGame.BLUE, \
						pos=(random.randint(-60,700), \
						-10), speed = (1,1),dir =random.randint(0,180))
			self.directionalbullettops.append(directionalbullettop)
		self.directionalbulletdowns =[]
		for i in range(1000):
			directionalbulletdown = DirectionalBullet(radius=4, \
						color=MainGame.BLUE, \
						pos=(random.randint(-60,700), \
						490), speed = (1,1),dir =random.randint(180,360))
			self.directionalbulletdowns.append(directionalbulletdown)
			
		self.bullets = Bullet(radius=10, \
						color=MainGame.BLUE, \
						pos=(self.window_size[0]/2, \
						self.window_size[1]/2), )

		self.police1lst = []
		for i in range(12):
			police1 = Police1(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(-400,1040), \
						-10),\
						speed = (1,1))
			self.police1lst.append(police1)
		
		self.police2lst = []
		for i in range(9):
			police2 = Police2(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						random.randint(0,480)),\
						speed = (1.5,1.5))
			self.police2lst.append(police2)
			
		self.police3lst = []
		for i in range(6):
			police3 = Police3(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						random.randint(0,480)),\
						speed = (2,2))
			self.police3lst.append(police3)
		
		self.police4lst = []
		for i in range(3):
			police4 = Police4(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						random.randint(0,480)),\
						speed = (2.5,2.5))
			self.police4lst.append(police4)
			
		self.riotlst = []
		for i in range(2):
			riot = Riot(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						random.randint(0,480)),\
						speed = (2.8,2.8))
			self.riotlst.append(riot)
		
		self.randomdirectionalbullet = RandomDirectionalBullet(radius=10, \
						color=MainGame.BLUE, \
						pos=(self.window_size[0]/2, \
						self.window_size[1]/2), speed = (1,1),dir = 200)
		
		
	def init(self):
		super(MainGame, self).init()
		
	def render(self,surface):
		self.player.render(surface)
		self.bullet.render(surface)
		for i in range(1000):
			self.directionalbullettops[i].render(surface)
		for i in range(1000):
			self.directionalbulletdowns[i].render(surface)
		self.randomdirectionalbullet.render(surface)
		for i in range(12):
			self.police1lst[i].render(surface)
		for i in range(9):
			self.police2lst[i].render(surface)
		for i in range(6):
			self.police3lst[i].render(surface)
		for i in range(3):
			self.police4lst[i].render(surface)
		for i in range(2):
			self.riotlst[i].render(surface)
			
	
	def collisiondetector(self):
		RADIUS_CHAR = 15
		for i in range(10):
			if self.player.x+RADIUS_CHAR > self.directionalbulletdowns[i].x-4 and  self.player.x-RADIUS_CHAR > self.directionalbulletdowns[i].x+4 and \
				self.player.y+RADIUS_CHAR > self.directionalbulletdowns[i].y-4  and  self.player.y-RADIUS_CHAR > self.directionalbulletdowns[i].y+4:
				return False
		
	def update(self):
		if self.is_key_pressed(K_UP):
			self.player.move_up()
		if self.is_key_pressed(K_DOWN):
			self.player.move_down()
		if self.is_key_pressed(K_LEFT):
			self.player.move_left()
		if self.is_key_pressed(K_RIGHT):
			self.player.move_right()
			
		if self.collisiondetector() == True:
			self.is_terminated = True
		
		print pygame.time.get_ticks()
		self.bullet.move()
		for i in range(10):
			self.directionalbullettops[i].move()
		for i in range(10):
			self.directionalbulletdowns[i].move()
			
		for i in range(12):
			self.police1lst[i].move(self.player)
		if (pygame.time.get_ticks())/1000  >10 :
			for i in range(9):
				self.police2lst[i].move(self.player)
		if pygame.time.get_ticks()  >5000 :
			for i in range(6):
				self.police3lst[i].move(self.player)
		for i in range(3):
			self.police4lst[i].move(self.player)
		for i in range(2):
			self.riotlst[i].move(self.player)
			
		self.randomdirectionalbullet.move()
		
def main():
	game = MainGame()
	game.run()
	
	
if __name__ == '__main__':
	main()