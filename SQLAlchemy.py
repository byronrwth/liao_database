#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入:
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()



# 初始化数据库连接:
# MySQL
#engine = create_engine('mysql+mysqlconnector://root:flyeagle@localhost:3306/testAlchemy_MySQL')
# SQLite
#engine = create_engine('sqlite:///C:\\sqlitedbs\\school.db', echo=True)
#engine = create_engine('sqlite:////C:/Users/chengxi/Dropbox/python/liao/database/testAlchemy_slqite.db', echo=True)
DATABASE = 'sqlite:////Users/chengxi/Dropbox/python/liao/database/testAlchemy_slqite.db'
engine = create_engine(DATABASE, convert_unicode=True)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

    
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
print "new_user.id:", new_user.id
print "new_user.name:", new_user.name

session.commit()

print "new_user.id:", new_user.id
print "new_user.name:", new_user.name

'''
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
'''

# 提交即保存到数据库:
#session.commit()

# 关闭session:
session.close()