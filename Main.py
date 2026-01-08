from Cacto import cacto
from Abobora import abobora
from Misto import misto
from Girassol import girassol
from Functions import goTo
from Fertilizante import maze

while True:
	if num_items(Items.Hay) < 50000 or num_items(Items.Wood) < 50000 or num_items(Items.Carrot) < 50000:
		misto()
	elif num_items(Items.Power) < 5000:
		girassol()
	elif num_items(Items.Pumpkin) < 100000:
		abobora()
	elif num_items(Items.Gold) < 100000 and num_items(Items.Fertilizer) > 1000:
		maze()
	else:
	#elif num_items(Items.Cactus) < 900000:
		cacto()