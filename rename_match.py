# Script for automatically rename BinDiff matches
# Youtube demo: https://www.youtube.com/watch?v=QO9eZjfM2pE

import idc

# Insert copied string between six '
# For example '''abc'''

copy = ''''''.split("\n")

for i in copy:
	a = i.split("\t")
	idc.set_name(int(a[3], 16), a[6])
