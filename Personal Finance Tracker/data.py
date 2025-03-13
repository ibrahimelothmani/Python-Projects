np=input("donner son nom et prenom:")
l=len(np)
espace=np.find(" ")
prenom=np[espace+1:l]
print("bienvenue,",prenom)
