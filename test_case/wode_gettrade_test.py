#coding:utf-8
import pytest
import requests
'''根据订单编号查询订单信息'''
Url = "https://mysteelapi.steelphone.com/v4/finance/pay/queryOrderByOutTradeNO.htm?"

def test_creat_success():
	payload = {'outTradeNO':'138392059411522132610322'}
	r = requests.post(Url,params = payload)
	code = r.status_code
	result = r.json()
	# print(result)
	# print(result['result'])
	assert code == 200
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "wode_gettrade_test.py"])