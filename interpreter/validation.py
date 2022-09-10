

class Validation:

    @classmethod
    def validate(cls,input_str):

        fully_stripped = input_str.replace(" ","")
        split_by_plus = fully_stripped.split('+')
        input_arr = []
        for i in range(0,len(split_by_plus)):
            splited_by_minus = split_by_plus[i].split('-')
            for x in range(0,len(splited_by_minus)):
                input_arr.append(splited_by_minus[x])
                if(x != len(splited_by_minus)-1):
                    input_arr.append("-")
            if (i != len(split_by_plus)-1):
                input_arr.append("+")
        if (input_arr.count('')>0):
            return False
        return input_arr