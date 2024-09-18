# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='账号' )
    xingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='姓名' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    lianxidianhua=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='联系电话' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )

class gongxiangdanche(Base_model):
    __doc__ = u'''gongxiangdanche'''
    __tablename__ = 'gongxiangdanche'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='标题' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    bianqian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='便签' )
    zuozhe=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='作者' )
    liulanliang=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='浏览量' )
    zhaiyao=db.Column( db.Text,  nullable=True, unique=False,comment='摘要' )
    fanduishu=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='反对数' )
    dianzanshu=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='点赞数' )
    detail=db.Column( db.Text,  nullable=True, unique=False,comment='详情' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class chat(Base_model):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    adminid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='管理员id' )
    ask=db.Column( db.Text,  nullable=True, unique=False,comment='提问' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复' )
    isreply=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='是否回复' )

class forum(Base_model):
    __doc__ = u'''forum'''
    __tablename__ = 'forum'



    __authTables__={}
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='帖子标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='帖子内容' )
    parentid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='父节点id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    username=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    isdone=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='状态' )
    istop=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='是否置顶' )
    toptime=db.Column( db.DateTime,  nullable=True, unique=False,comment='置顶时间' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class systemintro(Base_model):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class discussgongxiangdanche(Base_model):
    __doc__ = u'''discussgongxiangdanche'''
    __tablename__ = 'discussgongxiangdanche'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    score=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='评分' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

