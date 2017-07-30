#!/usr/bin/env python
# coding:utf-8

import sys
import logging
import os
import operator


class evalNumbers():
    def __init__(self, mode, srcpath, dstpath):
        self.source_path = srcpath
        self.target_path = dstpath
        self.mode=mode
        self.numEval()
    def readfile(self, path):
        data = None
        with open(path, "r") as text_file:
            data = text_file.read()
        return data


    def savefile(self, path, data):
        with open(path, "w") as text_file:
            text_file.write(data)
            if os.path.isfile(path):
                return True
            else:
                return False
    def docount(self,num):
        if self.numcounts.has_key(num):
            self.numcounts[num]+=1
        else:
            self.numcounts[num]=1

    def sortdictdata(self):
        d_sorted_by_value=sorted(self.numcounts.items(), key=operator.itemgetter(1))
        return d_sorted_by_value

    def numEval(self):
        if self.source_path is None:
            logging.ERROR("Missing parameter of csvPath")
            return -1
        if self.target_path is None:
            logging.ERROR("Missing parameter of csvPath")
            return -1

        lotto=self.readfile(self.source_path)
        lotto=lotto.split("\n")
        self.numcounts=dict()

        for row in range(0,len(lotto)):
            nums=lotto[row].split(",")
            for num in nums:
                n=int(num)
                self.docount(n)

        lottosorted=self.sortdictdata()

        rpt = "\"Lotto\",\"Count\"\n"

        for r in lottosorted:
            row = "{},{}\n".format( r[0],r[1])
            rpt+=row
        self.savefile(self.target_path,rpt)
        print(rpt)



def main():
    if len(sys.argv) == 3:
        print sys.argv
        num = evalNumbers(0, sys.argv[1], sys.argv[2])
    else:
        print sys.argv

if __name__ == '__main__':
    main()


