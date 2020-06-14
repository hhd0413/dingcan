'''
    每次发版都有个版本号： 201805011400 201805021500
'''

from flask import Flask, url_for
from imooc import route_imooc
from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint( route_imooc, url_prefix = '/imooc' )

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/mysql'
db = SQLAlchemy(app)

@app.route('/')
def hello():
    url = url_for('index')

    url_1 = UrlManager.buildUrl('/api')

    url_2 = UrlManager.buildStaticUrl('/css/bootstrap.css')

    msg = 'hello world, url:%s,url1:%s,url2:%s'%(url,url_1,url_2)

    app.logger.error( msg )
    app.logger.info( msg )

    return msg

@app.route('/api')
def index():
    return 'index page'

# 错误页面处理
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/api/hello')
def hello_():
    from sqlalchemy import text
    sql = text('select * from user')
    result = db.engine.execute(sql)
    for row in result:
        app.logger.info(row)
    return 'hello world'

if __name__ == '__main__':
    app.run( debug=True )