def build_profile(first, last, **user_info):#double ** create empty dict
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for k,v in user_info.items():
		profile[k] = v
	return profile

user_profile = build_profile('jimmy', 'kyalo',location='ruaka',field='IT')
print(user_profile)
