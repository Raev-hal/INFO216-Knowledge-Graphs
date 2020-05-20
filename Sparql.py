from rdflib.namespace import RDF, RDFS, XSD, FOAF, OWL
from rdflib import Graph, Namespace, Literal, URIRef, BNode
from prettytable import PrettyTable

def AddQuationMark(textVar):
    return "\"" + textVar + "\""

#Inputdata
if(input("Press enter to use the example, for custom inputs write anything ") != ""):
    OpponentsCharacter = input("Opponents Character:\n")
    OpponentMove = input("Opponents Move in commandform:\n")
    UserCharacter = input("Playing as:\n")
else:
    OpponentsCharacter = "Astaroth"
    OpponentMove = ":1::(A):"
    UserCharacter = "Astaroth"
    print("Example is being used\nYou %s vs Opponent %s and opponentsmove is %s" % (
        UserCharacter, OpponentsCharacter, OpponentMove))

# Parsing a local file
g = Graph()
parsed_graph = g.parse(location="data.ttl", format="turtle")

OpponentRecoveryState = g.query(
    """SELECT ?RecoveryGuard
       WHERE {
          ?a ns1:performedBy ns1:%s.
          ?a ns1:Command %s.
          ?a ns1:RecoveryGuard ?RecoveryGuard.
       }""" % (OpponentsCharacter,AddQuationMark(OpponentMove)))

for i in OpponentRecoveryState:
    OpponentRecoveryState = i[0].toPython()

BlockPunish = g.query(
    """SELECT ?Command ?Impact ?Damage ?GuardDamage ?Height
       WHERE {
          ?a ns1:performedBy ns1:%s.
          ?a ns1:Impact ?Impact.
          ?a ns1:Command ?Command.
          ?a ns1:Damage ?Damage.
          ?a ns1:GuardDamage ?GuardDamage.
          ?a ns1:Height ?Height.
          FILTER(?Impact <= %s)
       }
       ORDER BY ?Damage""" % (UserCharacter, abs(OpponentRecoveryState)))


#Formats everything into a nice table
moveTable = PrettyTable()
for row in BlockPunish:
    moveTable.field_names = list(row.labels.keys())
    temp = []
    for i in row:
            temp.append(i.toPython())
    moveTable.add_row(temp)

print(moveTable)
