try:
	f = open("/etc/hosts", "w+")
	f.write("Succes!")
except FileNotFoundError:
	print("Data file not found")
except Exception as ex:
	print("Error appending to file: " + str(ex))
else:
	f.close()
