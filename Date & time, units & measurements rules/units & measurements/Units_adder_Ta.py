#!/usr/bin/env python
# coding: utf-8

# In[1]:


def unitsMatcher(indexVal):
    if(indexVal == 1):
        return "மீட்டர்"
    elif(indexVal == 2):
        return "மீட்டர்"
    elif(indexVal == 3):
        return "மில்லிமீட்டர்"
    elif(indexVal == 4):
        return "சென்டிமீட்டர்"
    elif(indexVal == 5):
        return "தசமமீற்றர்"
    elif(indexVal == 6):
        return "கிலோமீட்டர்"
    elif(indexVal == 7):
        return "ஒளிஆண்டு"
    elif(indexVal == 8):
        return "அங்குலம்"
    elif(indexVal == 9):
        return "பாத"
    elif(indexVal == 10):
        return "மைல்"
#     ----------------
    elif(indexVal == 11):
        return "கடல் மைல்"
    elif(indexVal == 12):
        return "சதுர மீட்டர்"
    elif(indexVal == 13):
        return "ஏக்கர்"
    elif(indexVal == 14):
        return "ஹெக்டேர்"
    elif(indexVal == 15):
        return "சதுர அங்குலம்"
    elif(indexVal == 16):
        return "சதுர அடி"
    elif(indexVal == 17):
        return "சதுர மைல்கள்"
    elif(indexVal == 18):
        return "கன மீட்டர்"
    elif(indexVal == 19):
        return "லிட்டர்"
    elif(indexVal == 20):
        return "மில்லிலிட்டர்"
#     ----------------
    elif(indexVal == 21):
        return "டெசிலிட்டர்"
    elif(indexVal == 22):
        return "கன அங்குலம்"
    elif(indexVal == 23):
        return "கன பாத"
    elif(indexVal == 24):
        return "ஏக்கர் பாத"
    elif(indexVal == 25):
        return "தேக்கரண்டி"
    elif(indexVal == 26):
        return "தேக்கரண்டி"
    elif(indexVal == 27):
        return "அவுன்ஸ்"
    elif(indexVal == 28):
        return "கோப்பை"
    elif(indexVal == 29):
        return "பைண்ட்"
    elif(indexVal == 30):
        return "பைண்டு அளவு"
#     ----------------
    elif(indexVal == 31):
        return "கேலன்"
    elif(indexVal == 32):
        return "ரேடியன்"
    elif(indexVal == 33):
        return "பட்டம்"
    elif(indexVal == 34):
        return "இரண்டாவது"
    elif(indexVal == 35):
        return "மினிட்"
    elif(indexVal == 36):
        return "ஹவர்"
    elif(indexVal == 37):
        return "தினம்"
    elif(indexVal == 38):
        return "ஆண்டு"
    elif(indexVal == 39):
        return "ஹெர்ட்ஸ்"
    elif(indexVal == 40):
        return "கோண அதிர்வெண்"
#     ----------------
    elif(indexVal == 41):
        return "சத்தமான"
    elif(indexVal == 42):
        return "வினாடிக்கு கிலோமீட்டர்"
    elif(indexVal == 43):
        return "ஒரு மணி நேரத்திற்கு மைல்கள்"
    elif(indexVal == 44):
        return "வினாடிக்கு மீட்டர்"
    elif(indexVal == 45):
        return "வினாடிக்கு அடி"
    elif(indexVal == 46):
        return "கிராம்"
    elif(indexVal == 47):
        return "கிலோகிராம்"
    elif(indexVal == 48):
        return "பவுண்ட்"
    elif(indexVal == 49):
        return "அடர்த்தி"
    elif(indexVal == 50):
        return "நியூட்டன்"
#     ----------------
    elif(indexVal == 51):
        return "நியூட்டன் மீட்டர்"
    elif(indexVal == 52):
        return "ஜூல்"
    elif(indexVal == 53):
        return "வாட்"
    elif(indexVal == 54):
        return "கிலோவாட்"
    elif(indexVal == 55):
        return "குதிரைத்திறன்"
    elif(indexVal == 56):
        return "பாஸ்கல்"
    elif(indexVal == 57):
        return "பார்"
    elif(indexVal == 58):
        return "கெல்வின்"
    elif(indexVal == 59):
        return "சென்டிகிரேட்"
    elif(indexVal == 60):
        return "கலோரி"
#     ----------------
    elif(indexVal == 61):
        return "பாரன்ஹீட்"
    elif(indexVal == 62):
        return "ஆம்பியர்"
    elif(indexVal == 63):
        return "கூலோம்பின்"
    elif(indexVal == 64):
        return "வோல்ட்"
    elif(indexVal == 65):
        return "ஓம்"
    elif(indexVal == 66):
        return "சீமன்ஸ்"
    elif(indexVal == 67):
        return "ஹென்றி"
    elif(indexVal == 68):
        return "வெபர்"
    elif(indexVal == 69):
        return "டெஸ்லா"
    elif(indexVal == 70):
        return "பெக்கோரல்"
