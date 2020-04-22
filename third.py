T = int(input())
L = []
W = []
Map = []
for j in range(T):
  size = [int(i) for i in input().split(' ')]
  L.append(size[0])
  W.append(size[1])
  m = []
  for row in range(size[1]):
    m.append(input())
  Map.append(m)
  
def cal_res_num(l,w,map):
  res_pos = []
  mech_pos = []
  free_pos = []
  flag_mat = []
  dest_num = 0
  for r in range(w):
    col = []
    for c in range(l):
      col.append(0)
      if map[r][c] == 'G':
        godz_pos = [r,c]
      elif map[r][c] == 'M':
        mech_pos.append([r,c])
      elif map[r][c] == 'R':
        res_pos.append([r,c])
      else:
        free_pos.append([r,c])
    flag_mat.append(col)
  return calc_dest(godz_pos,res_pos,mech_pos,free_pos,flag_mat,dest_num,l,w)

def adjacent(l,w,r,c):
  adj = []
  if (r-1)>=0:
    adj.append([r-1, c])
  if (c+1)<l:
    adj.append([r, c+1])
  if (r+1)<w:
    adj.append([r+1, c])
  if (c-1)>=0:
    adj.append([r, c-1])
  return adj

def target(l, w, r, c, free_pos):
  target = []
  r1 = r
  while(r1>0):
    r1 = r1 - 1
    target.append([r1,c])
    if [r1,c] not in free_pos:
      break
  r2 = r
  while(r2<(w-1)):
    r2 = r2 + 1
    target.append([r2,c])
    if [r2,c] not in free_pos:
      break
  c1 = c
  while(c1>0):
    c1 = c1 - 1
    target.append([r,c1])
    if [r,c1] not in free_pos:
      break
  c2 = c
  while(c2<(l-1)):
    c2 = c2 + 1
    target.append([r,c2])
    if [r,c2] not in free_pos:
      break
  return target

def calc_dest(godz_pos,res_pos,mech_pos,free_pos,flag_mat,dest_num,l,w):
 
  # calculate the next position of the godz
  next_pos = [-1, -1]
  for pos in adjacent(l,w,godz_pos[0],godz_pos[1]):
    #print(godz_pos,'-',adjacent(l,w,godz_pos[0],godz_pos[1]),'-',res_pos)
    if pos in res_pos:
      next_pos = pos.copy()
      dest_num = dest_num + 1
      res_pos.remove(pos)
      free_pos.append(pos)
      flag_mat[godz_pos[0]][godz_pos[1]] = 1
      break
  if next_pos[0] == -1:
    for pos in adjacent(l,w,godz_pos[0],godz_pos[1]):
      if flag_mat[pos[0]][pos[1]] == 0:
        next_pos = pos.copy()
        flag_mat[godz_pos[0]][godz_pos[1]] = 1
        break
  elif next_pos[0] == -1:
    next_pos = godz_pos.copy()
  # the exit condition of this recursion function
  for mech in mech_pos:
    if next_pos in target(l,w,mech[0],mech[1],free_pos):
      return dest_num
      break
  cand = []
  cand1 = []
  for mech in mech_pos:
    for pos in adjacent(l,w,mech[0],mech[1]):
      #print(next_pos,'-',mech, target(l,w,pos[0],pos[1],free_pos),'-', dest_num)
      if next_pos in target(l,w,pos[0],pos[1],free_pos):
        if next_pos in res_pos:
          return (dest_num + 1)
        else:
          return dest_num
 
  # recursion part
      else:
        mech_pos.remove(mech)
        adj = adjacent(l,w,mech[0],mech[1])
        #adj.append(mech)
        for pos in adj:
          mech_pos.append(pos)
          if pos in res_pos:
            res_pos.remove(pos)
            free_pos.append(pos)
            dest_num = dest_num + 1
          #print(next_pos,res_pos,new_pos,flag_mat,dest_num)
          #print(godz_pos, next_pos)
          cand1.append(calc_dest(next_pos,res_pos,mech_pos,free_pos,flag_mat,dest_num,l,w))
        #print(cand1)
        return(min(cand1))
  

for test in range(T):
  print(cal_res_num(L[test],W[test],Map[test]))