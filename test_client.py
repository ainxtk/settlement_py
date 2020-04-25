#this is the test client for incoming transactions for settlement
# Incoming transaction message layout :
#
# From_account
# To_account
# Transaction_status
# Transaction_datetime
# Transaction_ref_num
# Transaction_type
# Transaction_reason
# settlement_amount
import math
from random import randint
def _randmon_acct(n):
    range_start = 10**(n-1)
    range_end = (10**n) -1
    return randint(range_start,range_end)
def _randomize(min,max,type,valid_list):
    if type in ('acct_num','txn_status','datetime','ref_num','txn_type','txn_reason','amount'):
        pass
    else:
        raise Exception('not a valid type for random function')
    if type == 'num':
        return _randmon_acct(max)

if __name__ == '__main__':
    print(_randmon_acct(16))