#     ----------------
    elif(indexVal == 71):
        return "மோல்"
    elif(indexVal == 72):
        return "டஜன்"
    elif(indexVal == 73):
        return "அவகாட்ரோ மாறிலி"
    elif(indexVal == 74):
        return "போல்ட்ஜ்மானின் மாறிலி"
    elif(indexVal == 75):
        return "பை"
    elif(indexVal == 76):
        return "பிளாங்க் மாறிலி"
    elif(indexVal == 77):
        return "ஸ்டீபன்-போல்ட்ஜ்மேன் மாறிலி"
    elif(indexVal == 78):
        return ("NB")
    elif(indexVal == 79):
        return ("µB")
    elif(indexVal == 80):
        return ("A0")
#     ----------------
    elif(indexVal == 81):
        return ("k")
    elif(indexVal == 82):
        return ("Mₑ")
    elif(indexVal == 83):
        return ("Qₑ")
    elif(indexVal == 84):
        return ("ɑ")
    elif(indexVal == 85):
        return ("G")
    elif(indexVal == 86):
        return ("1/ɑ")
    elif(indexVal == 87):
        return ("mn")
    elif(indexVal == 88):
        return ("µn")
    elif(indexVal == 89):
        return ("µ₀")
    elif(indexVal == 90):
        return ("Ε0")
#     ----------------
    elif(indexVal == 91):
        return ("π")
    elif(indexVal == 92):
        return ("h")
    elif(indexVal == 93):
        return ("Mp")
    elif(indexVal == 94):
        return ("c")
    elif(indexVal == 95):
        return ("σ")
    elif(indexVal == 96):
        return ("τ")
    elif(indexVal == 97):
        return ("Da")
    
#     ////////////////////////////

    elif(indexVal == 98):
        return "m"
    elif(indexVal == 99):
        return "mm"
    elif(indexVal == 100):
        return "cm"
#     ----------------
    elif(indexVal == 101):
        return "dm"
    elif(indexVal == 102):
        return "km"
    elif(indexVal == 103):
        return "in"
    elif(indexVal == 104):
        return "ft"
    elif(indexVal == 105):
        return "mi"
    elif(indexVal == 106):
        return "m²"
    elif(indexVal == 107):
        return "in²"
    elif(indexVal == 108):
        return "ft²"
    elif(indexVal == 109):
        return "mi²"
    elif(indexVal == 110):
        return "m³"
#     ----------------
    elif(indexVal == 111):
        return "l"
    elif(indexVal == 112):
        return "ml"
    elif(indexVal == 113):
        return "cl"
    elif(indexVal == 114):
        return "dl"
    elif(indexVal == 115):
        return "hl"
    elif(indexVal == 116):
        return "in³"
    elif(indexVal == 117):
        return "ft³"
    elif(indexVal == 118):
        return "acre ft"
    elif(indexVal == 119):
        return "tsp"
    elif(indexVal == 120):
        return "tbsp"
#     ----------------
    elif(indexVal == 121):
        return "qt"
    elif(indexVal == 122):
        return "gal"
    elif(indexVal == 123):
        return "rad"
    elif(indexVal == 124):
        return "deg"
    elif(indexVal == 125):
        return "s"
    elif(indexVal == 126):
        return "min"
    elif(indexVal == 127):
        return "h"
    elif(indexVal == 128):
        return "d"
    elif(indexVal == 129):
        return "Hz"
    elif(indexVal == 130):
        return "ω"
#     ----------------
    elif(indexVal == 131):
        return "dB"
    elif(indexVal == 132):
        return "kg m/s"
    elif(indexVal == 133):
        return "mph"
    elif(indexVal == 134):
        return "kph"
    elif(indexVal == 135):
        return "ft/s²"
    elif(indexVal == 136):
        return "m/s²"
    elif(indexVal == 137):
        return "ft/s"
    elif(indexVal == 138):
        return "g"
    elif(indexVal == 139):
        return "kg"
    elif(indexVal == 140):
        return "oz"
#     ----------------
    elif(indexVal == 141):
        return "lb"
    elif(indexVal == 142):
        return "ton"
    elif(indexVal == 143):
        return "t"
    elif(indexVal == 144):
        return "kg/m³"
    elif(indexVal == 145):
        return "N"
    elif(indexVal == 146):
        return "p"
    elif(indexVal == 147):
        return "Nm"
    elif(indexVal == 148):
        return "J"
    elif(indexVal == 149):
        return "w"
    elif(indexVal == 150):
        return "kw"
#     ----------------
    elif(indexVal == 151):
        return "hp"
    elif(indexVal == 152):
        return "Pa"
    elif(indexVal == 153):
        return "bar"
    elif(indexVal == 154):
        return "K"
    elif(indexVal == 155):
        return "°C"
    elif(indexVal == 156):
        return "°F"
    elif(indexVal == 157):
        return "cd"
    elif(indexVal == 158):
        return "A"
    elif(indexVal == 159):
        return "Amps"
    elif(indexVal == 160):
        return "C"
