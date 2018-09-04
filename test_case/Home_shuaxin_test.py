import pytest
import requests
import time
import datetime
import re

'''首页上拉刷新'''
Url = "https://mysteelapi.steelphone.com/v4/getHotArticleToFourPO.htm?"
def test_HotArticle_art_null():
	'''首页文章页码参数为空'''
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'','protocolVersion':'4.6.5'}
	r = requests.post(Url,data = body)
	code = r.status_code
	assert code == 400

def test_HotArticle_art_error():
	'''首页文章页码参数传入错误，大于100'''
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'101','protocolVersion':'4.6.5'}
	result = requests.post(Url,data = body).json()
	assert len(result) == 1  

def test_HotArticle_first_success():
	'''首页文章第1页：榜单-好文推荐、文章排序和条数'''
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'1','protocolVersion':'4.6.5'}
	result = requests.post(Url,data = body).json()
	resultbd = requests.post('https://mysteelapi.steelphone.com/v4/article/queryBillBoard.htm?&userId=566453&page=1&size=15&isPad=').json()   #榜单-好文推荐
	#resultbd = rbd.json()
	#print(resultbd)
	
	#===============断言榜单-好文推荐==============
	bdlist = []      #首页榜单列表
	bddlist = []     #榜单页列表

	#获取首页榜单文章id
	for art in result['articles']:     
		if len(art['articlePicArray']) != 0:
			bd = art['articlePicArray']
			#print(bd)
			for bdid in bd:
				#print(len(bdid))
				bdlist.append(bdid['id'])
			#print(bdlist)

	#获取榜单详细页文章id
	for artbd in resultbd['articles']:   
		bddlist.append(artbd['id'])
	#print(bddlist)

	for l in range (5):
		bo = int(bdlist[l]) - int(bddlist[l])   
		#print(bo)
		assert bo == 0   #断言首页榜单文章为榜单详细页前五篇文章

	#====================断言非置顶文章降序排序和条数===================
	tm = []
	zd = 0
	r = time.strftime('%Y%m%d',time.localtime(time.time()))  #获取当前时间年、月、日
	y = time.strftime('%Y',time.localtime(time.time()))   #获取当前时间年
	#print(s)

	for art in result['articles']:
		#print(art['date2'])
		#print(art)
		i = re.findall(r"\d+\.?\d*",art['date2'])   #提取字符串中的数据
		j = (('').join(i))  #将列表转换为字符串
		#print(j)
		
		#若只显示时、分则时间格式转换为年月日时分
		if art['isTop'] == 'false':
			if len(j) == 4: 
				j = r + j     
				#print(j)
			elif len(j) == 8:
				j = y + j
			tm.append(j)
		#置顶文章数量
		elif art['isTop'] == 'true':
			zd = zd + 1  
	#print(tm)
	for k in range (len(tm)-1):
		bo = int(tm[k])-int(tm[k+1]) 
		assert bo>=0   #断言降序排序
		
	#assert zd+len(tm) == 15   #断言每页15条数据

if __name__ == '__main__':
	pytest.main(["-s", "Home_shuaxin_test.py"])