#coding:utf-8
import pymysql.cursors
import json
class OperationMysql:
	def __init__(self):
		self.conn = pymysql.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='123',
			db='test',
			charset='utf8',
			#可以用于获取字段字典类型的
			cursorclass=pymysql.cursors.DictCursor
			)
        #使用cursor()方法创建一个游标对象cursor
		self.cur = self.conn.cursor()

	#查询一条数据 execute()  方法执行 SQL 查询
    #使用 fetchone() 方法获取单条数据.
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		result = json.dumps(result)
		return result

if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("select * from sort1 where sid=5")
	print(res)