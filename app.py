import os
import argparse
from PIL import Image

from functions import *


def main():
	parser = argparse.ArgumentParser(description='Steg')
	parser.add_argument("-r", "--reveal", dest="r", help="Provide an image with a hidden message to reveal the text.")
	parser.add_argument("-c", "--conceal", dest="c", help="Provide an image file to conceal a message.")
	parser.add_argument("-m", "--message", dest="m", help="Provide a message in the form of text that will be hidden in an image.")
	
	args = parser.parse_args()

	if not args.r:
		if args.c and args.m:
			binary = msg_to_binary(args.m)
			msg_length = len(binary)
			msg_length_binary = format(msg_length, '08b')
			data_length = msg_length + 1
			
			im = Image.open(args.c)
			im.convert('RGB')
			data = get_image_data(im)
			if ((len(data) / 8) - 1) < msg_length:
				print "There is not enough room for your message. Use a larger photo or a smaller message."
			
			data = write_msg_length(data, msg_length_binary)
			data = write_msg(data, binary, msg_length)

			cloak = Image.new(im.mode, im.size)
			cloak.putdata(data)
			cloak.save('cloak.png', 'PNG')
		elif args.c and not args.m:
			print "Please provide a message to hide... \n"
			parser.print_help()
		elif args.m and not args.c:
			print "Please provide an image to conceal your message... \n"
			parser.print_help()
		else: 
			parser.print_help()
	elif args.r:
		im = Image.open(args.r)
		data = get_image_data(im)

		print reveal_msg(data)
	else: 
		parser.print_help()



if __name__ == '__main__':
	main()

