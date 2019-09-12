from affixes import PhysicalDamage, AttackSpeed, AttacksHaveBleeding, WeaponRange

class TwoHandedAxe:
    pass

class VaalAxe(TwoHandedAxe):
    pass

class Unique:
    pass

class AtzirisDisfavour(Unique, VaalAxe):

    name = "Atziri's Disfavour"

    affixes = [
        PhysicalDamage(200),
        AttackSpeed(14),
        AttacksHaveBleeding(),
        WeaponRange(2)
    ]