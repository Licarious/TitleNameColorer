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



for file in inputFiles:
    name = file.split("\\")[-1]
    #print(name)
    path = file.replace("Input\\","Output\\").replace("\\%s"%name,"")
    #print(path)
    
    
    f = open(file, "r",encoding='utf-8-sig',errors='ignore')
    print(file)
    

    writeFile = False
    titleList = []
    for line in f:
        if "_male_" in line.lower() or "_female_" in line.lower():
            if "\"\"" in line or "\" \"" in line or "[ROOT." in line or "[CHARACTER." in line or "$" in line or "councillor" in line:
                pass
            else:
                if " baron_" in line.lower() or "_baron_" in line.lower():
                    l1 = replacenth(line,"\"","\"#tier0 ",1)
                    l2 = replacenth(l1,"\"","#!\"",2)
                    #print(l2)
                    titleList.append(l2)
                    writeFile = True
                if " count_" in line.lower() or "_count_" in line.lower():
                    l1 = replacenth(line,"\"","\"#tier1 ",1)
                    l2 = replacenth(l1,"\"","#!\"",2)
                    #print(l2)
                    titleList.append(l2)
                    writeFile = True
                if " duke_" in line.lower() or "_duke_" in line.lower():
                    l1 = replacenth(line,"\"","\"#tier2 ",1)
                    l2 = replacenth(l1,"\"","#!\"",2)
                    #print(l2)
                    titleList.append(l2)
                    writeFile = True
                if " king_" in line.lower() or "_king_" in line.lower():
                    l1 = replacenth(line,"\"","\"#tier3 ",1)
                    l2 = replacenth(l1,"\"","#!\"",2)
                    #print(l2)
                    titleList.append(l2)
                    writeFile = True
                if " emperor_" in line.lower() or "_emperor_" in line.lower():
                    l1 = replacenth(line,"\"","\"#tier4 ",1)
                    l2 = replacenth(l1,"\"","#!\"",2)
                    #print(l2)
                    titleList.append(l2)
                    writeFile = True
    if writeFile:
        if not os.path.exists(path):
            os.makedirs(path)
        f2 = open(file.replace("Input\\","Output\\").replace(name,"z_ctt_patch_%s"%name), "w",encoding='utf-8-sig',errors='ignore')
        f2.write("l_english:\n\n")
        for i in titleList:
            f2.write(i)
        f2.close()
    #print(file)