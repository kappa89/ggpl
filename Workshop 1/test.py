from pyplasm import *

X = [.1,-.1]
a = QUOTE(X*5)
aa = PROD([a,a])
#(bx,bz) (given dimensions of beam section)
#(px,py) (given dimensions of pillar section)
#[dy1,dy2,...] (distances between axes of the pillars)
#[hz1,hz2,...] (interstory heights)


pillarSection = (.1, .5)
pillarDistance = [-.2, -.7, -.9]

bxQ = QUOTE([pillarSection[0], -.2, pillarSection[0], -.7, pillarSection[0], -.9, pillarSection[0]])
byQ = QUOTE([pillarSection[1]])

lineaQ = QUOTE([2])
base = PROD([bxQ, byQ])
x = PROD([base, lineaQ])

VIEW(x)