from RiotAPI import RiotAPI
api = RiotAPI('<Your API Key>')

def getChampionSpells(championId,i):
    championSpells = []
    champSpell = api.get_champion_spells(championId)
    tempSpell = champSpell['spells'][i]
    maxRank = tempSpell['maxrank']
    if(championId == 99):#thanks a lot Lux -_-
        return 1
    else:
        spellList = len(tempSpell['effect']) - 1
        checkIfSpellListDamageIsNull = tempSpell['effect'][1]
        if checkIfSpellListDamageIsNull ==None: #changes the effect list index for champions who have no effect
            spellList = len(tempSpell['effect']) - 1
        else:
            spellList = 1
        spellEffect = tempSpell['effect'][spellList]
        initalSpellEffect = spellEffect[0]
        if(initalSpellEffect > 799):#to adjust for Nunu's Q which only applies to minons/monsters
            initalSpellEffect = 0
        finalSpellEffect = spellEffect[maxRank - 1]
        if(finalSpellEffect > 799):#to adjust for Nunu's Q which only applies to minons/monsters
            finalSpellEffect = 0
        diffSpellEffect = finalSpellEffect - initalSpellEffect
        if(diffSpellEffect > 799) | (diffSpellEffect < 0): #warwick's e effect setup is outragous in value so this sets it as zero
            diffSpellEffect = 0
        spellCost = tempSpell['cost']
        initalSpellCost = spellCost[0]
        finalSpellCost = spellCost[maxRank - 1]
        diffSpellCost = finalSpellCost - initalSpellCost
        if(diffSpellCost <= 0):
            diffSpellCost = 1
        score = diffSpellEffect/diffSpellCost
        return score

def calculateChampionStats(id):
    championSpell = []
    championBestSpell = [id]
    championId = api.get_champion_stats(id)
    championSkill = api.get_champion_stats(id)
    championName = championId['name']
    print "Calculating",championName,"score"
    championAD = championId['stats']['attackdamage']
    championADperLevel = championId['stats']['attackdamageperlevel']
    championAttackSpeedOffset = championId['stats']['attackspeedoffset']
    championAttackSpeedperLevel = championId['stats']['attackspeedperlevel']
    championAttackRange = championId['stats']['attackrange']
    championMPRegen = championId['stats']['mpregen']
    championMPRegenPerLevel = championId['stats']['mpregenperlevel']
    initalAttack = championAD + championADperLevel
    FinalAttack = championAD + (championADperLevel * 18)
    diffChampionAttackStat = (FinalAttack - initalAttack)/18
    initalAttackSpeed = championAttackSpeedperLevel + championAttackSpeedOffset
    finalAttackSpeed = (championAttackSpeedperLevel * 18)+championAttackSpeedOffset
    diffChampionAttackSpeedStat = (finalAttackSpeed - initalAttackSpeed)/18
    initalMPRegen = championMPRegen + championMPRegenPerLevel
    finalMPRegen = championMPRegen + (championMPRegenPerLevel * 18)
    diffMPRegen = (finalMPRegen - initalMPRegen)/18
    ADScore = (diffChampionAttackStat * (championAttackRange/100))/diffChampionAttackSpeedStat
    if(diffChampionAttackStat <= 0):
        diffChampionAttackStat = 1
    if(diffChampionAttackSpeedStat <= 0):
        diffChampionAttackSpeedStat = 1
    if(diffMPRegen <= 0):
        diffMPRegen = 1
    for i in range(0,4):
        APScore = (getChampionSpells(id, i)) * (diffMPRegen)
        score = int(ADScore + APScore)
        championSpell.append(score)
    score = 0
    for i in range(0,4):
        tempSpell = championSpell[i]
        if(score < tempSpell):
            score = tempSpell
    championBestSpell.append(score)
    championBestSpell.append(i)
    return championBestSpell


def compareSpells():
    championListSource =api.get_champions()['data']
    championList = []
    for key, value in championListSource.iteritems():
        temp = [key,value]
        championList.append(calculateChampionStats(value['id']))
    return championList

def compareChampions(championList):
    topChampionId = '000'
    topSpellScore = 0
    spellIndex = 0
    for i in range(0,len(championList)):
        if(championList[i][1] > topSpellScore):
            topChampionId = championList[i][0]
            topSpellScore = championList[i][1]
            spellIndex = championList[i][2]
    championStats = api.get_champion_stats(topChampionId)
    champSpell = api.get_champion_spells(topChampionId)
    championName = championStats['name']
    championTitle = championStats['title']
    tempSpell = champSpell['spells'][spellIndex]
    spellName = tempSpell['name']
    spellDescription = tempSpell['description']
    spellEffect = tempSpell['effectBurn'][1]
    spellCost = tempSpell['costBurn']
    print "The champion with the most efficent spell is",championName,",",championTitle
    print "The most efficent spell is",spellName,"with a score of", topSpellScore,"points"
    print "Spell Description:",spellDescription
    print "Effect:",spellEffect
    print "Cost",spellCost


def main():
    compareChampions(compareSpells())

if __name__=="__main__":
    main()
else:
    print("Error")
