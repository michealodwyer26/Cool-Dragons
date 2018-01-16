# This just imports all the Pygame modules
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('St.Patrick game')

clock = pygame.time.Clock()

pygame.mixer.init(44100, -16,2,2048)
pygame.mixer.music.load('The Tonight Show Star Wars The Bee Gees Stayin Alive Shortened.mp3')
pygame.mixer.music.play(-1, 0.0)

image = pygame.image.load('Sprite-01.png')
# initialize variables
image_x = 0
image_y = 0



while 1:
	clock.tick(30)	   
	for event in pygame.event.get():
		if event.type == pygame.quit():
			pygame.quit()
			pygame.mixer.music.stop(52)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			pygame.quit()
			pygame.mixer.music.stop(52)

			
	image_x += 0
	
	key = pygame.key.get_pressed()
	
	if key[pygame.K_LEFT]:
			image_x -= 10
	if key[pygame.K_RIGHT]:
			image_x += 10
	if key[pygame.K_UP]:
			image_y -= 10
	if key[pygame.K_DOWN]:
			image_y += 10

	screen.fill((200, 200, 200))
	
	screen.blit(image, (image_x, image_y))
	
	pygame.display.flip()


