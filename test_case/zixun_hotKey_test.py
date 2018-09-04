#coding:utf-8
import pytest
import requests
'''首页文章热门搜索'''
Url = "https://mysteelapi.steelphone.com/v4/article/hotKey.htm?"
def test_hotkey_list():
	'''首页文章热门搜索词'''
	result = requests.post(Url,params = {'userId':'','machineCode':''}).json()
	hotkey = result['hotTitle']
	#print(hotkey)
	hot = ['废钢','钢坯','唐山','钢铁','沙钢','唐山钢市快报','铁矿石','煤焦','库存']
	for i in range(len(hotkey)):
		assert hotkey[i]['title'] in hot

if __name__ == '__main__':
	pytest.main(["-s", "zixun_hotKey_test.py"])