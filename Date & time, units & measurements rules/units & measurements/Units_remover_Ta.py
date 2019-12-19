#!/usr/bin/env python
# coding: utf-8

# In[1]:


def unitsMatcher(unit):
    if(unit == "மீட்டர்"):
        return 1
    elif(unit == "மீட்டர்"):
        return 2
    elif(unit == "மில்லிமீட்டர்"):
        return 3
    elif(unit == "சென்டிமீட்டர்"):
        return 4
    elif(unit == "தசமமீற்றர்"):
        return 5
    elif(unit == "கிலோமீட்டர்"):
        return 6
    elif(unit == "ஒளிஆண்டு"):
        return 7
    elif(unit == "அங்குலம்"):
        return 8
    elif(unit == "பாத"):
        return 9
    elif(unit == "மைல்"):
        return 10
#     ----------------
    elif(unit == "கடல் மைல்"):
        return 11
    elif(unit == "சதுர மீட்டர்"):
        return 12
    elif(unit == "ஏக்கர்"):
        return 13
    elif(unit == "ஹெக்டேர்"):
        return 14
    elif(unit == "சதுர அங்குலம்"):
        return 15
    elif(unit == "சதுர அடி"):
        return 16
    elif(unit == "சதுர மைல்கள்"):
        return 17
    elif(unit == "கன மீட்டர்"):
        return 18
    elif(unit == "லிட்டர்"):
        return 19
    elif(unit == "மில்லிலிட்டர்"):
        return 20
#     ----------------
    elif(unit == "டெசிலிட்டர்"):
        return 21
    elif(unit == "கன அங்குலம்"):
        return 22
    elif(unit == "கன பாத"):
        return 23
    elif(unit == "ஏக்கர்-பாத"):
        return 24
    elif(unit == "தேக்கரண்டி"):
        return 25
    elif(unit == "தேக்கரண்டி"):
        return 26
    elif(unit == "அவுன்ஸ்"):
        return 27
    elif(unit == "கோப்பை"):
        return 28
    elif(unit == "பைண்ட்"):
        return 29
    elif(unit == "பைண்டு அளவு"):
        return 30
#     ----------------
    elif(unit == "கேலன்"):
        return 31
    elif(unit == "ரேடியன்"):
        return 32
    elif(unit == "பட்டம்"):
        return 33
    elif(unit == "இரண்டாவது"):
        return 34
    elif(unit == "மினிட்"):
        return 35
    elif(unit == "ஹவர்"):
        return 36
    elif(unit == "தினம்"):
        return 37
    elif(unit == "ஆண்டு"):
        return 38
    elif(unit == "ஹெர்ட்ஸ்"):
        return 39
    elif(unit == "கோண அதிர்வெண்"):
        return 40
#     ----------------
    elif(unit == "சத்தமான"):
        return 41
    elif(unit == "வினாடிக்கு கிலோமீட்டர்"):
        return 42
    elif(unit == "ஒரு மணி நேரத்திற்கு மைல்கள்"):
        return 43
    elif(unit == "வினாடிக்கு மீட்டர்"):
        return 44
    elif(unit == "வினாடிக்கு அடி"):
        return 45
    elif(unit == "கிராம்"):
        return 46
    elif(unit == "கிலோகிராம்"):
        return 47
    elif(unit == "பவுண்ட்"):
        return 48
    elif(unit == "அடர்த்தி"):
        return 49
    elif(unit == "நியூட்டன்"):
        return 50
#     ----------------
    elif(unit == "நியூட்டன் மீட்டர்"):
        return 51
    elif(unit == "ஜூல்"):
        return 52
    elif(unit == "வாட்"):
        return 53
    elif(unit == "கிலோவாட்"):
        return 54
    elif(unit == "குதிரைத்திறன்"):
        return 55
    elif(unit == "பாஸ்கல்"):
        return 56
    elif(unit == "பார்"):
        return 57
    elif(unit == "கெல்வின்"):
        return 58
    elif(unit == "சென்டிகிரேட்"):
        return 59
    elif(unit == "கலோரி"):
        return 60
#     ----------------
    elif(unit == "பாரன்ஹீட்"):
        return 61
    elif(unit == "ஆம்பியர்"):
        return 62
    elif(unit == "கூலோம்பின்"):
        return 63
    elif(unit == "வோல்ட்"):
        return 64
    elif(unit == "ஓம்"):
        return 65
    elif(unit == "சீமன்ஸ்"):
        return 66
    elif(unit == "ஹென்றி"):
        return 67
    elif(unit == "வெபர்"):
        return 68
    elif(unit == "டெஸ்லா"):
        return 69
    elif(unit == "பெக்கோரல்"):
        return 70
