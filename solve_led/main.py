import sys
import argparse
import urllib.request

# create a led box of n size
def create_board(led_box_len):
	"""Creates a board with a parsed size"""
	return [[False] * led_box_len for _ in range(led_box_len)]

def check_for_outliers(board_size, plot_point):
	"""Checks if the point is less than the grid size
	if it is less than the girid size, set the point to 0
	if the point is greater than the grid size, set it to the grid's max value
	"""
	board_size = len(board_size)
	if plot_point > board_size:
		plot_point = board_size - 1
	elif plot_point < 0:
		plot_point = 0
	return plot_point


def clean_up_input_file(commands):
	"""Cleans up input file and returns usable values"""

	final_data = []
	for i in range(len(commands)):
		each_line = commands[i].split(" ")
		for item in each_line:
			if item == "turn" or item == "through" or item ==" ":
				each_line.remove(item)

		row_start = each_line[1]
		row_end = each_line[2]
		first = row_start.split(',')
		second = row_end.split(',')
		action = each_line[0]
		final_data.append([action, int(first[0]),int(first[1]),int(second[0]),int(second[1])])

	return final_data

def board_plotter(final_data, board):
	"""Cycles the board and turns on, off or switches lights"""

	for i in range(len(final_data)):
		for r in range(check_for_outliers(board,final_data[i][1]),check_for_outliers(board,final_data[i][3]) + 1):
			for c in range(check_for_outliers(board,final_data[i][2]), check_for_outliers(board,final_data[i][4]) + 1):

				if final_data[i][0] == "on":
					board[r][c] = True

				elif final_data[i][0] == "off":
					board[r][c] = False

				elif final_data[i][0] == "switch":
					if board[r][c] == True:
						board[r][c] = False
					else:
						board[r][c] = True
				else:
					raise ValueError('invalid action found : {}'.format(final_data[i][0]))
					continue

	return board

def print_lights_totals(result):
	"""Prints to the number of on lights"""
	return ("On count is : ", sum(x.count(True) for x in result))



def read_from_file():
	"""Pull data from a link"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="you need to parse a link to a file")
	args = (parser.parse_args())

	uri = str(args.input)
	req = urllib.request.urlopen(uri)
	data = req.read().decode('utf-8')

	led_box_len = int(data.splitlines()[0])

	board = (create_board(led_box_len))

	commands = data.splitlines()[1:]

	final_data = clean_up_input_file(commands)

	result = board_plotter(final_data, board)
	print(print_lights_totals(result))



def main():
	read_from_file()

if __name__ == '__main__':
	main()