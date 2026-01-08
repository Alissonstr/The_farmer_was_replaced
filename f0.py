from Functions import index, seguroPlantar

direcoes = (North, East, South, West)

def direcaoOposta(direcao):
	return direcoes[(index(direcoes, direcao) + 2) % len(direcoes)]
		
def explore(direcao):
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	if not move(direcao):
		return False
	for explora_direcao in direcoes:
		if direcaoOposta(explora_direcao) == direcao:
			continue
		if explore(explora_direcao):
			return True
	move(direcaoOposta(direcao))
			
def maze():
	seguroPlantar(Entities.Bush)
	substance = get_world_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
	for direcao in direcoes:
		if explore(direcao):
			break