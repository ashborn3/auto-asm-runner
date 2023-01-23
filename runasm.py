from os import system,listdir

dir = listdir()

for i in dir:
	l = len(i) - 1
	if i[(l-3):] == ".asm" :
		file = i[:(l-3)]

print(f"Compiling and linking {file}.asm")

system(f"nasm -f elf64 {file}.asm")

system(f"ld {file}.o -o {file}.out")

print("OUTPUT :")

system(f"./{file}.out")

