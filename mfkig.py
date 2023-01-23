

import os
import re
import sys
from  ClassMFKiG import MFKiG
import time







# import ClassMFKiG

# Sposób na sortowanie
# https://stackoverflow.com/questions/65956598/sort-a-alphanumeric-list-in-python
#
# sort_this =  ['file.1.txt','file.10.txt', 'file.99.txt', 'file.8.txt']
# sort_this.sort(key=lambda x: int(re.findall("\.\d+\.", x)[0]))


__version__ = "0.1.0"



# if (sys.version.split("."))


major, minor, micro = (sys.version.split(" ")[0].split("."))
print(major,minor,micro)


FILE_MFKIG = "c:\_temp_\mfkig.txt"

def mfkig_method_2(aFileName:str) -> list:

    with open(aFileName) as file:
        lst_sort_by_exibit = list()
        for line in file:
            line = line.rstrip()
            temp = line.split("=")
            stand_num = temp[0]
            exibit_name = temp[1]
            lst_sort_by_exibit .append((exibit_name, stand_num))    #   dodawanie krotek do listy, przygotowanie do sortowania

        lst_sort_by_exibit.sort()   #   sortowanie po pierwszym elemencie krotki

        # for i in range(len(lst_sort_by_exibit)):
        #     result.append(f"{i+1}. {lst_sort_by_exibit[i][0]} - {lst_sort_by_exibit[i][1]}")


    return lst_sort_by_exibit


# teochę o cssach
# https://www.w3schools.com/html/html_table_borders.asp
#  https://www.w3schools.com/tags/tag_style.asp





def html_table_export(aTupleList:list) -> list:



    def addLead0(aValue:int) -> str:
        aValue = abs(aValue)
        return str(aValue) if aValue > 9 else "0{}".format(aValue)

    def tagHTML_P(aText:str) -> str:
        return "<P>{0}</p>".format(aText)

    def tagHTML_H1(aText:str) -> str:
        return "<H1>{0}</h1>".format(aText)

    def tagHTML_REMARK(aText:str) -> str:
        return ("<!--%s-->" % aText)

    # dokumentowanie kodu:
    # https://realpython.com/documenting-python-code/
    #
    def tagHTML_LIST(aType:int, aList:list) -> str:
        """
           aType values:

           1   -   undordered list html tag UL

           2   -   orderered list html tag OL

           aList:

            a list to generate in html code

        """
        #   aType
        #   1   -   undordered list UL
        #   2   -   orderered list OL
        listtype = {1 : "UL", 2 : "OL"}.get(aType, "UL")
        result = ""
        if aList != None:
            result = "<{}>\n".format(listtype)
            for item in aList:
                result += "<li> {}\n".format(item)
        result += "</{}>\n".format(listtype)

        return result

        

    def tagHTML_UNORDER_LIST(aList:list) -> str:
        return tagHTML_LIST(1, aList)

    def tagHTML_ORDER_LIST(aList:list) -> str:
        return tagHTML_LIST(2, aList)

    result = list()

    tstamp = time.localtime()


    result.append("<html>")
    result.append(tagHTML_REMARK(" ********** CREATED BY MFKiG {0}/{1}/{2} {3}:{4}:{5} ********** ".format(
        addLead0(tstamp.tm_mday),addLead0(tstamp.tm_mon), tstamp.tm_year,
        addLead0(tstamp.tm_hour),addLead0(tstamp.tm_min), addLead0(tstamp.tm_sec)
    )))
    result.append("<head>")
    result.append("<title>")
    result.append("MFKiG - wystawcy")
    result.append("</title>")


    # <style>
    # table, th, td {
    # border: 1px solid black;
    # border-collapse: collapse;
    # }
    # </style>

    # styl jeden
    result.append("<style>")
    result.append("""
      h1 {color:red;}
    p {color:blue;}
 th, td {
  border-style: solid;
  border-color: #96D4D4;
  border-radius: 15px;
  background-color: #96D4D4;
}
    """)


    result.append("</style>")
    # result.append("table, th, td {")
    # result.append("border: 1px solid black;")
    # result.append("border-collapse: collapse;")
    # result.append("}")
    # result.append("</style>")

    result.append("</head>")
    result.append("<body>")
    result.append(tagHTML_ORDER_LIST(["jeden","dwa","trzy"]))
    result.append(tagHTML_H1("MFKiG - wystawcy"))
    result.append("<table>")
    result.append("<tr>")
    result.append("<th>Lp.</th>")
    result.append("<th>Wystawca</th>")
    result.append("<th>Stoisko</th>")
    result.append("</tr>")
    for i in range(len(aTupleList)):
        result.append("<tr>")

        result.append("<td>")   #   Lp.
        result.append(f"{i+1}")
        result.append("</td>")
        result.append("<td>")   #   Wystawca
        result.append(f"{aTupleList[i][0]}")
        result.append("</td>")
        result.append("<td>")   #   numer stoiska
        result.append(f"{aTupleList[i][1]}")
        result.append("</td>")


        result.append("</tr>")


    result.append("</table>")

    result.append("</body>")
    result.append("</html>")


    return result

