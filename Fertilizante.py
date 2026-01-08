from Functions import seguroPlantar, index

direcoes = (North, East, South, West)

def fertilizante():
	plant(Entities.Grass)
	use_item(Items.Fertilizer)
	harvest()

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
	if num_items(Items.Weird_Substance) < 20000:
		if num_items(Items.Fertilizer) < 1000:
			return -1
		fertilizante()
	seguroPlantar(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
	for direcao in direcoes:
		if explore(direcao):
			break