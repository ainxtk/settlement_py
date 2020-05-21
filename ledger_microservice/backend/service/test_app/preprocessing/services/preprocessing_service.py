from app import ledger,session
import json
def Preprocessing(content):
	try:
		TransRecord={}
		data=[]
		print(f"---{content}")
		TransRecord['from_acc']=content['record'].split(',')[0]
		TransRecord['to_acc']=content['record'].split(',')[1]
		TransRecord['amount']=content['record'].split(',')[2]
		TransRecord['transaction_id']=content['record'].split(',')[3]
		TransRecord['transaction_datetime']=content['record'].split(',')[4]
		print(TransRecord)
		data.append(TransRecord)
		session.bulk_insert_mappings(Transaction_Record,data)
		session.commit()
		print("insertion successfull")
		return {'status':True,'data':TransRecord}
	except Exception as e:
		print(str(e))
		return {'status':False,'err_msg':str(e)}




