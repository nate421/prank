import os

def rename_files():

     file_list = os.listdir("./files")
    #  print(file_list)
     saved_path = os.getcwd()
     print("Current Working Directory is "+ saved_path)

    #  for file_name in file_list:
    #      os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
