#!/usr/bin/env python
# take two xml files as an input
# first file - xml with requirements, second file - protocol

import sys
import os

xml_reqs = sys.argv[1] #file 1
xml_prot = sys.argv[2] #file 2

if not os.path.isfile(xml_reqs):
    print("File path {} does not exist. Exiting...".format(xml_reqs))
    sys.exit()

if not os.path.isfile(xml_prot):
    print("File path {} does not exist. Exiting...".format(xml_prot))
    sys.exit()

freqs = open(xml_reqs, 'r')
fprot = open(xml_prot, 'r')

for line in fp:

freqs.close()
fprot.close()