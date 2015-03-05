#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='flyeagle', database='test', use_unicode=True)  # 我的root
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])   # database is user, table is user
# >cursor.rowcount
# >1
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', '1,')   # notice:'1'  is wrong !
values = cursor.fetchall()
#>values
#>[(u'1', u'Michael')]
# 关闭Cursor和Connection:
cursor.close()
#>True
conn.close()



############
## >>> help(cursor)
'''
 execute(self, operation, params=None, multi=False)
     Executes the given operation

     Executes the given operation substituting any markers with
     the given parameters.

     For example, getting all rows where id is 5:
       cursor.execute("SELECT * FROM t1 WHERE id = %s", (5,))

     The multi argument should be set to True when executing multiple
     statements in one operation. If not set and multiple results are
     found, an InterfaceError will be raised.

     If warnings where generated, and connection.get_warnings is True, then
     self._warnings will be a list containing these warnings.

     Returns an iterator when multi is True, otherwise None. '''