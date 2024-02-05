# by P.Salehi 
# First Version 1/2024

from copy import deepcopy
import numpy as np 
import cv2 
from os.path import exists 
from os import makedirs
from os.path import join
class utils : 
    @staticmethod 
    def CreateFolderIfnotExists(f) : 
        if not exists(f) : 
            makedirs(f)
        else : 
            pass
class Addernode : 
    def __init__(self, start, end, level = 0) : 
        self._s = start 
        self._e = end
        self._l = level
        assert(end >= start)
    def get(self, returnLevel = False) : 
        if(returnLevel == False) : 
            return self._s, self._e
        else : 
            return self._s, self._e, self._l
    def copyFrom(self, n) : 
        start, end, level = n.get(True)
        self._s = start 
        self._e = end 
        self._l = level

    def setLayer(self, l) :
        self._l = l
    @property
    def IsFinished(self) : 
        return self._s == 0
    def __str__(self) : 
        return self.getStr(False)
    

    def getStr(self, include_layer = False) : 
        if(include_layer) : 
            return "({2}, {0}, {1})".format(self._s, self._e, self._l)
        else : 
            return "[{1} : {0}]".format(self._s, self._e) 

    def getIndexed(self, wname, include_layer = True) : 
        if(include_layer) : 
         return "{0}_{3}_{1}_{2}".format(wname, self._s, self._e, self._l)
        else : 
         return "{0}_{1}_{2}".format(wname, self._s, self._e)

    @staticmethod 
    def adds(n1 , n2) :

        s1, e1, l1 = n1.get(True)
        s2, e2, l2 = n2.get(True)
       # assert(l1 == l2)

        if(s1 <= s2) :
            assert(e1 <= e2)
            min_s = s1 
            min_e = e1 
            max_s = s2 
            max_e = e2 
        else : 
            assert(e1 >= e2)
            min_s = s2 
            min_e = e2 
            max_s = s1 
            max_e = e1
        if ( not(max_s - min_e <= 1 and min_e <= max_s) ) : 
            raise RuntimeError("(ERROR) : Concatenation is failed for {0}, {1}".format(n1 ,n2))
        return Addernode(min_s, max_e, l1 + 1)
    
    def add(self, n) : 
        d = Addernode.add2(self, n) 
        self.copyFrom(d)
        return self

class Layer :
    @property 
    def L(self) : 
        return self._l 
    @property 
    def N(self) : 
        return self._n
    def __init__(self, *args) : 
        assert(len(args) <= 2) 
        if(len(args) == 2) : 
            n , value = args 
            print(n , value)
            self._l = [deepcopy(value)] * n 
            self._n = n

        else :
            arg = args[0]
            if(type(arg) == Layer) : 
                self._n = len(arg.N) 
                self._l = deepcopy(arg.L)
            elif(type(arg) == list) : 
                self._n = arg.N
                self._l = arg.L
            elif (type(arg) == int) : 
                # n = adder bitwidth
                self._n = arg
                self._l = [Addernode(x, x) for x in range(self._n)]
            else : 
                raise NotImplementedError("ERROR")
    
    def __len__(self) : 
        return len(self._l)
    def __getitem__(self, key):
        return self._l[key]

    def __setitem__(self, key, value):
        self._l[key] = value

    def __str__(self) : 
        s = ", ".join(str(x) for x in self.L)
        s = "[" + s + "]"
        return s



class Cell : 
    def __init__(self, name : str, wires: list) : 
        self._wires = wires
        self._name = name
    @property 
    def Wires(self) : 
        return self._wires
    @property 
    def Name(self) : 
        return self._name
    

class GPCell(Cell) : 
    def __init__(self, A, B, G, P , name = "") :
        self._g = G 
        self._p = P 
        self._a = A 
        self._b = B 
        wires = [G, P]
        Cell.__init__(self, name, wires)
    def __str__(self) : 
        return "GPCell {4} (.A({0}), .B({1}), .G({2}), .P({3}));".format(self._a, self._b, self._g, self._p, self.Name)
