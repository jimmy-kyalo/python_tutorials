#users that need to be verified
unconfirmed_users = ['john', 'jimmy', 'ann']
#empty list to hold verified users
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Veryfying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nConfirmed users:")
for confirmed_user in confirmed_users:
	print("\t" + confirmed_user.title())