#coding:utf-8
import pytest
import requests

'''短信-短信订制页面'''
Url = "https://mysteelapi.steelphone.com/v4/sms/search.htm?"
def test_page_null():
	'''页码为空'''
	body = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','page':'','keywords':''}
	r = requests.post(Url,data = body)
	code = r.status_code
	assert code == 400

def test_get_success():
	'''查询成功'''
	body = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','page':1,'keywords':''}
	result = requests.post(Url,data = body).json()
	#print(result)
	assert result['pagenum'] == '75'

if __name__ == '__main__':
	pytest.main(["-s", "duanxin_mysearch_test.py"])