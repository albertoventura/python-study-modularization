import os
import sys

#fpath = os.path.join(os.path.dirname(__file__), 'utils')
#sys.path.append(fpath)

#print(sys.path)

#import length
#import upper
#import lower

#txt = "Hello"
#res_len = length.get_length(txt)
#print("The length of the string is: ",res_len)
#res_up = upper.to_upper(txt)
#print("Uppercase txt: ", res_up)
#res_low = lower.to_lower(txt)
#print("Uppercase txt: ", res_low)

import utils
txt = "Hello"
res_len = utils.get_length(txt)
print(res_len)
res_up = utils.to_upper(txt)
print(res_up)
res_low = utils.to_lower(txt)
print(res_low)