#     ----------------
    elif(unit == "மோல்"):
        return 71
    elif(unit == "டஜன்"):
        return 72
    elif(unit == "அவகாட்ரோ மாறிலி"):
        return 73
    elif(unit == "போல்ட்ஜ்மானின் மாறிலி"):
        return 74
    elif(unit == "பை"):
        return 75
    elif(unit == "பிளாங்க் மாறிலி"):
        return 76
    elif(unit == "ஸ்டீபன்-போல்ட்ஜ்மேன் மாறிலி"):
        return 77
    elif(unit == ("NB")):
        return 78
    elif(unit == ("µB")):
        return 79
    elif(unit == ("A0")):
        return 80
#     ----------------
    elif(unit == ("k")):
        return 81
    elif(unit == ("Mₑ")):
        return 82
    elif(unit == ("e") or unit == ("Qₑ")):
        return 83
    elif(unit == ("ɑ")):
        return 84
    elif(unit == ("G")):
        return 85
    elif(unit == ("1/ɑ")):
        return 86
    elif(unit == ("mn")):
        return 87
    elif(unit == ("µn")):
        return 88
    elif(unit == ("µ₀")):
        return 89
    elif(unit == ("Ε0")):
        return 90
#     ----------------
    elif(unit == ("π")):
        return 91
    elif(unit == ("h")):
        return 92
    elif(unit == ("Mp")):
        return 93
    elif(unit == ("c")):
        return 94
    elif(unit == ("σ")):
        return 95
    elif(unit == ("τ")):
        return 96
    elif(unit == ("u") or unit == ("Da")):
        return 97
    
#     ////////////////////////////

    elif(unit == "m"):
        return 98
    elif(unit == "mm"):
        return 99
    elif(unit == "cm"):
        return 100
#     ----------------
    elif(unit == "dm"):
        return 101
    elif(unit == "km"):
        return 102
    elif(unit == "in" or unit == "“"):
        return 103
    elif(unit == "ft"):
        return 104
    elif(unit == "mi"):
        return 105
    elif(unit == "sqm" or unit == "m²"):
        return 106
    elif(unit == "in²"):
        return 107
    elif(unit == "ft²"):
        return 108
    elif(unit == "mi²"):
        return 109
    elif(unit == "m³"):
        return 110
#     ----------------
    elif(unit == "l"):
        return 111
    elif(unit == "ml"):
        return 112
    elif(unit == "cl"):
        return 113
    elif(unit == "dl"):
        return 114
    elif(unit == "hl"):
        return 115
    elif(unit == "cu in" or unit == "in³"):
        return 116
    elif(unit == "cu ft" or unit == "ft³"):
        return 117
    elif(unit == "acre ft"):
        return 118
    elif(unit == "tsp"):
        return 119
    elif(unit == "tbsp"):
        return 120
#     ----------------
    elif(unit == "qt"):
        return 121
    elif(unit == "gal"):
        return 122
    elif(unit == "rad"):
        return 123
    elif(unit == "°" or unit == "deg"):
        return 124
    elif(unit == "s"):
        return 125
    elif(unit == "min"):
        return 126
    elif(unit == "h"):
        return 127
    elif(unit == "d"):
        return 128
    elif(unit == "Hz"):
        return 129
    elif(unit == "ω"):
        return 130
#     ----------------
    elif(unit == "dB"):
        return 131
    elif(unit == "kg m/s"):
        return 132
    elif(unit == "mph"):
        return 133
    elif(unit == "kph"):
        return 134
    elif(unit == "ft/s²"):
        return 135
    elif(unit == "m/s²"):
        return 136
    elif(unit == "ft/s"):
        return 137
    elif(unit == "g"):
        return 138
    elif(unit == "kg"):
        return 139
    elif(unit == "oz"):
        return 140
#     ----------------
    elif(unit == "lb"):
        return 141
    elif(unit == "ton"):
        return 142
    elif(unit == "t"):
        return 143
    elif(unit == "kg/m³"):
        return 144
    elif(unit == "N"):
        return 145
    elif(unit == "p"):
        return 146
    elif(unit == "Nm"):
        return 147
    elif(unit == "J"):
        return 148
    elif(unit == "w"):
        return 149
    elif(unit == "kw"):
        return 150
#     ----------------
    elif(unit == "hp"):
        return 151
    elif(unit == "Pa"):
        return 152
    elif(unit == "bar"):
        return 153
    elif(unit == "K"):
        return 154
    elif(unit == "°C"):
        return 155
    elif(unit == "°F"):
        return 156
    elif(unit == "cd"):
        return 157
    elif(unit == "A"):
        return 158
    elif(unit == "Amps"):
        return 159
    elif(unit == "C"):
        return 160
#     ----------------
    elif(unit == "V"):
        return 161
    elif(unit == "Ω"):
        return 162
    elif(unit == "F"):
        return 163
    elif(unit == "S"):
        return 164
    elif(unit == "H"):
        return 165
    elif(unit == "Wb"):
        return 166
    elif(unit == "T"):
        return 167
    elif(unit == "Bq"):
        return 168
    elif(unit == "mol"):
        return 169
    elif(unit == "dz"):
        return 170
