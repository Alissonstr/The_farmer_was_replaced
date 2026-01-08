from Functions import goTo, seguroPlantar

def ordenaX():
	while True:
		posicoes = []
		while get_pos_x() != get_world_size() - 1:
			posicoes.append(measure())
			move(East)
		posicoes.append(measure())
		while posicoes:
			maior = max(posicoes)

			while measure() != maior:
				move(West)

			while get_pos_x() < len(posicoes) - 1:
				swap(East)
				move(East)
			posicoes.remove(maior)

			while get_pos_x() > len(posicoes) - 1 and get_pos_x() > 0:
				move(West)

		if get_pos_y() == get_world_size() - 1:
			harvest()
			break
		move(North)
			
def ordenaY():
	while True:
		posicoes = []
		while get_pos_y() != get_world_size() - 1:
			seguroPlantar(Entities.Cactus)
			posicoes.append(measure())
			move(North)
		seguroPlantar(Entities.Cactus)
		posicoes.append(measure())
		while posicoes:
			maior = max(posicoes)

			while measure() != maior:
				move(South)

			while get_pos_y() < len(posicoes) - 1:
				swap(North)
				move(North)
			posicoes.remove(maior)

			while get_pos_y() > len(posicoes) - 1 and get_pos_y() > 0:
				move(South)

		if get_pos_x() == get_world_size() - 1:
			goTo(0, 0)
			ordenaX()
			break
		move(East)
			
def cacto():
	goTo(0, 0)
	ordenaY()