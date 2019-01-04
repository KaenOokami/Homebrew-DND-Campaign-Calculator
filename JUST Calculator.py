import numpy 
#CALCTYPE Gets a Users Input on what part of the calculator they would like to use.
CALCTYPE = input("What would you like to do with the calculator? Level,Zenkai,Training,Booster?")

#Functions to determine which calculator will be active by returning a boolean
if (CALCTYPE == "Level"):
  Level = True
  Zenkai = False
  Training = False
  Booster = False

elif (CALCTYPE == "Zenkai"):
  Level = False
  Zenkai = True
  Training = False
  Booster = False

elif (CALCTYPE == "Training"):
  Level = False
  Zenkai = False
  Training = True
  Booster = False

elif (CALCTYPE == "Booster"):
  Level = False
  Zenkai = False
  Training = False
  Booster = True

else:
  print ("ERROR NOT AN AVAILBLE FUNCTION")

#A while loop that only runs while Level == True
while Level == True:
  #Creates an Array with a Name STATS that holds Strings
  STAT = ["STR","DEX","CON","INT","WIS","CHA"]
  i = 0
  #Creates an empty Array named STATS with a for loop that inputs the values of STATS into the array
  STATS = []
  for STAT in STAT:
    print (STAT)
    STATS.append(int(input("Please enter the unmodified value of the Stat above: ")))
    print (STATS)
  #Creates an Array with a Name APTITUDES that holds Strings
  APTITUDES = ["STR","DEX","CON","INT","WIS","CHA"]
  #Creates an empty Array named APT with a for loop that inputs the values of STATS into the array
  APT = []
  for APTITUDES in APTITUDES:
    print (APTITUDES)
    APTVAL = (int(input("Please enter the aptitude of the Stat above(DO NOT ENTER ANY SIGNS): ")))
    SIGN = input("Is this Aptitude Positive or Negative?")
    if (SIGN == "Positive" or SIGN == "positive" or SIGN == "P" or SIGN == "p"):
      APTVAL = APTVAL * 1
    else:
      APTVAL = APTVAL * -1
    APT.append(APTVAL/100)
    print (APT)
  #Uses numpy to make an array named BASEGAIN that gets to base level up valuses of stats
  BASEGAIN = numpy.array([STATS * .08 for STATS in STATS])
  #Prints BASEGAIN
  print (BASEGAIN)
  #Uses numpy to add together BASEGAIN and APT
  STATGAINED = numpy.add(BASEGAIN,APT)
  #Prints STATGAINED
  print (STATGAINED)
  #Uses numpy to add together STATS and STATGAINED
  LEVELUP = numpy.round(numpy.add(STATS,STATGAINED))
  #New array for labeling reasons
  STAT2 = ["STR","DEX","CON","INT","WIS","CHA"]
  for STAT2 in STAT2:
    print (STAT2)
    print (LEVELUP[i])
    i = i + 1

  CONTINUE = input("Would you like to continue? Y or N")

  if (CONTINUE == "Y"):
    Level = True
  else:
    break

while Zenkai == True:
  TRUESTR = int(input("Please Enter your Unmodified STR Score: "))

  TRUEDEX = int(input("Please Enter your Unmodified DEX Score: "))

  TRUECON = int(input("Please Enter your Unmodified CON Score: "))

  ZENKAI = int(input("Please Enter Zenkai Value (DO NOT ENTER ANY SIGNS)"))

  STATS = numpy.array([TRUESTR,TRUEDEX,TRUECON])

  ZENKAISTR = TRUESTR * (ZENKAI/100)

  ZENKAIDEX = TRUEDEX * (ZENKAI/100)

  ZENKAICON = TRUECON * (ZENKAI/100)

  ZENKAIGAIN = numpy.array([ZENKAISTR,ZENKAIDEX,ZENKAICON])

  ZENKAISTATS = numpy.round(numpy.add(STATS,ZENKAIGAIN))

  STAT = ["STR","DEX","CON"]

  i = 0

  for STAT in STAT:
    print (STAT)
    print (ZENKAISTATS[i])
    i = i + 1

while Training == True:
  
  STRTRAIN = input("Do you have training in STR? True or False")

  if (STRTRAIN == "True"):
    TRUESTR = int(input("Please Enter your Unmodified STR Score: "))
    TRAINPER = int(input("Please Enter your Training Value (DO NOT ENTER ANY SIGNS): "))

    TRAINEDSTR = TRUESTR * (TRAINPER/100)

    TRAININGSTR = numpy.round(numpy.add(TRUESTR, TRAINEDSTR))

    print (TRAININGSTR, "This is your current STR Score with Training Applied, This number can be used in place of your Base STR when running the Level Up Calculator")

  DEXTRAIN = input("Do you have training in DEX? True or False")

  if (DEXTRAIN == "True"):
    TRUEDEX = int(input("Please Enter your Unmodified DEX Score: "))
    TRAINPER = int(input("Please Enter your Training Value (DO NOT ENTER ANY SIGNS): "))

    TRAINEDDEX = TRUEDEX * (TRAINPER/100)

    TRAININGDEX = numpy.round(numpy.add(TRUEDEX, TRAINEDDEX))

    print (TRAININGDEX, "This is your current DEX Score with Training Applied, This number can be used in place of your Base DEX when running the Level Up Calculator")

  CONTRAIN = input("Do you have training in CON? True or False")

  if (CONTRAIN == "True"):
    TRUECON = int(input("Please Enter your Unmodified CON Score: "))
    TRAINPER = int(input("Please Enter your Training Value (DO NOT ENTER ANY SIGNS): "))

    TRAINEDCON = TRUECON * (TRAINPER/100)

    TRAININGCON = numpy.round(numpy.add(TRUEDEX, TRAINEDDEX))

    print (TRAININGCON, "This is your current CON Score with Training Applied, This number can be used in place of your Base CON when running the Level Up Calculator")
  
  INTTRAIN = input("Do you have training in INT? True or False")

  if (INTTRAIN == "True"):
    TRUEINT = int(input("Please Enter your Unmodified INT Score: "))
    TRAINPER = int(input("Please Enter your Training Value (DO NOT ENTER ANY SIGNS): "))

    TRAINEDINT = TRUEINT * (TRAINPER/100)

    TRAININGINT = numpy.round(numpy.add(TRUEINT, TRAINEDINT))

    print (TRAININGINT, "This is your current INT Score with Training Applied, This number can be used in place of your Base INT when running the Level Up Calculator")

  WISTRAIN = input("Do you have training in WIS? True or False")

  if (WISTRAIN == "True"):
    TRUEWIS = int(input("Please Enter your Unmodified WIS Score: "))
    TRAINPER = int(input("Please Enter your Training Value (DO NOT ENTER ANY SIGNS): "))

    TRAINEDWIS = TRUEWIS * (TRAINPER/100)

    TRAININGWIS = numpy.round(numpy.add(TRUEDEX, TRAINEDWIS))

    print (TRAININGWIS, "This is your current WIS Score with Training Applied, This number can be used in place of your Base WIS when running the Level Up Calculator")

  CHATRAIN = input("Do you have training in CHA? True or False")

  if (CHATRAIN == "True"):
    TRUECHA = int(input("Please Enter your Unmodified CHA Score: "))
    TRAINPER = int(input("Please Enter your Training Value (DO NOT ENTER ANY SIGNS): "))

    TRAINEDCHA = TRUECHA * (TRAINPER/100)

    TRAININGCHA = numpy.round(numpy.add(TRUECHA, TRAINEDCHA))

    print (TRAININGCHA, "This is your current CHA Score with Training Applied, This number can be used in place of your Base CHA when running the Level Up Calculator")

while Booster == True:
  BASESTAT = int(input("Please enter the unmodified version of the STAT you have boosters in.: "))

  Enhance = True

  while Enhance == True:
    BOOSTER = int(input("Please enter the value of the booster (DO NOT ENTER SIGNS): "))

    print (BASESTAT)

    BONUSGAIN = BASESTAT * (BOOSTER/100)

    BOOSTEDSTAT = numpy.round(numpy.add(BASESTAT, BONUSGAIN))

    BASESTAT = BOOSTEDSTAT

    print (BASESTAT)

    CONTINUE = input("Anymore Boosters to apply to this stat? Y or N?")

    if (CONTINUE == "Y"):
      Enhance = True
    
    else:
      Enhance = False