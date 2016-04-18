class Board:
	board=[[" "," "," ",],[" "," "," "],[" "," "," "]]; 
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.currentPlayer=p1
		self.nextPlayer=p2

	#Dummy algorithm. Change this please...
	def getBoard(self):
		s=""
		for i in self.board :
			if isinstance(i,list):
				for j in i:
					s+=j
					s+="|"
				s+="\n -----"
			else:
				s+=j
			s+="\n"
		return s

	def play(self,play):
		if( not self.isValidPlay(play)):
			return False
		aux=self.currentPlayer
		self.board[self.getLine(play)][self.getCol(play)]=self.currentPlayer
		self.currentPlayer=self.nextPlayer
		self.nextPlayer=aux
	def getNextPlayer(self):
		return self.nextPlayer
	def getLine(self,play):
		count=0
		while play-3 >= 0:
			play=play-3
			count=count+1
		return count
	def getCol(self,play):
		return play%3

	def win(self):
		if( not self.checkCol() and not self.checkLine() and not self.checkDiag()):
			return False
		return True
	def checkLine(self):
		for i in self.board:
			if i[0]==i[1]==i[2] and i[0]!=" ":
				return True
		return False
	def checkCol(self):
		for i in range(len(self.board)):
			if self.board[0][i]==self.board[1][i]==self.board[2][i] and self.board[0][i]!=" ":
				return True
		return False
	def checkDiag(self):
		if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][0]!=" ":
			return True
		if self.board[2][0]==self.board[1][1]==self.board[0][2] and self.board[2][0]!=" ":
			return True
		else:
			return False

	def isValidPlay(self,play):
		if play>=0 and play<=8 and self.board[self.getLine(play)][self.getCol(play)]==" ":
			return True
		else:
			return False
