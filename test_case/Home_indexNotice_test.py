#coding:utf-8
import pytest
import requests

'''首页我的、短信是否打点'''
Url = "https://mysteelapi.steelphone.com/v4/indexNotice.htm?"

def test_indexNotice_success():
	''''''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF'}).json()   #李平平

	'''首页短信红点'''
	if result['smsNoticeCount'] == '':
		assert result['smsNotice'] == '0' 	#没有红点
		print("没有红点")
	else:
		assert result['smsNotice'] == '1'	#有红点
		print("有红点")
		
	'''首页“我的”红点'''
	if result['myNotice'] == '0':
		print("没有红点")
	else:
		print("有红点")
		
if __name__ == '__main__':
	pytest.main(["-s", "Home_indexNotice_test.py"])