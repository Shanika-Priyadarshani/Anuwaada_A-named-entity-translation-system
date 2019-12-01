def rootNamedEntitySinhala(namedEntity):
    rootNamedEntity = ''
    tag = 0
    if(namedEntity[-2:] == 'ගේ'):
        rootNamedEntity = namedEntity[0:-2]
        print('ගේ is here')
        tag = 1
    elif(namedEntity[-4:] == 'ගෙන්'):
        rootNamedEntity = namedEntity[0:-4]
        print('ගෙන් is here')
        tag = 2
    elif(namedEntity[-1:] == 'ට'):
        rootNamedEntity = namedEntity[0:-1]
        print('ට is here')
        tag = 3
    elif(namedEntity[-6:] == 'විසින්'):
        rootNamedEntity = namedEntity[0:-6]
        print('විසින් is here')
        tag = 4
    elif(namedEntity[-4:] == 'තුමා'):
        rootNamedEntity = namedEntity[0:-4]
        print('තුමා is here')
        tag = 5
    elif(namedEntity[-5:] == 'තුමිය'):
        rootNamedEntity = namedEntity[0:-5]
        print('තුමිය is here')
        tag = 6
    elif(namedEntity[-4:] == 'තුමෝ'):
        rootNamedEntity = namedEntity[0:-4]
        print('තුමෝ is here')
        tag = 7
    elif(namedEntity[-2:] == 'හට'):
        rootNamedEntity = namedEntity[0:-2]
        print('හට is here')
        tag = 8
    elif(namedEntity[-3:] == 'ටත්'):
        rootNamedEntity = namedEntity[0:-3]
        print('ටත් is here')
        tag = 9
    elif(namedEntity[-2:] == 'ත්'):
        if(namedEntity[-3:-2] == 'ු'):
            rootNamedEntity = namedEntity[0:-3] + '්'
            print('ත් is here')
        else:
            rootNamedEntity = namedEntity[0:-2]
            print('ත් is here')
        tag = 10
    elif(namedEntity[-1:] == 'ව'):
        rootNamedEntity = namedEntity[0:-1]
        print('ව is here')
        tag = 11
    elif(namedEntity[-1:] == 'ද'):
        rootNamedEntity = namedEntity[0:-1]
        print('ද is here')
        tag = 12
    elif(namedEntity[-3:] == 'සමග'):
        rootNamedEntity = namedEntity[0:-4]
        print('සමග is here')
        tag = 13
    elif(namedEntity[-1:] == 'ේ'):
        rootNamedEntity = namedEntity[0:-1]
        print('ේ is here')
        tag = 14
    elif(namedEntity[-2:] == 'ලග'):
        rootNamedEntity = namedEntity[0:-2]
        print('ලග is here')
        tag = 15
    else:
        rootNamedEntity = namedEntity
        print('nothing is here')
        
    print(tag)
    return rootNamedEntity, tag


namedEntity = input('Enter text:- ')
print(namedEntity)

rootForm, tagNum = rootNamedEntitySinhala(namedEntity)

print("root word is " + rootForm + ' --> ' + str(tagNum))

