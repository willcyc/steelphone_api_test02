#coding:utf-8
import pytest
import requests
'''资讯页面标签'''
Url = "https://mysteelapi.steelphone.com/v4/channel/zixun.htm?"
def test_channel_title():
	'''资讯页面标题'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','protocolVersion':'4.5.0'}).json()
	#print(result)
	assert result['channels'][0]['name'] == '热点'
	assert result['channels'][1]['name'] == '快讯'
	assert result['channels'][2]['name'] == '专题'
	assert result['channels'][3]['name'] == '微谈'
	assert result['channels'][4]['name'] == '国际'

if __name__ == '__main__':
	pytest.main(["-s", "zixun_channel_test.py"])