#coding:utf-8
import pytest
import requests
'''资讯页面子标签'''
Url = "https://mysteelapi.steelphone.com/v4/channel/getSon.htm?"
def test_channel_son_title():
	'''资讯页面子标题'''
	list = ['01','0502']
	for al in list:
		result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','channelId':str(al)}).json()
		#print(result)
		if al == '01':
			assert result['channels'][0]['name'] == '宏观'
			assert result['channels'][1]['name'] == '行情'
			assert result['channels'][2]['name'] == '库存'
			assert result['channels'][3]['name'] == '钢厂'
		else:
			assert result['channels'][0]['name'] == '全部'
			assert result['channels'][1]['name'] == '热点评述'
			assert result['channels'][2]['name'] == '反倾销'
			assert result['channels'][3]['name'] == '市场汇总'
			assert result['channels'][4]['name'] == '出口报价'
			assert result['channels'][5]['name'] == '国际新闻'

if __name__ == '__main__':
	pytest.main(["-s", "zixun_channelson_test.py"])