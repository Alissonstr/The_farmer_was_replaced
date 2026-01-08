def reset():
	while (get_pos_y() != 0):
		move(South)
	while (get_pos_x() != 0):
		move(West)  

def goTo(x, y):
	while (x !=get_pos_x()):
		if x > get_pos_x():
			move(East)
		else:
			move(West)
	while (y !=get_pos_y()):
		if y > get_pos_y():
			move(North)
		else:
			move(South)
			
def index(lista, valor):
	i = 0
	while i < len(lista):
		if lista[i] == valor:
			return i
		i = i + 1
	return -1

def wait(tempo):
	i = 0
	while i < tempo:
		do_a_flip()
		i = i + 1

def seguroPlantar(planta):
	if get_entity_type() != planta:
		harvest()
	if get_ground_type() != Grounds.Soil:
			till()
	plant(planta)