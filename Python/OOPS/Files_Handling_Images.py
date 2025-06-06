#Basically Copy the Image_1 to Image_02
F1 = open("Files/Image_1.jpg", "rb")
F2 = open("Files/Image_2.jpg", "wb")
for i in F1:
    F2.write(i)
F1.read()



