from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
def main():
	root=Tk().withdraw()
	in_path=askopenfilename()
	print(in_path)

if __name__ == "__main__":
	main()	