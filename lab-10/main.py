from camera import  Camera


def main():
	
	nikon = Camera('4k', '512gb', 15, 'Japan', 23500, 'black', 'Nikon d3100', 24)
	canon = Camera('4k', '256gb', 12, 'Japan', 27500, 'green', 'Canon EOS 850D', 26)
	sony = Camera('4k', '256gb', 14, 'Japan', 28350, 'black', 'Sony A7 III', 24)

	cameras = [nikon, canon, sony]

	for count_of_object in cameras:
		print(count_of_object)

if __name__ == "__main__":
    main()