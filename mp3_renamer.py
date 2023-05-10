import os
import sys
import glob
import prettyprinter
import argparse

'''
MP3 Renamer
Assume you ripped a book on tape CD to a directory and the
files aren't in a file name convention you need.. like the file
name looks like Bob_Smith_Where_The_Roses_Bloom_D1_T2.mp3
which is just too long for your display.
This quick script will iterate through the files and rename
them to part{nn}.mp3 which will show up on the screen.

--type   File extension, default is .mp3
--token  What the beginning of the file looks like so the track
         can be parsed.  ex. "Bob_Smith_Where_The_Roses_Bloom_D1_T"
--endmode if selected, says the number is at the end
--test   doesn't actually rename 

Example A:
   track name: "Bob_Smith_Where_The_Roses_Bloom_D1_T2.mp3"
   The track number is at the end, so we want
      --endmode --token "_D1_"

Example B:
    track name: "12 - Red Ferns Grow Wildly.mp3"
    The track number is at the beginning, so we want
       --token " - "
'''

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--endmode",   help="run in endmode", action="store_true")
parser.add_argument("-t", "--token",    help="token", default=None)
parser.add_argument("-x", "--test", help="Test mode", action="store_true")
parser.add_argument("-o", "--type",    help="file ext", default=".mp3")
args = parser.parse_args()

FILES = glob.glob("./*.%s" % args.type)
if args.test:
    prettyprinter.pprint(FILES)

for F in FILES:
    if (args.endmode):
        N = F.find(args.token)
        if N < 0:
            continue
        N += len(args.token)
        WKS = F[N:].strip()
        N = WKS.find(".")
        VALS = WKS[0:N]
        VAL = int(VALS)
        NEWF = "part%02d.%s" % (VAL, args.type)
        print ("rename %s to %s" % (F, NEWF))
        if args.test == False:
            os.rename(F, NEWF)
    else:
        WKS = F[2:]
        if args.token != None:
            N = WKS.find(args.token)
            WKS = WKS[0:N]
        NEWF = "part%s.mp3" % WKS
        print ("rename %s to %s" % (F, NEWF))
        if args.test == False:
            os.rename(F, NEWF)
