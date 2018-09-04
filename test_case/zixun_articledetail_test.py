#coding:utf-8
import pytest
import requests
'''资讯页面原生文章详情页底部信息'''
Url = "https://mysteelapi.steelphone.com/v4/article/detail.htm?"
def test_both_null():
	'''参数id、type为空'''
	payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'','type':''}
	r = requests.post(Url,params = payload)
	code = r.status_code
	#print(code)	
	assert code == 400

def test_id_null():
	'''参数id为空'''
	body = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'','type':'1'}
	result = requests.post(Url,data = body).json()
	assert result['errorstr'] == '参数不能为空'

def test_type_null():
	'''参数type为空'''
	body = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'638280','type':''}
	r = requests.post(Url,data = body)
	code = r.status_code	
	assert code == 400

def test_id_error():
	'''参数id错误'''
	body = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'6382886','type':'1'}
	result = requests.post(Url,data = body).json()
	if result['result'] == 'true':
		assert result['channelName'] == ''
	else:
		assert result['errorstr'] == '文章不存在'

def test_type_error():
	'''参数type错误'''
	payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'638280','type':'225'}
	result = requests.post(Url,params = payload).json()
	assert result['channelName'] == ''

def test_both_error():
	'''参数id、type均错误'''
	payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'63828230','type':'225'}
	result = requests.post(Url,params = payload).json()
	assert result['channelName'] == ''


def test_articledetail_success():
	'''参数id、type均正确'''
	payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'638280','type':'1'}
	result = requests.post(Url,params = payload).json()
	#print(result)
	assert result['id'] == '638280'
	assert result['channelName'] == '五元报告'
	assert result['channelId'] == '0203'

if __name__ == '__main__':
	pytest.main(["-s", "zixun_articledetail_test.py"])