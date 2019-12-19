#!/usr/bin/env python
# coding: utf-8

# In[1]:


def unitsMatcher(unit):
    if(unit == "මීටර්"):
        return 1
    elif(unit == "මීටර්"):
        return 2
    elif(unit == "මිලිමීටර්"):
        return 3
    elif(unit == "සෙන්ටිමීටර්"):
        return 4
    elif(unit == "ඩෙසිමීටර්"):
        return 5
    elif(unit == "කිලෝමීටර්"):
        return 6
    elif(unit == "ආලෝක වර්ෂ"):
        return 7
    elif(unit == "අඟල්"):
        return 8
    elif(unit == "අඩි"):
        return 9
    elif(unit == "සැතපුම්"):
        return 10
#     ----------------
    elif(unit == "නාවුක සැතපුම්"):
        return 11
    elif(unit == "වර්ග මීටර්"):
        return 12
    elif(unit == "අක්කර"):
        return 13
    elif(unit == "හෙක්ටයාර"):
        return 14
    elif(unit == "වර්ග අඟල්"):
        return 15
    elif(unit == "වර්ග අඩි"):
        return 16
    elif(unit == "වර්ග සැතපුම්"):
        return 17
    elif(unit == "ඝන මීටර්"):
        return 18
    elif(unit == "ලීටර්"):
        return 19
    elif(unit == "මිලිලීටර්"):
        return 20
#     ----------------
    elif(unit == "ඩෙසිලීටර්"):
        return 21
    elif(unit == "ඝන අඟල්"):
        return 22
    elif(unit == "ඝන අඩි"):
        return 23
    elif(unit == "අක්කර අඩි"):
        return 24
    elif(unit == "තේ හැඳි"):
        return 25
    elif(unit == "මේස හැඳි"):
        return 26
    elif(unit == "අවුන්ස"):
        return 27
    elif(unit == "කෝප්ප"):
        return 28
    elif(unit == "පයින්ට්"):
        return 29
    elif(unit == "කාල"):
        return 30
#     ----------------
    elif(unit == "ගැලුම්"):
        return 31
    elif(unit == "රේඩියන්"):
        return 32
    elif(unit == "අංශක"):
        return 33
    elif(unit == "තත්පර"):
        return 34
    elif(unit == "මිනිත්තු"):
        return 35
    elif(unit == "පැය"):
        return 36
    elif(unit == "දවස්"):
        return 37
    elif(unit == "අවුරුදු"):
        return 38
    elif(unit == "හර්ට්ස්"):
        return 39
    elif(unit == "කෝණික සංඛ්‍යාතය"):
        return 40
#     ----------------
    elif(unit == "ඩෙසිබෙල්"):
        return 41
    elif(unit == "තත්පරයට කිලෝමීටර්"):
        return 42
    elif(unit == "පැයට සැතපුම්"):
        return 43
    elif(unit == "තත්පරයට මීටර්"):
        return 44
    elif(unit == "තත්පරයට අඩි"):
        return 45
    elif(unit == "ග්රෑම්"):
        return 46
    elif(unit == "කිලෝ ග්රෑම්"):
        return 47
    elif(unit == "පවුම්"):
        return 48
    elif(unit == "ඝනත්වය"):
        return 49
    elif(unit == "නිව්ටන්"):
        return 50
#     ----------------
    elif(unit == "නිව්ටන් මීටර්"):
        return 51
    elif(unit == "ජූල්"):
        return 52
    elif(unit == "වොට්"):
        return 53
    elif(unit == "කිලෝ වොට්"):
        return 54
    elif(unit == "අශ්ව බල"):
        return 55
    elif(unit == "පැස්කල්"):
        return 56
    elif(unit == "බාර්"):
        return 57
    elif(unit == "කෙල්වින්"):
        return 58
    elif(unit == "සෙන්ටිග්‍රේඩ්"):
        return 59
    elif(unit == "කැලරි"):
        return 60
