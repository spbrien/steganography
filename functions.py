from PIL import Image


def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

def binary_to_msg(binary):
	return chr(int(str(binary), 2))
		
def msg_to_binary(msg):
	binary_msg = []
	for x in msg:
		binary = format(ord(x), '08b')
		binary_msg.append(binary)
	binary_msg = ''.join(binary_msg)
	return binary_msg

def get_image_data(im):
	data = list(im.getdata())

	return data

def increment_pixel(pixel):
	new = (pixel[0], pixel[1], pixel[2] + 1)
	return new

def is_even(pixel):
	if pixel[2] % 2 == 0:
		return True
	else: 
		return False

def write_msg_length(data, msg_length_binary):
	for i in range(0,8):
		pixel = data[i]
		bit = msg_length_binary[i]
		
		if bit == '0' and not is_even(pixel):
			new = pixel[2] + 1
		elif bit == '1' and is_even(pixel):
			new = pixel[2] + 1
		else:
			new = pixel[2]

		data[i] = (pixel[0], pixel[1], new)

	return data

def write_msg(data, binary, msg_length):
	for i in range(8, (msg_length + 8)):
		pixel = data[i]
		bit = binary[(i-8)]

		if bit == '0' and not is_even(pixel):
			new = pixel[2] + 1
		elif bit == '1' and is_even(pixel):
			new = pixel[2] + 1
		else:
			new = pixel[2]

		data[i] = (pixel[0], pixel[1], new)
	return data

def pixel_to_binary(pixel):
	binary_str = ''
	if is_even(pixel):
		new = '0'
	else:
		new = '1'
	binary_str = binary_str + new

	return binary_str

def reveal_msg(data):
	msg_length_binary = ''
	for i in range(0,8):
		#print pixel_to_binary(data[i])
		msg_length_binary = msg_length_binary + pixel_to_binary(data[i])

	msg_length = int(msg_length_binary, 2)

	binary_msg = ''
	for i in range(8, (msg_length + 8)):
		pixel = data[i]
		binary = pixel_to_binary(pixel)
		binary_msg = binary_msg + binary

	chars = splitCount(binary_msg, 8)
	
	msg = ''
	for char in chars:
		msg = msg + binary_to_msg(char)

	return msg






























