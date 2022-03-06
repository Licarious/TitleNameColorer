import glob
import re
import os


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    #print(newString)
    return (newString)

inputFiles = glob.glob("Input/**/*.yml",recursive = True)

T0 = [" baron_", "_baron_"]
T1 = [" count_", "_count_"]
T2 = [" duke_", "_duke_"]
T3 = [" king_", "_king_"]
T4 = [" emperor_", "_emperor_", "emperor_"]



for file in inputFiles:
    name = file.split("\\")[-1]
    #print(name)
    path = file.replace("Input\\","Output\\").replace("\\%s"%name,"")
    #print(path)

    
    f = open(file, "r",encoding='utf-8-sig',errors='ignore')
    print(file)

    
    
    languageFound = False
    language = ""

    writeFile = False
    titleList = []
    for line in f:
        l0 = line.split(":")[0]
        if line.strip().startswith("l_") and not languageFound:
            language = line
            print(language)
        if "_male_" in l0.lower() or "_female_" in l0.lower():
            tierFound = False
            if "\"\"" in line:
                pass
            else:
                for e in T0:
                    if e in l0.lower() and not tierFound:
                        l1 = replacenth(line,"\"","\"#tier0 ",1)
                        l2 = replacenth(l1,"\"","#!\"",2)
                        #print(l2)
                        titleList.append(l2)
                        writeFile = True
                        tierFound = True
                for e in T1:
                    if e in l0.lower() and not tierFound:
                        l1 = replacenth(line,"\"","\"#tier1 ",1)
                        l2 = replacenth(l1,"\"","#!\"",2)
                        #print(l2)
                        titleList.append(l2)
                        writeFile = True
                        tierFound = True
                for e in T2:
                    if e in l0.lower() and not tierFound:
                        l1 = replacenth(line,"\"","\"#tier2 ",1)
                        l2 = replacenth(l1,"\"","#!\"",2)
                        #print(l2)
                        titleList.append(l2)
                        writeFile = True
                        tierFound = True
                for e in T3:
                    if e in l0.lower() and not tierFound:
                        l1 = replacenth(line,"\"","\"#tier3 ",1)
                        l2 = replacenth(l1,"\"","#!\"",2)
                        #print(l2)
                        titleList.append(l2)
                        writeFile = True
                        tierFound = True
                for e in T4:
                    if e in l0.lower() and not tierFound:
                        l1 = replacenth(line,"\"","\"#tier4 ",1)
                        l2 = replacenth(l1,"\"","#!\"",2)
                        #print(l2)
                        titleList.append(l2)
                        writeFile = True
                        tierFound = True
    if writeFile:
        if not os.path.exists(path):
            os.makedirs(path)
        f2 = open(file.replace("Input\\","Output\\").replace(name,"z_ctt_patch_%s"%name), "w",encoding='utf-8-sig',errors='ignore')
        f2.write("%s"%language)
        for i in titleList:
            f2.write(i)
        f2.close()
    f.close()
    #print(file)