class GrayCell(Cell) : 
    def __init__(self, PIK, GIK, GKJ, GIJ, name = "") :
        self._pik = PIK 
        self._gik = GIK 
        self._gkj = GKJ 
        self._gij = GIJ
        wires = [PIK, GIK, GKJ, GIJ]
        Cell.__init__(self, name, wires)
    def __str__(self) : 
        return "GrayCell {4} (.PIK({0}), .GIK({1}), .GKJ({2}), .GIJ({3}));".format(self._pik, self._gik, self._gkj, self._gij, self.Name)

class BlackCell(Cell): 
    def __init__(self, PIK, GIK, GKJ, PKJ, GIJ, PIJ,  name = "") :
        self._pik = PIK 
        self._gik = GIK 
        self._gkj = GKJ 
        self._gij = GIJ
        self._pkj = PKJ
        self._pij = PIJ
        wires = [PIK, GIK, GKJ, GIJ, PKJ, PIJ]
        Cell.__init__(self, name, wires)
    def __str__(self) : 
        return "BlackCell {6} (.PIK({0}), .GIK({1}), .GKJ({2}), .PKJ({3}),  .GIJ({4}), .PIJ({5}));".format(self._pik, self._gik, self._gkj, self._pkj, self._gij, self._pij, self.Name)
    

class XorCell(Cell) : 
    def __init__(self, out, in1, in2, name = "") : 
        self._i0 = in1 
        self._i1 = in2 
        self._o  = out 
        wires = [in1, in2, out]
        Cell.__init__(self, name, wires)
    def __str__(self) : 
        return "xor {0} ({1}, {2}, {3});".format(self.Name, self._o, self._i0, self._i1)


class AssignCell(Cell) : 
    def __init__(self, out , inp, name = "") : 
        self._i = inp 
        self._o = out 
        wires = [inp, out]
        Cell.__init__(self, name, wires)
    def __str__(self) : 
        return "assign {0} = {1};".format(self._o, self._i)

class Connection : 
  def __str__(self) : 
        return str(self._conn)


  # conventional connection 
  # (lsrc, src), (ldst, dst), type
  def getTupple(self) : 
        return self._conn
  

class FlatConnection(Connection) :
    
    def __init__(self, l, src, dst , type) : 
        '''
            l : level 
            src, dst : index
            type : "G(GRAY)" , "B(BLACK)", "U(BUFFER)"
        '''
        if (dst < src) : 
            dst, src = src, dst
        self._conn = (l, src, dst, type)
    @property 
    def Level(self) : 
        return self._conn[0]
    @property
    def Type(self) : 
        return self._conn[3]
    @property 
    def Nodes(self) : 
        return self._conn[1], self._conn[2]
    
    def getTupple(self) : 
        l = self.Level 
        x, y = self.Nodes 
        t = self.Type
        return  ((l, x), (l + 1, y), t)

  
class Identifier() : 
    def __init__(self, name, istart = -1, iend = -1) : 
        self._base = name
        self._isVector = not (istart == iend == -1)
        self._s, self._e = (istart, iend) if (istart < iend) else (iend, istart)

    @property 
    def Start(self) : 
        return self._s
    @property 
    def End(self) : 
        return self._e
    @property 
    def Base(self) : 
        return self._base
    
    def __str__(self) : 
        return str((self._base, self._s, self._e))

    @staticmethod 
    def getIdentifier(s : str) : 
        # set inital for not vector identifier
        start = end = -1
        startstr = endstr = ""
        STATE_SEENOPEN = 1
        STATE_SEENCOLON  = 2 
        STATE_SEENCLOSE  = 0
        state = 0
        s = s.replace(" ", "")
        base = ""

        for c in s : 
            if(state == 0) : 
                if(c == "[") : 
                    state = STATE_SEENOPEN
                else : 
                    base += c
            elif(state == STATE_SEENOPEN) :
                if(c == ":") : 
                    state = STATE_SEENCOLON
                elif(c == "]") : 
                    start = end = int(startstr)
                    state = STATE_SEENCLOSE
                    break
                else :
                    startstr += c

            elif(state == STATE_SEENCOLON) : 
                if(c == "]") : 
                    state = STATE_SEENCLOSE
                    start = int(startstr)
                    end   = int(endstr)
                    break
                else :
                    endstr += c
        if(state != 0) : 
            raise RuntimeError("Identifier matching failed for " + s)
        return (Identifier(base, start, end))
    def getDeclaration(self ) : 
        if(self._isVector) : 
            return "{0} [{1} : {2}]".format(self._base, self._e, self._s)
        else : 
            return self.Base

    def update(self, idx) : 
        assert((idx.Base == self.Base) and (self._isVector == True))
        self._s =  min(idx.Start, self.Start) 
        self._e =  max(idx.End,   self.End)


    
    
