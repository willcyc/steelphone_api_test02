#coding:utf-8
import pytest
import requests

'''微信登录'''
Url = "https://mysteelapi.steelphone.com/v4/wxInfo/login.htm?&isPad="
def test_get_success():
	body = {'unionId':'oMkjMvnmIa77i5PnGCeYEdEw9AKc','machineCode':'90526B160362A7A4FECA22411080F8CF','token':'1507bfd3f797e28773a','machineInfo':'HUAWEI,PIC-AL00,26','ostype':'1','softVersion':'4.7.6'}
	r = requests.post(Url,data=body)
	#print(r)
	code = r.status_code
	assert code == 200
	result = r.json()
	#print(result)

	if result['result'] == 'true' and len(result) > 1:
		assert result['unionId'] == 'oMkjMvnmIa77i5PnGCeYEdEw9AKc'
	elif result['result'] == 'false' and result['errorcode'] == '90010006':
		assert result['errorstr'] == '该账户已在其他设备上登录，请联系管理员！'
	else:
		print("请设备HUAWEI,PIC-AL00,26微信先绑定手机版账号！")

if __name__ == '__main__':
	pytest.main(["-s", "weixin_login_test.py"])