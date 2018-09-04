#coding:utf-8
import pytest
import requests
from random import choice
'''获取收件地址列表、设置默认地址、删除列表中地址'''
Url = "https://mysteelapi.steelphone.com/v4/finance/address/list.htm?"

def test_creat_success():
	#=============获取收件地址列表=============
	payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'}
	r = requests.post(Url,params = payload)
	code = r.status_code
	result = r.json()
	assert code == 200
	assert result['result'] == 'true'
	
	#=============获取收件地址id=============
	list = []
	for i in result['addresses']:
		#print(i)
		list.append(i['id'])
	#print(list)
	
	#=============设置默认收件地址=============
	id01 = choice(list)   #获取随机地址
	#print(id01)
	payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':id01}  #id从列表中获取
	r = requests.post("https://mysteelapi.steelphone.com/v4/finance/address/setDefault.htm?",params = payload)
	code = r.status_code
	result = r.json()
	#print(code)
	#print(result)

	assert code == 200
	assert result['result'] == 'true'
	
	#=============删除收件地址列表中随机地址=============
	'''
	for id in list:
		#print(id)   #删除所有地址
	'''
	id02 = choice(list) 
	#print(id02)
	payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':id02}   #id从list列表中获取
	r = requests.post('https://mysteelapi.steelphone.com/v4/finance/address/delete.htm?',params = payload)
	code = r.status_code
	result = r.json()
	#print(code)
	#print(result)

	assert code == 200
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "wode_Shanlist_test.py"])