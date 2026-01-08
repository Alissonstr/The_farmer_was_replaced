from Functions import goTo, index, wait, seguroPlantar

def start():
	posicoes = list()
	while get_pos_y() != get_world_size() - 1:
		use_item(Items.Water)
		seguroPlantar(Entities.Sunflower)
		posicoes.append(measure())
		move(North)
	use_item(Items.Water)
	seguroPlantar(Entities.Sunflower)
	posicoes.append(measure())
	i = 0
	wait(1)
	while i < len(posicoes):
		maior =  index(posicoes, max(posicoes))
		goTo(get_pos_x(), maior)
		harvest()
		posicoes[maior] = 0
		i = i + 1

def girassol():	
	i = 0
	while num_drones() < max_drones():
		goTo(i, 0)
		spawn_drone(start)	
		i += 1
girassol()