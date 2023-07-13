import os
import sys
print ('@@@@ ',os.path.pardir)
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
import utils
print(utils.get_length("Hello"))
utils.eai('daaaale')