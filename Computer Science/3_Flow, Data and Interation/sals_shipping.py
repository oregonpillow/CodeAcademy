def ground_cost(weight):
  cost = 20.00
  if weight <= 2:
    cost += (1.50*weight)
  elif weight > 2 and weight <= 6:
    cost += (3.00*weight)
  elif weight > 6 and weight <= 10:
    cost += (4.00*weight)
  elif weight > 10:
    cost += (4.75*weight)
  return cost

  prem_ground = 125.00
  
  def drone_cost(weight):
    cost = 0.00
    if weight <= 2:
      cost += (4.50*weight)
    elif weight > 2 and weight <= 6:
      cost += (9.00*weight)
    elif weight > 6 and weight <= 10:
      cost += (12.00*weight)
    elif weight > 10:
      cost += (14.25*weight)
    return cost
  
  def sal_cost(weight):
  all_opts = (ground_cost(weight), prem_ground, drone_cost(weight))
  lowest = min(all_opts)
  if ground_cost(weight) == lowest:
    return "Ground Shipping is cheapest", lowest
  elif prem_ground == lowest:
    return "Premium Ground Shipping is cheapest", lowest
  elif drone_cost(weight) == lowest:
    return "Drone Shipping is cheapest", lowest