import unittest
from app import app
import json

class BasicTestCase(unittest.TestCase):

	def test_home(self):
		with app.test_client() as client:
		    # send data as POST form to endpoint
		    sent = {'data':'sample record'}
		    result = client.post('/receiver/post_update',data=json.dumps(sent),content_type='application/json')
                    
		# check result from server with expected data
		self.assertEqual(result.status_code,200)

		data = json.loads(result.get_data(as_text=True))
		print(f"here is {data} {json.dumps(sent)}")
               
		self.assertEqual(data['Web_result'],'sample output')

if __name__ == '__main__':
    unittest.main()
