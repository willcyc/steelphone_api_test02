#coding:utf-8
import pytest
import requests
'''获取默认收件地址'''
Url = "https://mysteelapi.steelphone.com/v4/finance/address/getDefault.htm?"

def test_creat_success():
	payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'} 
	r = requests.post(Url,params = payload)
	code = r.status_code
	result = r.json()
	assert code == 200
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "wode_getdefault_test.py"])