tamanho = get_world_size()

while True:
	for i in range(tamanho): 
		
		#if get_water() < .1:
		#use_item(Items.Water)
				
		plant(Entities.Cactus)
		if get_pos_y() == tamanho-1:
			move(East)	
		move(North)