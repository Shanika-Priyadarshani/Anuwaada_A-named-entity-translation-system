#!/usr/bin/env python
# coding: utf-8

# In[1]:


def unitsMatcher(indexVal):
    if(indexVal == 1):
        return "මීටර්"
    elif(indexVal == 2):
        return "මීටර්"
    elif(indexVal == 3):
        return "මිලිමීටර්"
    elif(indexVal == 4):
        return "සෙන්ටිමීටර්"
    elif(indexVal == 5):
        return "ඩෙසිමීටර්"
    elif(indexVal == 6):
        return "කිලෝමීටර්"
    elif(indexVal == 7):
        return "ආලෝක වර්ෂ"
    elif(indexVal == 8):
        return "අඟල්"
    elif(indexVal == 9):
        return "අඩි"
    elif(indexVal == 10):
        return "සැතපුම්"
#     ----------------
    elif(indexVal == 11):
        return "නාවුක සැතපුම්"
    elif(indexVal == 12):
        return "වර්ග මීටර්"
    elif(indexVal == 13):
        return "අක්කර"
    elif(indexVal == 14):
        return "හෙක්ටයාර"
    elif(indexVal == 15):
        return "වර්ග අඟල්"
    elif(indexVal == 16):
        return "වර්ග අඩි"
    elif(indexVal == 17):
        return "වර්ග සැතපුම්"
    elif(indexVal == 18):
        return "ඝන මීටර්"
    elif(indexVal == 19):
        return "ලීටර්"
    elif(indexVal == 20):
        return "මිලිලීටර්"
#     ----------------
    elif(indexVal == 21):
        return "ඩෙසිලීටර්"
    elif(indexVal == 22):
        return "ඝන අඟල්"
    elif(indexVal == 23):
        return "ඝන අඩි"
    elif(indexVal == 24):
        return "අක්කර අඩි"
    elif(indexVal == 25):
        return "තේ හැඳි"
    elif(indexVal == 26):
        return "මේස හැඳි"
    elif(indexVal == 27):
        return "අවුන්ස"
    elif(indexVal == 28):
        return "කෝප්ප"
    elif(indexVal == 29):
        return "පයින්ට්"
    elif(indexVal == 30):
        return "කාල"
#     ----------------
    elif(indexVal == 31):
        return "ගැලුම්"
    elif(indexVal == 32):
        return "රේඩියන්"
    elif(indexVal == 33):
        return "අංශක"
    elif(indexVal == 34):
        return "තත්පර"
    elif(indexVal == 35):
        return "මිනිත්තු"
    elif(indexVal == 36):
        return "පැය"
    elif(indexVal == 37):
        return "දවස්"
    elif(indexVal == 38):
        return "අවුරුදු"
    elif(indexVal == 39):
        return "හර්ට්ස්"
    elif(indexVal == 40):
        return "කෝණික සංඛ්‍යාතය"
#     ----------------
    elif(indexVal == 41):
        return "ඩෙසිබෙල්"
    elif(indexVal == 42):
        return "තත්පරයට කිලෝමීටර්"
    elif(indexVal == 43):
        return "පැයට සැතපුම්"
    elif(indexVal == 44):
        return "තත්පරයට මීටර්"
    elif(indexVal == 45):
        return "තත්පරයට අඩි"
    elif(indexVal == 46):
        return "ග්රෑම්"
    elif(indexVal == 47):
        return "කිලෝ ග්රෑම්"
    elif(indexVal == 48):
        return "පවුම්"
    elif(indexVal == 49):
        return "ඝනත්වය"
    elif(indexVal == 50):
        return "නිව්ටන්"
#     ----------------
    elif(indexVal == 51):
        return "නිව්ටන් මීටර්"
    elif(indexVal == 52):
        return "ජූල්"
    elif(indexVal == 53):
        return "වොට්"
    elif(indexVal == 54):
        return "කිලෝ වොට්"
    elif(indexVal == 55):
        return "අශ්ව බල"
    elif(indexVal == 56):
        return "පැස්කල්"
    elif(indexVal == 57):
        return "බාර්"
    elif(indexVal == 58):
        return "කෙල්වින්"
    elif(indexVal == 59):
        return "සෙන්ටිග්‍රේඩ්"
    elif(indexVal == 60):
        return "කැලරි"
