#coding:utf-8
import pytest
import requests
import datetime

'''首页底部菜单、及更新提示语'''
Url = "https://mysteelapi.steelphone.com/v4/versionBottomIcoAdv.htm?"

def test_versionBottom_success():

	result = requests.post(Url,
	params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'','type':'4','clientVersion':'4.7.0','clientType':'0',
	'marketType':'hicloud','protocolVersion':'4.6.5'}).json()
	tb = result['module']

	'''底部菜单-首页'''
	assert tb[0]['name'] == '首页'
	assert tb[0]['url'] == ''
	assert tb[0]['icoNor'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/index_nor.png'  #未选中时状态
	assert tb[0]['icoChoose'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/index_choose.png'   #选中时状态

	'''底部菜单-报告'''
	assert tb[1]['name'] == '报告'
	assert tb[1]['url'] == ''
	assert tb[1]['icoNor'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/report_nor.png'   #未选中时状态
	assert tb[1]['icoChoose'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/report_choose.png'   #选中时状态

	
	'''底部菜单-产经日历'''
	r = datetime.datetime.now().day  #获取当前时间日
	#print(r)
	icoNor = 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/calendar/' + str(r) + '_nor.png'
	icoChoose = 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/calendar/' + str(r) + '_choose.png' 
	assert tb[2]['name'] == '产经日历'
	assert tb[2]['url'] == 'https://m.steelphone.com/finance/calendar.html?UAlocal=1'
	assert tb[2]['icoNor'] == icoNor    #未选中时状态
	assert tb[2]['icoChoose'] == icoChoose   #选中时状态

	'''底部菜单-会议'''
	assert tb[3]['name'] == '会议'
	assert tb[3]['url'] == 'http://m.mysteel.com/huizhan/index.htm'
	assert tb[3]['icoNor'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/meeting_nor.png'  #未选中时状态
	assert tb[3]['icoChoose'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/meeting_choose.png'   #选中时状态

	'''底部菜单-我的'''
	assert tb[4]['name'] == '我的'
	assert tb[4]['url'] == ''
	assert tb[4]['icoNor'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/my_nor.png'  #未选中时状态
	assert tb[4]['icoChoose'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/my_choose.png'   #选中时状态

if __name__ == '__main__':
	pytest.main(["-s", "Home_dibuBottom_test.py"])