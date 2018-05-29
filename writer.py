print("Writer\nby alex3025")
def open_file():
	while True:
		try:
			filename_read = input("\nChe file vuoi aprire?: ")
			file_r = open(filename_read + ".txt", "r")
			print("\n" + file_r.read() + "\n")
			file_r.close()
		except FileNotFoundError:
			print("\nNome file errato!")
def new_file():
	filename_write = input("\nChe nome vuoi dare al nuovo file?: ")
	while True:
		try:
			confirm = input("\nIl nome sarà: " + filename_write + "\n\nSei sicuro? (si/no): ")
			if confirm == "si":
				file_w = open(filename_write + ".txt", "w")
				text = input("\nChe cosa vuoi scrivere nel file?: ")
				file_w.write(text)
				confirm_2 = input("\nVuoi salvare? (si/no): ")
				if confirm_2 == "no":
					print("\nIl testo non è stato salvato!\n")
					break
				elif confirm_2 == "si":
					file_w.close()
					print(" ")
					break
			elif confirm == "no":
				filename_write = input("\nCome vuoi rinominare il file?: ")
		except:
			print("\nErrore!")
while True:
	try:
		menu = input("\nChe cosa vuoi fare? (apri/nuovo/esci): ")
		if menu == "esci":
			break
		elif menu == "apri":
			open_file()
		elif menu == "nuovo":
			new_file()
	except:
		print("\nErrore!")
