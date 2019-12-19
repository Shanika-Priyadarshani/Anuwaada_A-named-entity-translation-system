#!/usr/bin/env python
# coding: utf-8

# In[1]:


def unitsMatcher(unit):
    if(unit.lower() == "meter" or unit.lower() == "meters"):
        return 1
    elif(unit.lower() == "metre" or unit.lower() == "metres"):
        return 2
    elif(unit.lower() == "millimeter" or unit.lower() == "millimeters"):
        return 3
    elif(unit.lower() == "centimeter" or unit.lower() == "centimeters"):
        return 4
    elif(unit.lower() == "decimeter" or unit.lower() == "decimeters"):
        return 5
    elif(unit.lower() == "kilometer" or unit.lower() == "kilometers"):
        return 6
    elif(unit.lower() == "light year" or unit.lower() == "light years"):
        return 7
    elif(unit.lower() == "inch" or unit.lower() == "inchs"):
        return 8
    elif(unit.lower() == "foot" or unit.lower() == "foots"):
        return 9
    elif(unit.lower() == "mile" or unit.lower() == "miles"):
        return 10
#     ----------------
    elif(unit.lower() == "nautical mile" or unit.lower() == "nautical miles"):
        return 11
    elif(unit.lower() == "square meter" or unit.lower() == "square meters"):
        return 12
    elif(unit.lower() == "acre" or unit.lower() == "acres"):
        return 13
    elif(unit.lower() == "hectare" or unit.lower() == "hectares"):
        return 14
    elif(unit.lower() == "square inche" or unit.lower() == "square inches"):
        return 15
    elif(unit.lower() == "square feet" or unit.lower() == "square feets"):
        return 16
    elif(unit.lower() == "square mile" or unit.lower() == "square miles"):
        return 17
    elif(unit.lower() == "cubic meter" or unit.lower() == "cubic meters"):
        return 18
    elif(unit.lower() == "liter" or unit.lower() == "liters"):
        return 19
    elif(unit.lower() == "milliliter" or unit.lower() == "milliliters"):
        return 20
#     ----------------
    elif(unit.lower() == "deciliter" or unit.lower() == "deciliters"):
        return 21
    elif(unit.lower() == "cubic inch" or unit.lower() == "cubic inchs"):
        return 22
    elif(unit.lower() == "cubic foot" or unit.lower() == "cubic foots"):
        return 23
    elif(unit.lower() == "acre foot" or unit.lower() == "acre foots"):
        return 24
    elif(unit.lower() == "teaspoon" or unit.lower() == "teaspoons"):
        return 25
    elif(unit.lower() == "tablespoon" or unit.lower() == "tablespoons"):
        return 26
    elif(unit.lower() == "ounce" or unit.lower() == "ounces"):
        return 27
    elif(unit.lower() == "cup" or unit.lower() == "cups"):
        return 28
    elif(unit.lower() == "pint" or unit.lower() == "pints"):
        return 29
    elif(unit.lower() == "quart" or unit.lower() == "quarts"):
        return 30
#     ----------------
    elif(unit.lower() == "gallon" or unit.lower() == "gallons"):
        return 31
    elif(unit.lower() == "radian" or unit.lower() == "radians"):
        return 32
    elif(unit.lower() == "degree" or unit.lower() == "degrees"):
        return 33
    elif(unit.lower() == "second" or unit.lower() == "seconds"):
        return 34
    elif(unit.lower() == "minute" or unit.lower() == "minutes"):
        return 35
    elif(unit.lower() == "hour" or unit.lower() == "hours"):
        return 36
    elif(unit.lower() == "day" or unit.lower() == "days"):
        return 37
    elif(unit.lower() == "year" or unit.lower() == "years"):
        return 38
    elif(unit.lower() == "hertz" or unit.lower() == "hertzs"):
        return 39
    elif(unit.lower() == "angular frequency" or unit.lower() == "angular frequencies"):
        return 40
#     ----------------
    elif(unit.lower() == "decibel" or unit.lower() == "decibels"):
        return 41
    elif(unit.lower() == "kilometer per second" or unit.lower() == "kilometers per second"):
        return 42
    elif(unit.lower() == "mile per hour" or unit.lower() == "miles per hour"):
        return 43
    elif(unit.lower() == "meter per second" or unit.lower() == "meters per second"):
        return 44
    elif(unit.lower() == "feet per second" or unit.lower() == "feets per second"):
        return 45
    elif(unit.lower() == "gram" or unit.lower() == "grams"):
        return 46
    elif(unit.lower() == "kilogram" or unit.lower() == "kilograms"):
        return 47
    elif(unit.lower() == "pound" or unit.lower() == "pounds"):
        return 48
    elif(unit.lower() == "density" or unit.lower() == "densities"):
        return 49
    elif(unit.lower() == "newton" or unit.lower() == "newtons"):
        return 50
