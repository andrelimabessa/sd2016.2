"""
	AGUA = 'A'
	NAVIO = 'N'
	ABATIDO ='B'

	def init_tab(self):
		self.matrix = [[self.AGUA for i in range(5)] for j in range(5)]

	def print_tab(self):
		print(self.matrix)

	def set_navios(self,x,y):
		self.matrix[x][y] = self.NAVIO

	def jogada(self, x, y):
		if self.matrix[x][y] == self.NAVIO:
			self.matrix[x][y] = self.ABATIDO
			print("Navio abatido")
		else:
			print('Água')
		print(self.matrix)

b = buttleship()
b.init_tab()
#b.print_tab()
b.set_navios(0,0)
b.set_navios(3,3)
b.jogada(1,2)
b.print_tab()
b.jogada(3,3)
b.print_tab()
"""
