#!/usr/bin/env python
# coding: utf-8

# In[69]:


def formatDate(inputDate, token):
    splittedList = []
    splitter = ""
    returnDate = ""
    if(token == 1 or token == 2):
        splittedList = inputDate.split("/")
        splitter = "/"
    elif(token == 3 or token == 4):
        splittedList = inputDate.split(".")
        splitter = "."
    else:
        splittedList = inputDate.split("-")
        splitter = "-"
#     print(splittedList)
    if(token%2 == 0):
        returnDate = splittedList[2] + splitter + splittedList[1] + splitter + splittedList[0]
    else:
        returnDate = splittedList[0] + splitter + splittedList[1] + splitter + splittedList[2]
    return returnDate


# In[70]:


def formatterTa(inputRowList):
    inputList = inputRowList[:-1]
    sender = inputRowList[-1]
    returnData = ""
    returnList = []
    newList = []
    for ele in inputList:
        if(not(ele[0] == 'of' or  ele[0] == 'වනදා' or ele[0] == '')):
            newList.append([str(ele[0]), int(ele[1])])
    for index, inputEle in enumerate(newList):
        inputData = inputEle[0]
        token = int(inputEle[1])
        checkList = [9, 10, 62]
        datesList = [36, 37, 38, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        monthsList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        
        
        if(sender == 1): # english
            if(token >=1 and token <= 6):
                returnList.append(' ' + formatDate(inputData, token) + ' ')
            elif(token == 7 or token == 8):
                returnList.append(' ')
                returnList.append(' ' + inputData + ' ')
            elif(token == 9):
                if((int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8) and (index-1)>=0):
                    returnList.insert(-1, (" காலை "))
                else:
                    returnList.append(" காலை ")
            elif(token == 10):
                if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8 and (index-1)>=0):
                    returnList.insert(-1, (" பிற்பகல் "))
                else:
                    returnList.append(" பிற்பகல் ")
            elif(token == 11):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.append((" ஜனவரி"))
#                 else:
                returnList.append(" ஜனவரி ")
    #             returnData = returnData + " ஜனவரி"
            elif(token == 12):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" பிப்ரவரி"))
#                 else:
                returnList.append(" பிப்ரவரி ")
    #             returnData = returnData + " பிப்ரவரி"
            elif(token == 13):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" மார்ச்"))
#                 else:
                returnList.append(" மார்ச் ")
    #             returnData = returnData + " மார்ச்"
            elif(token == 14):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஏப்ரல்"))
#                 else:
                returnList.append(" ஏப்ரல் ")
    #             returnData = returnData + " ஏப்ரல்"
            elif(token == 15):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ே"))
#                 else:
                returnList.append(" மே ")
    #             returnData = returnData + " மே"
            elif(token == 16):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூன்"))
#                 else:
                returnList.append(" ஜூன் ")
    #             returnData = returnData + " ஜூன்"
            elif(token == 17):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூலை"))
#                 else:
                returnList.append(" ஜூலை ")
    #             returnData = returnData + " ஜூலை"
            elif(token == 18):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஆகஸ்ட்"))
#                 else:
                returnList.append(" ஆகஸ்ட் ")
    #             returnData = returnData + " ஆகஸ்ட்"
            elif(token == 19):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" செப்டம்பர்"))
#                 else:
                returnList.append(" செப்டம்பர் ")
    #             returnData = returnData + " செப்டம்பர்"
            elif(token == 20):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" அக்டோபர்"))
#                 else:
                returnList.append(" அக்டோபர் ")
    #             returnData = returnData + " அக்டோபர்"
            elif(token == 21):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" நவம்பர்"))
#                 else:
                returnList.append(" நவம்பர் ")
    #             returnData = returnData + " நவம்பர்"
            elif(token == 22):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" டிசம்பர்"))
#                 else:
                returnList.append(" டிசம்பர் ")
    #             returnData = returnData + " டிசம்பர்"
            elif(token == 23):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜன."))
#                 else:
                returnList.append(" ஜன.")
    #             returnData = returnData + " ஜன."
            elif(token == 24):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" பிப்."))
