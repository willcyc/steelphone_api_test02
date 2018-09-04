#coding:utf-8
import pytest
import requests
from parameterized import parameterized

'''价格-选择城市页面'''
Url = "https://mysteelapi.steelphone.com/v4/market/city.htm?"
@parameterized.expand([
	#用例名称，参数：userId、machineCode
	("test_all_null",'','',''),    #参数均为空
	("test_userId_null",'','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','020301'), 
	("test_userId_error",'1545454151545','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','020301'),
	("test_machineCode_null",'566453','','020301'),
	("test_machineCode_error",'566453','4545000000000000006155','020301'),
	("test_breedId_null",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB',''),  #参数breedId为空
	("test_breedId_error",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','45656562212020100000000'),  #参数breedId不存在
	("test_all_error",'4454565123315468','47544','45656562212020100000000'),  #参数都不存在
	("test_all_right",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','01010302')  #参数均正确
])

def test_case(_,userid,machinecode,breedid):
	result = requests.post(Url,params = {'userId':userid,'machineCode':machinecode,'breedId':breedid}).json()
	#print(result)
	if result['result'] == 'false':
		assert result['errorstr'] == '传参异常！'
	elif result['result'] == 'true':
		if result['citys'] == []:
			assert result['citys'] == []
		elif len(result['cityLogs']) != 1 and  result['citys'] != []:
			assert len(result['citys'][0]['citys'])>0 
		elif len(result['cityLogs']) == 1:
			assert len(result['citys'][0]['citys'])>0   #断言选择城市页面城市列表不为空
			assert result['citys'][0]['citys'][0]['name'] == '上海'

if __name__ == '__main__':
	pytest.main(["-s", "Price_city_test.py"])