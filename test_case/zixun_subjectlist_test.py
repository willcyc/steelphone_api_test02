#coding:utf-8
import pytest
import requests
'''资讯页面-专题列表'''
Url = "https://mysteelapi.steelphone.com/v4/article/subject/list.htm?"
def test_keyword_in_list():
	'''资讯页面专题列表-输入存在的搜索关键字'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','keywords':'油价'}).json()
	assert '油价' in result['subjects'][0]['title']

def test_keyword_notin_list():
	'''资讯页面专题列表-输入不存在的搜索关键字'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','keywords':'啦啦啦哈哈哈'}).json()
	assert result['subjects'] == []

def test_subject_list():
	'''资讯页面专题列表'''
	r = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','keywords':''})
	result = r.json()
	#print(result)
	code = r.status_code
	assert code == 200
	print(result['subjects'][0]['time'])   #最新更新的时间

if __name__ == '__main__':
	pytest.main(["-s", "zixun_subjectlist_test.py"])