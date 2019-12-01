def rootNamedEntityTamil(namedEntity):
    rootNamedEntity = ''
    tag = 0
    if(namedEntity[-1:] == 'ை'): ################    ව done
        rootNamedEntity = namedEntity[0:-2]
        print('ை is here')
        tag = 11
    elif(namedEntity[-3:] == 'ால்'):  ###############   විසින් done
        rootNamedEntity = namedEntity[0:-3]
        print('ால் is here')
        tag = 4
    elif(namedEntity[-3:] == 'ோடு'): ################    සමග done
        rootNamedEntity = namedEntity[0:-3]
        print('ோடு is here')
        tag = 13
    elif(namedEntity[-3:] == 'ுடன்''): ################    සමග done
        rootNamedEntity = namedEntity[0:-3]
        print('ோடு is here')
        tag = 13
   # elif(namedEntity[-4:] == 'ுடன்'): ################    ත් එක්ක
    #    rootNamedEntity = namedEntity[0:-4]
     #   print('ுடன் is here')
      #  tag = 10
    elif(namedEntity[-4:] == 'க்கு'): ################    ට done
        rootNamedEntity = namedEntity[0:-4]
        print('க்கு is here')
        tag = 3

        if(a[-1]='ி' or b[-1]='ை'):
          add('க்கு')

         if(c[-1]='ா'):
             add('வுக்கு')
         if(d[-1]='்'):
             add('remove ் and add ுக்கு')
         
    elif(namedEntity[-3:] == 'ில்'): ################    ගෙන් 
        rootNamedEntity = namedEntity[0:-3]
        print('ில் is here')
        tag = 1
    elif(namedEntity[-3:] == 'ின்'): ################    ගේ
        rootNamedEntity = namedEntity[0:-3]
        print('ின் is here')
        tag = 1
    elif(namedEntity[-7:] == 'ிருந்து'): ################    ගෙන්
        rootNamedEntity = namedEntity[0:-7]
        print('ிருந்து is here')
        tag = 2
    elif(namedEntity[-2:] == 'து'): ################    ගේ
        rootNamedEntity = namedEntity[0:-2]
        print('து is here')
        tag = 1
    elif(namedEntity[-3:] == 'ில்'): ################    යේ,ලේ,ගේ පාසලේ, පන්තියේ, 
        rootNamedEntity = namedEntity[0:-3]
        print('ில் is here')
        tag = 14
    elif(namedEntity[-1:] == 'ே'): ################    ආමන්ත්‍රනයක්
        rootNamedEntity = namedEntity[0:-1]
        print('ே is here')
        tag = 16
    elif(namedEntity[-1:] == 'ோ'): ################    පුදුමයක්
        rootNamedEntity = namedEntity[0:-1]
        print('ோ is here')
        tag = 3
    elif(namedEntity[-2:] == 'கு'): ###############   ගේ
        rootNamedEntity = namedEntity[0:-2]
        print('கு is here')
        tag = 1
    elif(namedEntity[-4:] == 'க்கு'): ################    ලග
        rootNamedEntity = namedEntity[0:-4]
        print('க்கு is here')
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
