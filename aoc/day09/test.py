from pathlib import Path

path = Path(__file__).parent.resolve()
t = [('UDLR'.index(d),int(n))for d,n in(l.strip().split()for l in open(path / "./resources/input.txt"))]

def mv(d,k,h): # move in direction d, in knots k, head h, tail is always next
  if h==0: k[h][0]+=(0,0,-1,1)[d]; k[h][1]+=(-1,1,0,0)[d]
  t = h+1; d0 = k[h][0]-k[t][0]; d1 = k[h][1]-k[t][1] # tail, dx, dy
  if abs(d0)>1: k[t][0]+=d0//abs(d0); k[t][1]+=(d1!=0)*d1//max(abs(d1),1)
  elif abs(d1)>1: k[t][1]+=d1//abs(d1); k[t][0]+=(d0!=0)*d0//max(abs(d0),1)

def solve(m): # solve for m knot rope
  k = [[0,0] for _ in range(m)] # knots: h,1,2,...,m-1
  v = {(k[-1][0],k[-1][1])} # visited coords
  for d,n in t: # d - direction 0..3 (UDLR), n - steps, int
    for i in range(n): # repeat in the same direction
      for j in range(len(k)-1): mv(d,k,j)
      v.add((k[-1][0],k[-1][1]))

  return len(v)

print(solve(2), solve(10))