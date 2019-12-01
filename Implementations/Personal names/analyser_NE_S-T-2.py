def addMorpology(rootNamedEntity, tag):
    namedEntity = ''
    if(tag==1):     #################  ගේ
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யின்'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ின்' 
    elif(tag==2):     #################  ගෙන්
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யில்'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ில்' 
    elif(tag==3):     #################  සිට
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யிலிருந்து'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ிலிருந்து' 
    elif(tag==4):     #################  ගේ
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யினது'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ினது' 
    elif(tag==5):     #################  ළග
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யிடம்'
        else:
            namedEntity = rootNamedEntity[:-1] + 'விடம்' 
    elif(tag==6):     #################  !
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யே'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ே' 
    elif(tag==7):     #################  ද!
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யோ'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ோ' 
    elif(tag==8):     #################  විසින්
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யால்'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ால்' 
    elif(tag==9):     #################  සමග
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யுடன்'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ுடன்' 
    elif(tag==10):     #################  සමග
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யோடு'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ோடு' 
    elif(tag==11):     #################  ව
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'யை'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ை'
    elif(tag==12):     #################  ට
        if(rootNamedEntity[-1]=='ி' or rootNamedEntity[-1]=='ை'):
            namedEntity = rootNamedEntity + 'க்கு'
        else:
            namedEntity = rootNamedEntity[:-1] + 'ுக்கு'
    elif(tag==20):     #################  
        namedEntity = rootNamedEntity 
 #   else:
  #      namedEntity = rootNamedEntity
    return namedEntity

rootNamedEntity = input('Enter text:- ')
tag = input('Enter tag:- ')

namedEntity = addMorpology(rootNamedEntity, int(tag))

print("word is " + namedEntity)
