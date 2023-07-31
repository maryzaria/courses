import sys


pokemons = [name.strip() for name in sys.stdin]
print(len(pokemons) - len(set(pokemons)))