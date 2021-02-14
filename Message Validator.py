def is_a_valid_message(message=""):
	# mess = message.split(int)
	# isvalue = [int(i) for i in str(message)]
	temp = ''
	value = 0
	adaberapaint = 0
	oke = 0
	beneratautidak = False
	length = 0
	adadouble = None
	print(len(message))

	if message == '':
		return True
	if not message[0].isdecimal():
		return False
	print(message)
	for i in message:
		# print("ke -",length,"'",i,"'",)
		length += 1
		if i.isnumeric():
			# print(i)
			try:
				kedua = str(i) + message[length]
			except:
				kedua = "salahk"
			# print(i)
			if kedua.isnumeric():
				adadouble = True
				value = int(kedua) 
				print(value)
				adaberapaint+=1
			elif adadouble:	
				adadouble = False
				# print("ada double")
				continue
			else:
				# print(i)
				value = int(i)
				# print(value)
				adaberapaint +=1
					# print("ada int")

		else:
			temp += i

		if len(temp) == value:
			print("sama gak",len(temp),value)
			# print(message[length].isdecimal())
			try:
				# print(message[length])
				if not message[length].isnumeric():
					break
					# print("kalau dah selesai ada number lagi gak")
					# print(oke)
			except:
				pass
			temp = ''
			oke +=1
			# print(oke)
	if adaberapaint == oke:
		print("+ada int ",adaberapaint," dan ada ",oke, " yang betul")
		# print("okebanget" )
		beneratautidak = True
	else:
		beneratautidak = False

	# if message == "code4hello5":
	# 	return False

	# print("=====================")
	return beneratautidak

# print(is_a_valid_message("18BIDGEUBNDGAPYAST16NEFQPUBCKQHPEPMYKG"),False)
# print("masalah di selesaikan ")






def is_a_valid_message(message=""):
	temp = ''
	value = 0
	adaberapaint = 0
	oke = 0
	beneratautidak = False
	length = 0
	adadouble = None
	if message == '':
		return True
	if not message[0].isdecimal():
		return False
	for i in message:
		length += 1
		if i.isnumeric():
			try:
				kedua = str(i) + message[length]
			except:
				kedua = "salahk"
			if kedua.isnumeric():
				adadouble = True
				value = int(kedua) 
				adaberapaint+=1
			elif adadouble:	
				adadouble = False
				continue
			else:
				value = int(i)
				adaberapaint +=1
		else:
			temp += i
		if len(temp) == value:
			try:
				if not message[length].isnumeric():
					break
			except:
				pass
			temp = ''
			oke +=1
	if adaberapaint == oke:
		beneratautidak = True
	else:
		beneratautidak = False
	return beneratautidak


print(is_a_valid_message("12ssssssssssss3sss4ssss"))
print("masalah di selesaikan ")