#                 else:
                returnList.append(" பிப். ")
    #             returnData = returnData + " பிப்."
            elif(token == 25):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" மார்."))
#                 else:
                returnList.append(" மார். ")
    #             returnData = returnData + " மார்."
            elif(token == 26):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஏப்."))
#                 else:
                returnList.append(" ஏப். ")
    #             returnData = returnData + " ஏப்."
            elif(token == 27):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" மே"))
#                 else:
                returnList.append(" மே ")
    #             returnData = returnData + " மே"
            elif(token == 28):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூன்"))
#                 else:
                returnList.append(" ஜூன் ")
    #             returnData = returnData + " ஜூன்"
            elif(token == 29):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூலை"))
#                 else:
                returnList.append(" ஜூலை ")
    #             returnData = returnData + " ஜூலை"
            elif(token == 30):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஆக."))
#                 else:
                returnList.append(" ஆக. ")
    #             returnData = returnData + " ஆக."
            elif(token == 31):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" செப்."))
#                 else:
                returnList.append(" செப். ")
    #             returnData = returnData + " செப்."
            elif(token == 32):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" அக்."))
#                 else:
                returnList.append(" அக். ")
    #             returnData = returnData + " அக்."
            elif(token == 33):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" நவ."))
#                 else:
                returnList.append(" நவ. ")
    #             returnData = returnData + " நவ."
            elif(token == 34):
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" டிச."))
#                 else:
                returnList.append(" டிச. ")
    #             returnData = returnData + " டிச."
            elif(token == 35):
                returnList.append(" காலாண்டு ")
    #             returnData = returnData + " காலாண்டு"
            elif(token == 36):
                returnList.append(" ஞாயிறு ")
    #             returnData = returnData + " ஞாயிறு"
            elif(token == 37):
                returnList.append(" திங்கள் ")
    #             returnData = returnData + " திங்கள்"
            elif(token == 38):
                returnList.append(" செவ்வாய் ")
    #             returnData = returnData + " செவ்வாய்"
            elif(token == 39):
                returnList.append(" புதன் ")
    #             returnData = returnData + " புதன்"
            elif(token == 40):
                returnList.append(" வியாழன் ")
    #             returnData = returnData + " வியாழன்"
            elif(token == 41):
                returnList.append(" வெள்ளி ")
    #             returnData = returnData + " வெள்ளி"
            elif(token == 42):
                returnList.append(" சனி ")
    #             returnData = returnData + " சனி"
            elif(token == 43):
                returnList.append(" ஞாயி. ")
    #             returnData = returnData + " ஞாயி."
            elif(token == 44):
                returnList.append(" திங். ")
    #             returnData = returnData + " திங்."
            elif(token == 45):
                returnList.append(" செவ். ")
    #             returnData = returnData + " செவ்."
            elif(token == 46):
                returnList.append(" புத. ")
    #             returnData = returnData + " புத."
            elif(token == 47):
                returnList.append(" வியா. ")
    #             returnData = returnData + " வியா."
            elif(token == 48):
                returnList.append(" வெள். ")
    #             returnData = returnData + " வெள்."
            elif(token == 49):
                returnList.append(" சனி. ")
    #             returnData = returnData + " சனி."
            elif(token == 50):
                returnList.append(" நள்ளிரவு ")
    #             returnData = returnData + " நள்ளிரவு"
            elif(token == 51):
                returnList.append(" நண்பகல் ")
    #             returnData = returnData + " நண்பகல்"
            elif(token == 52):
                returnList.append(" அதிகாலை ")
    #             returnData = returnData + " அதிகாலை"
            elif(token == 53):
                returnList.append(" மதியம் ")
    #             returnData = returnData + " மதியம்"
            elif(token == 54):
                returnList.append(" மாலை ")
    #             returnData = returnData + " மாலை"
            elif(token == 55):
                returnList.append(" இரவு ")
    #             returnData = returnData + " இரவு"
            elif(token == 56):
                returnList.append(" பொ.ச.மு ")
    #             returnData = returnData + " பொ.ச.மு"
            elif(token == 57):
                returnList.append(" பொ.ச ")
    #             returnData = returnData + " பொ.ச"
            elif(token == 58):
                returnList.append(" கி.மு. ")
    #             returnData = returnData + " கி.மு."
            elif(token == 59):
                returnList.append(" பொ.ச.மு ")
    #             returnData = returnData + " பொ.ச.மு"
            elif(token == 60):
                returnList.append(" கி.பி. ")
    #             returnData = returnData + " கி.பி."
            elif(token == 61):
                returnList.append(" பொ.ச. ")
    #             returnData = returnData + " பொ.ச."
            elif(token == 62):
                returnList.append((' ' + inputData + "ம் திகதி "))
            else:
                if(inputData == 'of' or inputData == 'in' or inputData == 'වන' or inputData == 'වැනි'):
                    returnData = returnData
                else:
                    returnList.append(inputData + ' ')
    #                 returnData = returnData + inputData
    
