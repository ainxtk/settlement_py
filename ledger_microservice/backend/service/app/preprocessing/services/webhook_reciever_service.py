from app import Transaction_Record,session
import json
def Preprocessing(content):
	try:
		TransRecord={}
		print(f"---{content}")
		TransRecord['fromacc']="DDD"
		return {'status':True,'data':'sample output'}
	except exception as e:
		return {'status':False,'err_msg':str(e)}
