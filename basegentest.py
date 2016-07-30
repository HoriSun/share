import numpy
r = numpy.array([[ 0.333706 , -0.17241  ,  0.0336918],
       [ 0.333483 , -0.178289 ,  0.0337403],
       [ 0.33353  , -0.178335 ,  0.0337279],
       [ 0.3337   , -0.178297 ,  0.0337377],
       [ 0.333877 , -0.178258 ,  0.0337251],
       [ 0.334045 , -0.178319 ,  0.0336923],
       [ 0.334376 , -0.178262 ,  0.0336958],
       [ 0.334702 , -0.178211 ,  0.0336741],
       [ 0.335086 , -0.178205 ,  0.0336567],
       [ 0.335514 , -0.178202 ,  0.0336346],
       [ 0.335965 , -0.178139 ,  0.0335953],
       [ 0.33651  , -0.178119 ,  0.0335759],
       [ 0.337068 , -0.178124 ,  0.033542 ],
       [ 0.337662 , -0.17805  ,  0.0334956],
       [ 0.338342 , -0.17802  ,  0.0334675],
       [ 0.339067 , -0.177995 ,  0.0334375],
       [ 0.339741 , -0.177952 ,  0.0333663],
       [ 0.340568 , -0.177897 ,  0.0333371],
       [ 0.341445 , -0.177842 ,  0.033309 ],
       [ 0.342199 , -0.177837 ,  0.0332182],
       [ 0.343143 , -0.177764 ,  0.0331808],
       [ 0.344169 , -0.177677 ,  0.0331582],
       [ 0.345103 , -0.177633 ,  0.0330871],
       [ 0.346056 , -0.177595 ,  0.0330103],
       [ 0.347208 , -0.177509 ,  0.0329905],
       [ 0.348227 , -0.17745  ,  0.03291  ],
       [ 0.349254 , -0.177438 ,  0.0328249],
       [ 0.350508 , -0.177309 ,  0.0328019],
       [ 0.351619 , -0.177253 ,  0.0327222],
       [ 0.352689 , -0.17724  ,  0.0326225],
       [ 0.353928 , -0.177146 ,  0.0325672],
       [ 0.355203 , -0.177034 ,  0.032515 ],
       [ 0.356336 , -0.177059 ,  0.0324172],
       [ 0.357629 , -0.176929 ,  0.0323566],
       [ 0.358963 , -0.176846 ,  0.0323059],
       [ 0.36012  , -0.176828 ,  0.0321989],
       [ 0.361437 , -0.176724 ,  0.0321339],
       [ 0.362827 , -0.176608 ,  0.0320865],
       [ 0.364075 , -0.176539 ,  0.0319967],
       [ 0.365326 , -0.17652  ,  0.0319097],
       [ 0.366744 , -0.176402 ,  0.0318646],
       [ 0.367995 , -0.176316 ,  0.0317737],
       [ 0.369237 , -0.176315 ,  0.0316855],
       [ 0.370564 , -0.176185 ,  0.0316161],
       [ 0.371913 , -0.176093 ,  0.0315553],
       [ 0.373094 , -0.176081 ,  0.0314573],
       [ 0.374411 , -0.175978 ,  0.0313935],
       [ 0.375747 , -0.175881 ,  0.0313373],
       [ 0.376896 , -0.175891 ,  0.031244 ],
       [ 0.378155 , -0.175778 ,  0.031178 ],
       [ 0.379456 , -0.175696 ,  0.0311264],
       [ 0.38061  , -0.1756   ,  0.0310474],
       [ 0.381729 , -0.175562 ,  0.0309689],
       [ 0.383005 , -0.175463 ,  0.0309273],
       [ 0.38408  , -0.175407 ,  0.0308518],
       [ 0.385106 , -0.17538  ,  0.0307746],
       [ 0.386309 , -0.175304 ,  0.0307375],
       [ 0.387306 , -0.175231 ,  0.0306688],
       [ 0.388236 , -0.175226 ,  0.0305962],
       [ 0.389331 , -0.17509  ,  0.0305609],
       [ 0.390233 , -0.175044 ,  0.0304996],
       [ 0.391041 , -0.175059 ,  0.0304306],
       [ 0.391955 , -0.17496  ,  0.0303888],
       [ 0.392852 , -0.174904 ,  0.0303516],
       [ 0.393504 , -0.174901 ,  0.0302846],
       [ 0.394318 , -0.174822 ,  0.0302524],
       [ 0.395102 , -0.17481  ,  0.0302225],
       [ 0.395617 , -0.174758 ,  0.0301637],
       [ 0.396282 , -0.174712 ,  0.0301354],
       [ 0.396971 , -0.174692 ,  0.0301184],
       [ 0.397445 , -0.174642 ,  0.0300816],
       [ 0.397838 , -0.174633 ,  0.0300426],
       [ 0.398394 , -0.17462  ,  0.030034 ],
       [ 0.398728 , -0.174578 ,  0.0300066],
       [ 0.398991 , -0.17454  ,  0.0299795],
       [ 0.399364 , -0.174595 ,  0.0299724],
       [ 0.399577 , -0.17455  ,  0.0299577],
       [ 0.399709 , -0.174473 ,  0.0299436],
       [ 0.399866 , -0.174596 ,  0.0299349],
       [ 0.399948 , -0.174543 ,  0.0299324],
       [ 0.399953 , -0.174441 ,  0.0299317],
       [ 0.39997  , -0.174488 ,  0.0299127],
       [ 0.399987 , -0.17455  ,  0.0298464],
       [ 0.399932 , -0.174462 ,  0.0297323],
       [ 0.399964 , -0.174491 ,  0.029581 ],
       [ 0.400003 , -0.174537 ,  0.0293883],
       [ 0.399931 , -0.174479 ,  0.0291472],
       [ 0.399962 , -0.174496 ,  0.0288781],
       [ 0.400004 , -0.174523 ,  0.0285757],
       [ 0.399946 , -0.174498 ,  0.0282341],
       [ 0.399964 , -0.1745   ,  0.0278726],
       [ 0.399993 , -0.174508 ,  0.0274888],
       [ 0.399972 , -0.174519 ,  0.0270815],
       [ 0.399964 , -0.174502 ,  0.0266623],
       [ 0.400005 , -0.174514 ,  0.0262363],
       [ 0.399956 , -0.17451  ,  0.025799 ],
       [ 0.399961 , -0.174505 ,  0.0253657],
       [ 0.400002 , -0.174509 ,  0.0249387],
       [ 0.399972 , -0.1745   ,  0.0245171],
       [ 0.399965 , -0.174511 ,  0.0241101],
       [ 0.400005 , -0.174516 ,  0.0237239],
       [ 0.399985 , -0.174508 ,  0.0233578],
       [ 0.399946 , -0.174493 ,  0.0230181],
       [ 0.400016 , -0.174541 ,  0.0227104],
       [ 0.399991 , -0.17452  ,  0.0224353],
       [ 0.400017 , -0.174533 ,  0.0222459],
       [ 0.400003 , -0.174491 ,  0.0220852],
       [ 0.399574 , -0.174416 ,  0.021351 ],
       [ 0.398771 , -0.174322 ,  0.0204238],
       [ 0.397883 , -0.174246 ,  0.0195145],
       [ 0.397027 , -0.17421  ,  0.0186609],
       [ 0.396299 , -0.174216 ,  0.0179153],
       [ 0.395994 , -0.174326 ,  0.0175363],
       [ 0.395541 , -0.174339 ,  0.0169647],
       [ 0.394928 , -0.174371 ,  0.0162558],
       [ 0.394281 , -0.174408 ,  0.01553  ],
       [ 0.39382  , -0.174493 ,  0.0148996],
       [ 0.393431 , -0.174562 ,  0.0143142],
       [ 0.393062 , -0.174621 ,  0.0137637],
       [ 0.392697 , -0.174692 ,  0.0132183]])