class prefixAdder : 
    def __init__(self, n, name) : 
        '''
            n : number of bits (2**n)
            name : module name
        '''
        self._n = n
        assert(n > 1)
        self._lc  = 0
        self._layers = [Layer(n)]
        self._conns  = []
        self._name = name
    def AddLayer(self) : 
        self._lc += 1
        self._layers.append( deepcopy(self._layers[self._lc - 1]) )
       # for i in range(len(self._layers[self._lc])) : 
       #     self._layers[self._lc][i].setLayer(self._lc)

    @property 
    def Name(self) : 
        return "{0}{1}b".format(self._name, self._n)

    @property 
    def NBits(self) : 
        return self._n
    def drawTree(self, include_layer = False) : 
        N = self._n
        D = 100
        TextD = int(D * 0.2)
        L = len(self._layers)
        image = np.ones(((L+1) * D, (N+1) * D, 3), "uint8") * 255

        for layer in range(L) : 
            for i in range(N) : 
                image = cv2.circle(image, (D * (i + 1), (layer + 1) * D), int(D / 8), (0,0,255), 4)
                image = cv2.putText(image, (self._layers[layer][self._n - i - 1]).getStr(include_layer),  (D * (i + 1), (layer + 1) * D + (TextD)), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8,  
                 (0,0,255), 1, cv2.LINE_AA, False) 
        for conn  in self._conns :
            src = conn.getTupple()[0]
            dst = conn.getTupple()[1]
            image = cv2.line(image, (D * ( N - src[1] ), (  src[0] + 1 ) * D), (D * (N - dst[1]), (dst[0] + 1) * D), (255, 0, 0), 5) 
        cv2.imwrite("test.png", image)

        
    def checkFinal(self) : 
        starts = []
        for n in self._layers[-1] : 
            starts.append(n.get()[0])
        unmached = []
        for i, ii in enumerate(starts) :
            if(starts[i] != 0) : 
                unmached.append((i, ii))
        if(len(unmached)) : 
            print("(ERROR) : Unmached Items : ", unmached)
            return False
        else :
            return True


    '''
    B : Black 
    G : Gray 
    B : Buffer
    '''

    def SetConnection(self, connections) : 
        """
        Set Connection for raw PrefixAdder module 

        Params : 
            connections : a 2D Python list, where each row consists of connections in a single layer of prefix adder graph abstraction
        """
        for layerConns in connections : 
            self.AddLayer()
            for conn in layerConns :
                self.AddConnectionOnCurrentLayer(conn[0], conn[1])
    def AddConnectionOnCurrentLayer(self, i0 : int, i1 : int, type = "B") : 
        lp = self._lc  - 1
        #print(i0, i1)
        imax, imin = (i1 , i0) if (i1 > i0) else (i0, i1)
        self._layers[self._lc][imax] = Addernode.adds(self._layers[lp][imax], self._layers[lp][imin])
        self._conns.append(FlatConnection(lp, i0, i1, type))
        
    def printAllLayers(self) : 
        s = "" 
        for i, l in enumerate(self._layers) : 
            s +=  "     ({0}) -> {1}\n".format(i, l)
        print (s)   

    def GenerateCells(self, autoType = True) : 
        debug = True
        i = 0
        # Handling S[N]
        # Handling C[0]
        cells = [
            AssignCell("c[0]", "1'b0", "UASSc0"),
            AssignCell("c[1]", "g_0_0_0", "UASSc1"),
            AssignCell("S[{0}]".format(self._n), "c[{0}]".format(self._n), "UASS" + str(self._n))

            
        ]
        for i in range(self._n) : 
            temp_ii = Addernode(i, i, 0)
            # P And G Generators (GPCELLS)
            cells.append( 
                GPCell(
                       A = "A[{0}]".format(i),
                       B = "B[{0}]".format(i), 
                       G = temp_ii.getIndexed("g"),
                       P = temp_ii.getIndexed("p"),
                       name = "UGP" + str(i)
                      )
            )
            #Sum Generator (last bit is S[N] Carry)
            cells.append(
                XorCell(
                    "S[{0}]".format(i),
                    temp_ii.getIndexed("p"), 
                    "c[{0}]".format(i),
                    name = "UXOR" + str(i)
                    )
            )

        
      
        if(autoType) :
            for con in self._conns : 
                if(type(con) != FlatConnection) : 
                    raise NotImplementedError("The Connection Module only implemented for FlatConnection, But passed Type is ", type(con))
                #print(con)
                x, y = con.Nodes
                l = con.Level
                src0 = self._layers[l][x]
                src1 = self._layers[l][y]
                dst1 = self._layers[l + 1][y]
                u = []
                if dst1.IsFinished : 
                    u =  [
                        GrayCell(
                            PIK = src1.getIndexed("p"),
                            GIK = src1.getIndexed("g"),
                            GKJ = src0.getIndexed("g"),
                            GIJ = dst1.getIndexed("g"),
                            name = "U" + str(i)
                        ),
                        # assign  g_i_0 = gLl_i_0, g_i_0 used in sum xor
                        AssignCell(
                            "c[{0}]".format(y + 1),
                            dst1.getIndexed("g"),
                            "UASS{0}".format(y)
                        )
                        ]
                    
                else : 
                        u = [BlackCell( 
                            PIK = src1.getIndexed("p"),
                            GIK = src1.getIndexed("g"),
                            GKJ = src0.getIndexed("g"),
                            PKJ = src0.getIndexed("p"),
                            GIJ = dst1.getIndexed("g"),
                            PIJ = dst1.getIndexed("p"),
                            name = "U" + str(i)
                        )]
                cells.extend(u)
                if debug : 
                    pass
                   # print(con, cells[-1])
                i += 1
        else : 
            raise NotImplemented("Manual cell generation has not been implemented at this time.")
        return cells
    


    def retrieveWires(self, ws) : 
        ws = (set(ws))
        retwires = []
        inputoutputs = ["A", "B", "S", "1'b0", "1'b1"]
        identifiers = {}
        for w in ws : 
            id = Identifier.getIdentifier(w)
            if(id.Base not  in inputoutputs) : 
                if(id.Base in identifiers) : 
                    identifiers[id.Base].update(id)
                else : 
                    identifiers[id.Base] = id
        for idx in identifiers.values() : 
            retwires.append(idx.getDeclaration())
        return retwires

    def GenerateTestBench(self, Exhaustive = False, start = -1, end = -1, ntest = 1000, root = "") :
        '''
         Generates a Verilog test figure for prefix adder

         Params : 
             Exhaustive :
                Exhaustive = False => parameters : ntest(The number of test vector applied as input)
                Exhaustive = True  => parameters : start, end(Exhaustive search in (start, end) space)
             root :  the destination folder where the verilog file will be written.
        '''
        
        if (len(root)) : 
            utils.CreateFolderIfnotExists(root)
        if(Exhaustive) : 
            cond = (start <= end) and (end < 2 ** self._n - 1)
            start = 0 if start < 0 else start 
            end   = -1 if end < 0 else end 
            if(not cond) : 
                raise ValueError("(start <= end) and (end < 2 ** self._n - 1)")
            prefixAdder.generateExhTestbench(self, start, end, root) 
        else : 
            prefixAdder.generateRndTestbench(self, ntest, root)



    @staticmethod 
    def generateExhTestbench(pa, start, end, root = "") : 
        """Generates Exhaustive Testbench for prefixAdder ranged between (start, end) 
            pa : PrefixAdder Type 
            ntest : number of random testvector
        """
        fname = join(root, pa.Name + "_etb.v")
        with open(fname, "w") as fw : 
            with open("testbench.v") as tb : 
                for pline in tb :
                    pline = pline.replace("_X_", pa.Name).replace("_N_", str(pa.NBits)).replace("testbench", pa.Name + "_etb").replace(
                        "_E_", str(end + 1)).replace("_S_", str(start))
                    fw.write(pline + "\n")
    @staticmethod 
    def generateRndTestbench(pa, ntest, root = "") : 
        """Generates Random Testbench for prefixAdder 
            pa : PrefixAdder Type 
            ntest : number of random testvector
        """
        nbits = pa.NBits 
        from math import ceil
        n32 = ceil(nbits / 32) 
        xrx = ",".join((["$random()"] * n32))
        fname = join(root, pa.Name + "_rtb.v")
        with open(fname, "w") as fw : 
            with open("testbenchr.v") as tb : 
                for pline in tb :
                    pline = pline.replace("_N_", str(pa.NBits)).replace("_X_", pa.Name).replace("_T_", str(ntest)).replace("_R_", xrx).replace("testbench", pa.Name + "_rtb")
                    fw.write(pline + "\n")

    def GenerateFile(self, root = "") : 
        """ Generates Verilog File for Prefix Adder
            root :  the destination folder where the verilog file will be written.
        """
        if (len(root)) : 
            utils.CreateFolderIfnotExists(root)
        N = self._n
        moduleName = self._name
        ws = []
        for g in self.GenerateCells() : 
            ws.extend(g.Wires)
        ws = self.retrieveWires(ws)

        wires_line = ", ".join(ws)
        wires_line = "wire " + wires_line + ";\n"
        cells = [str(g) for g in self.GenerateCells()]
        cells.sort()
        
        modules_line = "\n".join(cells) + "\n"
        header_line = "module {0} (A, B, S);\n".format(self.Name)
        inputs_line =  "input [{0} : 0] A;\n".format(N - 1)
        inputs_line += "input [{0} : 0] B;\n".format(N - 1)
        inputs_line += "output [{0} : 0] S;\n".format(N)
        end_line=  "endmodule"
        module_description = header_line + inputs_line + wires_line +  modules_line + end_line 
        file = join(root, self.Name + ".v")
        with open(file,  "w") as f : 
            f.write(module_description)

    
    def printAllConnections(self) : 
        for con in self._conns : 
            print(con)
    @property 
    def Layers(self) : 
        return self._layers



