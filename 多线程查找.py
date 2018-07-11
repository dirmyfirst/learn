import time
import os
from threading import Thread

class greplt(Thread):
    def __init__(self,cdcfile,keyword):
        Thread.__init__(self)
        self.cdcf = cdcfile
        self.keyw = keyword.upper()
        self.report = ""
    def run(self):
        if ".cdc" in self.cdcf:
            self.report = mark(self.cdcf,self.keyw)
            
def grpSearch(cdcpath,keyword):
    begin = time.time()
    filelist = os.listdir(cdcpath)
    print (filelist)
    serachlist = []
    for cdcf in filelist:
        pathcdcf = "%s/%s"%(cdcpath,cdcf)
        current = greplt(pathcdcf,keyword)
        searchlist.append(current)
        current.start()
    for seracher in searchlist:
        searcher.join()
        print("Search from",searcher.cdcf,"out",searcher.report)
    print ("usage %s s"%(time.time()-begin))

if __name__ == "__main__":
    grpSearch("aa","time")