#     ----------------
    elif(unit.lower() == "newton meter" or unit.lower() == "newton meters"):
        return 51
    elif(unit.lower() == "joule" or unit.lower() == "joules"):
        return 52
    elif(unit.lower() == "watt" or unit.lower() == "watts"):
        return 53
    elif(unit.lower() == "kilowatt" or unit.lower() == "kilowatts"):
        return 54
    elif(unit.lower() == "horsepower" or unit.lower() == "horsepowers"):
        return 55
    elif(unit.lower() == "pascal" or unit.lower() == "pascals"):
        return 56
    elif(unit.lower() == "bar" or unit.lower() == "bars"):
        return 57
    elif(unit.lower() == "kelvin" or unit.lower() == "kelvins"):
        return 58
    elif(unit.lower() == "centigrade" or unit.lower() == "centigrades"):
        return 59
    elif(unit.lower() == "calorie" or unit.lower() == "calories"):
        return 60
#     ----------------
    elif(unit.lower() == "fahrenheit" or unit.lower() == "fahrenheits"):
        return 61
    elif(unit.lower() == "ampere" or unit.lower() == "amperes"):
        return 62
    elif(unit.lower() == "coulomb" or unit.lower() == "coulombs"):
        return 63
    elif(unit.lower() == "volt" or unit.lower() == "volts"):
        return 64
    elif(unit.lower() == "ohm" or unit.lower() == "ohms"):
        return 65
    elif(unit.lower() == "siemen" or unit.lower() == "siemens"):
        return 66
    elif(unit.lower() == "henry" or unit.lower() == "henrys"):
        return 67
    elif(unit.lower() == "weber" or unit.lower() == "webers"):
        return 68
    elif(unit.lower() == "tesla" or unit.lower() == "teslas"):
        return 69
    elif(unit.lower() == "becquerel" or unit.lower() == "becquerels"):
        return 70
#     ----------------
    elif(unit.lower() == "mole" or unit.lower() == "moles"):
        return 71
    elif(unit.lower() == "dozen" or unit.lower() == "dozens"):
        return 72
    elif(unit.lower() == "avogadro constant"):
        return 73
    elif(unit.lower() == "boltzmann’s constant"):
        return 74
    elif(unit.lower() == "pi"):
        return 75
    elif(unit.lower() == "planck constant"):
        return 76
    elif(unit.lower() == "stefan-boltzmann constant"):
        return 77
    elif(unit.lower() == ("NB")):
        return 78
    elif(unit.lower() == ("µB")):
        return 79
    elif(unit.lower() == ("A0")):
        return 80
#     ----------------
    elif(unit.lower() == ("k")):
        return 81
    elif(unit.lower() == ("Mₑ")):
        return 82
    elif(unit.lower() == ("e") or unit.lower() == ("Qₑ")):
        return 83
    elif(unit.lower() == ("ɑ")):
        return 84
    elif(unit.lower() == ("G")):
        return 85
    elif(unit.lower() == ("1/ɑ")):
        return 86
    elif(unit.lower() == ("mn")):
        return 87
    elif(unit.lower() == ("µn")):
        return 88
    elif(unit.lower() == ("µ₀")):
        return 89
    elif(unit.lower() == ("Ε0")):
        return 90
#     ----------------
    elif(unit.lower() == ("π")):
        return 91
    elif(unit.lower() == ("h")):
        return 92
    elif(unit.lower() == ("Mp")):
        return 93
    elif(unit.lower() == ("c")):
        return 94
    elif(unit.lower() == ("σ")):
        return 95
    elif(unit.lower() == ("τ")):
        return 96
    elif(unit.lower() == ("u") or unit.lower() == ("Da")):
        return 97
    
#     ////////////////////////////

    elif(unit.lower() == "m"):
        return 98
    elif(unit.lower() == "mm"):
        return 99
    elif(unit.lower() == "cm"):
        return 100
#     ----------------
    elif(unit.lower() == "dm"):
        return 101
    elif(unit.lower() == "km"):
        return 102
    elif(unit.lower() == "in" or unit.lower() == "“"):
        return 103
    elif(unit.lower() == "ft"):
        return 104
    elif(unit.lower() == "mi"):
        return 105
    elif(unit.lower() == "sqm" or unit.lower() == "m²"):
        return 106
    elif(unit.lower() == "in²"):
        return 107
    elif(unit.lower() == "ft²"):
        return 108
    elif(unit.lower() == "mi²"):
        return 109
    elif(unit.lower() == "m³"):
        return 110