#     ------------------------------------------------------------------------------------------------------
        elif(sender == 2): # sinhala

            if(token >=1 and token <= 6):
                returnList.append(' ' + formatDate(inputData, token) + ' ')
            elif(token == 7 or token == 8):
                if((index-1)>=0 and (newList[index-1][1] == 9 or newList[index-1][1] == 10)):
                    returnList.append((' ' + inputData + ' '))
                else:
                    returnList.append(' ' + inputData + ' ')
#                 returnList.append(' ' + inputData + ' ')
            elif(token == 9):
                if((index+1) < len(newList) and (newList[index+1][1] == 7 or newList[index+1][1] == 8)):
#                     returnList.append(' ')
                    returnList.append("காலை")
                else:
                    returnList.append("காலை")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" காலை"))
#                 else:
#                     returnList.append(" காலை")
#     #             returnData = "முற்பகல் " + returnData
            elif(token == 10):
                if((index+1) < len(newList) and (newList[index+1][1] == 7 or newList[index+1][1] == 8)):
#                     returnList.append(' ')
                    returnList.append("பிற்பகல்")
                else:
                    returnList.append("பிற்பகல்")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" பிற்பகல்"))
#                 else:
#                     returnList.append(" பிற்பகல்")
    #             returnData = "பிற்பகல் " + returnData
            elif(token == 11):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஜனவரி "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஜனவரி "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஜனவரி ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஜனவரி "))
                else:
                    returnList.append(" ஜனவரி ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜனவரி"))
#                 else:
#                     returnList.append(" ஜனவரி")
    #             returnData = returnData + " ஜனவரி"
            elif(token == 12):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" பிப்ரவரி "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" பிப்ரவரி "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" பிப்ரவரி ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" பிப்ரவரி "))
                else:
                    returnList.append(" பிப்ரவரி ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" பிப்ரவரி"))
#                 else:
#                     returnList.append(" பிப்ரவரி")
    #             returnData = returnData + " பிப்ரவரி"
            elif(token == 13):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" மார்ச் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" மார்ச் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" மார்ச் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" மார்ச் "))
                else:
                    returnList.append(" மார்ச் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" மார்ச்"))
#                 else:
#                     returnList.append(" மார்ச்")
    #             returnData = returnData + " மார்ச்"
            elif(token == 14):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஏப்ரல் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஏப்ரல் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஏப்ரல் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஏப்ரல் "))
                else:
                    returnList.append(" ஏப்ரல் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஏப்ரல்"))
#                 else:
#                     returnList.append(" ஏப்ரல்")
    #             returnData = returnData + " ஏப்ரல்"
            elif(token == 15):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" மே "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" மே "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" மே ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" மே "))
                else:
                    returnList.append(" மே ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ே"))
#                 else:
#                     returnList.append(" மே")
    #             returnData = returnData + " மே"
            elif(token == 16):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஜூன் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஜூன் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஜூன் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஜூன் "))
                else:
                    returnList.append(" ஜூன் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூன்"))
#                 else:
#                     returnList.append(" ஜூன்")
    #             returnData = returnData + " ஜூன்"
            elif(token == 17):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஜூலை "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஜூலை "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஜூலை ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஜூலை "))
                else:
                    returnList.append(" ஜூலை ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூலை"))
#                 else:
#                     returnList.append(" ஜூலை")
    #             returnData = returnData + " ஜூலை"
            elif(token == 18):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஆகஸ்ட் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஆகஸ்ட் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஆகஸ்ட் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஆகஸ்ட் "))
                else:
                    returnList.append(" ஆகஸ்ட் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஆகஸ்ட்"))
#                 else:
#                     returnList.append(" ஆகஸ்ட்")
    #             returnData = returnData + " ஆகஸ்ட்"
            elif(token == 19):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" செப்டம்பர் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" செப்டம்பர் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" செப்டம்பர் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" செப்டம்பர் "))
                else:
                    returnList.append(" செப்டம்பர் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" செப்டம்பர்"))
#                 else:
#                     returnList.append(" செப்டம்பர்")
    #             returnData = returnData + " செப்டம்பர்"
            elif(token == 20):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" அக்டோபர் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" அக்டோபர் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" அக்டோபர் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" அக்டோபர் "))
                else:
                    returnList.append(" அக்டோபர் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" அக்டோபர்"))
#                 else:
#                     returnList.append(" அக்டோபர்")
    #             returnData = returnData + " அக்டோபர்"
            elif(token == 21):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" நவம்பர் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" நவம்பர் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" நவம்பர் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" நவம்பர் "))
                else:
                    returnList.append(" நவம்பர் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" நவம்பர்"))
#                 else:
#                     returnList.append(" நவம்பர்")
    #             returnData = returnData + " நவம்பர்"
            elif(token == 22):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" டிசம்பர் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" டிசம்பர் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" டிசம்பர் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" டிசம்பர் "))
                else:
                    returnList.append(" டிசம்பர் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" டிசம்பர்"))
#                 else:
#                     returnList.append(" டிசம்பர்")
    #             returnData = returnData + " டிசம்பர்"
            elif(token == 23):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஜன. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஜன. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஜன. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஜன. "))
                else:
                    returnList.append(" ஜன. ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜன."))
#                 else:
#                     returnList.append(" ஜன.")
    #             returnData = returnData + " ஜன."
            elif(token == 24):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" பிப். "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" பிப். "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" பிப். ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" பிப். "))
                else:
                    returnList.append(" பிப். ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" பிப்."))
#                 else:
#                     returnList.append(" பிப்.")
    #             returnData = returnData + " பிப்."
            elif(token == 25):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" மார். "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" மார். "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" மார். ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" மார். "))
                else:
                    returnList.append(" மார். ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" மார்."))
#                 else:
#                     returnList.append(" மார்.")
    #             returnData = returnData + " மார்."
            elif(token == 26):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஏப். "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஏப். "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஏப். ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஏப். "))
                else:
                    returnList.append(" ஏப். ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஏப்."))
#                 else:
#                     returnList.append(" ஏப்.")
    #             returnData = returnData + " ஏப்."
            elif(token == 27):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" மே "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" மே "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" மே ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" மே "))
                else:
                    returnList.append(" மே ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" மே"))
#                 else:
#                     returnList.append(" மே")
    #             returnData = returnData + " மே"
            elif(token == 28):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஜூன் "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஜூன் "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஜூன் ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஜூன் "))
                else:
                    returnList.append(" ஜூன் ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூன்"))
#                 else:
#                     returnList.append(" ஜூன்")
    #             returnData = returnData + " ஜூன்"
            elif(token == 29):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஜூலை "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஜூலை "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஜூலை ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஜூலை "))
                else:
                    returnList.append(" ஜூலை ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஜூலை"))
#                 else:
#                     returnList.append(" ஜூலை")
    #             returnData = returnData + " ஜூலை"
            elif(token == 30):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" ஆக. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" ஆக. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" ஆக. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" ஆக. "))
                else:
                    returnList.append(" ஆக. ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" ஆக."))
#                 else:
#                     returnList.append(" ஆக.")
    #             returnData = returnData + " ஆக."
            elif(token == 31):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" செப். "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" செப். "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" செப். ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" செப். "))
                else:
                    returnList.append(" செப். ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" செப்."))
#                 else:
#                     returnList.append(" செப்.")
    #             returnData = returnData + " செப்."
            elif(token == 32):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" அக். "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" அக். "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" அக். ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" அக். "))
                else:
                    returnList.append(" அக். ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" அக்."))
#                 else:
#                     returnList.append(" அக்.")
    #             returnData = returnData + " அக்."
            elif(token == 33):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" நவ. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" நவ. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" நவ. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" நவ. "))
                else:
                    returnList.append(" நவ. ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" நவ."))
#                 else:
#                     returnList.append(" நவ.")
    #             returnData = returnData + " நவ."
            elif(token == 34):
                if((index+1)<len(newList) and (index-1)>=0 and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index-1][1] == 0) and (newList[index+2][1] in datesList)):
                    returnList.insert(-1, (" டிச. "))
                elif((index+1)<len(newList) and (index-1)>=0 and (newList[index+1][1] == 62) and (newList[index-1][1] == 0)):
                    returnList.insert(-1, (" டிச. "))
                elif((index+1)<len(newList) and (index+2)<len(newList) and (newList[index+1][1] == 62) and (newList[index+2][1] in datesList)):
                    returnList.append(' ')
                    returnList.append(' ')
                    returnList.append(" டிச. ")
#                    print(returnList)
                elif((index-1)>=0 and (newList[index-1][1] == 0)):
                    returnList.insert(-1,(" டிச. "))
                else:
                    returnList.append(" டிச. ")
#                 if(int(newList[index - 1][1]) == 7 or int(newList[index - 1][1]) == 8):
#                     returnList.insert(-1, (" டிச."))
#                 else:
#                     returnList.append(" டிச.")
    #             returnData = returnData + " டிச."
            elif(token == 35):
                returnList.append(" காலாண்டு")
    #             returnData = returnData + " காலாண்டு"
            elif(token == 36):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " ஞாயிறு ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " ஞாயிறு ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " ஞாயிறு ")
                else:
                    returnList.append(" ஞாயிறு ")
#                 returnList.append(" ஞாயிறு")
    #             returnData = returnData + " ஞாயிறு"
            elif(token == 37):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " திங்கள் ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " திங்கள் ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " திங்கள் ")
                else:
                    returnList.append(" திங்கள் ")
#                 returnList.append(" திங்கள்")
    #             returnData = returnData + " திங்கள்"
            elif(token == 38):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " செவ்வாய் ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " செவ்வாய் ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " செவ்வாய் ")
                else:
                    returnList.append(" செவ்வாய் ")
#                 returnList.append(" செவ்வாய்")
    #             returnData = returnData + " செவ்வாய்"
            elif(token == 39):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " புதன் ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " புதன் ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " புதன் ")
                else:
                    returnList.append(" புதன் ")
#                 returnList.append(" புதன்")
    #             returnData = returnData + " புதன்"
            elif(token == 40):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " வியாழன் ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " வியாழன் ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " வியாழன் ")
                else:
                    returnList.append(" வியாழன் ")