#     ----------------
    elif(unit == "ෆැරන්හයිට්"):
        return 61
    elif(unit == "ඇම්පියර්"):
        return 62
    elif(unit == "කූලෝම්"):
        return 63
    elif(unit == "වෝල්ට්"):
        return 64
    elif(unit == "ඕම්"):
        return 65
    elif(unit == "සීමන්ස්"):
        return 66
    elif(unit == "හෙන්රි"):
        return 67
    elif(unit == "වේබර්"):
        return 68
    elif(unit == "ටෙස්ලා"):
        return 69
    elif(unit == "බෙකරල්"):
        return 70
#     ----------------
    elif(unit == "මවුල"):
        return 71
    elif(unit == "දුසිම්"):
        return 72
    elif(unit == "ඇවගාඩ්රෝ නියතය"):
        return 73
    elif(unit == "බෝල්ට්ස්මාන් නියතය"):
        return 74
    elif(unit == "ෆයි"):
        return 75
    elif(unit == "ප්ලාන්ක් නියතය"):
        return 76
    elif(unit == "ස්ටෙෆන්-බෝල්ට්ස්මාන් නියතය"):
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

    elif(unit == "මී."):
        return 98
    elif(unit == "මි.මී."):
        return 99
    elif(unit == "සෙ.මී."):
        return 100
#     ----------------
    elif(unit == "ඩෙ.මී."):
        return 101
    elif(unit == "කි.මී."):
        return 102
    elif(unit == "අඟල්"):
        return 103
    elif(unit == "අඩි"):
        return 104
    elif(unit == "සැ."):
        return 105
    elif(unit == "ව.මී." ):
        return 106
    elif(unit == "ව.අඟල්"):
        return 107
    elif(unit == "ව.අඩි"):
        return 108
    elif(unit == "ව.සැ."):
        return 109
    elif(unit == "ඝ.මී."):
        return 110
#     ----------------
    elif(unit == "ලී."):
        return 111
    elif(unit == "මි.ලී."):
        return 112
    elif(unit == "සෙ.ලී."):
        return 113
    elif(unit == "ඩෙ.ලී."):
        return 114
    elif(unit == "හෙ.ලී."):
        return 115
    elif(unit == "ඝ.අඟල්"):
        return 116
    elif(unit == "ඝ.අඩි"):
        return 117
    elif(unit == "අක්කර අඩි"):
        return 118
    elif(unit == "තේ හැඳි"):
        return 119
    elif(unit == "මේස හැඳි"):
        return 120
#     ----------------
    elif(unit == "කාල"):
        return 121
    elif(unit == "ගැලුම්"):
        return 122
    elif(unit == "රේඩියන්"):
        return 123
    elif(unit == "අංශක"):
        return 124
    elif(unit == "තත්."):
        return 125
    elif(unit == "මිනි."):
        return 126
    elif(unit == "පැ."):
        return 127
    elif(unit == "දවස්"):
        return 128
    elif(unit == "හර්ට්ස්"):
        return 129
    elif(unit == "ω"):
        return 130
#     ----------------
    elif(unit == "dB"):
        return 131
    elif(unit == "kg m/s"):
        return 132
    elif(unit == "පැයට සැතපුම්"):
        return 133
    elif(unit == "පැයට කිලෝමීටර්"):
        return 134
    elif(unit == "ft/s²"):
        return 135
    elif(unit == "m/s²"):
        return 136
    elif(unit == "ft/s"):
        return 137
    elif(unit == "ග්රෑම්"):
        return 138
    elif(unit == "කිලෝ ග්රෑම්"):
        return 139
    elif(unit == "අවුන්ස"):
        return 140
