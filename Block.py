import hashlib
import datetime
from textwrap import wrap

class Block:
    global content_format
    content_format = "height|prev_hash|year|institution|accomplishment"
    
    def __init__(self,prev_hash="genesis",year=2000,institution="Mother",accomplishment="Birth",char="0",len=2,separator="|"):
        self.year = year
        self.institution = institution
        self.accomplishment = accomplishment
        self.prev_hash = prev_hash
        self.separator = "|"
        self.char = char
        self.len = len
        self.nonce = 0
        
        # print content_format
        # print "based on this format..."
        contents = self.prev_hash+self.separator+str(self.year)+self.separator+self.institution+self.separator+self.accomplishment+self.separator+str(self.nonce)
        
        # print contents
        self.hash = hashlib.sha256(contents).hexdigest()
        
        matchString = ""
        for i in range(0,self.len):
            matchString+=self.char
            
        print "Looking for a block hash starting with...\t"+matchString
        
        print "\n\nHashing .",
        while self.hash[:self.len] != matchString:
            self.hash = hashlib.sha256(contents).hexdigest()
            self.nonce+=1
            contents = self.prev_hash+self.separator+str(self.year)+self.separator+self.institution+self.separator+self.accomplishment+self.separator+str(self.nonce)
            # print self.hash
            if self.nonce % 1000 == 0:
                print '.',
        print "\nBLOCK FOUND!\tCONTENTS >\t"+contents
        print "\nHASH OF NEW BLOCK:\t"+self.hash
    
    def getHash(self):
        return self.hash
        
        
    def toString(self):
    
        #---------------------------------
        #|          HASH                 |
        #---------------------------------
        #|contents                       |
        #---------------------------------
        
        output = ""
        output += '|{:-^70}|'.format('')+"\n"
        output += '|{:^70}|'.format(self.prev_hash)+"\n"
        output += '|{:-^70}|'.format('')+"\n"
        output += '|{:<70}|'.format(self.year)+"\n"
        output += '|{:^70}|'.format(self.institution)+"\n"
        if len(self.accomplishment)>70:
            for line in wrap(self.accomplishment):
                output += '|{:>70}|'.format(line)+"\n"
        else:    
            output += '|{:>70}|'.format(self.accomplishment)+"\n"
        output += '|{:-^70}|'.format('')+"\n"        
        output += '|{:^70}|'.format(self.hash)+"\n"
        output += '|{:_^70}|'.format('')
        
        return output
    

    
def mainTester():
    print 'testing'
    
    x = Block()
    
    
if __name__ == "__main__":
    mainTester()