#                 returnList.append(" வியாழன்")
    #             returnData = returnData + " வியாழன்"
            elif(token == 41):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " வெள்ளி ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " வெள்ளி ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " வெள்ளி ")
                else:
                    returnList.append(" வெள்ளி ")
#                 returnList.append(" வெள்ளி")
    #             returnData = returnData + " வெள்ளி"
            elif(token == 42):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " சனி ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " சனி ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " சனி ")
                else:
                    returnList.append(" சனி ")
#                 returnList.append(" சனி")
    #             returnData = returnData + " சனி"
            elif(token == 43):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " ஞாயி. ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " ஞாயி. ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " ஞாயி. ")
                else:
                    returnList.append(" ஞாயி. ")
#                 returnList.append(" ஞாயி.")
    #             returnData = returnData + " ஞாயி."
            elif(token == 44):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " திங். ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " திங். ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " திங். ")
                else:
                    returnList.append(" திங். ")
#                 returnList.append(" திங்.")
    #             returnData = returnData + " திங்."
            elif(token == 45):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " செவ். ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " செவ். ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " செவ். ")
                else:
                    returnList.append(" செவ். ")
#                 returnList.append(" செவ்.")
    #             returnData = returnData + " செவ்."
            elif(token == 46):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " புத. ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " புத. ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " புத. ")
                else:
                    returnList.append(" புத. ")
