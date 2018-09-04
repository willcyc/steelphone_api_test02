#coding:utf-8
import pytest
import requests
'''注册-第三步'''
Url = "https://mysteelapi.steelphone.com/v4/user/register.htm?"
def test_get_success():
	'''参数均正确'''
	body = {'userId':'','machineCode':'90526B160362A7A4FECA22411080F8CF','name':'测试','validateCode':'0018','password':'123456','cellphone':'18790000004'}
	result = requests.post(Url,data = body).json()																			
	#print(result)
	#print(len(result))
	if len(result) == 1:
		assert result['result'] == 'true'
	else:
		assert result['errorstr'] == '注册请求失效！'

if __name__ == '__main__':
	pytest.main(["-s", "zhuce_third_test.py"])