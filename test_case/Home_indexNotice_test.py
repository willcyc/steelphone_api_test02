#coding:utf-8
import pytest
import requests

'''首页我的、短信是否打点'''
Url = "https://mysteelapi.steelphone.com/v4/indexNotice.htm?"

def test_indexNotice_success():
	''''''
	result = requests.post(Url,params = {'userId':'129647','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'}).json()   #李平平

	'''首页短信红点'''
	if result['smsNoticeCount'] == '':
		assert result['smsNotice'] == '0' 	#没有红点
		print("没有红点")
	else:
		assert result['smsNotice'] == '1'	#有红点
		print("有红点")
		
	'''首页“我的”红点'''
	for x in range(1,5):
		a = 0
		url = 'https://mysteelapi.steelphone.com/v4/comment/reply/replyToMe.htm?&userId=129647&machineCode=2ACCCCDC5FBDBE59ADD70F1C100FE4BB&page=' + str(x)
		resultms = requests.post(url).json()   #李平平
		print(resultms)
		a += int(resultms['smsNotice'])
	if a == 0:
		assert resultms['myNotice'] == '0'
		print("没有红点")
	else:
		assert resultms['myNotice'] == '1'
		print("有红点")
			
if __name__ == '__main__':
	pytest.main(["-s", "Home_indexNotice_test.py"])