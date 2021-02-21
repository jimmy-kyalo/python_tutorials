#modifying a list in a function
"""
unprinted_designs = ['case', 'pendant', 'sphere']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print("\nPrinting model: " + current_design)
	completed_models.append(current_design)

print("\nThe printed models are: ")
for completed_model in sorted(completed_models):
	print(completed_model.title())
"""

#------------------------------------------------
#             ALTERNATIVE

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("\nPrinting model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe printed models are: ")
	for completed_model in sorted(completed_models):
		print(completed_model.title())

unprinted_designs = ['case', 'pendant', 'sphere']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