#                 returnList.append(" புத.")
    #             returnData = returnData + " புத."
            elif(token == 47):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " வியா. ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " வியா. ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " வியா. ")
                else:
                    returnList.append(" வியா. ")
#                 returnList.append(" வியா.")
    #             returnData = returnData + " வியா."
            elif(token == 48):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " வெள். ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " வெள். ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " வெள். ")
                else:
                    returnList.append(" வெள். ")
#                 returnList.append(" வெள்.")
    #             returnData = returnData + " வெள்."
            elif(token == 49):
                if((index-1)>=0 and (index-2>=0) and (index-3)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList) and (newList[index-3][1] == 0)):
                    returnList.insert(-3, " சனி. ")
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] == 62) and(newList[index-2][1] in monthsList)):
                    returnList.insert(-2, " சனி. ")
                elif((index-1)>=0 and (newList[index-1][1] == 62)):
                    returnList.insert(-1, " சனி. ")
                else:
                    returnList.append(" சனி. ")
#                 returnList.append(" சனி.")
    #             returnData = returnData + " சனி."
            elif(token == 50):
                returnList.append(" நள்ளிரவு")
    #             returnData = returnData + " நள்ளிரவு"
            elif(token == 51):
                returnList.append(" நண்பகல்")
    #             returnData = returnData + " நண்பகல்"
            elif(token == 52):
                returnList.append(" அதிகாலை")
    #             returnData = returnData + " அதிகாலை"
            elif(token == 53):
                returnList.append(" மதியம்")
    #             returnData = returnData + " மதியம்"
            elif(token == 54):
                returnList.append(" மாலை")
    #             returnData = returnData + " மாலை"
            elif(token == 55):
                returnList.append(" இரவு")
    #             returnData = returnData + " இரவு"
            elif(token == 56):
                returnList.append(" பொ.ச.மு")
    #             returnData = returnData + " பொ.ச.மு"
            elif(token == 57):
                returnList.append(" பொ.ச")
    #             returnData = returnData + " பொ.ச"
            elif(token == 58):
                returnList.append(" கி.மு.")
    #             returnData = returnData + " கி.மு."
            elif(token == 59):
                returnList.append(" பொ.ச.மு")
    #             returnData = returnData + " பொ.ச.மு"
            elif(token == 60):
                returnList.append(" கி.பி.")
    #             returnData = returnData + " கி.பி."
            elif(token == 61):
                returnList.append(" பொ.ச.")
            elif(token == 62):
                if((index+1)< len(newList) and (index-2)>=0 and (index-1)>=0 and (newList[index+1][1] in datesList) and (newList[index-1][1] in monthsList) and (newList[index-2][1] == 0)):
                    returnList.insert(-2, (' ' + inputData + 'ம் திகதி '))
                elif((index-1)>=0 and (index+1)<=len(newList) and (newList[index+1][1] in datesList) and (newList[index-1][1] in monthsList)):
                    returnList.insert(-1, (' ' + (inputData) + 'ம் திகதி '))
                elif((index-1)>=0 and (index-2)>=0 and (newList[index-1][1] in monthsList) and (newList[index-1][1] == 0)):
                    returnList.insert(-2, (' ' + (inputData) + 'ம் திகதி '))
                elif((index+1)>=0 and (newList[index+1][1] in monthsList)):
                    returnList.insert(-1, (' ' + (inputData) + 'ம் திகதி '))
                elif((index+1)<len(newList) and (newList[index+1][1] in datesList)):
                    returnList.append(' ')
                    returnList.append((' ' + (inputData) + 'ம் திகதி '))
                else:
                    returnList.append((' ' + (inputData) + 'ம் திகதி '))
            else:
                if(inputData == 'of' or inputData == 'in' or inputData == 'වන' or inputData == 'වැනි'):
                    returnData = returnData
                else:
                    if((index+1)< len(newList) and (index+2)< len(newList) and (index+3)< len(newList) and (newList[index+2][1] == 62) and (newList[index+1][1] in monthsList) and (newList[index+3][1] in datesList)):
                        returnList.append(' ')
                        returnList.append(' ')
                        returnList.append(' ')
                        returnList.append((' ' + inputData + ' '))
                    elif((index+1)< len(newList) and (index+2)< len(newList) and (newList[index+2][1] == 62) and (newList[index+1][1] in monthsList)):
                        returnList.append(' ')
                        returnList.append(' ')
                        returnList.append((' ' + inputData + ' '))
                    elif((index+1)< len(newList) and (newList[index+1][1] in monthsList)):
                        returnList.append(' ')
                        returnList.append((' ' + inputData + ' '))
