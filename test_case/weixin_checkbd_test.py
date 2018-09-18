#coding:utf-8
import pytest
import requests

Url = "http://mysteelapi.steelphone.com/v4/wxInfo/checkUnionId.htm?&isPad="
def test_get_success():
	'''检查微信号是否已绑定过手机用户'''
	body = {'unionId':'oMkjMvnmIa77i5PnGCeYEdEw9AKc','machineCode':'90526B160362A7A4FECA22411080F8CF'}
	r = requests.post(Url,data=body)
	#print(r)
	code = r.status_code
	assert code == 200
	result = r.json()
	#print(result)
	if result['isConnect'] == 'no':
		assert result['number'] == ''
		print("该手机微信号未绑定手机版账号")
	else:
		assert result['number'] != ''
		print("该手机微信号已绑定手机版账号")

if __name__ == '__main__':
	pytest.main(["-s", "weixin_checkbd_test.py"])