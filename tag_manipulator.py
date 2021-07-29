import re

class TagManipulator():    
    def parse_string(self, tags, regex=",\\ *"):
        result = []

        tempResult = re.split( regex, tags )
        
        if( len(tempResult[0]) > 0 ):
            result=tempResult
        else:
            for unit in tempResult:
                if not unit=="":
                    result.append(unit) 

        return result