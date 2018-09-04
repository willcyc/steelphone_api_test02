#coding:utf-8
import pytest
import requests
'''资讯页面文章列表'''
Url = "https://mysteelapi.steelphone.com/v4/article/list.htm?"
def test_articlelist_success():
	'''资讯页面'''
	list = ['0501','0101','03','0502','02']  #资讯页面：热点、快讯、微谈、国际列表，报告页面
	for al in list:
		r = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','channelId':str(al)})
		code = r.status_code
		assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "zixun_articlelist_test.py"])