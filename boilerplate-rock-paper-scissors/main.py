# Para ejecutar las pruebas automáticamente
# from test_module import test
# test()
from RPS_game import play
from RPS import player
from RPS_game import quincy  # Un bot que ya está en el repositorio

# Jugar 1000 partidas y ver los resultados
play(player, quincy, 1000, verbose=True)


