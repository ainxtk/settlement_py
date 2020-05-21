from flask import Blueprint, make_response
from flask_restplus import Api, Resource
from json import dumps, load
from flask import json, jsonify,request
import os
from app.webhook_receiver.services import webhook_reciever_service as wrs
from app.preprocessing.services import preprocessing_service as prs

blueprint = Blueprint('webhook_receiver_controller',__name__,url_prefix='/receiver')
webhook_receiver_controller = Api(blueprint)

@webhook_receiver_controller.route('/post_update', methods=['POST'])
##Get input data frame in JSON
class WebhookReceiver(Resource):
	def post(self):
		print("here now")
		response = {
			'status' : 'faliure',
			'err_msg' : ''
			} 
		if not request.is_json:
			response['err_msg'] = 'Input json format not valid'
			return jsonify(response,400)
		content = request.get_json()
		print(dir(wrs))
		dt = wrs.webhookservice(content)
		print('here now---')
		if dt['status']:
			response['Web_result'] = dt['data']
			response['status'] = 'success'
			pt=prs.Preprocessing(content)
			if pt['status']:
				response['prs_status'] = 'success'
			else:
				response['prs_status'] = 'failed'
			temp=json.dumps(response,default=str)
			response=json.loads(temp)
			return jsonify(response)
		else:
			response['err_msg'] = dt['err_msg']
			return jsonify(response,400)

@webhook_receiver_controller.errorhandler
def default_error_handler(error):
	return {'message':'Err Occured'}, getattr(error,'code',500)
