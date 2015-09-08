class GameObject(object):
    def __init__(self, spec):
        self.spec = spec
        self.name = spec.get('name', '')
        self.description = spec.get('description', "")


class SluggedObject(GameObject):
    def __init__(self, slug, spec):
        super(SluggedObject, self).__init__(spec)
        self.slug = slug


DamageTypes = {}
# bludgeoning 0
# slashing 1
# piercing 2
# burning 1
# freezing 2
# shocking 3
# arcane 0
# holy 1
# dark 3


class DamageType(SluggedObject):
    def __init__(self, slug, spec):
        super(DamageType, self).__init__(slug, spec)
        self.piercing = spec.get('piercing', 0)
        DamageTypes[slug] = self


WeaponSpecials = {}


class WeaponSpecial(SluggedObject):
    def __init__(self, slug, spec):
        super(WeaponSpecial, self).__init__(slug, spec)
        WeaponSpecials[slug] = self


Feats = {}


class Feat(SluggedObject):
    def __init__(self, slug, spec):
        super(Feat, self).__init__(slug, spec)
        Feats[slug] = self


Equipments = {}


class Equipment(SluggedObject):
    def __init__(self, slug, spec):
        super(Equipment, self).__init__(slug, spec)
        self.cost = spec.get('cost')
        self.required_feat = Feats.get(spec.get('required_feat'))

        Equipments[slug] = self


Weapons = {}


class Weapon(Equipment):
    def __init__(self, slug, spec):
        super(Weapon, self).__init__(slug, spec)
        self.attack_range = spec.get('range', 1)
        self.damage = spec.get('damage', 1)
        self.rate = spec.get('rate', 1)
        self.damage_type = DamageTypes.get(spec.get('type'))

        special_slugs = spec.get('specials', [])
        self.special = []
        for special in special_slugs:
            self.special.append(WeaponSpecial.get(special))

        Weapons[slug] = self


Outfits = {}


class Outfit(Equipment):
    def __init__(self, slug, spec):
        super(Outfit, self).__init__(slug, spec)
        self.armour = spec.get('armour')
        self.defense = spec.get('defense')

        abilities = spec.get('abilities', {})
        self.abilities = {}
        for ability in abilities:
            # ability: int
            self.abilities[ability] = abilities[ability]

        feats = spec.get('feats', [])
        self.feats = {}
        for feat in feats:
            self.feats[feat] = Feats.get('feat')

        Outfits[slug] = self


Mounts = {}


class Mount(Equipment):
    def __init__(self, slug, spec):
        super(Equipment, self).__init__(slug, spec)
        self.speed = spec.get('speed')
        self.hp = spec.get('hp')

        Mounts[slug] = self


Items = {}


class Item(Equipment):
    def __init__(self, slug, spec):
        super(Equipment, self).__init__(slug, spec)

        self.defense = spec.get('defense')

        abilities = spec.get('abilities', {})
        self.abilities = {}
        for ability in abilities:
            # ability: int
            self.abilities[ability] = abilities[ability]

        feats = spec.get('feats', [])
        self.feats = {}
        for feat in feats:
            self.feats[feat] = Feats.get('feat')

        Items[slug] = self


class Template(SluggedObject):
    def __init__(self, slug, spec):
        super(Template, self).__init__(slug, spec)

        abilities = spec.get('abilities', {})
        self.abilities = {}
        for ability in abilities:
            # ability: int
            self.abilities[ability] = abilities[ability]

        feats = spec.get('feats', [])
        self.feats = {}
        for feat in feats:
            self.feats[feat] = Feats.get('feat')


Races = {}


class Race(Template):
    def __init__(self, slug, spec):
        super(Class, self).__init__(slug, spec)
        self.base_speed = spec.get('base_speed')
        self.base_hp = spec.get('base_hp')
        self.base_strength = spec.get('base_strength')
        self.base_agility = spec.get('base_agility')
        self.base_constitution = spec.get('base_constitution')
        self.base_intelligence = spec.get('base_intelligence')
        self.base_wisdom = spec.get('base_wisdom')
        self.base_charisma = spec.get('base_charisma')

Classes = {}


class Class(Template):
    def __init__(self, slug, spec):
        super(Class, self).__init__(slug, spec)
        self.hp_per_level = spec.get('hp_per_level', 3)
        self.levels_per_bab = spec.get('levels_per_bab', 3)

        self.weapon = Weapons.get(spec.get('weapon'))
        self.sidearm = Weapons.get(spec.get('sidearm'))
        self.outfit = Outfits.get(spec.get('outfit'))
        self.mount = Mounts.get(spec.get('mount'))
        self.item1 = Items.get(spec.get('item1'))
        self.item2 = Items.get(spec.get('item2'))
        self.equipment = [self.weapon, self.sidearm, self.outfit, self.mount,
                          self.item1, self.item2]

        upgrades = spec.get('upgrades', [])
        self.upgrades = {}
        for upgrade in upgrades:
            # {class: class_slug, level_requirement: int, cost: int}
            self.upgrades[upgrade['class']] = {
                'class': Classes.get(upgrade['class']),
                'level_requirement': upgrade['level_requirement'],
                'cost': upgrade['cost']
            }

        Classes[slug] = self


class Combatant(GameObject):
    def _recalculate_speed(self):
        if self.klass.mount:
            self.speed = self.klass.mount.speed
        else:
            self.speed = self.race.base_speed

    def _recalculate_strength(self):
        self.strength = self.race.base_strength
        self.strength += self.klass.abilities.get('strength', 0)

    def _recalculate_agility(self):
        self.agility = self.race.base_agility
        self.agility += self.klass.abilities.get('agility', 0)

    def _recalculate_constitution(self):
        self.constitution = self.race.base_constitution
        self.constitution += self.klass.abilities.get('constitution', 0)

    def _recalculate_intelligence(self):
        self.intelligence = self.race.base_intelligence
        self.intelligence += self.klass.abilities.get('intelligence', 0)

    def _recalculate_wisdom(self):
        self.wisdom = self.race.base_wisdom
        self.wisdom += self.klass.abilities.get('wisdom', 0)

    def _recalculate_charisma(self):
        self.charisma = self.race.base_charisma
        self.charisma += self.klass.abilities.get('charisma', 0)

    def _recalculate_hp(self):
        self.hp = self.race.base_hp + self.level * self.klass.hp_per_level

    def _recalculate_bab(self):
        self.bab = self.level / self.klass.levels_per_bab

    def _recalculate_stats(self):
        self._recalculate_speed()
        self._recalculate_strength()
        self._recalculate_agility()
        self._recalculate_constitution()
        self._recalculate_intelligence()
        self._recalculate_wisdom()
        self._recalculate_charisma()
        self._recalculate_hp()
        self._recalculate_bab()

    def _reequip(self):
        self.weapon = self.klass.weapon
        self.sidearm = self.klass.sidearm
        self.outfit = self.klass.outfit
        self.mount = self.klass.mount
        self.item1 = self.klass.item1
        self.item2 = self.klass.item2

    def _recalculate_all(self):
        self._recalculate_stats()
        self._reequip()

    def __init__(self, spec):
        super(Combatant, self).__init__(self, spec)

        # add basic templates
        self.race = Races.get(spec['race'])
        self.klass = Classes.get(spec['class'])

        self.level = spec.get('level', 1)
        self.experience = spec.get('experience', 0)

        self._recalculate_all()

        # state values
        self.morale = spec.get('morale', 0)
        self.current_hp = spec.get('current_hp', self.hp)
        self.status = spec.get('status', 'healthy')
