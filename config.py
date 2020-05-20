from rdflib import URIRef

#Domain
baseDomain = "https://8wayrun.com"

#History link for each character
characterHistoryLink = {
    "Amy": "https://8wayrun.com/wiki/amy-frame-data-sc6/history",
    "2B": "https://8wayrun.com/wiki/2b-frame-data-sc6/history",
    "Astaroth": "https://8wayrun.com/wiki/astaroth-frame-data-sc6/history",
    "Azwel": "https://8wayrun.com/wiki/azwel-frame-data-sc6/history",
    "Cassandra": "https://8wayrun.com/wiki/Cassandra-frame-data-sc6/history",
    "Cervantes": "https://8wayrun.com/wiki/Cervantes-frame-data-sc6/history",
    "Geralt": "https://8wayrun.com/wiki/Geralt-frame-data-sc6/history",
    "Groh": "https://8wayrun.com/wiki/groh-frame-data-sc6/history",
    "Haohmaru": "https://8wayrun.com/wiki/Haohmaru-frame-data-sc6/history",
    "Hilde": "https://8wayrun.com/wiki/Hilde-frame-data-sc6/history",
    "Ivy": "https://8wayrun.com/wiki/Ivy-frame-data-sc6/history",
    "Kilik": "https://8wayrun.com/wiki/Kilik-frame-data-sc6/history",
    "Maxi": "https://8wayrun.com/wiki/Maxi-frame-data-sc6/history",
    "Mitsurugi": "https://8wayrun.com/wiki/Mitsurugi-frame-data-sc6/history",
    "Nightmare": "https://8wayrun.com/wiki/Nightmare-frame-data-sc6/history",
    "Raphael": "https://8wayrun.com/wiki/Raphael-frame-data-sc6/history",
    "Seong-Mi-Na": "https://8wayrun.com/wiki/Seong-Mi-Na-frame-data-sc6/history",
    "Siegfried": "https://8wayrun.com/wiki/Siegfried-frame-data-sc6/history",
    "Sophitia": "https://8wayrun.com/wiki/Sophitia-frame-data-sc6/history",
    "Taki": "https://8wayrun.com/wiki/Taki-frame-data-sc6/history",
    "Talim": "https://8wayrun.com/wiki/Talim-frame-data-sc6/history",
    "Tira": "https://8wayrun.com/wiki/Tira-frame-data-sc6/history",
    "Voldo": "https://8wayrun.com/wiki/Voldo-frame-data-sc6/history",
    "Xianghua": "https://8wayrun.com/wiki/Xianghua-frame-data-sc6/history",
    "Yoshimitsu": "https://8wayrun.com/wiki/Yoshimitsu-frame-data-sc6/history",
    "Zasalamel": "https://8wayrun.com/wiki/Zasalamel-frame-data-sc6/history"
}
#URIRef("")
characterDbpedia = {
    "Astaroth": URIRef("http://dbpedia.org/page/Astaroth_(Soulcalibur)"),
    "Cassandra": URIRef("http://dbpedia.org/page/Cassandra_Alexandra"),
    "Cervantes": URIRef("http://dbpedia.org/page/Cervantes_de_Leon"),
    "Geralt": URIRef("http://dbpedia.org/page/Geralt_of_Rivia"),
    "Haohmaru": URIRef("http://dbpedia.org/page/Haohmaru"),
    "Hilde": URIRef("http://dbpedia.org/page/Hildegard_von_Krone"),
    "Ivy": URIRef("http://dbpedia.org/page/Ivy_Valentine"),
    "Sophitia": URIRef("http://dbpedia.org/page/Sophitia"),
    "Taki": URIRef("http://dbpedia.org/page/Taki_(Soulcalibur)"),
    "Talim": URIRef("http://dbpedia.org/page/Talim_(Soulcalibur)"),
    "Tira": URIRef("http://dbpedia.org/page/Tira_(Soulcalibur)"),
    "Voldo": URIRef("https://en.wikipedia.org/wiki/Voldo"),
    "Xianghua": URIRef("http://dbpedia.org/page/Chai_Xianghua"),
    "Yoshimitsu": URIRef("http://dbpedia.org/page/Yoshimitsu")
}

def percentToFloat(guardbreak: str):
    guardbreak = guardbreak.strip(" ")
    if(guardbreak != ""):
        return float(guardbreak.strip('%'))/100
    else:
        return float(0)

#Move properties with format they are stored in
moveProperties = {
    "cmd" : str,  # Command
    "atk": str,  # Name of move
    "lvl": str,  # Heigh high,mid,low,spMid,SpLow
    "dmg": int,  # Amount of damage
    "chip": int,  # Amount of damage taken on block
    "imp": int,  # Frames to impact
    "grd": int,  # Recovery on block
    "hit": int,  # Recovery on hit
    "cnt": int,  # Recovery on Counterhit
    "gb": percentToFloat,  # Percentage of guardDamage taken
    "nts": str,  # Notes if anything is special about the move
}

movePropertiesDictTranslate = {
    "MoveCategory": "MoveCategory",
    "stance": "Stance",
    "cmd": "Command",
    "atk": "Name",
    "lvl": "Height",
    "dmg": "Damage",
    "chip": "ChipDamage",
    "imp": "Impact",
    "grd": "RecoveryGuard",
    "hit": "RecoveryHit",
    "cnt": "RecoveryCounterHit",
    "gb": "GuardDamage",
    "nts": "Notes",
    "guardImpact": "GuardImpact",
    "lethalHit": "isLethalHit",
    "breakAttack": "isBreakAttack",
    "stanceShift": "StanceShift",
    "unblockableAttack": "Unblockable",
    "spendGauge": "SpendGauge",
    "attackThrow": "AttackThrow"
}

#Tags for stance notation 
stancePrefix = "[h3]"
stanceSuffix = "[/h3]"


