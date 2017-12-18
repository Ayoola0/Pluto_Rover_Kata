x= 0
y= 0
position_x = input('Please enter your starting x co-ordinates')
position_y = input('Please enter your starting y co-ordinates')
initial_direction = input('Please enter your starting direction')

def forward(position_x, position_y, initial_direction, command):
	if initial_direction == 'N' and command == 'F':
		new_position = (x, (y+1))
	elif initial_direction == 'S' and command == 'F':
		new_position = (x,(y-1))	
	elif initial_direction == 'E' and command == 'F':
		new_position = ((x+1),y)
	elif initial_direction == 'W' and command == 'F':
		new_position = ((x-1),y)
		

def backward(position_x, position_y, initial_direction, command):
	if initial_direction == 'N' and command == 'B':
		new_position = (x, (y-1))
	elif initial_direction == 'S' and command == 'B':
		new_position = (x,(y+1))	
	elif initial_direction == 'E' and command == 'B':
		new_position = ((x-1),y)
	elif initial_direction == 'W'and command == 'B':
		new_position = ((x+1),y)
		
def left(position_x, position_y, initial_direction, command):
	if initial_direction == 'N' and command == 'L':
		new_direction = 'W'
	elif initial_direction == 'S' and command == 'L':
		new_direction = 'E'	
	elif initial_direction == 'E' and command == 'L':
		new_direction = 'N'
	elif initial_direction == 'W' and command == 'L':
		new_direction = 'S'
		

def right(position_x, position_y, initial_direction, command):
	if initial_direction == 'N' and command == 'R':
		new_direction = 'E' 
	elif initial_direction == 'S' and command == 'R':
		new_direction = 'W'	
	elif initial_direction == 'E' and command == 'R':
		new_direction = 'S'
	elif initial_direction == 'W' and command == 'R':
		new_direction = 'N'
