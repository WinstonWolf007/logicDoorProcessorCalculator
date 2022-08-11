from package2 import Binary

b1 = list(map(int, list(input('bin 1> '))))
b2 = list(map(int, list(input('bin 2> '))))


bins = Binary(b1, b2)
bins.exe()
bins.log()