#     ----------------
    elif(indexVal == 61):
        return "ෆැරන්හයිට්"
    elif(indexVal == 62):
        return "ඇම්පියර්"
    elif(indexVal == 63):
        return "කූලෝම්"
    elif(indexVal == 64):
        return "වෝල්ට්"
    elif(indexVal == 65):
        return "ඕම්"
    elif(indexVal == 66):
        return "සීමන්ස්"
    elif(indexVal == 67):
        return "හෙන්රි"
    elif(indexVal == 68):
        return "වේබර්"
    elif(indexVal == 69):
        return "ටෙස්ලා"
    elif(indexVal == 70):
        return "බෙකරල්"
#     ----------------
    elif(indexVal == 71):
        return "මවුල"
    elif(indexVal == 72):
        return "දුසිම්"
    elif(indexVal == 73):
        return "ඇවගාඩ්රෝ නියතය"
    elif(indexVal == 74):
        return "බෝල්ට්ස්මාන් නියතය"
    elif(indexVal == 75):
        return "ෆයි"
    elif(indexVal == 76):
        return "ප්ලාන්ක් නියතය"
    elif(indexVal == 77):
        return "ස්ටෙෆන්-බෝල්ට්ස්මාන් නියතය"
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
        return "මී."
    elif(indexVal == 99):
        return "මි.මී."
    elif(indexVal == 100):
        return "සෙ.මී."
#     ----------------
    elif(indexVal == 101):
        return "ඩෙ.මී."
    elif(indexVal == 102):
        return "කි.මී."
    elif(indexVal == 103):
        return "අඟල්"
    elif(indexVal == 104):
        return "අඩි"
    elif(indexVal == 105):
        return "සැ."
    elif(indexVal == 106):
        return "ව.මී."
    elif(indexVal == 107):
        return "ව.අඟල්"
    elif(indexVal == 108):
        return "ව.අඩි"
    elif(indexVal == 109):
        return "ව.සැ."
    elif(indexVal == 110):
        return "ඝ.මී."
#     ----------------
    elif(indexVal == 111):
        return "ලී."
    elif(indexVal == 112):
        return "මි.ලී."
    elif(indexVal == 113):
        return "සෙ.ලී."
    elif(indexVal == 114):
        return "ඩෙ.ලී."
    elif(indexVal == 115):
        return "හෙ.ලී."
    elif(indexVal == 116):
        return "ඝ.අඟල්"
    elif(indexVal == 117):
        return "ඝ.අඩි"
    elif(indexVal == 118):
        return "අක්කර අඩි"
    elif(indexVal == 119):
        return "තේ හැඳි"
    elif(indexVal == 120):
        return "මේස හැඳි"
#     ----------------
    elif(indexVal == 121):
        return "කාල"
    elif(indexVal == 122):
        return "ගැලුම්"
    elif(indexVal == 123):
        return "රේඩියන්"
    elif(indexVal == 124):
        return "අංශක"
    elif(indexVal == 125):
        return "තත්."
    elif(indexVal == 126):
        return "මිනි."
    elif(indexVal == 127):
        return "පැ."
    elif(indexVal == 128):
        return "දවස්"
    elif(indexVal == 129):
        return "හර්ට්ස්"
    elif(indexVal == 130):
        return "ω"
#     ----------------
    elif(indexVal == 131):
        return "dB"
    elif(indexVal == 132):
        return "kg m/s"
    elif(indexVal == 133):
        return "පැයට සැතපුම්"
    elif(indexVal == 134):
        return "පැයට කිලෝමීටර්"
    elif(indexVal == 135):
        return "ft/s²"
    elif(indexVal == 136):
        return "m/s²"
    elif(indexVal == 137):
        return "ft/s"
    elif(indexVal == 138):
        return "ග්රෑම්"
    elif(indexVal == 139):
        return "කිලෝ ග්රෑම්"
    elif(indexVal == 140):
        return "අවුන්ස"
