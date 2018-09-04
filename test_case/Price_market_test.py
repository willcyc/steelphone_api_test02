#coding:utf-8
import pytest
import requests
from parameterized import parameterized

'''价格页面'''
Url = "https://mysteelapi.steelphone.com/v4/market/getMarket.htm?"
i = 0
@parameterized.expand([
	#用例名称，参数：breedName、tableId、cityName、cityId、userId、deepBreedId、machineCode、type、isSub、breedId、marketId
	("test_breedName_null",'','','安阳','01030110','566453','','','price','0','01020101',''),   #breedName为空
	("test_breedName_error",'啦啦啦','','安阳','01030110','566453','','','price','0','01020101',''),   #无相关breedName
	("test_breedId_null",'碳结圆钢','','安阳','01030110','566453','','','price','0','',''),    #breedId为空
	("test_breedId_error",'碳结圆钢','','安阳','01030110','566453','','','price','0','123456789',''),    #无相关breedId
	("test_cityId_null",'碳结圆钢','','安阳','','566453','','','price','0','01020101',''),   #cityId为空
	("test_cityId_error",'碳结圆钢','','安阳','8454512312156456451231321231535556','566453','','','price','0','01020101',''),    #无相关cityId
	("test_cityName_null",'碳结圆钢','','','01030110','566453','','','price','0','01020101',''),    #cityName为空
	("test_cityName_error",'碳结圆钢','','啦啦啦','01030110','566453','','','price','0','01020101',''), #无相关cityName
	("test_market_success",'碳结圆钢','','安阳','01030110','566453','','','price','0','01020101','')   #参数全部正确
	])

def test_case(_,breedName,tableId,cityName,cityId,userId,deepBreedId,machineCode,type,isSub,breedId,marketId):
	body = {'breedName':breedName,'tableId':tableId,'cityName':cityName,'cityId':cityId,'userId':userId,'deepBreedId':deepBreedId,'machineCode':machineCode,
	'type':type,'isSub':isSub,'breedId':breedId,'marketId':marketId}
	result = requests.post(Url,data = body).json()
	global i
	i += 1
	#print(result)
	if i == 1 or i == 2 or i == 4:
		assert result['toastMsg'] == '对不起，没有相应行情表单，可切换其他品种或城市'
	elif i == 3:
		assert result['breedId'] == '010101'
	elif i == 5:
		assert result['cityName'] == '上海'
	elif i == 6 or i == 7 or i == 8:
		assert result['cityName'] == '安阳'
		assert result['cityId'] == '01030110'
	else:
		assert result['breedName'] == '碳结圆钢'    #断言查询的品种名称和选择的品种名称一致   
		assert result['cityName'] == '安阳'         #断言查询的城市名称和选择的城市名称一致  
		assert result['cityName'] in result['tableName']    #断言城市名称字段包含于当前行情表单名称中
		assert result['breedName'] in result['tableName']    #断言品种名称字段包含于当前行情表单名称中
		assert result['breedId'] == '01020101'      #断言查询的品种id与传入的品种id一致
		assert result['cityId'] == '01030110'		 #断言查询的城市id与传入的城市id一致
		if result['toastMsg'] == '':
			assert result['toastMsg'] == ''             #toastMsg为空表示当前行情不为空，否则“对不起，没有相应行情表单，可切换其他品种或城市”
		else:
			assert result['toastMsg'] == '今日行情尚未发布，您可以查看其他行情'

		if result['markets'][0]['price'] == '****':
			assert result['hasRight'] == 'no'       #断言是否有权限
			print("没有权限")
		else:
			assert result['hasRight'] == 'yes'
			print("有权限")

if __name__ == '__main__':
	pytest.main(["-s", "Price_market_test.py"])