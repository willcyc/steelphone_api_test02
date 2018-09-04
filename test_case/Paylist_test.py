#coding:utf-8
import pytest
import requests

'''获取缴费记录'''
Url = "https://mysteelapi.steelphone.com/v4/finance/payInpour/list.htm?"

def test_creat_success():
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'','size':''} 
	r = requests.post(Url,data = body)
	code = r.status_code
	result = r.json()

	assert code == 200
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "Paylist_test.py"])