class ConnectionGenerator : 
    TYPE_RIPPLE = 0
    TYPE_LFA = 1 # Ladner Fischer 
    TYPE_KOGGESTONE = 2 # Kogge Stone
    TYPE_HANCARLSON = 3 # Han Carlson
    TYPE_BRENTKUNG  = 4 # Brent Kung
    def __init__(self, type, n) : 
        '''
             n : number of bits (2**n)

             Type : PrefixAdderType, implemented Types : 
                TYPE_RIPPLE = 0

                TYPE_LFA = 1 # Ladner Fischer

                TYPE_KOGGESTONE = 2 # Kogge Stone

                TYPE_HANCARLSON = 3 # Han Carlson

                TYPE_BRENTKUNG  = 4 # Brent Kung

        '''
        self._n = n 
        self._t = type 
        if(type not  in [ConnectionGenerator.TYPE_RIPPLE, ConnectionGenerator.TYPE_LFA, ConnectionGenerator.TYPE_KOGGESTONE, ConnectionGenerator.TYPE_HANCARLSON, ConnectionGenerator.TYPE_BRENTKUNG]) :
            raise ValueError("{0} is not a valid type.".format(type))
    def GetAsList(self) : 
        """Returns Connection Matrix as python list."""
        if(self._t == ConnectionGenerator.TYPE_RIPPLE) : 
            return ConnectionGenerator._conn_ripple(self._n)
        elif(self._t == ConnectionGenerator.TYPE_LFA) : 
            return ConnectionGenerator._conn_lfa(self._n)
        elif(self._t == ConnectionGenerator.TYPE_KOGGESTONE) : 
            return ConnectionGenerator._conn_ks(self._n)
        elif(self._t == ConnectionGenerator.TYPE_HANCARLSON) : 
            return ConnectionGenerator._conn_hc(self._n)
        elif(self._t == ConnectionGenerator.TYPE_BRENTKUNG) : 
            return ConnectionGenerator._conn_bk(self._n)

        

    @staticmethod
    def _power2Checker(n : int) : 
        """check if n is a power of two"""
        cond = (n > 1 and (n & (n-1) == 0))
        if(not cond) : 
            raise ValueError("Ensure that n is greater than 1 and is a power of two")
    @staticmethod 
    def _conn_ripple(n : int) : 
        "Ripple Carry Adder Connection Generator"
        if(n <= 1 ) : 
            raise ValueError("n must be greater than 1")
        conns = []
        for i in range(n - 1) : 
            conns.append([(i, i + 1)])
        return conns
    

    @staticmethod 
    def _conn_hc(n : int) : 
        """Han Carlson Connection Generator"""
        ConnectionGenerator._power2Checker(n)
        from math import log2 
        imax = int(log2(n))
        conns = [] 
        # L0 
        n0s = list(range(0, n, 2))
        n1s = list(range(1, n, 2))
        conns.append(list(zip(n0s, n1s)))
        # Li 
        for i in range(1, imax) : 
            step = 2**i 
            n0s = list(range(1, n, 2))
            n1s = list(range(step + 1, n, 2))
            conns.append(list(zip(n0s,n1s)))
            
        # LFinal
        n0s = list(range(1, n, 2))
        n1s = list(range(2, n, 2))
        conns.append(list(zip(n0s, n1s)))
        return conns
    


    
    @staticmethod 
    def _conn_bk(n : int) : 
        "Brenk-Kung Connection Generator"
        
        ConnectionGenerator._power2Checker(n)
        return ConnectionGenerator._conn_bk_rec(n)
    
    @staticmethod 
    def _conn_bk_rec(n : int) : 
        # recursive implementation of brent-kung
        if(n == 2) : 
            return [[(0,1)]]
        # add first Layer
        conns = []
        conns.append(list(zip(range(0, n  - 1, 2), range(1,  n, 2))))
        # construct K2 
        connsk2 = ConnectionGenerator._conn_bk(n // 2)
        # translate to current state 
        new_conns = []
        for layer in connsk2 : 
            new_conns.append([])
            for c in layer : 
                new_conns[-1].append((c[0] * 2 + 1, c[1] * 2 + 1))
        conns.extend(new_conns)

        # add final Layer
        conns.append(list(zip(range(1 , n - 2, 2), range(2, n - 1, 2))))
        return conns

    @staticmethod 
    def _conn_ks(n : int) :
        "KoggeStone Connection Generator"
        ConnectionGenerator._power2Checker(n)
        from math import log2 
        imax = int(log2(n))
        conns = []
        for i in range(imax) : # 0, 1, 2 ... log2(n) - 1
            clayer  = [] #current layer 
            stepi = 2 ** i 
            n0s = list(range(0, n - stepi))
            n1s = list(range(stepi, n))
            clayer.extend(list(zip(n0s, n1s))) # (i -> {(i + 1), ... (i + 1 + ri)})
            conns.append(clayer)
        return conns 
    
    @staticmethod 
    def _conn_lfa(n : int) : 
        "Lander Fischer Connection Generator"
        ConnectionGenerator._power2Checker(n)
        from math import log2
        imax  = int(log2(n))
        conns = []
        #imax = N - 1
        for i in range(imax) : 
            starti = 2 ** i - 1 
            stepi  = 2 ** (i + 1)
            ri     = 2 ** i 
            clayer = [] #current layer
            for nodei in range(starti, n, stepi) : # [starti, starti + stepi ....] 
                neigbours = list(range(nodei + 1, nodei + 1 + ri)) # neighbours = [nodei + 1, ... nodei + ri]
                clayer.extend(list(zip([nodei] * len(neigbours), neigbours))) # (i -> {(i + 1), ... (i + 1 + ri)})
            conns.append(clayer)
        return conns        




