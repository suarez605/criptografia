def get_dictionaries():
    dic = {
        "A": AB().initalize_dic(AB.MOVEMENT),
        "B": AB().initalize_dic(AB.MOVEMENT),
        "C": CD().initalize_dic(CD.MOVEMENT),
        "D": CD().initalize_dic(CD.MOVEMENT),
        "E": EF().initalize_dic(EF.MOVEMENT),
        "F": EF().initalize_dic(EF.MOVEMENT),
        "G": GH().initalize_dic(GH.MOVEMENT),
        "H": GH().initalize_dic(GH.MOVEMENT),
        "I": IJ().initalize_dic(IJ.MOVEMENT),
        "J": IJ().initalize_dic(IJ.MOVEMENT),
        "K": KL().initalize_dic(KL.MOVEMENT),
        "L": KL().initalize_dic(KL.MOVEMENT),
        "M": MN().initalize_dic(MN.MOVEMENT),
        "N": MN().initalize_dic(MN.MOVEMENT),
        "O": OP().initalize_dic(OP.MOVEMENT),
        "P": OP().initalize_dic(OP.MOVEMENT),
        "Q": QR().initalize_dic(QR.MOVEMENT),
        "R": QR().initalize_dic(QR.MOVEMENT),
        "S": ST().initalize_dic(ST.MOVEMENT),
        "T": ST().initalize_dic(ST.MOVEMENT),
        "U": UV().initalize_dic(UV.MOVEMENT),
        "V": UV().initalize_dic(UV.MOVEMENT),
        "W": WX().initalize_dic(WX.MOVEMENT),
        "X": WX().initalize_dic(WX.MOVEMENT),
        "Y": YZ().initalize_dic(YZ.MOVEMENT),
        "Z": YZ().initalize_dic(YZ.MOVEMENT)
    }
    return dic

class base_dictionary:
    list_1 = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    list_2 = [ "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def initalize_dic(self, movement):
        dic = {}
        count = 0
        for key in self.list_1:
            position = count + movement
            if position >= len(self.list_2):
                position = len(self.list_2) - count
            dic[key] = self.list_2[position]
            count += 1
        return dic

class AB (base_dictionary):
    MOVEMENT = 0
    NAME = "AB"

class CD (base_dictionary):
    MOVEMENT = -1
    NAME = "CD" 
    
class EF (base_dictionary):
    MOVEMENT = -2
    NAME = "EF"

class GH (base_dictionary):
    MOVEMENT = -3
    NAME = "GH"

class IJ (base_dictionary):
    MOVEMENT = -4
    NAME = "IJ"

class KL (base_dictionary):
    MOVEMENT = -5
    NAME = "KL"

class MN (base_dictionary):
    MOVEMENT = -6
    NAME = "MN"

class OP (base_dictionary):
    MOVEMENT = -7
    NAME = "OP"
    
class QR (base_dictionary):
    MOVEMENT = -8
    NAME = "QR"

class ST (base_dictionary):
    MOVEMENT = -9
    NAME = "ST"

class UV (base_dictionary):
    MOVEMENT = -10
    NAME = "UV"

class WX (base_dictionary):
    MOVEMENT = -11
    NAME = "WX"

class YZ (base_dictionary):
    MOVEMENT = -12
    NAME = "YZ"