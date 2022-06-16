import random
dob=input("Enter DOB as dd/mm/yyyy:")
my_dob="17/12/2002"
l1=['Nice DOB!','You are Amazing!','WOW!','YOU ARE THE GOAT!']
l2=['That sucks!',"That's Dumb",'WHat da Hell??!!','BOOOORINGGG!!!!!!']
if dob==my_dob:
    print(random.choice(l1))
else:
    print(random.choice(l2))
