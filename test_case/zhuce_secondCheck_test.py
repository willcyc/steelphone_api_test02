#coding:utf-8
import pytest
import requests
'''注册-核对验证码'''
Url = "https://mysteelapi.steelphone.com/v4/user/validateCode/check.htm?"
def test_get_success():
	'''参数均正确'''
	body = {'userId':'','machineCode':'90526B160362A7A4FECA22411080F8CF','validateCode':'0018','cellphone':'18790000004'}
	result = requests.post(Url,data = body).json()											
	#print(result)
	#print(len(result))
	if len(result) == 1:
		assert result['result'] == 'true'
	else:
		assert result['errorstr'] == '验证码失效！'

if __name__ == '__main__':
	pytest.main(["-s", "zhuce_secondCheck_test.py"])