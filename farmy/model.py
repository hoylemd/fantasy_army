class GameObject(object):
    def __init__(self, slug, spec):
        self.slug = slug
        self.spec = spec
        self.name = spec.get('name', '')
        self.description = spec.get('description', "")


class DamageType(GameObject):
    values = {}

    def __init__(self, slug, spec):
        super(DamageType, self).__init__(slug, spec)
        self.piercing = spec.get('piercing', 0)
        DamageType.values[slug] = self

    @staticmethod
    def get(slug):
        return DamageType.values.get(slug)


class Special(GameObject):
    values = {}

    def __init__(self, slug, spec):
        super(Special, self).__init__(slug, spec)
        Special.values[slug] = self

    @staticmethod
    def get(slug):
        return Special.values.get(slug)


class Feat(GameObject):
    values = {}

    def __init__(self, slug, spec):
        super(Feat, self).__init__(slug, spec)
        Feat.values[slug] = self

    @staticmethod
    def get(slug):
        return Feat.values.get(slug)


class Class(GameObject):
    values = {}

    def __init__(self, slug, spec):
        super(Class, self).__init__(slug, spec)
        Class.values[slug] = self

    @staticmethod
    def get(slug):
        return Class.values.get(slug)


class Weapon(GameObject):
    def __init__(self, slug, spec):
        super(Weapon, self).__init__(slug, spec)
        self.attack_range = spec.get('range', 1)
        self.damage = spec.get('damage', 1)
        self.rate = spec.get('rate', 1)

        type_slug = spec.get('type', 'blunt')
        self.damage_type = DamageType.values.get(type_slug)

        special_slugs = spec.get('specials', [])
        self.special = []
        for special in special_slugs:
            self.special.append(Special.get(special))


class Combatant(object):
    def __init__(self, spec):
        self.weapon = None
        self.sidearm = None
        self.outfit = None
        self.mount = None
        self.equipment = ()
        self.level = 1
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.hp = 10
        self.template = None
