# This program was not made with speed in mind, rather
# the visual aspect of seeing how a recursive backtracking
# algorithm works.

import pygame
import numpy as np
import time

sudoku = [
	[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

pygame.init()
pygame.display.set_caption("Sudoku Solver")

screen = pygame.display.set_mode((900,900))

def check(y,x,n):	# Function to check if a number n can be placed
	global sudoku 	# in cords xy inline with the sudoku rules
	for i in range(0,9):
		if sudoku[y][i] == n:
			return False
	for i in range(0,9):
		if sudoku[i][x] == n:
			return False

	xGrid = (x//3)*3
	yGrid = (y//3)*3

	for i in range(0,3):
		for j in range(0,3):
			if sudoku[yGrid+i][xGrid+j] == n:
				return False
	return True

def solve():		# A recursive backtracking algorythm for solving
	for x in range(9):
		for y in range(9):
			if sudoku[y][x] == 0:
				for n in range(1,10):
					if  check(y,x,n):
						sudoku[y][x] = n
						text = font.render(str(n), True,(0,255,0),(255,255,255))
						try:
							screen.blit(text, (x*100+30,y*100+30))
						except:
							return
						time.sleep(0.1)
						pygame.display.update()
						solve()
						sudoku[y][x] = 0
				return
	screen.lock()	# Locking the surface because we still have calls
					# in the recursionstack

running = True
setup = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	while(setup):	# General setup, drawing grids
		screen.fill((255,255,255))
		for i in range(1,10):
			if(i % 3 == 0): # Draw 3x3 grids
				pygame.draw.line(screen,(0,0,0),(0,100*i),(900,100*i),(5))
				pygame.draw.line(screen,(0,0,0),(100*i,0),(100*i,900),(5))
				continue	
		
			pygame.draw.line(screen,(0,0,0),(0,100*i),(900,100*i))
			pygame.draw.line(screen,(0,0,0),(100*i,0),(100*i,900))

		pygame.display.update()

					# Setting up the unsolved sudoku, blit "?" on
					# empty spaces

		font = pygame.font.Font('freesansbold.ttf', 42)

		for col in range(9):
			for row in range(9):
				if(sudoku[col][row] == 0):
					text = font.render("?", True,(255,0,0),(255,255,255))	
				else:
					text = font.render(str(sudoku[col][row]), True,(0,0,0),(255,255,255))
				
				screen.blit(text, (row*100+30,col*100+30))
				pygame.display.update()
		solve()

		setup = False # End the setup loop
pygame.quit()