#     ----------------
    elif(unit.lower() == "l"):
        return 111
    elif(unit.lower() == "ml"):
        return 112
    elif(unit.lower() == "cl"):
        return 113
    elif(unit.lower() == "dl"):
        return 114
    elif(unit.lower() == "hl"):
        return 115
    elif(unit.lower() == "cu in" or unit.lower() == "in³"):
        return 116
    elif(unit.lower() == "cu ft" or unit.lower() == "ft³"):
        return 117
    elif(unit.lower() == "acre ft"):
        return 118
    elif(unit.lower() == "tsp"):
        return 119
    elif(unit.lower() == "tbsp"):
        return 120
#     ----------------
    elif(unit.lower() == "qt"):
        return 121
    elif(unit.lower() == "gal"):
        return 122
    elif(unit.lower() == "rad"):
        return 123
    elif(unit.lower() == "°" or unit.lower() == "deg"):
        return 124
    elif(unit.lower() == "s"):
        return 125
    elif(unit.lower() == "min"):
        return 126
    elif(unit.lower() == "h"):
        return 127
    elif(unit.lower() == "d"):
        return 128
    elif(unit.lower() == "Hz"):
        return 129
    elif(unit.lower() == "ω"):
        return 130
#     ----------------
    elif(unit.lower() == "dB"):
        return 131
    elif(unit.lower() == "kg m/s"):
        return 132
    elif(unit.lower() == "mph"):
        return 133
    elif(unit.lower() == "kph"):
        return 134
    elif(unit.lower() == "ft/s²"):
        return 135
    elif(unit.lower() == "m/s²"):
        return 136
    elif(unit.lower() == "ft/s"):
        return 137
    elif(unit.lower() == "g"):
        return 138
    elif(unit.lower() == "kg"):
        return 139
    elif(unit.lower() == "oz"):
        return 140
#     ----------------
    elif(unit.lower() == "lb"):
        return 141
    elif(unit.lower() == "ton"):
        return 142
    elif(unit.lower() == "t"):
        return 143
    elif(unit.lower() == "kg/m³"):
        return 144
    elif(unit.lower() == "N"):
        return 145
    elif(unit.lower() == "p"):
        return 146
    elif(unit.lower() == "Nm"):
        return 147
    elif(unit.lower() == "J"):
        return 148
    elif(unit.lower() == "w"):
        return 149
    elif(unit.lower() == "kw"):
        return 150
#     ----------------
    elif(unit.lower() == "hp"):
        return 151
    elif(unit.lower() == "Pa"):
        return 152
    elif(unit.lower() == "bar"):
        return 153
    elif(unit.lower() == "K"):
        return 154
    elif(unit.lower() == "°C"):
        return 155
    elif(unit.lower() == "°F"):
        return 156
    elif(unit.lower() == "cd"):
        return 157
    elif(unit.lower() == "A"):
        return 158
    elif(unit.lower() == "Amps"):
        return 159
    elif(unit.lower() == "C"):
        return 160
#     ----------------
    elif(unit.lower() == "V"):
        return 161
    elif(unit.lower() == "Ω"):
        return 162
    elif(unit.lower() == "F"):
        return 163
    elif(unit.lower() == "S"):
        return 164
    elif(unit.lower() == "H"):
        return 165
    elif(unit.lower() == "Wb"):
        return 166
    elif(unit.lower() == "T"):
        return 167
    elif(unit.lower() == "Bq"):
        return 168
    elif(unit.lower() == "mol"):
        return 169
    elif(unit.lower() == "dz"):
        return 170
#     ----------------
    elif(unit.lower() == "doz"):
        return 171
    elif(unit.lower() == "centiliter" or unit.lower() == "centiliters"):
        return 172
    elif(unit.lower() == "hectoliter" or unit.lower() == "hectoliters"):
        return 173
    elif(unit.lower() == "steradian" or unit.lower() == "steradians"):
        return 174
    elif(unit.lower() == "ton" or unit.lower() == "tons"):
        return 175
    elif(unit.lower() == "kilopond" or unit.lower() == "kiloponds"):
        return 176
    elif(unit.lower() == "candela" or unit.lower() == "candelas"):
        return 177
    elif(unit.lower() == "farad" or unit.lower() == "farads"):
        return 178
    elif(unit.lower() == "tau"):
        return 179
    elif(unit.lower() == "yotta"):
        return 180
