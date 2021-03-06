import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import Player, DirectionalBullet ,Police1,Police2,Police3,Police4,Riot,Captain,RandomDirectionalBullet
import random

class MainGame(SimpleGame):
	BLACK = pygame.Color('black')
	BLUE = pygame.Color('blue')
	WHITE = pygame.Color('white')
	RED = pygame.Color('red')
	SPEED = [0.1,0.5,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,0.1,0.5,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,0.1,0.5,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,10,15,20,45,55,70]
	STAR_SPEED = [2,2,2,2,2,2,2,2,2,2,2,20]
	def __init__(self):
		super(MainGame, self).__init__('Prison Flee', MainGame.BLACK)
		self.bosstime = 20
		self.score = 0
		self.stat = 'normal'
		self.player = Player(color=MainGame.WHITE, \
						pos=(self.window_size[0]/2, \
						self.window_size[1]/2), )
		
		self.directionalbullettops =[]
		for i in range(1000):
			directionalbullettop = DirectionalBullet(radius=4, \
						color=MainGame.BLUE, \
						pos=(random.randint(-60,700), \
						-10), speed = (random.choice(MainGame.SPEED),random.choice(MainGame.SPEED)),dir =random.randint(0,180))
			self.directionalbullettops.append(directionalbullettop)

		self.directionalbulletdowns =[]
		for i in range(1000):
			directionalbulletdown = DirectionalBullet(radius=4, \
						color=MainGame.BLUE, \
						pos=(random.randint(-60,700), \
						490), speed = (random.choice(MainGame.SPEED),random.choice(MainGame.SPEED)),dir =random.randint(180,360))
			self.directionalbulletdowns.append(directionalbulletdown)

		self.police1lst = []
		for i in range(100):
			police1 = Police1(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(-400,1040), \
						-30),\
						speed = (0.5,0.5))
			self.police1lst.append(police1)
		
		self.police2lst = []
		for i in range(50):
			police2 = Police2(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(-400,1040), \
						510),\
						speed = (1,1))
			self.police2lst.append(police2)
			
		self.police3lst = []
		for i in range(20):
			police3 = Police3(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						-30),\
						speed = (1.5,1.5))
			self.police3lst.append(police3)
		
		self.police4lst = []
		for i in range(10):
			police4 = Police4(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						520),\
						speed = (2,2))
			self.police4lst.append(police4)
			
		self.riotlst = []
		for i in range(10):
			riot = Riot(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						-30),\
						speed = (2.2,2.2))
			self.riotlst.append(riot)

		self.captain = Captain(radius=10, \
						color=MainGame.BLUE, \
						pos=(random.randint(0,640), \
						-30),\
						speed = (0.2,0.2))

		self.starbulletlst = []
		if (pygame.time.get_ticks())/1000 %5==0 :
			for i in range(12):
				starbullet = DirectionalBullet(radius=4, \
						color=MainGame.WHITE, \
						pos=(self.captain.x, \
						self.captain.y), speed = (random.choice(MainGame.STAR_SPEED),random.choice(MainGame.STAR_SPEED)),dir =i*30)
				self.starbulletlst.append(starbullet)
		
	def init(self):
		super(MainGame, self).init()
		self.render_score()
		
	def render(self,surface):
		if self.stat == 'proof':
			self.player.bulletproofrender(surface)
		else :
			self.player.render(surface)
		self.player.edgecontrol()

		self.score = (pygame.time.get_ticks())
		self.render_score()
		surface.blit(self.score_image, (10,10))
		if 5>=(pygame.time.get_ticks())/1000 %30>=0 and  (pygame.time.get_ticks())/1000  >= 30 :
			surface.blit(self.warn_image, (195,230))

		if (pygame.time.get_ticks())/1000 %5==0 and (pygame.time.get_ticks())/1000  > self.bosstime :
			for i in range(12):
				starbullet = DirectionalBullet(radius=4, \
						color=MainGame.WHITE, \
						pos=(self.captain.x, \
						self.captain.y), speed = (random.choice(MainGame.STAR_SPEED),random.choice(MainGame.STAR_SPEED)),dir =i*30)
				self.starbulletlst.append(starbullet)

		if (pygame.time.get_ticks())/1000 %5==4 and (pygame.time.get_ticks())/1000  > self.bosstime :
			self.starbulletlst = []
		self.captain.render(surface)
		if 4>(pygame.time.get_ticks())/1000 %5>0 and (pygame.time.get_ticks())/1000  > self.bosstime :
			for i in range(12):
				self.starbulletlst[i].render(surface)

		for i in range(1000):
			self.directionalbullettops[i].render(surface)
		for i in range(1000):
			self.directionalbulletdowns[i].render(surface)
		for i in range(10):
			self.police1lst[i].render(surface)
		for i in range(10):
			self.police2lst[i].render(surface)
		for i in range(10):
			self.police3lst[i].render(surface)
		for i in range(10):
			self.police4lst[i].render(surface)
		for i in range(10):
			self.riotlst[i].render(surface)

	def render_score(self):
		self.score_image = self.font.render("Score = %d" % self.score,0,MainGame.WHITE)
		self.warn_image = self.font.render('Press \'s\' To Use Armour',0,MainGame.RED)
	
	def collisiondetector(self,):
		CHAR_SIZE = 15
		BULLET_SIZE = 4
		ENEMY_SIZE = 15

		for i in range(1000):
			if self.directionalbulletdowns[i].x-BULLET_SIZE < self.player.x+CHAR_SIZE and self.directionalbulletdowns[i].x+BULLET_SIZE > self.player.x-CHAR_SIZE :
				if self.directionalbulletdowns[i].y+BULLET_SIZE > self.player.y-CHAR_SIZE and self.directionalbulletdowns[i].y-BULLET_SIZE < self.player.y+CHAR_SIZE:
					return True
			if self.directionalbullettops[i].x-BULLET_SIZE < self.player.x+CHAR_SIZE and self.directionalbullettops[i].x+BULLET_SIZE > self.player.x-CHAR_SIZE :
				if self.directionalbullettops[i].y+BULLET_SIZE > self.player.y-CHAR_SIZE and self.directionalbullettops[i].y-BULLET_SIZE < self.player.y+CHAR_SIZE:
					return True
		for i in range(10):
			if self.police1lst[i].x-ENEMY_SIZE < self.player.x+CHAR_SIZE and self.police1lst[i].x+ENEMY_SIZE > self.player.x-CHAR_SIZE :
				if self.police1lst[i].y+ENEMY_SIZE > self.player.y-CHAR_SIZE and self.police1lst[i].y-ENEMY_SIZE < self.player.y+CHAR_SIZE:
					return True
		for i in range(10):
			if self.police2lst[i].x-ENEMY_SIZE < self.player.x+CHAR_SIZE and self.police2lst[i].x+ENEMY_SIZE > self.player.x-CHAR_SIZE :
				if self.police2lst[i].y+ENEMY_SIZE > self.player.y-CHAR_SIZE and self.police2lst[i].y-ENEMY_SIZE < self.player.y+CHAR_SIZE:
					return True
		for i in range(10):
			if self.police3lst[i].x-ENEMY_SIZE < self.player.x+CHAR_SIZE and self.police3lst[i].x+ENEMY_SIZE > self.player.x-CHAR_SIZE :
				if self.police3lst[i].y+ENEMY_SIZE > self.player.y-CHAR_SIZE and self.police3lst[i].y-ENEMY_SIZE < self.player.y+CHAR_SIZE:
					return True
		for i in range(10):
			if self.police4lst[i].x-ENEMY_SIZE < self.player.x+CHAR_SIZE and self.police4lst[i].x+ENEMY_SIZE > self.player.x-CHAR_SIZE :
				if self.police4lst[i].y+ENEMY_SIZE > self.player.y-CHAR_SIZE and self.police4lst[i].y-ENEMY_SIZE < self.player.y+CHAR_SIZE:
					return True
		for i in range(10):
			if self.riotlst[i].x-ENEMY_SIZE < self.player.x+CHAR_SIZE and self.riotlst[i].x+ENEMY_SIZE > self.player.x-CHAR_SIZE :
				if self.riotlst[i].y+ENEMY_SIZE > self.player.y-CHAR_SIZE and self.riotlst[i].y-ENEMY_SIZE < self.player.y+CHAR_SIZE:
					return True
		for i in range(12):
			if self.starbulletlst[i].x-BULLET_SIZE < self.player.x+CHAR_SIZE and self.starbulletlst[i].x+BULLET_SIZE > self.player.x-CHAR_SIZE :
				if self.starbulletlst[i].y+BULLET_SIZE > self.player.y-CHAR_SIZE and self.starbulletlst[i].y-BULLET_SIZE < self.player.y+CHAR_SIZE:
					return True
		
	def update(self):
		if self.is_key_pressed(K_UP):
			self.player.move_up()
		if self.is_key_pressed(K_DOWN):
			self.player.move_down()
		if self.is_key_pressed(K_LEFT):
			self.player.move_left()
		if self.is_key_pressed(K_RIGHT):
			self.player.move_right()
		self.stat = 'normal'
		if 5>=(pygame.time.get_ticks())/1000 %30>=0 and  (pygame.time.get_ticks())/1000  >= 30 :
			if self.is_key_pressed(K_s):
				self.stat = 'proof'	
		try:
			if self.stat == 'normal':
				if self.collisiondetector() == True:
					self.is_terminated = True
			else:
				pass
		except:
			pass
		
		if ((pygame.time.get_ticks())/1000) < 100:
			for i in range(pygame.time.get_ticks()/1000):
				self.directionalbullettops[i].move()
			for i in range(pygame.time.get_ticks()/1000):
				self.directionalbulletdowns[i].move()
		else:
			for i in range(2*((pygame.time.get_ticks())/1000)):
				self.directionalbullettops[i].move()
			for i in range(2*((pygame.time.get_ticks())/1000)):
				self.directionalbulletdowns[i].move()

		if (pygame.time.get_ticks())/1000 > 20:
			for i in range(2):
				self.police1lst[i].move(self.player)
		if (pygame.time.get_ticks())/1000 > 30:
			a=2
			for i in range(2,4):
				self.police1lst[i].move(self.player)

		if (pygame.time.get_ticks())/1000  > 40 :
			for i in range(2):
				self.police2lst[i].move(self.player)

		if (pygame.time.get_ticks())/1000  > 50 :
			for i in range(2):
				self.police3lst[i].move(self.player)

		if (pygame.time.get_ticks())/1000  > 60 :
			for i in range(2):
				self.police4lst[i].move(self.player)
		if (pygame.time.get_ticks())/1000  > 70 :
			for i in range(1):
				self.riotlst[i].move(self.player)
		if (pygame.time.get_ticks())/1000  > self.bosstime :
			self.captain.move(self.player)

		if 4>(pygame.time.get_ticks())/1000 %5>0 and (pygame.time.get_ticks())/1000  > self.bosstime :
			for i in range(12):
				self.starbulletlst[i].move()
		
def main():
	game = MainGame()
	game.run()
	
	
if __name__ == '__main__':
	main()