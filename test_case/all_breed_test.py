#coding:utf-8
import requests
import pytest
'''获取所有ios/android品种信息'''
def test_get_ios():	
	url = "https://mysteelapi.steelphone.com/v4/finance/ios/breed/all.htm?"
	body = {'cellphone':'17715161441','machineCode':'B05B8726-29CB-4E14-BC88-AC17AB038A0D','ostype':'2','protocolVersion':'4.6.4','userId':'733321'}
	result = requests.post(url,data = body)
	code = result.status_code
	assert code == 200

def test_get_android():	
	url = "https://mysteelapi.steelphone.com/v4/finance/breed/all.htm?&isPad="
	body = {'userId':'503879','machineCode':'90526B160362A7A4FECA22411080F8CF','protocolVersion':'4.6.4'}
	result = requests.post(url,data = body)
	#print(result)
	code = result.status_code
	assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "all_breed_test.py"])