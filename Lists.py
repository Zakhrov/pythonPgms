friends=["aki","ron","arti","mona","papu"]
lucky_num=[1,2,3,5,4]
friends[0]="agi"
#??????????
print(friends[2:3])
print(friends[0])
friends.extend(lucky_num)
friends.append("mom")
print(friends)
friends.insert(1,"dad")
print(friends)
friends.pop()
print(friends)
print(friends.count("ron"))
# asc order- friends.sort()- for this int and str should not be together
#list.reverse
luckynum_copy=lucky_num.copy()
luckynum_copy.sort()
print(luckynum_copy)



