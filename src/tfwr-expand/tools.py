def has_item(item):
	return num_items(item) > 0

def cost_enough(entity, level=None, scale=1.0):
	cost = get_cost(entity, level)

	if cost is None:
		return True
	
	for item in cost:
		if num_items(item) < cost[item] * scale:
			return False
	return True
