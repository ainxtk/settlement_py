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
# import math
# from random import randint
# def _randmon_acct(n):
#     range_start = 10**(n-1)
#     range_end = (10**n) -1
#     return randint(range_start,range_end)
# def _randomize(min,max,type,valid_list):
#     if type in ('acct_num','txn_status','datetime','ref_num','txn_type','txn_reason','amount'):
#         pass
#     else:
#         raise Exception('not a valid type for random function')
#     if type == 'num':
#         return _randmon_acct(max)
#
# if __name__ == '__main__':
#     print(_randmon_acct(16))

import time
from random import randint
import random
from datetime import datetime


class SampleTransactionGenerator:
    '''This call will generate a dummy transaction recrod within a certain interval
         which will be consumed by SQS/WebHook listener'''

    def __init__(self, interval=1):
        self.interval = interval

    def generateaccountid(self, n_digit=16):
        '''This method will take digit as input and will generate a number
            input n_digit number
                        output number of n_digit'''
        try:
            range_start = 10 ** (n_digit - 1)
            range_end = (10 ** n_digit) - 1
            print(f"[INFO:generateaccountid() generated account_no]")

            return {'status': True,
                    'accountid': randint(range_start, range_end)
                    }

        except Exception as e:
            print(f"[ERROR:generateaccountid() failed to generate account_no]")
            return {'status': False,
                    'err_msg': str(e)
                    }

    def GenerateAmount(self, amountstart, amountend):
        '''this method will take amount range as input and will generate random no
            input amountstart ex 20.5
            input amountend ex 20000.5
                        output randomfloat 3456.3'''
        try:
            secure_random = random.SystemRandom()
            randomfloat = secure_random.uniform(amountstart, amountend)
            print(f"[INFO:GenerateAmount() generated randomfloat]")
            return {'status': True,
                    'randomfloat': randomfloat
                    }

        except Exception as e:
            print(f"[ERROR:GenerateAmount() failed to randomfloat]")
            return {'status': False,
                    'err_msg': str(e)
                    }

    def GenerateDateTime(self):
        '''this method will generate current timestamp'''
        try:
            now = datetime.now()
            now.strftime("%d/%m/%Y %H:%M:%S")
            print(f"[INFO:GenerateDateTime() generated randomfloat]")
            return {'status': True,
                    'timenow': now.strftime("%d/%m/%Y %H:%M:%S")
                    }
        except Exception as e:
            print(f"[ERROR:GenerateDateTime() failed to timenow]")
            return {'status': False,
                    'err_msg': str(e)
                    }


if __name__ == '__main__':
    sampletrans1 = SampleTransactionGenerator(2)
    print(sampletrans1.__doc__)
    while (1):
        sampletrans = SampleTransactionGenerator()
        result = sampletrans.generateaccountid()
        if result:
            fromacc = result['accountid']

        result = sampletrans.generateaccountid()
        if result:
            toacc = result['accountid']

        result = sampletrans.GenerateAmount(10, 20000.5)
        if result:
            amount = result['randomfloat']

        result = sampletrans.generateaccountid(10)
        if result:
            ref_no = result['accountid']

        result = sampletrans.GenerateDateTime()
        if result:
            datetimes = result['timenow']

        time.sleep(5)
        print(f"{fromacc},{toacc},{amount},{ref_no},{datetimes}")



