#coding:utf-8
import pytest
import requests
import re

'''短信-我的短信页面'''		
Url = "https://mysteelapi.steelphone.com/v4/sms/myNewSmsContent.htm?"

def test_page_null():
	'''传入页码为空'''
	body = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','page':'','breedId':''}
	r = requests.post(Url,data = body)
	code = r.status_code
	assert code == 400

def test_get_success01():
	'''查询成功，断言短信列表按时间降序排序、且为短信-我的定制页面中定制的短信'''
	body = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','page':'1','breedId':''}
	result = requests.post(Url,data = body).json()
	#print(result)
	
	#====================获取短信-我的短信页面第一页短信标题==================
	zuixin = []
	for duanxin in result['sms']:
		#print(duanxin['name'])
		zuixin.append(duanxin['name'])
	#print(zuixin)

	#====================读取短信-我的定制页面中定制的短信====================
	f = open('C:/Users/Administrator/Desktop/桌面文件/steelphone_api_test_v2.0/test_case/html.txt')
	jieguo = f.read()
	#print(jieguo)

	#====================断言短信-我的短信中收到的信息，为短信-我的定制页面定制的短信================
	for i in range(len(zuixin)):
		assert zuixin[i] in jieguo
		#print(i)

if __name__ == '__main__':
	pytest.main(["-s", "duanxin_myNewSms_test.py"])