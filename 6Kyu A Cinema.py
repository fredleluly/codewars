def cinema(b, g):
	import re
	sitDown = ""
	# boy = ["B" for i in range(b)]
	# girl = ["G" for i in range(g)]
	boy = ''.join(["B" for i in range(b+g)])
	girl = ''.join(["G" for i in range(g+b)])
	if b > g:
		# for i in range(len(girl)):

		boy = re.sub(r"BB","BG",boy,len(girl))
	if g > b:
		# for i in range(len(boy)):

		girl = re.sub(r"GG","BG",boy,len(girl))
	print(boy)
	print(girl)
	# print("sitDown : ",sitDown)
	# print(''.join(boy))
	# print(''.join(girl))
	print(len(boy))
	print(len(girl))
	print(" ")
	print(boy == "BGBGBBGB")
	print(boy == "BGBBGBBG")
	print(boy == "BGBBGBGB")

def cinema(b, g):
    print(b,g)
    sitDown = ""
    ganti = True
    boy = ["B" for i in range(b)]
    girl = ["G" for i in range(g)]
#     boy = ["B" for i in range(b)]
#     girl = ''.join(["G" for i in range(g)])
    if len(girl) > len(boy):
        try:
            for i in range(1,len(girl)):
                # print(girl[i-1])
                if girl[i-1] == "G":
                    print(girl[i])
                    girl[i] = "BG"
                    boy.pop()
                if i == len(girl)-1 and boy != []:
                    boy.pop()
                    girl.append("B")
            jadi = ''.join(girl)
            if jadi[-1] == "G":
                try:
                    if jadi[-2] == "G":
                        return None
                except:
                    pass
            print("jadi : ",jadi)
            return jadi
        except:
            return None
    if len(boy) > len(girl):
        try:
            for i in range(1,len(boy)):
                # print(boy[i-1])
                if boy[i-1] == "B":
                    print(boy[i])
                    boy[i] = "GB"
                    girl.pop()
                if i == len(boy)-1 and girl != []:
                    girl.pop()
                    boy.append("G")
            jadi = ''.join(boy)
            if jadi[-1] == "B":
                try:
                    if jadi[-2] == "B":
                        return None
                except:
                    pass
            print("jadi : ",jadi)
            return jadi
        except:
            return None
    else:
        ganti = True 
        for i in range(b+g):
            if ganti:
                sitDown += "B"
                ganti = False
            else:
                sitDown+= "G"
                ganti = True
        jadi = sitDown
        print("jadi : ",jadi)
        return sitDown
print(cinema(5,3))