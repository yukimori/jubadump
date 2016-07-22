#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import codecs
import os
import binascii
from pprint import pprint

print sys.argv
path=sys.argv[1]
file=os.path.basename(path)
decoded='decoded_'+file
print "{0} decoded file".format(decoded)

print "{0} file open.".format(path)
with open(path, mode='rb') as f:
    with open(decoded, mode='w') as wf:
#        wf = codecs.lookup('utf-8')[-1](wf)
        for line in f:
#            print line
#            print binascii.b2a_qp(line)
            print repr(line)
#            print line.decode('unicode_escape')
            #encode("utf-8")しなくてもprintで表示はできる
            #リダイレクトでファイルに書き込む際にはencode('urf-8')が必要
#            decoded_line = line.decode('unicode_escape').encode('utf-8')
#            print decoded_line.rstrip()
#            wf.write(decoded_line)
wf.close()
f.close()