#     ----------------
    elif(indexVal == 161):
        return "V"
    elif(indexVal == 162):
        return "Ω"
    elif(indexVal == 163):
        return "F"
    elif(indexVal == 164):
        return "S"
    elif(indexVal == 165):
        return "H"
    elif(indexVal == 166):
        return "Wb"
    elif(indexVal == 167):
        return "T"
    elif(indexVal == 168):
        return "Bq"
    elif(indexVal == 169):
        return "mol"
    elif(indexVal == 170):
        return "dz"
#     ----------------
    elif(indexVal == 171):
        return "doz"
    elif(indexVal == 172):
        return "centiliter"
    elif(indexVal == 173):
        return "hectoliter"
    elif(indexVal == 174):
        return "steradian"
    elif(indexVal == 175):
        return "ton"
    elif(indexVal == 176):
        return "kilopond"
    elif(indexVal == 177):
        return "candela"
    elif(indexVal == 178):
        return "farad"
    elif(indexVal == 179):
        return "tau"
    elif(indexVal == 180):
        return "yotta"
#     ----------------
    elif(indexVal == 181):
        return "zetta"
    elif(indexVal == 182):
        return "exa"
    elif(indexVal == 183):
        return "peta"
    elif(indexVal == 184):
        return "tera"
    elif(indexVal == 185):
        return "giga"
    elif(indexVal == 186):
        return "mega"
    elif(indexVal == 187):
        return "kilo"
    elif(indexVal == 188):
        return "hecto"
    elif(indexVal == 189):
        return "deka"
    elif(indexVal == 190):
        return "deci"
#     ----------------
    elif(indexVal == 191):
        return "centi"
    elif(indexVal == 192):
        return "milli"
    elif(indexVal == 193):
        return "micro"
    elif(indexVal == 194):
        return "nano"
    elif(indexVal == 195):
        return "pico"
    elif(indexVal == 196):
        return "femto"
    elif(indexVal == 197):
        return "atto"
    elif(indexVal == 198):
        return "zepto"
    elif(indexVal == 199):
        return "yocto"
    
#     ////////////////////
    elif(indexVal == 200):
        return "AE"
#     ----------------
    elif(indexVal == 201):
        return "lj"
    elif(indexVal == 202):
        return "pc"
    elif(indexVal == 203):
        return "sr"
    elif(indexVal == 204):
        return "m/s"
    elif(indexVal == 205):
        return "gr"
    elif(indexVal == 206):
        return "dr"
    elif(indexVal == 207):
        return "cwt"
    elif(indexVal == 208):
        return "slug"
    elif(indexVal == 209):
        return "den"
    elif(indexVal == 210):
        return "tex"
#     ----------------
    elif(indexVal == 211):
        return "dtex"
    elif(indexVal == 212):
        return "mm"
    elif(indexVal == 213):
        return "lbf/in²"
    elif(indexVal == 214):
        return "Cal"
    elif(indexVal == 215):
        return "cd/m²"
    elif(indexVal == 216):
        return "lm"
    elif(indexVal == 217):
        return "lx"
    elif(indexVal == 218):
        return "ls"
    elif(indexVal == 219):
        return "dpt"
    elif(indexVal == 220):
        return "ream"
# #     ----------------
#     elif(indexVal == ""):
#         return 161
#     elif(indexVal == ""):
#         return 162
#     elif(indexVal == ""):
#         return 163
#     elif(indexVal == ""):
#         return 164
#     elif(indexVal == ""):
#         return 165
#     elif(indexVal == ""):
#         return 166
#     elif(indexVal == ""):
#         return 167
#     elif(indexVal == ""):
#         return 168
#     elif(indexVal == ""):
#         return 169
#     elif(indexVal == ""):
#         return 170
# #     ----------------
#     elif(indexVal == ""):
#         return 161
#     elif(indexVal == ""):
#         return 162
#     elif(indexVal == ""):
#         return 163
#     elif(indexVal == ""):
#         return 164
#     elif(indexVal == ""):
#         return 165
#     elif(indexVal == ""):
#         return 166
#     elif(indexVal == ""):
#         return 167
#     elif(indexVal == ""):
#         return 168
#     elif(indexVal == ""):
#         return 169
#     elif(indexVal == ""):
#         return 170
# #     ----------------
#     elif(indexVal == ""):
#         return 161
#     elif(indexVal == ""):
#         return 162
#     elif(indexVal == ""):
#         return 163
#     elif(indexVal == ""):
#         return 164
#     elif(indexVal == ""):
#         return 165
#     elif(indexVal == ""):
#         return 166
#     elif(indexVal == ""):
#         return 167
#     elif(indexVal == ""):
#         return 168
#     elif(indexVal == ""):
#         return 169
#     elif(indexVal == ""):
#         return 170
# #     ----------------
    else:
        return 0


# In[2]:


sList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,   172,173,174,175,176,177,178]


# In[3]:


def converterTa(inputList):
    unit = unitsMatcher(inputList[1])
    if(inputList[1] in sList):
        return unit + ' ' + str(inputList[0])
    return str(inputList[0]) + " " + unit


# In[ ]:


