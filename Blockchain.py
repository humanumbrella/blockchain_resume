from Block import Block
import datetime

class Blockchain:
    
    def __init__(self,char="0",len=2,genYear=1980):
        self.mainchain = []
        self.char = char
        self.len = len
        self.genYear = genYear
        self.addBlock("genesis")
    
    def addBlock(self,contents):
        if contents == "genesis":
            newBlock = Block(char=self.char,len=self.len,year=self.genYear)
        else:
            c = contents.split("|")
            
            #format year|institution|accomplishment
            yr = c[0]
            inst = c[1]
            accomp = c[2]

            
            prev_hash = self.mainchain[len(self.mainchain)-1].getHash()
            newBlock = Block(prev_hash=prev_hash,year=yr, institution=inst,accomplishment=accomp,char=self.char,len=self.len)
            
        self.mainchain.append(newBlock)
    
    def getHeight(self):
        return str(len(self.mainchain))
        
    def toString(self,heights=False):
        output = ""
        count = 0
        for block in self.mainchain:
            if block is not None:
                if heights:
                    output+= "\nheight:\t"+str(count)+"\n"
                output+= block.toString()+"\n"
                output+= ' {:~^70} '.format('')+"\n"
                count+=1
        return output
        
if __name__ == "__main__":
    t0 = datetime.datetime.now()
    
    b = Blockchain(char="0",len=3)
    b.addBlock("2001|life|birthday")
    b.addBlock("2004|life|birthday")
    b.addBlock("2005|surgery|broken arm")
    
    t1 = datetime.datetime.now()
    
    print '\n\n'
    print "Blockchain height: "+b.getHeight()
    print b.toString()
    print '\n\nRuntime: '
    print t1-t0