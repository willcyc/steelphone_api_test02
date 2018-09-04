#coding:utf-8
import pytest
import requests
'''注册-获取验证码'''
Url = "https://mysteelapi.steelphone.com/v4/user/validateCode/get.htm?"

def test_get_success():
	'''参数均正确'''
	body = {'userId':'','machineCode':'90526B160362A7A4FECA22411080F8CF','validateCodeKey':'SGOBggiFjjcVb3ltmk-yOXy8z-O08Z-duaOfRjIImBWsT7l5tp4xE3ys16mDBMIG','protocolVersion':'4.3.0'}
	result = requests.post(Url,data = body).json()																		
	#print(result)
	#print(len(result))
	if len(result) == 1:
		assert result['result'] == 'true'
	else:
		assert result['errorstr'] == '短信发送频繁'

if __name__ == '__main__':
	pytest.main(["-s", "zhuce_second_test.py"])