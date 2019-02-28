class userstory_an():

    def us_04(mar,div,i):   
        if div!='NA' and mar!='NA' and mar[0]!='Invalid' and div[0]!='Invalid':
            if mar[0]>div[0]:
                return "Error US04 in line " + str(div[1]) +" or line "+ str(mar[1])+":Marriage date occurs after Divorce date in "+ i +" family"
            else:
                return 0
        else:
            return 0

    def us_07(birth,death,Age,i):
        if Age!='NA' and Age!='Invalid':
            if Age>=150:
                if death!='NA':
                    return "Error US07 in line "+ str(birth[1]) +" or line "+ str(death[1])+":Age of person is 150 years with "+ i +" id"
                else:
                    return "Error US07 in line "+ str(birth[1]) +":Age of person is 150 years with "+ i +" id"
            else:
                return 0
        else:
            return 0
    
    def parse_data_04(family):
        for x in family:
            answer=userstory_an.us_04(family[x]['MARR_DATE'],family[x]['DIV_DATE'],x)
            if answer!=0:
                print(answer)
        return 0

    def parse_data_07(ind):
        for x in ind:
            answer=userstory_an.us_07(ind[x]['BIRT_DATE'],ind[x]['DEAT_DATE'],ind[x]['AGE'],x)
            if answer!=0:
                print(answer)
        return 0