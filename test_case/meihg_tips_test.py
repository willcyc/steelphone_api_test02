#coding:utf-8
import pytest
import requests

Url = "http://mysteelapi.steelphone.com/v4/getMhgTips.htm?isPad="
def test_get_success():
	'''煤化工提示语'''
	r = requests.post(Url)
	#print(r)
	code = r.status_code
	assert code == 200
	result = r.json()
	#print(result)
	assert result['info'] == '为了给您提供更专业的煤化工服务，本版块信息已停更，更多资讯关注“隆众石化通APP”获取'
	assert result['phone'] == '0533-2591688'

if __name__ == '__main__':
	pytest.main(["-s", "meihg_tips_test.py"])