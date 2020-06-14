'''
    基础环境
'''
# 端口号
SERVER_PORT = 8889

SQLALCHEMY_ECHO = False

DEBUG = False

AUTH_COOKIE_NAME = "mooc_food"

##过滤url
IGNORE_URLS = [
    '^/user/login'
]

API_IGNORE_URLS = [
    '^/api'
]

IGNORE_CHECK_LOGIN_URLS = [
    '^/static',
    '^favicon.ico'
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

MINA_APP = {
    'appid':'wx3e738875d01d80aa',
    'appkey':'d2c5a56b5e524cd9d713d16ea5ccfeb5',
    'paykey':'',
    'mch_id':'',
    'callback_url':'/api/order/callback',    # 回调地址
}

UPLOAD = {
    'ext':['jpg','gif','bmp','jpeg','png'],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain': 'http://127.0.0.1:8889'
}
PAY_STATUS_DISPLAY_MAPPING = {
    '0': '订单关闭',
    '1': '支付成功',
    '-8': '待支付',
    '-7': '待发货',
    '-6': '待收货',
    '-5': '待评价'

}


PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}












