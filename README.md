found = False
card = drawCard()
while not found:
  if card == 0:
    card = drawCard()
  else:
    found = True
  
