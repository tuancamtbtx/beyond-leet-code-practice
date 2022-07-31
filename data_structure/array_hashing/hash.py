def func_hash(value):
	return hash(value) % 100

def add_hash_table(dict, value):
	key = func_hash(value)
	dict[key] = value

