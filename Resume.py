from Blockchain import Blockchain
import time
import datetime

def main():
    
    t0 = datetime.datetime.now()
    
    b = Blockchain(char="0",len=5,genYear=1980)
    
    b.addBlock("1984|Life|Memristor Initialized")
    b.addBlock("1998|Education|High School Graduation")
    b.addBlock("2002|Project|Bitcoin seed")
    b.addBlock("2002|Education|College Graduation")
    b.addBlock("2004|Project|Refurbish machine")
    b.addBlock("2015|Leadership|Win a National Championship")
    b.addBlock("2018|Employment|Build cool stuff.")
    
    t1 = datetime.datetime.now()
    print "\n\n\n"
    
    chain = b.toString()
    
    print '\n\n'
    print "Blockchain height: "+b.getHeight()
    print chain
    print '\n\nRuntime: '
    print t1-t0
    
    
    now = time.strftime("%Y%m%d-%H%M%S")
    
    file = open("Resume-"+now+".txt",'w')
    file.write(chain)
    file.close()

if __name__ == "__main__":
    main()