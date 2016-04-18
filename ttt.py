import PySide
from Board import Board

def main():
	print("Welcome to python game!!!");
	b = Board("X","Y")
	print(b.getBoard())
	while  b.win() != True:	
		print("Next player: "+str(b.getNextPlayer()))
		nextMove=eval(input("Posicao?"))
		while not b.isValidPlay(nextMove):
			nextMove=eval(input("Posicao?"))
		b.play(nextMove)
		print(b.getBoard())
	print("Player: "+b.getNextPlayer()+" won!")


main()
