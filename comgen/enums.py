from enum import Enum

class SuperEnum(Enum):
    """Adds an id property that gets the order of an enum member in the class"""

    def __init__(self, *args):
        for key, value in enumerate(args):
            for namekey, name in enumerate(self.__keys__):
                if key == namekey:
                    setattr(self, name, value)

    def to_dict(self):
        """converts an enum member to a dict"""
        rep = dict([(key, getattr(self, key)) for key in self.__keys__])
        rep["name"] = self.name
        return rep

    @classmethod
    def get(cls, id_):
        idx = [
            item for item in list(cls.__members__) if getattr(cls[item], "id") == id_
        ]
        if idx is not None and len(idx) > 0:
            return cls[idx[0]]
        else:
            return None

    @classmethod
    def items(cls):
        return list(cls.__members__)

    @classmethod
    def pluck(cls, key="name"):
        return [getattr(cls[x], key) for x in list(cls.__members__)]

    @classmethod
    def dump(cls):
        return [cls[x].to_dict() for x in list(cls.__members__)]

    @classmethod
    def all(cls):
        return [cls[x].to_dict() for x in list(cls.__members__)]

    @classmethod
    def members(cls):
        return [cls[x].name for x in list(cls.__members__)]

    @classmethod
    def list(cls):
        return [cls[x] for x in list(cls.__members__)]

    @classmethod
    def getTitle(cls):
        return [cls[x].title for x in list(cls.__members__)]

class Race(SuperEnum):
    __keys__ = ["id", "title"]

    astra = (1, "Astra Militarum")
    marines = (2, "Space Marines")
    astra_chaos = (3, "Traitor Guard")
    chaos = (4, "Chaos Space Marines")

class Sex(SuperEnum):
    __keys__ = ["id", "title"]

    male = (1, "Male")
    female = (2, "Female")

class Subtype(SuperEnum):
    __keys__ = ["id", "race", "title"]

    cadian =        (1, "Astra Militarum", "Cadian")
    krieg =         (2, "Astra Militarum", "Krieg")
    catachan =      (3, "Astra Militarum", "Catachan")
    valhalla =      (4, "Astra Militarum", "Valhallan")
    tallarn =       (5, "Astra Militarum", "Tallarn")
    vostroyan =     (6, "Astra Militarum", "Vostroyan")
    mordian =       (7, "Astra Militarum", "Mordian")
    ultramarine =   (8, "Space Marines", "Ultramarines")
    dark_angels =   (9, "Space Marines", "Dark Angels")
    imperial_fists =(10, "Space Marines", "Imperial Fists")
    salamanders =   (11, "Space Marines", "Salamanders")
    word_bearers =  (12, "Chaos Space Marines", "Word Bearers")
    iron_warriors = (13, "Chaos Space Marines", "Iron Warriors")
    thousand_sons = (14, "Chaos Space Marines", "Thousand Sons")

    @classmethod
    def getByRace(cls, race):
        return [cls[x] for x in list(cls.__members__) if getattr(cls[x], "race") == race]

class Rank(SuperEnum):
    __keys__ = ["id", "race","title"]

    general = (1, ["Astra Militarum"], "General")
    captain = (2, ["Astra Militarum", "Space Marines"], "Captain")
    colonel = (3, ["Astra Militarum"], "Colonel")
    major = (4, ["Astra Militarum"], "Major")
    lieutenant = (5, ["Astra Militarum", "Space Marines"], "Lieutenant")
    commissar = (6, ["Astra Militarum"], "Commissar")
    chaplain = (7, ["Space Marines"], "Chaplain")

    @classmethod
    def getByRace(cls, race):
        return [cls[x] for x in list(cls.__members__) if race in getattr(cls[x], "race")]