#coding:utf-8
import pytest
import requests
'''期货-上期所'''
Url = "https://mysteelapi.steelphone.com/v4/futures/sqs.htm?"
def test_get_success():
	'''参数id、type均正确'''
	body = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915'}
	r = requests.post(Url,data = body)
	code = r.status_code
	assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "qihuo_sqs_test.py"])