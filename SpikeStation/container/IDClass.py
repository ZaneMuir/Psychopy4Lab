#
#  Created by Zane Muir
#  Copyright (c) 2016 ZaneMuir. All rights reserved.
#

class IDClass(object):
    """docstring for IDClass."""
    def __init__(self, l1,l2,l3):
        super(IDClass, self).__init__()
        self.lvl1 = l1
        self.lvl2 = l2
        self.lvl3 = l3

    def getID(self):
        return '%d-%d-%d'%(self.lvl1,self.lvl2,self.lvl3)

    def getLevel1(self):
        return str(self.lvl1)

    def getLevel2(self):
        return str(self.lvl2)

    def getLevel3(self):
        return str(self.lvl3)

    def getSessionID(self):
        return '%d%d'%(self.lvl1,self.lvl2)
