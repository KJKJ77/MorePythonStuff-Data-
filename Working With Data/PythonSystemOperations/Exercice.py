import io
ch="Learning python and data analysis"
file = io.StringIO(ch)
print(file.read())
print(file.write(" Master the Data handeling concepts"))
file.seek(0)
print(file.read())

