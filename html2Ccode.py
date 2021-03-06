#!/usr/bin/python

import sys, getopt
import time;  # This is required to include time module.

inputfile =""
outputfile =""
param =""

def openFile(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:o:p:",["ifile=","ofile=","para="])
   except getopt.GetoptError:
      print 'html2Ccode.py -i <inputfile> -o <outputfile> -p <parameter>'
      print str(IOError)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'html2Ccode.py -i <inputfile> -o <outputfile> -p <parameter>'
         sys.exit(3)
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-p", "--para"):
         parameter = arg
   print 'Input file is ', inputfile
   print 'Output file is ', outputfile
   print 'Parameter is ', parameter
   return inputfile,outputfile,parameter

def main(argv):
   Ifile, Ofile, Param = openFile(argv)
   txtTmp = []
   s = ""
   try:
      localtime = time.asctime( time.localtime(time.time()) )
      InputObj = open(Ifile,'r+')
      OutputObj = open(Ofile,'w+')
      #OutputObj.write('/*Generated by html2Ccode.py\n')
      s = '/*Generated by html2Ccode.py\n'
      #OutputObj.write('Made by PlayElek.com\n')
      s += 'Made by PlayElek.com\n'
      #OutputObj.write('Generated on \n')
      s += 'Generated on \n'
      #OutputObj.write(localtime + '\n')
      s += localtime + '\n'
      #OutputObj.write('Parameter is '+ Param +'\n')
      s += 'Parameter is '+ Param +'\n'
      #OutputObj.write('*/\n')
      s += '*/\n'
      #print s
      txtTmp.append(s)
      endline = 0
      txtsize = 0
      pgsize = 0
      try:
         #OutputObj.write("#ifndef " + Param +"_H\n")
         s = "#ifndef " + str(Param) +"_H\n"
         #OutputObj.write("#define " + Param +"_H\n")
         s += "#define " + str(Param) +"_H\n"
         s += "#include <string.h>\n"
         #OutputObj.write("#define pageCount "+pgsize+"\n")
         s += "#define pageCount "+str(pgsize)+"\n"
         searchDef = "#define pageCount \n"
         #OutputObj.write("int "+Param+"Size = 0;\n")
         s += "String "+str(Param)+"[pageCount];\n"
         #OutputObj.write("char "+Param+'[pageCount][] = "HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n\\'+'\n')
         s += "void htmlCode_Init(void){\n"
         s += str(Param)+'[0] = "HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n\\'+'\n'
         #OutputObj.write('"') 
         #print s
         
         txtTmp.append(s)
         s = ""
         for c in InputObj.read():
            if c == "'" or c == '"': 
               #OutputObj.write("\\"+c)
               s += "\\"+c
               endline = 0 
            elif c=='\n' or c=="\n":
               if endline == 0:
                  #OutputObj.write("\\n\\"+"\n")
                  s += "\\n\\"+"\n"
                  endline = 1
               elif endline == 1 :
                  #OutputObj.write("\";\n")
                  s += "\";\n"
                  #print s
                  txtTmp.append(s)
                  pgsize += 1
                  txtsize = 0
                  #OutputObj.write("char "+Param+'['+str(pgsize)+'][] = \"\\'+'\n')
                  s = str(Param)+'['+str(pgsize)+'] = \"\\'+'\n'
                  endline = 2
            else:
               #OutputObj.write(c)
               s += c
               endline = 0
            if txtsize < 1000:
               txtsize += 1
            else :
               #OutputObj.write("\";\n")
               s += "\";\n"
               #print s
               txtTmp.append(s)
               pgsize += 1
               txtsize = 0
               #OutputObj.write("char "+Param+'['+str(pgsize)+'[] = \"\\'+'\n')
               s = str(Param)+'['+str(pgsize)+'] = \"\\'+'\n'

         #OutputObj.write("\";\n")
         s += "\";\n}\n"
         #OutputObj.write("int "+Param+"Size = "+str(txtsize+1)+';\n')
         #OutputObj.write("#endif\n")
         s += "#endif\n"
         #print s
         txtTmp.append(s)
         i = 0
         s = str(txtTmp[1])
         i = s.index ("0")
         print "\nindex : " + str(i) + "in text : " +s+ '\n'
         s_before = s[:i]
         s_after = s[i+1:]

         s = s_before + str(pgsize+1) + s_after
         print "New text : " +s+'\n'
         txtTmp[1] = s

         for c in txtTmp:
            OutputObj.write(c)
            i += 1
            print " - " +str(c) + " Count - " + str(i)

         OutputObj.close()

      except Exception as e:
         print str(e)
         sys.exit(4)

   except IOError:
      print str(IOError)
      print "Cannot open file"



if __name__ == "__main__":
   main(sys.argv[1:])