class us_rs:
    
    # UserStory 15
    def siblingCount(family):
        if(type(family) is not (dict)):
            raise TypeError("Argument isn't an dict")
        validity = True
        for x, values in family.items():
            
            if values.__contains__("CHIL"):
                length = len(values["CHIL"])    
            else:
                length = 0
            if length > 15:
                validity = False
                print("ERROR: Line number " + str(values['CHIL'][0][1]) + ". There are more than 15 siblings for family. " )
                return validity

          
        return validity

  