def normalize(v,axis=1): #vectors, shape=(n,3)
    v_norm = numpy.linalg.norm( v, axis=axis )
    nonzero = v_norm != 0 # zero may exists
    v[nonzero] /= numpy.expand_dims(v_norm,2)[nonzero] 


def gett(r): # r is the curve, r.shape = (n,3)
    assert len(r.shape) is 2
    assert r.shape[1] is 3

    c = r.shape[0] # count
    t = numpy.zeros(r.shape)
    t[:c-1] = r[1:] - r[:c-1]
    t[c-1] = t[c-2]

    # normalize t
    normalize(t)
    return t


# Discrete fenet frame B (binormal vector)
def getb(t): # t is the tangent vector
    assert len(t.shape) is 2
    assert t.shape[1] is 3
    
    c = t.shape[0]
    b = numpy.zeros(t.shape)
    b[1:] = numpy.cross(t[:c-1],t[1:]) #
    b[0] = b[1]
    
    normalize(b)

    norm = lambda x:numpy.linalg.norm(x,axis=1)
    keepn = (norm(b)==0)#*(norm(t)!=0) # straight line

    c = t.shape[0]
    i = 0
    while i < c:
        if not keepn[i]:
            for j in xrange(i-1,-1,-1):
                b[j] = b[j+1]
            break
        i += 1

    while i < c:
        if keepn[i]:
            b[i] = b[i-1]
        i += 1
    
    b[norm(t)==0] = numpy.zeros((3,))
    return b





