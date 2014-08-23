from tealight.logo import move, turn

def spiral(size):
  
  if size > 100:
    return
  
  move(size)
  turn(180)
  spiral(size + 8)
  
spiral(0)