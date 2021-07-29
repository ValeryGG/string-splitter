import re

class TagManipulator():    
    def parse_string(self, tags, regex=",\\ *"):
        result = []

        tempResult = re.split( regex, tags )
        
        for unit in tempResult:
                if not unit=="":
                    result.append(unit) 

        return result