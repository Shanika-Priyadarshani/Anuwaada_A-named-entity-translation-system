def rootNamedEntityTamil(namedEntity):
    rootNamedEntity = ''
    tag = 0
    if(namedEntity[-2:] == 'ගේ'): ################
        rootNamedEntity = namedEntity[:-2]
        tag = 1
    elif(namedEntity[-4:] == 'ගෙන්'):  ###############   
        rootNamedEntity = namedEntity[:-4]
        tag = 2
    elif(namedEntity[-1:] == '!'): ################    
        rootNamedEntity = namedEntity[:-1]
        tag = 6
    elif(namedEntity[-2:] == 'ද!'): ################
        rootNamedEntity = namedEntity[:-2]
        tag = 7
    elif(namedEntity[-6:] == 'විසින්'): ################
        rootNamedEntity = namedEntity[:-6]
        tag = 8
    elif(namedEntity[-3:] == 'සමග'): ################
        rootNamedEntity = namedEntity[:-3]
        tag = 9
    elif(namedEntity[-4:] == 'එක්ක'): ################
        rootNamedEntity = namedEntity[:-4]
        tag = 10
    elif(namedEntity[-1:] == 'ව'): ################    
        rootNamedEntity = namedEntity[:-1]
        tag = 11
    elif(namedEntity[-1:] == 'ට'): ################    
        rootNamedEntity = namedEntity[:-1]
        tag = 12
    else:
        rootNamedEntity = namedEntity
        tag = 20
    ####---------------------------------------------------------------####
    print(tag)
    print(rootNamedEntity)
    return rootNamedEntity, tag

namedEntity = input('Enter text:- ')
print(namedEntity)

rootForm, tagNum = rootNamedEntityTamil(namedEntity)

print("root word is " + rootForm + ' --> ' + str(tagNum))
