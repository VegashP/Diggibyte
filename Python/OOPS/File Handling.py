
F1 = open("Files/File_01.txt","x") # TO CREATE A FILE
F2 = open("Files/File_01.txt","r") # To Read the Content from the Beginning
F3 = open("Files/File_01.txt","w") # Write from Beginning
F4 = open("Files/File_01.txt","r+") # Used to Read and Write but Read First then Write (Recommanded)
F5 = open("Files/File_01.txt","w+") # Used to Read and Write but Write First then Read  (Recommanded)

F4.tell() # Shows Where Its Pointing like Index Values
F4.seek() # Making the pointer to point on Beginning

