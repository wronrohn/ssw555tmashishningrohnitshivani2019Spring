valid_tags = {"INDI":"0","NAME":"1","SEX":"1","BIRT":"1","DEAT":"1","FAMC":"1","FAMS":"1","FAM":"0","MARR":"1","HUSB":"1","WIFE":"1","CHIL":"1","DIV":"1","DATE":"2","HEAD":"0","TRLR":"0","NOTE":"0"}
is_valid = "N"
with open('My-Family-27-Jan-2019-275.ged','r') as f:
    with open("Output.text","w") as output:
        content = f.readlines()

        for line in content:
            try:
                line1 = line.split(" ")
                output.write("--> "+line)

                level = line1[0]
                tag = line1[1].strip()
                if tag in valid_tags:
                    if tag not in ["INDI","FAM"]:
                        if valid_tags[tag] == level:
                            is_valid = "Y"
                    else: 
                        is_valid = "N"
                    args = [' '.join(line1[2:])]
                    args = args[0]
                elif line1[2].strip() in ["INDI","FAM"]:
                    args = line1[2].strip() 
                    if valid_tags[args] == level:
                        tag , args = args , tag
                        is_valid = "Y"
                else:
                    is_valid = "N"
                    args = [' '.join(line1[2:])]
                    args = args[0]
                
                output.write(f"<--{level}|{tag}|{is_valid}|{args}\n")
            except:
                output.write(f"<--{level}|{tag}|{is_valid}|{args}\n")   