#     ----------------
    elif(unit.lower() == "zetta"):
        return 181
    elif(unit.lower() == "exa"):
        return 182
    elif(unit.lower() == "peta"):
        return 183
    elif(unit.lower() == "tera"):
        return 184
    elif(unit.lower() == "giga"):
        return 185
    elif(unit.lower() == "mega"):
        return 186
    elif(unit.lower() == "kilo"):
        return 187
    elif(unit.lower() == "hecto"):
        return 188
    elif(unit.lower() == "deka"):
        return 189
    elif(unit.lower() == "deci"):
        return 190
#     ----------------
    elif(unit.lower() == "centi"):
        return 191
    elif(unit.lower() == "milli"):
        return 192
    elif(unit.lower() == "micro"):
        return 193
    elif(unit.lower() == "nano"):
        return 194
    elif(unit.lower() == "pico"):
        return 195
    elif(unit.lower() == "femto"):
        return 196
    elif(unit.lower() == "atto"):
        return 197
    elif(unit.lower() == "zepto"):
        return 198
    elif(unit.lower() == "yocto"):
        return 199
    
#     ////////////////////
    elif(unit.lower() == "AE"):
        return 200
#     ----------------
    elif(unit.lower() == "lj"):
        return 201
    elif(unit.lower() == "pc"):
        return 202
    elif(unit.lower() == "sr"):
        return 203
    elif(unit.lower() == "m/s"):
        return 204
    elif(unit.lower() == "gr"):
        return 205
    elif(unit.lower() == "dr"):
        return 206
    elif(unit.lower() == "cwt"):
        return 207
    elif(unit.lower() == "slug"):
        return 208
    elif(unit.lower() == "den" or unit.lower() == "D"):
        return 209
    elif(unit.lower() == "tex"):
        return 210
#     ----------------
    elif(unit.lower() == "dtex"):
        return 211
    elif(unit.lower() == "mm"):
        return 212
    elif(unit.lower() == "psi" or unit.lower() == "lbf/in²"):
        return 213
    elif(unit.lower() == "Cal" or unit.lower() == "kcal/cal"):
        return 214
    elif(unit.lower() == "cd/m²"):
        return 215
    elif(unit.lower() == "lm"):
        return 216
    elif(unit.lower() == "lx"):
        return 217
    elif(unit.lower() == "ls"):
        return 218
    elif(unit.lower() == "dpt"):
        return 219
    elif(unit.lower() == "ream"):
        return 220
# #     ----------------
#     elif(unit.lower() == ""):
#         return 161
#     elif(unit.lower() == ""):
#         return 162
#     elif(unit.lower() == ""):
#         return 163
#     elif(unit.lower() == ""):
#         return 164
#     elif(unit.lower() == ""):
#         return 165
#     elif(unit.lower() == ""):
#         return 166
#     elif(unit.lower() == ""):
#         return 167
#     elif(unit.lower() == ""):
#         return 168
#     elif(unit.lower() == ""):
#         return 169
#     elif(unit.lower() == ""):
#         return 170
# #     ----------------
#     elif(unit.lower() == ""):
#         return 161
#     elif(unit.lower() == ""):
#         return 162
#     elif(unit.lower() == ""):
#         return 163
#     elif(unit.lower() == ""):
#         return 164
#     elif(unit.lower() == ""):
#         return 165
#     elif(unit.lower() == ""):
#         return 166
#     elif(unit.lower() == ""):
#         return 167
#     elif(unit.lower() == ""):
#         return 168
#     elif(unit.lower() == ""):
#         return 169
#     elif(unit.lower() == ""):
#         return 170
# #     ----------------
#     elif(unit.lower() == ""):
#         return 161
#     elif(unit.lower() == ""):
#         return 162
#     elif(unit.lower() == ""):
#         return 163
#     elif(unit.lower() == ""):
#         return 164
#     elif(unit.lower() == ""):
#         return 165
#     elif(unit.lower() == ""):
#         return 166
#     elif(unit.lower() == ""):
#         return 167
#     elif(unit.lower() == ""):
#         return 168
#     elif(unit.lower() == ""):
#         return 169
#     elif(unit.lower() == ""):
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


def formatterEn(inputData):
    stringVal = []
    inputData = " ".join(inputData.split())
    splittedArray = inputData.split(" ", 1)
    if(isFloat(splittedArray[0])):
        stringVal.append(float(splittedArray[0]))
    if(not isFloat(splittedArray[0])):
        return_1 = unitsMatcher(splittedArray[0])
        stringVal.append(return_1)
    if(not isFloat(splittedArray[1])):
        return_2 = unitsMatcher(splittedArray[1])
        stringVal.append(return_2)
    if(isFloat(splittedArray[1])):
        stringVal.append(unitsMatcher(splittedArray[1]))
    return (stringVal)


# In[4]:


