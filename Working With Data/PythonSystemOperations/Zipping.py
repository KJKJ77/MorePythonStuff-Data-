
new_file = open("to_zip.txt","w+")
new_file.write("This is demo 1")
new_file.close()

new_file = open("to_zip2.txt","w+")
new_file.write("This is demo 2")
new_file.close()

import zipfile

compress=zipfile.ZipFile("zipped.zip","w")
compress2=zipfile.ZipFile("zipped2.zip","w")

compress.write("to_zip.txt", compress_type= zipfile.ZIP_DEFLATED)
compress2.write("to_zip2.txt", compress_type= zipfile.ZIP_DEFLATED)

compress.close()  # Important Step
compress2.close()  # Important Step

extraction = zipfile.ZipFile("zipped.zip","r")
extraction.extractall("This is your extracted content")