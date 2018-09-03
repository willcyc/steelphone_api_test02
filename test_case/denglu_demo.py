#coding:utf-8
import pytest
import requests

class TestDengLu():
	'''登录'''
	@pytest.fixture()
	def url(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/user/login.htm?"

		yield
		print("==========")


	def test_both_null(self,url):
		'''用户名、密码为空'''
		body = {
				'cellphone':'',
				'password':'',
				'token':'1507bfd3f797e28773a',
				'ostype':'1',
				'machineInfo':'HUAWEI,PIC-AL00,26',
				'softVersion':'4.7.3'
		}
		
		r = requests.post(self.base_url,data = body)
		result = r.json()
		#print(result)
		assert result['result'] == 'false'
		assert result['errorstr'] == '传参异常！'


	def test_cellphone_null(self,url):
		'''用户名为空'''
		body = {
				'cellphone':'',
				'password':'e10adc3949ba59abbe56e057f20f883e',
				'token':'1507bfd3f797e28773a',
				'ostype':'1',
				'machineInfo':'HUAWEI,PIC-AL00,26',
				'softVersion':'4.7.3'
		}

		r = requests.post(self.base_url,data = body)
		result = r.json()
		#print(self.result)
		assert result['result'] == 'false'
		assert result['errorstr'] == '传参异常！'

	
	def test_password_null(self,url):
		'''密码为空'''
		body = {
				'cellphone':'13839205941',
				'password':'',
				'token':'1507bfd3f797e28773a',
				'ostype':'1',
				'machineInfo':'HUAWEI,PIC-AL00,26',
				'softVersion':'4.7.3'
		}

		r = requests.post(self.base_url,data = body)
		result = r.json()
		#print(self.result)
		assert result['result'] == 'false'
		assert result['errorstr'] == '传参异常！'

	
	def test_both_error(self,url):
		'''用户名、密码错误'''
		name_pwd = {'sioasdhk':'7694f4a66316e53c8cdd9d9954bd611d',  #密码：'q'
					'4512':'202cb962ac59075b964b07152d234b70',       #密码：'123'
					'^&!%^@$%^':'f2631c59312c33b8338a866e75b93eb4',  #密码：'^&*%$^!$'
					'啦啦啦':'2a8f10ddd89053b514162abb4e9d10f8',		#密码：'我的密码你猜呀'
					'hhd256担   惊受恐￥%￥@%':'70114e7cd5e52e992a0e6e6aa2d4ab8e'  #密码：'hhd256担   惊受恐￥%￥@%'
		}
		for cellphone,password in name_pwd.items():
			#print(cellphone)
			body = {
				'cellphone':cellphone,
				'password':password,
				'token':'1507bfd3f797e28773a',
				'ostype':'1',
				'machineInfo':'HUAWEI,PIC-AL00,26',
				'softVersion':'4.7.3'
			}
			r = requests.post(self.base_url,data = body)
			result = r.json()
			#print(result)
			assert result['result'] == 'false'
			assert result['errorstr'] == '用户不存在'

	def test_cellphone_error(self,url):
		'''用户名错误'''
		username = ['138392059411','123','00000000000','qwertyuiope','~!@#$%^&*()','手机版接口测试数据测试','138Jh*&啦啦 l#']
		for cellphone in username:
			#print(cellphone)
			body = {
				'cellphone':cellphone,
				'password':'96e79218965eb72c92a549dd5a330112',
				'token':'1507bfd3f797e28773a',
				'ostype':'1',
				'machineInfo':'HUAWEI,PIC-AL00,26',
				'softVersion':'4.7.3'
			}
			r = requests.post(self.base_url,data = body)
			result = r.json()
			#print(result)
			assert result['result'] == 'false'
			assert result['errorstr'] == '用户不存在'
	
	def test_password_error(self,url):
		'''密码错误'''
		password = ['c4ca4238a0b923820dcc509a6f75849b','b3ddbc502e307665f346cbd6e52cc10d','21b95a0f90138767b0fd324e6be3457b','abeac07d3c28c1bef9e730002c753ed4','dea53b816e4909fa993a2e460315607b',
		'fbb1b3d8ca94bac2fb046742c957b61c','9eb01db007ac03248049e91e0281963b','27961c9959e1a23aa197c139ed4256ad']  
					#1、12312、789789、1234567890123456、qwertyuiope、~!@#$%^&*()、手机版接口测试数据测试、138Jh*&啦啦 l#
		for pwd in password:
			body = {
				'cellphone':'13839205941',
				'password':pwd,
				'token':'1507bfd3f797e28773a',
				'ostype':'1',
				'machineInfo':'HUAWEI,PIC-AL00,26',
				'softVersion':'4.7.3'
			}
			r = requests.post(self.base_url,data = body)
			result = r.json()
			#print(self.result)
			assert result['result'] == 'false'
			assert result['errorstr'] == '密码不匹配！'
	
	def test_denglu_success(self,url):
		'''登录成功'''
		body = {
				'cellphone':'13839205941',
				'password':'e10adc3949ba59abbe56e057f20f883e',
				'token':'1507bfd3f797e28773a',
				'ostype':'1',
				'machineInfo':'HUAWEI,PIC-AL00,26',
				'softVersion':'4.7.3'
			}
		r = requests.post(self.base_url,data = body)
		result = r.json()
		#print(result)
		if result['result'] == 'true':
			assert result['nickName'] == '程一川测试'
			assert result['userId'] == '566453'
			assert result['adminName'] == '岳宗平'
			assert result['adminPhone'] == '15898950165'
		else:
			assert result['errorstr'] == '该账户已在其他设备上登录，请联系管理员！'

	def test_logout(self):
		'''请求退出登录接口'''
		r = requests.post("https://mysteelapi.steelphone.com/v4/user/logout.htm?userId=566453&machineCode=&isPad=")
		code = r.status_code
		assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "denglu_demo_test.py"])