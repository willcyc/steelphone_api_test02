#coding:utf-8
import pytest
import requests

'''微信解绑、绑定'''
url02 = "https://mysteelapi.steelphone.com/v4/wxInfo/toConnect.htm?&isPad="
def test_bangding_success():
	body = {'number':'13839205941','password':'e10adc3949ba59abbe56e057f20f883e','machineCode':'90526B160362A7A4FECA22411080F8CF','unionId':'oMkjMvnmIa77i5PnGCeYEdEw9AKc','openId':'oMkjMvnmIa77i5PnGCeYEdEw9AKc'}
	r = requests.post(url02,data=body)
	#print(r)
	code = r.status_code
	assert code == 200
	result = r.json()
	#print(result)
	if result['result'] == 'false' and 'errorcode' == '10160021':
		assert result['errorstr'] == '该号码已绑定了微信号'
	elif result['result'] == 'true':
		assert result['result'] == 'true'
	else:
		print("请查看传参是否正确")

url01 = "https://mysteelapi.steelphone.com/v4/wxInfo/cancelConnect.htm?&isPad="
def test_jiebang_success():
	'''微信解绑'''
	body = {'number':'13839205941','machineCode':'90526B160362A7A4FECA22411080F8CF','unionId':'oMkjMvnmIa77i5PnGCeYEdEw9AKc','userId':'566453'}
	r = requests.post(url01,data=body)
	#print(r)
	code = r.status_code
	assert code == 200
	result = r.json()
	#print(result)
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "weixin_jiebbd_test.py"])