import time
from random import randint
import random
from datetime import datetime
import requests,json

class SampleTransactionGenerator:
	'''This call will generate a dummy transaction recrod within a certain interval
         which will be consumed by SQS/WebHook listener'''
	
	def __init__(self,interval=1):
		self.interval=interval
	
	def generateaccountid(self,n_digit=16):
		'''This method will take digit as input and will generate a number
			input n_digit number 
                        output number of n_digit'''
		try:
			range_start = 10**(n_digit-1)
			range_end = (10**n_digit)-1
			print(f"[INFO:generateaccountid() generated account_no]")
			
			return {'status':True,
				'accountid':randint(range_start, range_end)
				}

		except Exception as e:
			print(f"[ERROR:generateaccountid() failed to generate account_no]")
			return {'status':False,
				'err_msg':str(e)
				}

	def GenerateAmount(self,amountstart,amountend):
		'''this method will take amount range as input and will generate random no
			input amountstart ex 20.5 
			input amountend ex 20000.5 
                        output randomfloat 3456.3'''
		try:
			secure_random = random.SystemRandom()
			randomfloat = secure_random.uniform(amountstart,amountend)
			print(f"[INFO:GenerateAmount() generated randomfloat]")
			return {'status':True,
				'randomfloat':randomfloat
				}

		except Exception as e:
			print(f"[ERROR:GenerateAmount() failed to randomfloat]")
			return {'status':False,
				'err_msg':str(e)
				}

	def GenerateDateTime(self):
		'''this method will generate current timestamp'''
		try:
			now=datetime.now()
			now.strftime("%d/%m/%Y %H:%M:%S")
			print(f"[INFO:GenerateDateTime() generated randomfloat]")
			return {'status':True,
				'timenow':now.strftime("%d/%m/%Y %H:%M:%S")
				}
		except Exception as e:
			print(f"[ERROR:GenerateDateTime() failed to timenow]")
			return {'status':False,
				'err_msg':str(e)
				}

	def ProcessWebHook(self,msg):
		headers = {'content-type' : 'application/json'}
		data ={'record':msg}
		url = 'http://0.0.0.0:5000/receiver/post_update'
		res=requests.post(url,data=json.dumps(data),headers=headers)
		print(res)

if __name__ == '__main__':
	while(1):
		sampletrans=SampleTransactionGenerator()
		result=sampletrans.generateaccountid()
		if result:
			fromacc=result['accountid']
		result=sampletrans.generateaccountid()
	
		if result:
			toacc=result['accountid']
		result=sampletrans.GenerateAmount(20.5,20000.5)
	
		if result:
			amount=result['randomfloat']

		result=sampletrans.generateaccountid(10)
	
		if result:
			ref_no=result['accountid']
	
		result=sampletrans.GenerateDateTime()
		if result:
			datetimes=result['timenow']

		time.sleep(5)
		sampletrans.ProcessWebHook(f"{fromacc},{toacc},{amount},{ref_no},{datetimes}")
		print(f"{fromacc},{toacc},{amount},{ref_no},{datetimes}")
		
