#coding:utf-8
import requests
import pytest

class TestYuanLiao():
	'''原料饼图'''

	def test_Volume_success(self):
		'''获取饼图'''
		self.base_url = "https://mysteelapi.steelphone.com/v4/breed/query/sonBreed.htm?"
		body = {
				'userId':'566453',
				'machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB',
				'breedId':'09',
				'protocolVersion':'4.6.6'
		}
		r = requests.post(self.base_url,data = body)
		self.result = r.json()
		#print(self.result)
		s = self.result['breeds']
		#print(s)

		'''废钢'''
		assert s[0]['name'] == '废钢'
		assert s[0]['hot'] == '1'
		assert s[0]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0306.png'

		'''煤焦'''
		assert s[1]['name'] == '煤焦'
		assert s[1]['hot'] == '0'
		assert s[1]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/05.png'

		'''耐材'''
		assert s[2]['name'] == '耐材'
		assert s[2]['hot'] == '0'
		assert s[2]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0309.png'

		'''生铁'''
		assert s[3]['name'] == '生铁'
		assert s[3]['hot'] == '0'
		assert s[3]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0305.png'

		'''铁合金'''
		assert s[4]['name'] == '铁合金'
		assert s[4]['hot'] == '0'
		assert s[4]['ico'] == 'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0303.png'

		'''铁矿石'''
		assert s[5]['name'] == '铁矿石'
		assert s[5]['hot'] == '1'
		assert s[5]['ico'] =='http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0311.png'

if __name__ == '__main__':
	pytest.main(["-s", "bingtu_yuanliao_test.py"])
	#pytest.main()