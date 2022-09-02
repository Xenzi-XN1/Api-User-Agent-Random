from flask import Flask,request
from flask_cors import CORS
from flask_restful import Resource,Api
from fake_useragent import UserAgent

app=Flask(__name__)
CORS(app)
api=Api(app)

class User_agent(Resource):
	def get(self):
		user_agent = UserAgent()
		get_user_agent = user_agent.random
		return ({
			'status': 'success',
			'user_agent_random': get_user_agent,
			'developer': 'Xenzi Ganz',
			'github_admin': 'https://github.com/Xenzi-XN1'
		})
api.add_resource(User_agent,"/api/user-agent-random")

if __name__=="__main__":
	app.run(debug=True)
