#coding:utf-8
import pytest
import requests

'''版本信息，蒙层广告，底部模块信息协议整合'''
Url = "http://mysteelapi.steelphone.com/v4/versionBottomIcoAdv.htm?&isPad="
def test_page_null():
	'''页码为空'''
	body = {'userId':'503879','machineCode':'90526B160362A7A4FECA22411080F8CF','versionCode':'93','type':'4','protocolVersion':'4.7.5','marketType':'hicloud',
	'machineCode':'90526B160362A7A4FECA22411080F8CF','id':'','clientVersion':'4.7.6','clientType':'0'}
	r = requests.post(Url,data = body)
	code = r.status_code
	assert code == 200
	result = r.json()
	assert result['curVerUrl'] == 'download/4.7.6/app-hicloud-release.apk'
	assert result['module'][0]['name'] == '首页'
	assert result['module'][1]['name'] == '报告'
	assert result['module'][2]['name'] == '产经日历'
	assert result['module'][3]['name'] == '会议'
	assert result['module'][4]['name'] == '我的'
	assert result['updateInfo'] == '1、终于等到第三方微信登录咯~\n2、首页向下滑，悬赏问答，答题赢红包\n3、钢坯从[钢铁]移到[原料]\n4、安卓端支持查看PDF文件'

if __name__ == '__main__':
	pytest.main(["-s", "Home_version_test.py"])