#     ----------------
    elif(unit == "රාත්තල්"):
        return 141
    elif(unit == "ටොන්"):
        return 142
    elif(unit == "ටොන්"):
        return 143
    elif(unit == "kg/m3"):
        return 144
    elif(unit == "නිව්ටන්"):
        return 145
    elif(unit == "පවුම්"):
        return 146
    elif(unit == "නිව්ටන් මීටර්"):
        return 147
    elif(unit == "ජූල්"):
        return 148
    elif(unit == "වොට්"):
        return 149
    elif(unit == "කිලෝ වොට්"):
        return 150
#     ----------------
    elif(unit == "අශ්ව බල"):
        return 151
    elif(unit == "පැස්කල්"):
        return 152
    elif(unit == "බාර්"):
        return 153
    elif(unit == "කෙල්වින් අංශක"):
        return 154
    elif(unit == "සෙල්සියස් අංශක"):
        return 155
    elif(unit == "ෆැරන්හයිට් අංශක"):
        return 156
    elif(unit == "කැන්ඩෙලා"):
        return 157
    elif(unit == "ඇම්පියර්"):
        return 158
    elif(unit == "ඇම්පියර්"):
        return 159
    elif(unit == "කූලෝම්"):
        return 160
#     ----------------
    elif(unit == "වෝල්ට්"):
        return 161
    elif(unit == "ඕම්"):
        return 162
    elif(unit == "ෆැරඩ්"):
        return 163
    elif(unit == "සීමන්ස්"):
        return 164
    elif(unit == "හෙන්රි"):
        return 165
    elif(unit == "වේබර්"):
        return 166
    elif(unit == "ටෙස්ලා"):
        return 167
    elif(unit == "බෙකරල්"):
        return 168
    elif(unit == "මවුල"):
        return 169
    elif(unit == "දුසිම්"):
        return 170
#     ----------------
    elif(unit == "දුසිම්"):
        return 171
    elif(unit == "සෙන්ටිලීටර්"):
        return 172
    elif(unit == "හෙක්ටොලීටර්"):
        return 173
    elif(unit == "ස්ටෙරේඩියන්"):
        return 174
    elif(unit == "ටොන්"):
        return 175
    elif(unit == "කිලෝ පවුම්"):
        return 176
    elif(unit == "කැන්ඩෙලා"):
        return 177
    elif(unit == "ෆැරඩ්"):
        return 178
    elif(unit == "ටෝ"):
        return 179
    elif(unit == "යෝටා"):
        return 180
#     ----------------
    elif(unit == "සෙටා"):
        return 181
    elif(unit == "එක්ස"):
        return 182
    elif(unit == "පෙටා"):
        return 183
    elif(unit == "ටෙරා"):
        return 184
    elif(unit == "ගිගා"):
        return 185
    elif(unit == "මෙගා"):
        return 186
    elif(unit == "කිලෝ"):
        return 187
    elif(unit == "හෙක්ටො"):
        return 188
    elif(unit == "ඩෙකා"):
        return 189
    elif(unit == "ඩෙසි"):
        return 190
#     ----------------
    elif(unit == "සෙන්ටි"):
        return 191
    elif(unit == "මිලි"):
        return 192
    elif(unit == "මයික්‍රො"):
        return 193
    elif(unit == "නැනෝ"):
        return 194
    elif(unit == "පිකෝ"):
        return 195
    elif(unit == "ෆෙම්ටො"):
        return 196
    elif(unit == "ඇටෝ"):
        return 197
    elif(unit == "සෙප්ටො"):
        return 198
    elif(unit == "යොක්ටො"):
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


def formatterSi(inputData):
    stringVal = []
    inputData = " ".join(inputData.split())
    splittedArray = inputData.rsplit(" ", 1)
    if(isFloat(splittedArray[1])):
        stringVal.append(float(splittedArray[1]))
    if(not isFloat(splittedArray[0])):
        stringVal.append(unitsMatcher(splittedArray[0]))
    if(isFloat(splittedArray[0])):
        stringVal.append(splittedArray[0])
    if(not isFloat(splittedArray[1])):
        stringVal.append(unitsMatcher(splittedArray[1]))
    return (stringVal)


# In[ ]:



