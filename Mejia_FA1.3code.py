# Create the Hero class
class Hero:

  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

  def take_damage(self, amount):
    self.hp -= amount


# Create 2 hero objects
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

# Arthur gets hit with 10 damage
arthur.take_damage(10)

# Display HP levels
print(f"{arthur.name} HP: {arthur.hp}")
print(f"{morgana.name} HP: {morgana.hp}")
