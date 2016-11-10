"""
COMAOPtriathlon.py
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame, Sound, SoundAsset, TextAsset
import time
import random

"""
sl=int(input("Length of swim (in kilometers)"))
bl=int(input("Length of bike (in kilometers)"))
rl=int(input("Length of run (in kilometers)"))
fprostart=int(input("Time female pros start (in minutes after male pro start)"))
mprestart=int(input("Time male premiere start (in minutes after male pro start)"))
fprestart=int(input("Time female premiere start (in minutes after male pro start)"))
mopenstart=int(input("Time male open start (in minutes after male pro start)"))
fopenstart=int(input("Time female open start (in minutes after male pro start)"))
clystart=int(input("Time Clydsedale start (in minutes after male pro start)"))
athstart=int(input("Time Athena start (in minutes after male pro start)"))
"""
#average swim speeds
mpros=0.114213198
fpros=0.1156812339
mpres=0.09
fpres=0.08806262231
mops=0.06517016655
fops=0.06603081438
cyls=0.05851755527
aths=0.0640569395
#average t1 times
mprot1=3.266666667
fprot1=3.633333333
mpret1=4.4
fpret1=4.95
mopt1=8.033333333
fopt1=10.33333333
cylt1=8.05
atht1=11.63333333
#average bike speeds
mprob=0.6434316354
fprob=0.591424347
mpreb=0.582807188
fpreb=0.5244755245
mopb=0.4643064423
fopb=0.4010025063
cylb=0.4531722054
athb=0.3670285976
#average t2 times
mprot2=0.85
fprot2=0.9166666667
mpret2=1.25
fpret2=1.433333333
mopt2=3.116666667
fopt2=3.816666667
cylt2=3.466666667
atht2=4.516666667
#average run speeds
mpror=0.2830188679
fpror=0.2609830361
mprer=0.251572327
fprer=0.2265861027
mopr=0.1635322976
fopr=0.124403898
cylr=0.1401541696
athr=0.1291433491


# colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xE8E8E8, 1.0)
orange=Color(0xFFa500,1.0)
platc=Color(0xB9BDBB,1.0)
gooy=Color(0xCDF238,1.0)
white=Color(0xFFFFFF,1.0)
darkblue=Color(0x052099,1.0)

# lines
thinline= LineStyle(1, black)
thickline= LineStyle(5, black)
thickliner= LineStyle(5, red)
thicklineb= LineStyle(5, blue)
thickishline= LineStyle(2.5, black)
noline= LineStyle(0, black)
portalline= LineStyle(1, blue)
portalline2= LineStyle(1, orange)

class start(Sprite):
    asset = RectangleAsset(.5,500,thinline,black)
    def __init__(self, position):
        super().__init__(start.asset, position)
        self.vx=0
        
class finish(Sprite):
    asset = RectangleAsset(.5,500,thinline,black)
    def __init__(self, position):
        super().__init__(finish.asset, position)
        self.vx=0

class mpro(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(0)
        self.p=1
    def step(self):
        if self.p==1:
            self.x += mpros
            if self.x >= 55+(945/51.5):
                self.p = 0
        if self.p == 0:
            self.x += 0
        
        
class fpro(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(1)
    def step(self):
        self.x += fpros
        
class mpre(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(2)
    def step(self):
        self.x += mpres

class fpre(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(3)
    def step(self):
        self.x += fpres

class mop(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(4)
    def step(self):
        self.x += mops

class fop(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(5)
    def step(self):
        self.x += fops
        
class cyl(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(6)
    def step(self):
        self.x += cyls

class ath(Sprite):
    def __init__(self, position):
        super().__init__(triathlon.asset, position)
        self.setImage(7)
    def step(self):
        self.x += aths
        
class triathlon(App):
    asset = ImageAsset("images/spritesforathletes.jpg", Frame(0,0,55,50), 8, 'horizontal')
    def __init__(self, width, height):
        super().__init__(width, height)
        mpro((0,0))
        fpro((0,50))
        mpre((0,100))
        fpre((0,150))
        mop((0,200))
        fop((0,250))
        cyl((0,300))
        ath((0,350))
        start((55,0))
        finish((999,0))
    def step(self):
        for mp in self.getSpritesbyClass(mpro):
            mp.step()
        for fp in self.getSpritesbyClass(fpro):
            fp.step()
        for mpr in self.getSpritesbyClass(mpre):
            mpr.step()
        for fpr in self.getSpritesbyClass(fpre):
            fpr.step()
        for mo in self.getSpritesbyClass(mop):
            mo.step()
        for fo in self.getSpritesbyClass(fop):
            fo.step()    
        for c in self.getSpritesbyClass(cyl):
            c.step()
        for a in self.getSpritesbyClass(ath):
            a.step()    
myapp = triathlon(1000,1000)
myapp.run()
