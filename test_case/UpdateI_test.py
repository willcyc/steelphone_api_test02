#coding:utf-8
import pytest
import requests
'''修改我的信息'''
Url = "https://mysteelapi.steelphone.com/v4/user/info/update.htm?"
def test_creat_success():
	payload = {'address':'南极','userId':'483098','machineCode':'','sex':'男','nickName':'小博','email':'zhangboqi@163.com','company':'上海钢联'}
	r = requests.post(Url,params = payload)
	code = r.status_code
	result = r.json()
	#print(code)
	#print(result)
	assert code == 200
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "UpdateI_test.py"])