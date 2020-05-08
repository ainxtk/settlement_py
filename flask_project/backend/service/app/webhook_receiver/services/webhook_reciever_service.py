def webhookservice(content):
	try:
		print(content)
		return {'status':True,'data':'sample output'}
	except exception as e:
		return {'status':False,'err_msg':str(e)}