def main(args):

    # for e in mfkig_method_2(FILE_MFKIG):
    #     print(e)

    with open("mfkig.html","w") as file:
        html_export = html_table_export(mfkig_method_2(FILE_MFKIG))
        for line in html_export:
            file.write("{}\n".format(line))

        file.close()
    # for e in html_table_export(mfkig_method_2(FILE_MFKIG)):
    #     print(e)

    exit()


    # os.system("dir")
    in_file = "c:\_temp_\mfkig.txt"
    out_file = "c:\_temp_\mfkig.txt.sort_1"

    if (os.path.exists(in_file)):
        print("plik dostępny")
    else:
        print("plik niedostępny")



    file_exists = True


    try:
        file = open(in_file,"rt")
    except IOError:
        print(in_file + " - plik nie istnieje!!!")
        # file.close()
        file_exists = False


    lines = []
    if (file_exists) :
        # data = file.read()
        # lines = data.split("\n")

        lines = (file.read()).split("\n")

        if (lines[len(lines)-1] == ""):
            # print(lines[len(lines)-1])
            # print("usuwanie ostatniej pustej pozycji z listy")
            lines.pop()
            # print(lines[len(lines)-1])
        #
        # nowa wersja
        # bardziej finezyjna (sophisticated and finesse)
        #


        # for line in lines:
        #     print(re.findall("[A-Z][a-z]+",line))

        # lines.sort(key=lambda x: re.findall("\[a-z]+",x)[0])
        lines.sort(key=lambda x: re.split("=", x)[1])
        # print(lines)

        count =1
        print("\nPosortowane...\n")

        mfList = []
        if (os.path.exists(out_file) == True):
            file_2_save = open(out_file,"wt"    )

            


            for line in lines:
                # tworzymy listę obiektów wystawców
                stdNum = int(line.split("=")[0])
                exibName = line.split("=")[1]
                mfList.append(MFKiG(stdNum, exibName))

                file_2_save.write(str(count) +
                    ". "+
                        line.split("=")[1] +
                    " - "+
                        line.split("=")[0]+
                                      "\n"
                    )
                count+=1

            # sortowanie listy wystawców po n
            mfList = sorted(mfList, key=lambda mf: mf.standNum) #    i z powrotem po numerze stoiska

            # zliczanie obietków
            #
            # print(f'obiektów MFKiG: {mfList[1].getTotalCount()}')
            # for n in range(10):
            #     if (mfList[n] != None):
            #         mfList.pop(0)
            # print(f'obiektów MFKiG: {mfList[1].getTotalCount()} - a na liście: {len(mfList)}')


            for m in mfList:
                print(m)



            # while len(mfList) > 0:
            #     mfList.pop()

            file_2_save.flush()
            file_2_save.close()
            print("Zapisane... " + out_file)
        else:
            print("Problem z zapisem - " + out_file)


        #
        #  stara wersja
        #
        # out_lines = []
        # for line in lines:
        #     if (len(line) > 0):
        #         pair = line.split("=")
        #
        #
        #         # key=value
        #
        #         # print(keyval[1])
        #         buffer = pair[1] + " - " + pair[0]
        #         out_lines.append(buffer)
        #
        # out_lines.sort()
        # print("\nPosortowane...\n")
        # file_2_save = open(out_file,"wt")
        #
        # count = 1
        # for line in out_lines:
        #     file_2_save.write(str(count)+". "+line+"\n")
        #     # print(line)
        #     count+=1
        #
        # file_2_save.flush()
        # file_2_save.close()

        return 0


if __name__ == '__main__':
    import sys


    sys.exit(main(sys.argv))

