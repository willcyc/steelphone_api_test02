#coding:utf-8
import requests
import pytest
'''品种定制列表'''
def test_get_subPageList():
	url = "http://mysteelapi.steelphone.com/v4/subBreedInfo/subPageList.htm?"
	result = requests.post(url,params = {"userId":""}).json()
	print(result)

	assert result['breeds'][0]['pageType'] == '2'
	assert result['breeds'][0]['name'] == '综合'

	assert result['breeds'][1]['pageType'] == '1'
	assert result['breeds'][1]['id'] == '01'
	assert result['breeds'][1]['icon'] == 'http://img04.mysteelcdn.com/wz/uploaded/steelphone4/subBreed/hsjs.png'
	assert result['breeds'][1]['name'] == '黑色金属'
	assert result['breeds'][1]['note'] == '建筑钢材、铁矿石、煤焦、废钢、不锈钢、热轧、冷轧、中厚板、型钢、钢管、优特钢、工业线材、铁合金等'

	assert result['breeds'][2]['pageType'] == '1'
	assert result['breeds'][2]['id'] == '02'
	assert result['breeds'][2]['icon'] == 'http://img04.mysteelcdn.com/wz/uploaded/steelphone4/subBreed/ysjs.png'
	assert result['breeds'][2]['name'] == '有色金属'
	assert result['breeds'][2]['note'] == '铜、铝、镍、稀土、铅锌'

	assert result['breeds'][3]['pageType'] == '1'
	assert result['breeds'][3]['id'] == '07'
	assert result['breeds'][3]['icon'] == 'http://img04.mysteelcdn.com/wz/uploaded/steelphone4/subBreed/ncp.png'
	assert result['breeds'][3]['name'] == '农产品'
	assert result['breeds'][3]['note'] == '油脂粕类、玉米类、小麦类、棉花类'

	assert result['breeds'][4]['pageType'] == '1'
	assert result['breeds'][4]['id'] == '08'
	assert result['breeds'][4]['icon'] == 'http://img04.mysteelcdn.com/wz/uploaded/steelphone4/subBreed/jzcl.png'
	assert result['breeds'][4]['name'] == '建筑材料'
	assert result['breeds'][4]['note'] == '水泥、混凝土'

	assert result['breeds'][5]['pageType'] == '3'
	assert result['breeds'][5]['id'] == '03'
	assert result['breeds'][5]['icon'] == 'http://img04.mysteelcdn.com/wz/uploaded/steelphone4/subBreed/nyhg.png'
	assert result['breeds'][5]['name'] == '能源化工'
	assert result['breeds'][5]['note'] == '能源、化工、塑料、橡胶、煤化工、化肥等'


if __name__ == '__main__':
	pytest.main(["-s", "dingzhi_subPageList.py"])
