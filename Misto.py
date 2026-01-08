tamanho = get_world_size()

def misto():
	for i in range(tamanho): 				
		if num_items(Items.hay) < 50000:
			plant(Entities.Grass)
		elif num_items(Items.Wood) < num_items(Items.Carrot):
			if (get_pos_x()+get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
			else:
				#if get_ground_type() != Grounds.Soil:
					#till()
				plant(Entities.Carrot)
		else:
			#if get_ground_type() != Grounds.Soil:
				#till()
			plant(Entities.Carrot)	
				
		if get_pos_y() == tamanho-1:
			move(East)
		move(North)
		harvest()