def basegenRot(t, n, b):
    base = numpy.transpose(numpy.array([t,n,b]),axes=(1,2,0))
    return base


def test():
    global r
    t = gett(r[::10])
    b = getb(t)
    n = numpy.cross(b,t)
    base = basegenRot(t,n,b)
    return t,b,n

db = numpy.array([[ 0.,  1.,  0.],
       [ 1.,  0.,  0.],
       [ 0.,  0.,  1.],
       [ 0., -1.,  0.],
       [ 0.,  0., -1.],
       [ 0.,  0.,  0.],
       [-1.,  0.,  0.]])


db1 = numpy.array([[ 0.        ,  1.        ,  0.        ],
       [-0.70710678,  0.70710678,  0.        ],
       [-0.70710678,  0.        ,  0.70710678],
       [ 1.        ,  0.        ,  0.        ],
       [ 0.70710678,  0.        ,  0.70710678],
       [ 0.        , -1.        ,  0.        ],
       [ 0.        ,  0.        ,  1.        ],
       [-0.70710678, -0.70710678,  0.        ],
       [-1.        ,  0.        ,  0.        ],
       [ 0.70710678,  0.70710678,  0.        ],
       [-0.70710678,  0.        , -0.70710678],
       [ 0.        ,  0.70710678, -0.70710678],
       [ 0.        , -0.70710678,  0.70710678],
       [ 0.        ,  0.70710678,  0.70710678],
       [ 0.        ,  0.        , -1.        ],
       [ 0.        , -0.70710678, -0.70710678],
       [ 0.70710678,  0.        , -0.70710678],
       [ 0.        ,  0.        ,  0.        ],
       [ 0.70710678, -0.70710678,  0.        ]])


def basegen19One(t, n, b):
    nb = -b
    nt = -t
    nn = -n
    # DCC19 base directions
    base = numpy.transpose(
        numpy.dstack([
            numpy.zeros(t.shape),
            t,n,b,nb,nn,nt,
            n +t, n +nt, nn+t, nn+nt,
            b +t, b +nt, b +n, b +nn,
            nb+t, nb+nt, nb+n, nb+nn
        ]),
        axes=(0,2,1))
    #print base
    #b_s = base
    #return base
    normalize(base,axis=2)
    return base[0]


def basegenOneRot(t, n, b, it=1): # default for DCC19
    assert len(t.shape) is 1
    assert len(n.shape) is 1
    assert len(b.shape) is 1
    rot = numpy.array([t,n,b]).T
    return numpy.dot(rot,db1.T).T

t,b,n = test()
base = basegenRot(*(test()))
base_ = numpy.transpose(numpy.dot(base,db.T),axes=(0,2,1))

T,N,B = t[0],n[0],b[0]
a = basegenOneRot(T,N,B).tolist()
b = basegen19One(T,N,B).tolist()
def cmp(x,y):
    for i in xrange(3):
        if(x[i]>y[i]):
            return 1
        elif x[i]<y[i]:
            return -1
    return 0

a.sort(cmp=cmp)
b.sort(cmp=cmp)
diff = numpy.array(a)-numpy.array(b)