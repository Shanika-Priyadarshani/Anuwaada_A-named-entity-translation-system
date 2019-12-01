def rootNamedEntityTamil(namedEntity):
    rootNamedEntity = ''
    tag = 0
    if(namedEntity[-3:] == 'ின்'): ################    ගේ
        if((namedEntity[-4:-3]=='ய') and (namedEntity[-5:-4]=='ி' or namedEntity[-5:-4]=='ை')):
            #remove('யின்')
            rootNamedEntity = namedEntity[:-4]
        else:
            #remove('ின்')
            rootNamedEntity = namedEntity[:-3]
        tag = 1
    elif(namedEntity[-3:] == 'ில்'):  ###############   ගෙන්
        if((namedEntity[-5:-4]=='ி' or namedEntity[-5:-4]=='ை') and (namedEntity[-4:-3]=='ய')):
            #remove('யில்')
            rootNamedEntity = namedEntity[:-4]
        else:
            #remove('ில்')
            rootNamedEntity = namedEntity[:-3]
        tag = 2
    elif(namedEntity[-9:] == 'ிலிருந்து'): ################    සිට
        if((namedEntity[-11:-10]=='ி' or namedEntity[-11:-10]=='ை') and (namedEntity[-10:-9]=='ய')):
            #remove('யிலிருந்து')
            rootNamedEntity = namedEntity[:-10]
        else:
            #remove('ிலிருந்து')
            rootNamedEntity = namedEntity[:-9]
        tag = 3
    elif(namedEntity[-4:] == 'ினது'): ################    ගේ
        if((namedEntity[-6:-5]=='ி' or namedEntity[-6:-5]=='ை') and (namedEntity[-5:-4]=='ய')):
            #remove('யினது')
            rootNamedEntity = namedEntity[:-5]
        else:
            #remove('ினது')
            rootNamedEntity = namedEntity[:-4]
        tag = 4
#    elif(namedEntity[-3:] == 'ில்'): ################    ස්ථානයක්
 #        if((namedEntity[-5:-4]=='ி' or namedEntity[-5:-4]=='ை') and (namedEntity[-4:-3]=='ய')):
  #          #remove('யில்')
   #         rootNamedEntity = namedEntity[:-4]
    #    else:
     #       rootNamedEntity = namedEntity[:-3]
      #      #remove('ில்')
       # tag = 5
    elif(namedEntity[-4:] == 'ிடம்'): ################    ළග
        if((namedEntity[-6:-5]=='ி' or namedEntity[-6:-5]=='ை') and (namedEntity[-5:-4]=='ய')):
            #remove('யிடம்')
            rootNamedEntity = namedEntity[:-5]
        elif((namedEntity[-6:-5]=='ி' or namedEntity[-6:-5]=='ை') and (namedEntity[-5:-4]=='வ')):
            #remove('விடம்')
            rootNamedEntity = namedEntity[:-5]
        else:
            print("")
            #something else
        tag = 5
    elif(namedEntity[-1:] == 'ே'): ################    ආමන්ත්‍රණයක් 
        if((namedEntity[-3:-2]=='ி' or namedEntity[-3:-2]=='ை') and (namedEntity[-2:-1]=='ய')):
            #remove('யே')
            rootNamedEntity = namedEntity[:-2]
        else:
            #remove('ே')
            rootNamedEntity = namedEntity[:-1]
        tag = 6
    elif(namedEntity[-1:] == 'ோ'): ################    පුදුමයක්
        if((namedEntity[-3:-2]=='ி' or namedEntity[-3:-2]=='ை') and (namedEntity[-2:-1]=='ய')):
            #remove('யோ')
            rootNamedEntity = namedEntity[:-2]
        else:
            #remove('ோ')
            rootNamedEntity = namedEntity[:-1]
        tag = 7
    elif(namedEntity[-3:] == 'ால்'): ################    විසින්
        if((namedEntity[-5:-4]=='ி' or namedEntity[-5:-4]=='ை') and (namedEntity[-4:-3]=='ய')):
            #remove('யால்')
            rootNamedEntity = namedEntity[:-4]
        else:
            #remove('ால்')
            rootNamedEntity = namedEntity[:-3]
        tag = 8
    elif(namedEntity[-4:] == 'ுடன்'): ################    සමග
        if((namedEntity[-6:-5]=='ி' or namedEntity[-6:-5]=='ை') and (namedEntity[-5:-4]=='ய')):
            #remove('யுடன்')
            rootNamedEntity = namedEntity[:-5]
        else:
            #remove('ுடன்')
            rootNamedEntity = namedEntity[:-4]
        tag = 9
    elif(namedEntity[-3:] == 'ோடு'): ################    සමග
        if((namedEntity[-5:-4]=='ி' or namedEntity[-5:-4]=='ை') and (namedEntity[-4:-3]=='ய')):
            #remove('யோடு')
            rootNamedEntity = namedEntity[:-4]
        else:
            #remove('ோடு')
            rootNamedEntity = namedEntity[:-3]
        tag = 10
    elif(namedEntity[-1:] == 'ை'): ################    ව
        if((namedEntity[-3:-2]=='ி' or namedEntity[-3:-2]=='ை') and (namedEntity[-2:-1]=='ய')):
            #remove('யை')
            rootNamedEntity = namedEntity[:-2]
        else:
            #remove('ை')
            rootNamedEntity = namedEntity[:-1]
        tag = 11
    elif(namedEntity[-4:] == 'க்கு'): ################    ට
        if(namedEntity[-5:-4]=='ி' or namedEntity[-5:-4]=='ை'):
            #remove('க்கு')
            rootNamedEntity = namedEntity[:-4]
        else:
            #remove('ுக்கு')
            rootNamedEntity = namedEntity[:-5]
        tag = 12
    else:
        rootNamedEntity = namedEntity
        tag = 20
    ####---------------------------------------------------------------####
    print(tag)
    print(rootNamedEntity)
    items = ['க', 'ச', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள', 'ற', 'ன', 'ஷ', 'ஸ', 'ஹ', 'க்ஷ']
    print(rootNamedEntity[-1])
    if(rootNamedEntity[-1] in items):
        rootNamedEntity = rootNamedEntity + '்'
    return rootNamedEntity, tag

namedEntity = input('Enter text:- ')
print(namedEntity)

rootForm, tagNum = rootNamedEntityTamil(namedEntity)

print("root word is " + rootForm + ' --> ' + str(tagNum))
