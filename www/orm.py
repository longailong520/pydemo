
#连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务：
@asyncio.coroutine
def create_pool(loop,**kw):
	global __pool
	__pool = yield from aiomysql.create_pool(
		host=kw.get('host', 'localhost'),
		port=kw.get('port', 3306),
		user=kw['user'],
		password= kw['password'],
		db=kw['db'],
		charset=kw.get('charset', 'utf8'),
		autocommit=kw.get('autocommit', True),
		maxsize=kw.get('maxsize',10),
		maxsize=kw.get('maxsize',1)
		loop=loop

	)