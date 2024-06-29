import time

groups = {
    "Groupe A": ["Allemagne", "Hongrie", "Ecosse", "Suisse"],
    "Groupe B": ["Espagne", "Albanie", "Croatie", "Italie"],
    "Groupe C": ["Angleterre", "Danemark", "Slovenie", "Serbie"],
    "Groupe D": ["France", "Autriche", "Pays-Bas", "Pologne"],
    "Groupe E": ["Belgique", "Roumanie", "Slovaquie", "Ukraine"],
    "Groupe F": ["Portugal", "Turquie", "République Tcheque", "Georgie"]
}

rankings = {}
ranking_thirds=  []

for group, teams in groups.items():
    print(f"\n{group}: {', '.join(teams)}")
    group_rankings = {}
    
    for team in teams:
        while True:
            print("\n",team)
            rank = int(input("\nQuel classement pour cette équipe ? "))
            if rank in group_rankings:
                print("Tu as déjà donné ce classement. Veuillez donner un autre classement.")
            elif rank > 4 or rank < 1:
                print("Ce n'est que 1 - 2 - 3 - 4")
            elif rank==3:
                ranking_thirds.append(team)
                group_rankings[rank] = team
                break
            else:
                group_rankings[rank] = team
                break
            
    rankings[group] = [group_rankings[i] for i in sorted(group_rankings.keys())]
    
"""
rankings=groups
ranking_thirds=["Ecosse","Croatie","Slovenie","Pays-Bas","Slovaquie","Republique Tcheque"]
"""

print("\nClassements:")
for group, teams in rankings.items():
    print(f"{group}: {', '.join(teams)}")

print("\nListe des équipes troisièmes :", ", ".join(ranking_thirds))
    
third_place_ranking = {}
for team in ranking_thirds:
    while True:
        print("\n", team)
        rank = int(input("\nQuel classement pour cette équipe ? "))
        if rank in third_place_ranking.values():
            print("Tu as déjà donné ce classement. Veuillez donner un autre classement.")
        elif rank > 6 or rank < 1:
            print("Le classement doit être entre 1 et 6.")
        else:
            third_place_ranking[team] = rank
            break

teams_qualified=[]
thirds=["","","","","",""]
thirds_qualified=[]
for teams in rankings.values():
    teams_qualified.extend(teams[:2])
    
for team, rank in third_place_ranking.items():
    if rank==1:
        thirds[0]=team
    elif rank==2:
        thirds[1]=team
    elif rank==3:
        thirds[2]=team
    elif rank==4:
        thirds[3]=team
    elif rank==5:
        thirds[4]=team
    elif rank==6:
        thirds[5]=team
        

print("\nClassements des équipes troisièmes :")
for i in range(6):
    print(i+1,".",thirds[i])
     
print("\nSeulement les 4 premiers sont qualifiés pour les 8emes de finale")
for i in range(4):
    teams_qualified.append(thirds[i])
    thirds_qualified.append(thirds[i])
    
time.sleep(2)

print("\nListe des équipes troisièmes qualifiés :", ", ".join(thirds_qualified))

print("\nListe des équipes qualifiés :", ", ".join(teams_qualified))

time.sleep(2)

print("\n_______________________________________________________________________")
print("\nPassons à la phase finale\nVoici les matchs:\n")

h1=[teams_qualified[1],teams_qualified[3]]
h2=[teams_qualified[0],teams_qualified[5]]
h3=[teams_qualified[4],teams_qualified[15]]
h4=[teams_qualified[2],teams_qualified[14]]
h5=[teams_qualified[7],teams_qualified[9]]
h6=[teams_qualified[10],teams_qualified[13]]
h7=[teams_qualified[8],teams_qualified[12]]
h8=[teams_qualified[6],teams_qualified[11]]
round16=[h1,h2,h3,h4,h5,h6,h7,h8]

for stage in round16:
    print(stage[0]," / ", stage[1])

for stage in round16:
    while True:
        print("\n",stage[0]," / ", stage[1])
        choice = int(input("Quelle équipe se qualifie ? (1 ou 2) "))
        if choice > 2 or choice < 1:
            print("C'est 1 ou 2")
        elif choice==1:
            stage.remove(stage[1])
            break
        elif choice==2:
            stage.remove(stage[0])
            break

print("\n_______________________________________________________________________")
print("\nMaintenant les quarts de finale !")

q1=[h4,h2]
q2=[h6,h5]
q3=[h3,h1]
q4=[h7,h8]
quarter=[q1,q2,q3,q4]

for stage in quarter:
    print(stage[0][0]," / ", stage[1][0])

for stage in quarter:
    while True:
        print("\n",stage[0][0]," / ", stage[1][0])
        choice = int(input("Quelle équipe se qualifie ? (1 ou 2) "))
        if choice > 2 or choice < 1:
            print("C'est 1 ou 2")
        elif choice==1:
            stage.remove(stage[1])
            break
        elif choice==2:
            stage.remove(stage[0])
            break
        
print("\n_______________________________________________________________________")
print("\nMaintenant les demis de finale !\n")
8
s1=[q1,q2]
s2=[q3,q4]
semi=[s1,s2]

for stage in semi:
    print(stage[0][0][0]," / ", stage[1][0][0])

for stage in semi:
    while True:
        print("\n",stage[0][0][0]," / ", stage[1][0][0])
        choice = int(input("Quelle équipe se qualifie ? (1 ou 2) "))
        if choice > 2 or choice < 1:
            print("C'est 1 ou 2")
        elif choice==1:
            stage.remove(stage[1])
            break
        elif choice==2:
            stage.remove(stage[0])
            break

print("\n_______________________________________________________________________")
print("\nMaintenant la finale !!!!\n")

while True:
    print("\n",semi[0][0][0][0]," / ", semi[1][0][0][0])
    choice = int(input("Quelle équipe sera championne d'Europe ? (1 ou 2) "))
    if choice > 2 or choice < 1:
        print("C'est 1 ou 2")
    elif choice==1:
        print("\n",semi[0][0][0][0],"est championne d'Europe !!!!")
        break
    elif choice==2:
        print("\n",semi[1][0][0][0],"est championne d'Europe !!!!")
        break
    
