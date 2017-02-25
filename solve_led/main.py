import sys
import argparse
import urllib.request

def read_from_file():
	"""Pull data from a link"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="you need to parse a link to a file")
	args = (parser.parse_args())

	uri = str(args.input)
	req = urllib.request.urlopen(uri)
	data = req.read().decode('utf-8')

	for line in data:
		line_values = line.strip()
		print(line_values,end="")



# def create_board(board_size):
# 	return [[False] * board_size for _ in range(board_size)]

def main():
	read_from_file()

if __name__ == '__main__':
	main()