#                     elif((index+1)>=0 and (newList[index+1][1] in monthsList)):
#                         returnList.insert(-1, (' ' + (inputData) + 'ம் திகதி '))
#                     elif((index+1)<len(newList) and (newList[index+1][1] in datesList)):
#                         returnList.append(' ')
#                         returnList.append((' ' + (inputData) + 'ம் திகதி '))
                    else:
                        returnList.append((' ' + inputData + ' '))
#                     returnList.append(inputData)
    #                 returnData = returnData + inputData
        else:
            returnList = ['Error']
#         print(returnList)
    returnList = [ elem for elem in returnList if elem != ' ' ]
    return returnList


# In[71]:


# print(formatter([['08:56', 7], ['a.m.', 9]]))


# In[72]:


# print(formatter([['\xe0\xae\x9c\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xb0\xe0\xae\xbf', 11], ['\xe0\xae\x9c\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xb0\xe0\xae\xbf', 11], [u'02', 62], ['\xe0\xae\x9c\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xb0\xe0\xae\xbf', 11], ['2016', 0]]))


# In[73]:

#
#inpu = [['january', 11], ['10:30', 7], ['a.m.', 9], ['friday', 41], 1]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[74]:
#
#
#inpu = [['friday', 41], ['05', 62], ['of', 0], ['january', 11], ['10:30', 7], ['a.m.', 9], 1]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[75]:
#
#
#inpu = [['2014', 0], ['\xe0\xb6\xa2\xe0\xb6\xb1\xe0\xb7\x80\xe0\xb7\x8f\xe0\xb6\xbb\xe0\xb7\x92', 11], ['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 9], ['10:30', 7], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[76]:
#
#
#inpu = [['\xe0\xb6\xb4\xe0\xb7\x99.\xe0\xb7\x80.', 10], ['10:30', 7], 2]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[77]:
#
#
#inpu = [['14/12/2018', 2], 1]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[ ]:
#
#
#
#
#
## In[78]:
#
#
#inpu = [['sunday', 36], ['2', 62], ['of', 0], ['january', 11], ['2017', 0], ['10:30', 7], ['a.m.', 9], 1]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[79]:
#
#
#inpu = [['10:30', 7], ['a.m.', 9], 1]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[80]:
#
#
#inpu = [['14/12/2018', 2], 1]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[81]:
#
#
#inpu = [['2', 62], ['of', 0], ['january', 11], ['2017', 0], ['10:30', 7], ['a.m.', 9], 1]
#resul = formatter(inpu[:-1], inpu[-1])
#stri = ''
#print(resul)
#for i in resul:
#    try:
#        stri += (i)
#    except UnicodeDecodeError:
#        print('error')
#print(stri)
#
#
## In[ ]:
#
#
#
#
#
## In[ ]:
#
#
#

