ranked = [1,2,3,5,2,2,4,5,2,5]
ranked = sorted(list(set(ranked)), reverse=True)
#set of ranked, list of set, reverse sort on list = [5, 4, 3, 2, 1]

ranked1 = [1,2,3,5,2,2,4,5,2,5]
ranked1 = sorted(list(ranked1), reverse=True)
#list of ranked, reverse sort on list = [5, 5, 5, 4, 3, 2, 2, 2, 2, 1]

ranked2 = [1,2,3,5,2,2,4,5,2,5]
ranked2 = sorted(set(ranked2), reverse=True)
#set of ranked, sort of set (same as 1st) = [5, 4, 3, 2, 1]

ranked3 = [1,2,3,5,2,2,4,5,2,5]
ranked3 = list(set(ranked3))
#set of ranked, list of set (no sorted but is sorted) = [5, 4, 3, 2, 1]

print(ranked)
print(ranked1)
print(ranked2)
print(ranked3)

player = sorted([2,4,3,9,6,5,1,8,7], reverse=True)
print(player)