#     ----------------
    elif(unit == "doz"):
        return 171
    elif(unit == "centiliter"):
        return 172
    elif(unit == "hectoliter"):
        return 173
    elif(unit == "steradian"):
        return 174
    elif(unit == "ton"):
        return 175
    elif(unit == "kilopond"):
        return 176
    elif(unit == "candela"):
        return 177
    elif(unit == "farad"):
        return 178
    elif(unit == "tau"):
        return 179
    elif(unit == "yotta"):
        return 180
#     ----------------
    elif(unit == "zetta"):
        return 181
    elif(unit == "exa"):
        return 182
    elif(unit == "peta"):
        return 183
    elif(unit == "tera"):
        return 184
    elif(unit == "giga"):
        return 185
    elif(unit == "mega"):
        return 186
    elif(unit == "kilo"):
        return 187
    elif(unit == "hecto"):
        return 188
    elif(unit == "deka"):
        return 189
    elif(unit == "deci"):
        return 190
#     ----------------
    elif(unit == "centi"):
        return 191
    elif(unit == "milli"):
        return 192
    elif(unit == "micro"):
        return 193
    elif(unit == "nano"):
        return 194
    elif(unit == "pico"):
        return 195
    elif(unit == "femto"):
        return 196
    elif(unit == "atto"):
        return 197
    elif(unit == "zepto"):
        return 198
    elif(unit == "yocto"):
        return 199
    
#     ////////////////////
    elif(unit == "AE"):
        return 200
#     ----------------
    elif(unit == "lj"):
        return 201
    elif(unit == "pc"):
        return 202
    elif(unit == "sr"):
        return 203
    elif(unit == "m/s"):
        return 204
    elif(unit == "gr"):
        return 205
    elif(unit == "dr"):
        return 206
    elif(unit == "cwt"):
        return 207
    elif(unit == "slug"):
        return 208
    elif(unit == "den" or unit == "D"):
        return 209
    elif(unit == "tex"):
        return 210
#     ----------------
    elif(unit == "dtex"):
        return 211
    elif(unit == "mm"):
        return 212
    elif(unit == "psi" or unit == "lbf/in²"):
        return 213
    elif(unit == "Cal" or unit == "kcal/cal"):
        return 214
    elif(unit == "cd/m²"):
        return 215
    elif(unit == "lm"):
        return 216
    elif(unit == "lx"):
        return 217
    elif(unit == "ls"):
        return 218
    elif(unit == "dpt"):
        return 219
    elif(unit == "ream"):
        return 220
# #     ----------------
#     elif(unit == ""):
#         return 161
#     elif(unit == ""):
#         return 162
#     elif(unit == ""):
#         return 163
#     elif(unit == ""):
#         return 164
#     elif(unit == ""):
#         return 165
#     elif(unit == ""):
#         return 166
#     elif(unit == ""):
#         return 167
#     elif(unit == ""):
#         return 168
#     elif(unit == ""):
#         return 169
#     elif(unit == ""):
#         return 170
# #     ----------------
#     elif(unit == ""):
#         return 161
#     elif(unit == ""):
#         return 162
#     elif(unit == ""):
#         return 163
#     elif(unit == ""):
#         return 164
#     elif(unit == ""):
#         return 165
#     elif(unit == ""):
#         return 166
#     elif(unit == ""):
#         return 167
#     elif(unit == ""):
#         return 168
#     elif(unit == ""):
#         return 169
#     elif(unit == ""):
#         return 170
# #     ----------------
#     elif(unit == ""):
#         return 161
#     elif(unit == ""):
#         return 162
#     elif(unit == ""):
#         return 163
#     elif(unit == ""):
#         return 164
#     elif(unit == ""):
#         return 165
#     elif(unit == ""):
#         return 166
#     elif(unit == ""):
#         return 167
#     elif(unit == ""):
#         return 168
#     elif(unit == ""):
#         return 169
#     elif(unit == ""):
#         return 170
# #     ----------------
    else:
        return 0


# In[2]:


def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


# In[3]:


def formatterTa(inputData):
    stringVal = []
    inputData = " ".join(inputData.split())
    splittedArray = inputData.split(" ", 1)
    if(isFloat(splittedArray[0])):
        stringVal.append(float(splittedArray[0]))
        stringVal.append(unitsMatcher(splittedArray[1]))
    else:
        splittedArray = inputData.rsplit(" ", 1)
        stringVal.append(float(splittedArray[1]))
        stringVal.append(unitsMatcher(splittedArray[0]))
        
#     if(isFloat(splittedArray[1])):
#         stringVal.append(float(splittedArray[1]))
#     if(not isFloat(splittedArray[0])):
#         stringVal.append(unitsMatcher(splittedArray[0]))
#     if(isFloat(splittedArray[0])):
#         stringVal.append(splittedArray[0])
#     if(not isFloat(splittedArray[1])):
#         stringVal.append(unitsMatcher(splittedArray[1]))
    return stringVal


# In[ ]:

