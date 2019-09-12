class Affix:
    
    values = {}
    tier = 0

    def get_values(self):
        return self.values

class SimpleValueAffix(Affix):
    self.value_name = ''

    def __init__(self, value):
        self.values[self.value_name] = value
    
    def get_value(self):
        return self.values.get(self.value_name)

class WeaponBaseAffix(SimpleValueAffix):

    def attach(self):
        id = self.weapon.register_multiplier(
            self.attribute,
            self.get_value
            )
        self.id = id

    def detach(self):
        self.weapon.remove_multiplier(id)

class PhysicalDamage(WeaponBaseAffix):

    value_name = 'phys_dmg'
    base_attribute = 'physical_damage' 

class AttackSpeed(WeaponBaseAffix):

    value_name = 'attack_speed'
    base_attribute = 'attack_speed'

class WeaponRange(WeaponBaseAffix):

    value_name = 'weapon_range'
    base_attribute = 'weapon_range'

class AttacksHaveBleeding(Affix):

    def calculation(self):
        self.character.bleeding_chance = 100

