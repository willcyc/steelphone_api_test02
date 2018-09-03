#coding:utf-8
import pytest
import requests

'''首页饼图及所有两侧指数'''
Url = "https://mysteelapi.steelphone.com/v4/getVolumeXpicIndexNotice.htm?"

def test_Volume_success():
	'''获取首页饼图及指数'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','protocolVersion':'4.6.5'}).json()
	#print(result)
	a = result['module']
	b = result['subBreeds']
	c = result['datas']
	d = result['xpic']
	#print(a,b,c,d)
	
	'''首页第一排饼图'''
	assert a[0]['name'] == '价格'
	assert a[1]['name'] == '资讯'
	assert a[2]['name'] == '短信'
	assert a[3]['name'] == '期货'
	assert a[4]['name'] == '供求'
	assert a[0]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/price.png'
	assert a[1]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/zixun.png'
	assert a[2]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/sms_free.png'
	assert a[3]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/qihuo.png'
	assert a[4]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/gq.png'

	'''首页第二排饼图'''
	assert b[0]['name'] == '钢铁'
	assert b[1]['name'] == '原料'
	assert b[2]['name'] == '有色'
	assert b[3]['name'] == '农产品'
	assert b[4]['name'] == '更多'
	assert b[0]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/01.png'
	assert b[1]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/09.png'
	assert b[2]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/02.png'
	assert b[3]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/04.png'
	assert b[4]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/10.png'

	'''首页中部右侧-钢银指数'''
	assert c[0]['title'] == '钢银·今日成交量'
	assert c[1]['title'] == '钢银·城市周库存量'
	#assert c[2]['title'] == '钢银·实时成交价'
	assert c[0]['url'] == 'https://zhushou.banksteel.com/a/#/data/msapp'
	assert c[1]['url'] == 'https://zhushou.banksteel.com/a/#/data/msapp/kucun'
	#assert c[2]['url'] == 'https://zhushou.banksteel.com/a/#/data/msapp/jiage'

	'''首页中部左侧-价格指数'''
	assert d[0]['name'] == '钢材综合指数'
	assert d[2]['name'] == '焦炭指数'
	assert d[1]['name'] == '62%进口矿指数'
	assert d[0]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=gczh_abs&UAlocal=1&zs=1#hqzs'
	assert d[2]['url'] == 'https://m.steelphone.com/app/map/index.html?Source=app&zsoption=shuju_jiaotan#hqzs'
	assert d[1]['url'] == 'https://m.steelphone.com/app/map/index.html?UAlocal=1&zs=1#hqzs'

if __name__ == '__main__':
	pytest.main(["-s", "Home_bingtu_test.py"])