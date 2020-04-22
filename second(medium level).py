num = [int(i) for i in input().split(' ')]
N = num[0]
M = num[1]
relations = []
candidates = []
childs = []
founder = input()
for i in range(N):
  names = [name for name in input().split(' ')]
  childs.append(names[0])
  relations.append(names)
for i in range(M):
  candidates.append(input())

def calc_vein(name):
  if name not in childs:
    return 0
  else:
    ind = childs.index(name)
    if founder == relations[ind][1]:
      return (0.5 + 0.5 * calc_vein(relations[ind][2]))
    elif founder == relations[ind][2]:
      return (0.5 + 0.5 * calc_vein(relations[ind][1])) 
    else:
      return (calc_vein(relations[ind][1])+calc_vein(relations[ind][2]))*0.5
amount = 0
n = -1
cand_ind = -1
for candidate in candidates:
  n = n + 1
  if amount < calc_vein(candidate):
    amount = calc_vein(candidate)
    cand_ind = n
print(candidates[cand_ind])

