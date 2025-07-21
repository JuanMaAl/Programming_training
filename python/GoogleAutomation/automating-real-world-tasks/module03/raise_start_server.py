def start_server(port):
	if not isinstance(port, int):
		raise TypeError("Port number must be an integer")
	elif port < 1024 or port > 65535:
		raise ValueError("Port number is invalid")
