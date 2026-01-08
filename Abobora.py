from Functions import reset, goTo, wait, seguroPlantar

posicao = []
plantar = True
tamanho = get_world_size() - 1

def scan():
	if get_entity_type() != Entities.Pumpkin:
		x, y = get_pos_x(), get_pos_y()
		nova_pos = x, y
		if nova_pos not in posicao:
			posicao.append((x, y))			
		seguroPlantar(Entities.Pumpkin)

def abobora():
	goTo(0, 0)
	while True:
		seguroPlantar(Entities.Pumpkin)
		if (get_pos_x() == tamanho) and (get_pos_y() == 1):
			move(direcao)
			seguroPlantar(Entities.Pumpkin)
			reset()
			break
		if (get_pos_y() == tamanho):
			direcao = South
		elif (get_pos_y() == 0):
			direcao = North
		move(direcao)
		if get_pos_y() == tamanho or get_pos_y() == 0:
			seguroPlantar(Entities.Pumpkin)
			move(East)
	
	while True:
		scan()
			
		if (get_pos_x() == tamanho) and (get_pos_y() == 1):
			move(direcao)
			scan()
			reset()
			break
		if (get_pos_y() == tamanho):
			direcao = South
		elif (get_pos_y() == 0):
			direcao = North
		move(direcao)
		if get_pos_y() == tamanho or get_pos_y() == 0:
			scan()
			move(East)
			
	n = len(posicao)
	#for i in range(n):
	#	for j in range(i+1, n):
	#		xi, yi = posicao[i]
	#		xj, yj = posicao[j]
	#					
	#	if yi > yj or (yi == yj and xi > xj):
	#		posicao[i], posicao[j] = posicao[j], posicao[i]
					
	while posicao:
		for x, y in posicao:
			goTo(x, y)
			if get_entity_type() == Entities.Pumpkin:
				posicao.remove((x, y))
			seguroPlantar(Entities.Pumpkin)
	wait(3)
	harvest()