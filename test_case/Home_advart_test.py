#coding:utf-8
import pytest
import requests
import time,re


'''首页：顶部广告、文章、榜单'''
Url = "https://mysteelapi.steelphone.com/v4/getAdvArrayArticle.htm?"

def test_get_adv_success():
	'''顶部广告获取成功'''
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,1','page':'1','type':'5,17,6','protocolVersion':'4.6.5'}
	result = requests.post(Url,data = body).json()
	#print(result)
	#print(result['advArray'][0]['adv'])
	advs = result['advArray'][0]['adv']
	#print(advs)
	
	'''固定广告位置'''
	for adv in advs:
		#print(adv)
		if adv['id'] == '3448':
			adv0 = adv
			#print(adv0)
		elif adv['id'] == '3460':
			adv1 = adv
			#print(adv1)
		else:
			adv2 = adv
			#print(adv2)
	
	#顶部广告1
	assert adv0['id'] == '3448'    #广告id
	assert adv0['title'] == '天津友发钢管集团股份有限公司'   #广告标题
	assert adv0['description'] == '5'   #广告位置
	assert adv0['src'] == 'http://www.yfgg.com/?hmsr=mystealSY&hmmd=&hmpl=&hmkw=&hmci='   #广告跳转地址
	assert adv0['type'] == '1'   #广告的频道id
	assert adv0['url'] == 'http://mfs.mysteelcdn.com/group1/M00/06/F4/rBL63lrxE6WAZr6JAABun6BtIBw900.jpg'   #广告图片路径

	#顶部广告2
	assert adv1['id'] == '3460'    #广告id
	assert adv1['title'] == '河南鹏达金属制品有限公司'  #广告标题
	assert adv1['description'] == '5'   #广告位置
	assert adv1['src'] == ''   #广告跳转地址
	assert adv1['type'] == '1'  #广告的频道id
	assert adv1['url'] == 'http://mfs.mysteelcdn.com/group1/M00/05/AC/rBL63lqmZIiARpQaAACM3Lmobzc324.jpg'    #广告图片路径

	#顶部广告3
	assert adv2['id'] == '3521'     #广告id
	assert adv2['title'] == '晋城福盛钢铁有限公司'   #广告标题
	assert adv2['description'] == '5'   #广告位置
	assert adv2['src'] == 'http://www.steelphone.com/jingang.html'   #广告跳转地址
	assert adv2['type'] == '1'   #广告的频道id
	assert adv2['url'] == 'http://mfs.mysteelcdn.com/group1/M00/06/F4/rBL63lrxEuyATLOwAACAiJXFgRc261.jpg'  #广告图片路径

def test_get_art_null():
	'''首页文章页码参数为空'''
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'','type':'5,17,6','protocolVersion':'4.6.5'}
	r = requests.post(Url,data = body)
	code = r.status_code
	#print(self.result)
	assert code == 400

def test_get_art_error():
	'''首页文章页码参数传入错误，大于100'''
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'101','type':'5,17,6','protocolVersion':'4.6.5'}
	result = requests.post(Url,data = body).json()
	#print(len(result))
	assert len(result) == 1    


def test_get_artfirst_success():
	'''首页文章第1页：榜单-好文推荐、文章排序和条数'''
	body = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'1','type':'5,17,6','protocolVersion':'4.6.5'}
	result = requests.post(Url,data = body).json()  #首页文章
	resultbd = requests.post('http://mysteelapi.steelphone.com/v4/article/queryBillBoard.htm?&userId=566453&page=1&size=15&isPad=').json()   #榜单-好文推荐
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

	#====================断言非置顶文章降序排序===================
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
		assert bo>=0    #断言降序排序
		
	#assert == zd+len(tm) == 15   #断言每页15条数据
	
if __name__ == '__main__':
	pytest.main(["-s", "Home_advart_test.py"])