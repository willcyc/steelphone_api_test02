#coding:utf-8
import pytest
import requests
from parameterized import parameterized

'''价格-选择品种页面'''
Url = "https://mysteelapi.steelphone.com/v4/market/breed.htm?"

@parameterized.expand([
	#用例名称，参数：userId、machineCode，实际结果，预期结果
	("both_null",'','','breeds',9),
	("userId_null",'','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breeds',9),
	("machineCode_null",'566453','','breeds',9),
	("machineCode__error",'566453','4546165132','breeds',9),
	("both_right",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breeds',9)
])

def test_case(_,type,id,a,c):
	result = requests.post(Url,params = {'userId':type,'machineCode':id}).json()
	#print(result)
	#assert result[a] == c
	assert len(result[a]) == c

def test_userId_error():
	'''参数userId不存在'''
	result = requests.post(Url,params = {'userId':'784541564864897489468465','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'}).json()
	#print(result)
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员' 

def test_all_error():
	'''参数userId、machineCode不存在'''
	result = requests.post(Url,params = {'userId':'784541564864897489468465','machineCode':'4546165132'}).json()
	#print(result)
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员' 
	
if __name__ == '__main__':
	pytest.main(["-s", "Price_breed_test.py"])