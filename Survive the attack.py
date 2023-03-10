def is_defended(attackers, defenders):
    winner_list=[]
    for a in attackers:
        for d in defenders:
            if a<d:
                winner_list.append(1)
            else:
                winner_list.append(-1)
        if sum(winner_list)>0:
            return True
            if sum(winner_list)<0:
                return False

print(is_defended([1,3,4,5,1,2,5],[2,4,5]))
