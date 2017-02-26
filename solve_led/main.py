import sys
import argparse
import urllib.request

# create a led box of n size
def create_board(led_box_len):
	"""Creates a board with a parsed size"""
	return [[False] * led_box_len for _ in range(led_box_len)]

def clean_up_input_file(commands):
	"""Cleans up input file and returns usable values"""

	return False

def board_plotter(final_data, board):
	"""Cycles the board and turns on, off or switches lights"""
	return False

def print_lights_totals(result):
	"""Prints to the number of on lights"""
	return False


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