#     ----------------
    elif(indexVal == 141):
        return "රාත්තල්"
    elif(indexVal == 142):
        return "ටොන්"
    elif(indexVal == 143):
        return "ටොන්"
    elif(indexVal == 144):
        return "kg/m³"
    elif(indexVal == 145):
        return "නිව්ටන්"
    elif(indexVal == 146):
        return "පවුම්"
    elif(indexVal == 147):
        return "නිව්ටන් මීටර්"
    elif(indexVal == 148):
        return "ජූල්"
    elif(indexVal == 149):
        return "වොට්"
    elif(indexVal == 150):
        return "කිලෝ වොට්"
#     ----------------
    elif(indexVal == 151):
        return "අශ්ව බල"
    elif(indexVal == 152):
        return "පැස්කල්"
    elif(indexVal == 153):
        return "බාර්"
    elif(indexVal == 154):
        return "කෙල්වින් අංශක"
    elif(indexVal == 155):
        return "සෙල්සියස් අංශක"
    elif(indexVal == 156):
        return "ෆැරන්හයිට් අංශක"
    elif(indexVal == 157):
        return "කැන්ඩෙලා"
    elif(indexVal == 158):
        return "ඇම්පියර්"
    elif(indexVal == 159):
        return "ඇම්පියර්"
    elif(indexVal == 160):
        return "කූලෝම්"
#     ----------------
    elif(indexVal == 161):
        return "වෝල්ට්"
    elif(indexVal == 162):
        return "ඕම්"
    elif(indexVal == 163):
        return "ෆැරඩ්"
    elif(indexVal == 164):
        return "සීමන්ස්"
    elif(indexVal == 165):
        return "හෙන්රි"
    elif(indexVal == 166):
        return "වේබර්"
    elif(indexVal == 167):
        return "ටෙස්ලා"
    elif(indexVal == 168):
        return "බෙකරල්"
    elif(indexVal == 169):
        return "මවුල"
    elif(indexVal == 170):
        return "දුසිම්"
#     ----------------
    elif(indexVal == 171):
        return "දුසිම්"
    elif(indexVal == 172):
        return "සෙන්ටිලීටර්"
    elif(indexVal == 173):
        return "හෙක්ටොලීටර්"
    elif(indexVal == 174):
        return "ස්ටෙරේඩියන්"
    elif(indexVal == 175):
        return "ටොන්"
    elif(indexVal == 176):
        return "කිලෝ පවුම්"
    elif(indexVal == 177):
        return "කැන්ඩෙලා"
    elif(indexVal == 178):
        return "ෆැරඩ්"
    elif(indexVal == 179):
        return "ටෝ"
    elif(indexVal == 180):
        return "යෝටා"
#     ----------------
    elif(indexVal == 181):
        return "සෙටා"
    elif(indexVal == 182):
        return "එක්ස"
    elif(indexVal == 183):
        return "පෙටා"
    elif(indexVal == 184):
        return "ටෙරා"
    elif(indexVal == 185):
        return "ගිගා"
    elif(indexVal == 186):
        return "මෙගා"
    elif(indexVal == 187):
        return "කිලෝ"
    elif(indexVal == 188):
        return "හෙක්ටො"
    elif(indexVal == 189):
        return "ඩෙකා"
    elif(indexVal == 190):
        return "ඩෙසි"
#     ----------------
    elif(indexVal == 191):
        return "සෙන්ටි"
    elif(indexVal == 192):
        return "මිලි"
    elif(indexVal == 193):
        return "මයික්‍රො"
    elif(indexVal == 194):
        return "නැනෝ"
    elif(indexVal == 195):
        return "පිකෝ"
    elif(indexVal == 196):
        return "ෆෙම්ටො"
    elif(indexVal == 197):
        return "ඇටෝ"
    elif(indexVal == 198):
        return "සෙප්ටො"
    elif(indexVal == 199):
        return "යොක්ටො"
    
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


def converterSi(inputList):
    unit = unitsMatcher(inputList[1])
    return unit + " " +str(inputList[0])


# In[ ]:



