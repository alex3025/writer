print("File Editor\nby alex3025")
while True:
	command = input("\nChe cosa vuoi fare? (apri/nuovo/esci): ")
	try:
		if command == "esci":
			break
		elif command == "apri":
			chs_1 = input("\nChe file vuoi aprire?: ")
			file_r = open(chs_1 + ".txt", "r")
			cont = file_r.read()
			print(cont)
			file_r.close()
		elif command == "nuovo":
			while True:
				chs_2 = input("\nCome vuoi nominare il file?: ")
				chs_3 = input("\nIl nome corrente è: " + chs_2 + ". Sei sicuro? (si/no): ")
				if chs_3 == "no":				
					chs_2 = input("\nCome vuoi rinominare il file?: ")
					chs_3 = input("\nIl nome corrente è: " + chs_2 + ". Sei sicuro? (si/no): ")
				elif chs_3 == "si":
					print("\nIl nome corrente è: " + chs_2)
					file_w = open(chs_2 + ".txt", "w")
					txt = input("\nChe cosa vuoi scrivere nel file?: ")
					file_w.write(txt)
					chs_4 = input("\nVuoi salvare? (si/no): ")
					if chs_4 == "no":
						txt = input("\nChe cosa vuoi scrivere nel file?: ")
						file_w.write(txt)
						chs_4 = input("\nVuoi salvare? (si/no): ")
					elif chs_4 == "si":
						file_W.clos()
						file_w_r = open(chs_2 + ".txt", "r")
						print("\nEcco cosa hai scritto: " + file_w_r.read())
						file_w_r.close()
						print("\nFile salvato con successo!")
				False
		else:
			print("\nComando sconosciuto!\n")
	except FileNotFoundError:
		print("\nFile non trovato!")