#!/usr/bin/env python
# coding: utf-8

# In[7]:


def unitsMatcher(indexVal):
    if(indexVal == 1):
        return "meter"
    elif(indexVal == 2):
        return "metre"
    elif(indexVal == 3):
        return "millimeter"
    elif(indexVal == 4):
        return "centimeter"
    elif(indexVal == 5):
        return "decimeter"
    elif(indexVal == 6):
        return "kilometer"
    elif(indexVal == 7):
        return "light year"
    elif(indexVal == 8):
        return "inch"
    elif(indexVal == 9):
        return "foot"
    elif(indexVal == 10):
        return "mile"
#     ----------------
    elif(indexVal == 11):
        return "nautical mile"
    elif(indexVal == 12):
        return "square meter"
    elif(indexVal == 13):
        return "acre"
    elif(indexVal == 14):
        return "hectare"
    elif(indexVal == 15):
        return "square inches"
    elif(indexVal == 16):
        return "square feet"
    elif(indexVal == 17):
        return "square miles"
    elif(indexVal == 18):
        return "cubic meter"
    elif(indexVal == 19):
        return "liter"
    elif(indexVal == 20):
        return "milliliter"
#     ----------------
    elif(indexVal == 21):
        return "deciliter"
    elif(indexVal == 22):
        return "cubic inch"
    elif(indexVal == 23):
        return "cubic foot"
    elif(indexVal == 24):
        return "acre foot"
    elif(indexVal == 25):
        return "teaspoon"
    elif(indexVal == 26):
        return "tablespoon"
    elif(indexVal == 27):
        return "ounce"
    elif(indexVal == 28):
        return "cup"
    elif(indexVal == 29):
        return "pint"
    elif(indexVal == 30):
        return "quart"
#     ----------------
    elif(indexVal == 31):
        return "gallon"
    elif(indexVal == 32):
        return "radian"
    elif(indexVal == 33):
        return "degree"
    elif(indexVal == 34):
        return "second"
    elif(indexVal == 35):
        return "minute"
    elif(indexVal == 36):
        return "hour"
    elif(indexVal == 37):
        return "day"
    elif(indexVal == 38):
        return "year"
    elif(indexVal == 39):
        return "hertz"
    elif(indexVal == 40):
        return "angular frequency"
#     ----------------
    elif(indexVal == 41):
        return "decibel"
    elif(indexVal == 42):
        return "kilometers per second"
    elif(indexVal == 43):
        return "miles per hour"
    elif(indexVal == 44):
        return "meters per second"
    elif(indexVal == 45):
        return "feet per second"
    elif(indexVal == 46):
        return "grams"
    elif(indexVal == 47):
        return "kilogram"
    elif(indexVal == 48):
        return "pound"
    elif(indexVal == 49):
        return "density"
    elif(indexVal == 50):
        return "newton"
#     ----------------
    elif(indexVal == 51):
        return "newton meter"
    elif(indexVal == 52):
        return "joule"
    elif(indexVal == 53):
        return "watt"
    elif(indexVal == 54):
        return "kilowatt"
    elif(indexVal == 55):
        return "horsepower"
    elif(indexVal == 56):
        return "pascal"
    elif(indexVal == 57):
        return "bar"
    elif(indexVal == 58):
        return "kelvin"
    elif(indexVal == 59):
        return "centigrade"
    elif(indexVal == 60):
        return "calorie"
#     ----------------
    elif(indexVal == 61):
        return "fahrenheit"
    elif(indexVal == 62):
        return "ampere"
    elif(indexVal == 63):
        return "coulomb"
    elif(indexVal == 64):
        return "volt"
    elif(indexVal == 65):
        return "ohm"
    elif(indexVal == 66):
        return "siemens"
    elif(indexVal == 67):
        return "henry"
    elif(indexVal == 68):
        return "weber"
    elif(indexVal == 69):
        return "tesla"
    elif(indexVal == 70):
        return "becquerel"
#     ----------------
    elif(indexVal == 71):
        return "mole"
    elif(indexVal == 72):
        return "dozen"
    elif(indexVal == 73):
        return "avogadro constant"
    elif(indexVal == 74):
        return "boltzmann’s constant"
    elif(indexVal == 75):
        return "pi"
    elif(indexVal == 76):
        return "planck constant"
    elif(indexVal == 77):
        return "stefan-boltzmann constant"
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


# In[8]:


sList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,   172,173,174,175,176,177,178]


# In[9]:


def converterEn(inputList):
    unit = unitsMatcher(inputList[1])
    if(inputList[0] != 1 and (inputList[1] in sList)):
        return str(inputList[0]) + ' ' + unit + "s"
    return str(inputList[0]) + " " + (unit)


# In[ ]:



