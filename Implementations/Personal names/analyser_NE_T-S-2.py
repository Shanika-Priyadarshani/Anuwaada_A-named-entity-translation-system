def addMorpology(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):
        namedEntity = rootNamedEntity + 'ගේ'
    elif(tag==2):
        namedEntity = rootNamedEntity + 'ගෙන්'
    elif(tag==3):
        namedEntity = rootNamedEntity + ' සිට'
    elif(tag==4):
        namedEntity = rootNamedEntity + 'ගේ'
    elif(tag==5):
        namedEntity = rootNamedEntity + ' ළග'
    elif(tag==6):
        namedEntity = rootNamedEntity + '!'
    elif(tag==7):
        namedEntity = rootNamedEntity + ' ද!'
    elif(tag==8):
        namedEntity = rootNamedEntity + ' විසින්'
    elif(tag==9):
        namedEntity = rootNamedEntity + 'සමග'
    elif(tag==10):
        namedEntity = rootNamedEntity + 'සමග'
    elif(tag==11):
        namedEntity = rootNamedEntity + 'ව'
    elif(tag==12):
        namedEntity = rootNamedEntity + 'ට'
    elif(tag==20):
        namedEntity = rootNamedEntity
  #  else:
   #     namedEntity = rootNamedEntity
    return namedEntity

rootNamedEntity = input('Enter text:- ')
tag = input('Enter tag:- ')

namedEntity = addMorpology(rootNamedEntity, int(tag))

print("word is " + namedEntity)
