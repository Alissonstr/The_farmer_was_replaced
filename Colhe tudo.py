tamanho = get_world_size()

def eTill():
	return get_ground_type() != Grounds.Soil

while True:
	for i in range(tamanho): 	
		harvest()

		if eTill():
			till()
		
		if get_pos_y() == tamanho-1:
			move(East)	
		move(North)