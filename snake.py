import curses
from curses import wrapper, KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import random
import time

def main(stdscr):
	
	curses.curs_set(0)
	win = curses.newwin(20, 40, 1, 0)
	win.nodelay(True)
	win.keypad(True)
	win.clear()
	win.border(0, 0, ord('-'), ord('-'))
	
	left = KEY_LEFT
	right = KEY_RIGHT
	up = KEY_UP
	down = KEY_DOWN
	
	#(win_height, win_width) = win.getmaxyx()
	(win_height, win_width) =(20 - 1, 40 - 1)
	score = 0
	
	snake = [[5, 2], [4, 2], [3, 2]]
	
	key = right
	
	food = [5, 5]
	
	win.addstr(snake[-1][1], snake[-1][0], 'O' * len(snake))
	
	win.addch(food[1], food[0], '*')

	while True:
		new_key = win.getch()
		if (new_key not in {up, down, left, right}) or (key in {left, right} and new_key in {left, right}) or (key in {up, down} and new_key in {up, down}):
			pass
		else:
			key = new_key
		
		curses.flushinp()
		win.timeout(100)
		#win.clear()
		
		
		
		if snake[0] == food:
			score += 1
			stdscr.addstr(0, 0, 'Score: %s' % score)
			stdscr.refresh()
			win.border(0, 0, ord('-'), ord('-'))
			win.refresh()
			food = [random.randint(1, win_width - 1), random.randint(1, win_height - 1)]
			while food in snake:
				food = [random.randint(1, win_width - 1), random.randint(1, win_height - 1)]
				
			win.addch(food[1], food[0], '*')
		else:
			tail = snake.pop()
			win.addch(tail[1],tail[0],' ')
			
		snake.insert(0, [snake[0][0] + (key == right and 1 or key == left and -1), snake[0][1] + (key == down and 1 or key == up and -1)])
		if snake[0] in snake[1:]:
			raise Exception()
		
		if (snake[0][0] == win_width and key == right):
			snake[0][0] = 1
		elif (snake[0][0] == 0 and key == left):
			snake[0][0] = win_width - 1
			
		elif (snake[0][1] == win_height and key == down):
			snake[0][1] = 1
		elif (snake[0][1] == 0 and key == up):
			snake[0][1] = win_height - 1
			
			
		win.addch(snake[0][1], snake[0][0], 'O')
		#win.addstr(str(left) + ' ' +str(right) + ' ' + str(up) + ' ' + str(down) )
		#win.refresh()
		#time.sleep(1)
		
		
		
wrapper(main)