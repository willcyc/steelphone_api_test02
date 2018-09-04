#coding:utf-8
import pytest
import requests
from parameterized import parameterized
'''原生文章详情页：以报告页面原生文章详情页为例'''
Url = "https://mysteelapi.steelphone.com/v4/article/getContent.htm?"
i = 0
@parameterized.expand([
	#用例名称，参数：id、channelId
	("test_both_null",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','',''),   #文章id和频道channelId都为空
	("test_id_null",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','','0203'),  #文章id为空
	("test_id_error",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','564500','0203'),   #文章id正确，频道channelId不匹配
	("test_channelId_null",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','559313',''),   #频道channelId为空
	("test_channelId_error",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','559313','0604040401'),   #频道channelId正确、文章id不匹配
	("test_id_iserror",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','55','0604040401'),   #频道channelId正确、文章id错误
	("test_channelId_iserror",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','559313','0604401'),   #文章id正确、频道channelId错误
	("test_both_error",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','559','0604401'),    #频道channelId、文章id均错误
	("test_both_right",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','559313','0203')    #文章id和频道channelId匹配
	])
def test_case(_,userid,machinecode,id,channelid):
	body = {'userId':userid,'machineCode':machinecode,'id':id,'channelId':channelid}
	result = requests.post(Url,data = body).json()
	global i
	i += 1
	#print(result)
	if i == 1 or i == 2 or i == 4 or i == 6 or i == 7 or i == 8:
		assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员'
	elif i == 3:
		assert result['id'] != '559313'			#断言文章id不匹配正确的id
		assert result['channelId'] == '0203'		#断言频道id与传入参数相同
		assert result['title'] != 'Mysteel：3月钢坯或呈坚挺趋强运行之势'      #断言文章标题不匹配
	elif i == 5:
		assert result['id'] == '559313'			#断言文章id与传入参数相同
		assert result['channelId'] != '0203'	#断言频道id不匹配
		assert result['title'] == 'Mysteel：3月钢坯或呈坚挺趋强运行之势'
	else:
		assert result['id'] == '559313'            #断言文章id与传入参数相同
		assert result['channelId'] == '0203'		#断言频道id与传入参数相同
		assert result['title'] == 'Mysteel：3月钢坯或呈坚挺趋强运行之势'

"""
def test_both_null():
	'''文章id和频道channelId都为空'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'','channelId':''}).json()
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员' 

def test_id_null():
	'''文章id为空'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'','channelId':'0203'}).json()
	#print(result)
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员'

def test_id_error():
	'''文章id正确，频道channelId不匹配'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'564500','channelId':'0203'}).json()
	#print(result)
	assert result['id'] != '559313'			#断言文章id不匹配正确的id
	assert result['channelId'] == '0203'		#断言频道id与传入参数相同
	assert result['title'] != 'Mysteel：3月钢坯或呈坚挺趋强运行之势'      #断言文章标题不匹配

def test_channelId_null():
	'''频道channelId为空'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':''}).json()
	#print(result)
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员'

def test_channelId_error():
	'''频道channelId正确、文章id不匹配'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':'0604040401'}).json()
	#print(result)
	assert result['id'] == '559313'			#断言文章id与传入参数相同
	assert result['channelId'] != '0203'	#断言频道id不匹配
	assert result['title'] == 'Mysteel：3月钢坯或呈坚挺趋强运行之势'

def test_id_iserror():
	'''频道channelId正确、文章id错误'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'55','channelId':'0604040401'}).json()
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员' 

def test_channelId_iserror():
	'''文章id正确、频道channelId错误'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':'0604401'}).json()
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员'

def test_both_error():
	'''频道channelId、文章id均错误'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559','channelId':'0604401'}).json()
	assert result['errorstr'] == '客服紧急处理中，请等待或联系管理员'

def test_both_right():
	'''文章id和频道channelId匹配'''
	result = requests.post(Url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':'0203'}).json()
	assert result['id'] == '559313'            #断言文章id与传入参数相同
	assert result['channelId'] == '0203'		#断言频道id与传入参数相同
	assert result['title'] == 'Mysteel：3月钢坯或呈坚挺趋强运行之势'
"""
if __name__ == '__main__':
	pytest.main(["-s", "zixun_contentarticle_test.py"])