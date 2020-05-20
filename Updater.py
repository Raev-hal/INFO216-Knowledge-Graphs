#Lib
import requests
from bs4 import BeautifulSoup
import time
from rdflib.namespace import RDF, RDFS, XSD, FOAF, OWL
from rdflib import Graph, Namespace, Literal, URIRef, BNode


#Local config
import config

start_time = time.time()

#Gets the latest link for a characters frame data
def getLatestFrameDataEdit(CharacterHistoryLink):
    r = requests.get(CharacterHistoryLink)
    soup = BeautifulSoup(r.content,"lxml")
    links = soup.find_all("a")

    for link in links: #Finds the latest link
        if("Current version" in link.text):
            return(
                config.baseDomain + link.attrs["href"]
                )
    
    print("Current Framedata lookup failed" + CharacterHistoryLink)
    
    return None #if it fails

#
def dictGen(data: str):
    data = data.replace("[template=FD6ROW]", "")
    data = data.replace("[/template]", "")
    data = data.replace("[template=FD6END]", "")
    data = data.replace("\n\n", "")
    output = []
    data = data.split("[h2]")#Splits the text into sections Horizontal vertical etc

    for category in data[2:]:
        currentMoveCategory = category[0:category.find("[")]
        category = category.split("\n")
        stance = ""

        for move in category:
            currentMove = {"MoveCategory": currentMoveCategory}

            if(config.stancePrefix in move):#Looks for a subHeadline indicating a stance is required.
                stanceStart = move.find(config.stancePrefix)
                stanceEnd = move.find(config.stanceSuffix)
                stance = move[stanceStart+len(config.stancePrefix):stanceEnd]
            
            if(stance != ""):
                currentMove["stance"] = stance

            noteData = {  # Reset note data
                "guardImpact": "",
                "lethalHit": False,
                "breakAttack": False,
                "stanceShift": False,
                "unblockableAttack": False,
                "spendGauge": False,
                "attackThrow": False
            }

            for moveProperty in config.moveProperties.keys():
                if(moveProperty in move):
                    movePropStart = move.find(moveProperty) + len(moveProperty) + 1 #+2 for after =
                    movePropEnd = move.find("|", movePropStart)
                    movePropData = move[movePropStart:movePropEnd]
                    
                    if(len(movePropData) > 0 and movePropData[-1] == " "):# Remove empty space at end
                        movePropData = movePropData[:-1]
                    try:
                        currentMove[moveProperty] = config.moveProperties[moveProperty](
                            movePropData)
                    except ValueError:
                        if(moveProperty == "chip" and movePropData == " " and movePropData == 'n/a '):
                            movePropData = 0
                        
                        currentMove[moveProperty] = movePropData
                    

            #Parses user written notes for "important" information
            
            if("nts" in currentMove):
                if(":GI::H:" in currentMove["nts"]):
                    noteData["guardImpact"] = "high"
                elif(":GI::M:" in currentMove["nts"]):
                    noteData["guardImpact"] = "mid"
                elif(":GI::L:" in currentMove["nts"]):
                    noteData["guardImpact"] = "low"
                elif(":GI:" in currentMove["nts"]):
                    noteData["guardImpact"] = "all "
                
                if(":LH:" in currentMove["nts"]):
                    noteData["lethalHit"] = True
                if(":BA:" in currentMove["nts"]):
                    noteData["breakAttack"] = True
                if(":SS:" in currentMove["nts"]):
                    noteData["stanceShift"] = True
                if(":UA:" in currentMove["nts"]):
                    noteData["unblockableAttack"] = True
                if(":SG:" in currentMove["nts"]):
                    noteData["spendGauge"] = True
                if(":AT:" in currentMove["nts"]):
                    noteData["attackThrow"] = True

            for key, value in noteData.items():
                currentMove[key] = value

            # All moves has inputs so if there is no input.
            if("cmd" in currentMove and currentMove["cmd"] != ""):
                output.append(currentMove)
    
    return output


#Download to dictionary
CharacterFrameDataDict = {}
for characterName, historyLink in config.characterHistoryLink.items():

    frameDataLink = getLatestFrameDataEdit(historyLink)

    r = requests.get(frameDataLink)
    soup = BeautifulSoup(r.content, "lxml")
    links = soup.find_all("textarea")

    CharacterFrameDataDict[characterName] = dictGen(str(links))
    print("Characters left %s\t Downloaded %s " %
          (len(config.characterHistoryLink) - 
          list(config.characterHistoryLink.keys()).index(characterName) - 1,
          characterName))



print("\nDownload finished: %s seconds\n" % (round(time.time() - start_time,2)))

g = Graph()
ex = Namespace("http://example.org/")

for character, link in config.characterDbpedia.items():  # links to DBpedia
    g.add((URIRef(ex + character), OWL.sameAs, link))


index = 0

for character, moves in CharacterFrameDataDict.items():
    for move in moves:
        g.add((URIRef(ex + str(index)),ex.performedBy, URIRef(ex + character)))#Adds which character does the move 
        for key, value in move.items(): #Adds each move property
            g.add((
                URIRef(ex + str(index)),
                URIRef(ex + config.movePropertiesDictTranslate[key]),
                Literal(value)
                ))
        index += 1
    print("Characters left %s\t Created graph for %s " % (
        len(config.characterHistoryLink) -
        list(config.characterHistoryLink.keys()).index(character) - 1, character))


print("\nFinished creating graph: %s seconds\n" %
      (round(time.time() - start_time, 2)))

#Serialize data to data.ttl
print("Started Serialization...\n")
g.serialize(destination="data.ttl", format="turtle")

print("Finished serializing data: %s seconds\n" %
      (round(time.time() - start_time, 2)))
