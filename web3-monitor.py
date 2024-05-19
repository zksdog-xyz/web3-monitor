import requests
import json
import time

while True:
	# rapidapi接口
	url = "https://twitter154.p.rapidapi.com/user/details"

	#查询参数
	querystring = {"username":"zksdog"}

	# 查询参数
	headers = {
		"X-RapidAPI-Key": "e3f6269a6cmsh5eab2c23275a942p1e99c2jsn4d07525dd1b7",
		"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	# 拿到接口返回的数据
	print(response.json())

	name = response.json()["name"]
	location = response.json()["location"]
	description = response.json()["description"]

	# 将接口返回的数据拼接
	message = {
					"msg_type": "text",
					"content": {
						"text": f"昵称: {name}\n位置: {location}\n简介: {description}\n"
					}
				}

	# 将我们想要的数据推送到飞书频道
	webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/68a50578-32c4-439e-a37f-0ff58a87be19'
	requests.post(webhook_url, headers={"Content-Type": "application/json"}, data=json.dumps(message))
	time.sleep(1)