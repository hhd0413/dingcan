账户登录相关界面：

1.新建User

2.新建login,edit，reset-pwd方法

3.新建对应的视图层



账户管理相关界面：

1.新建Account

2.新建index,set,info方法

3.新建对应视图层



账号功能：

后台账户模块：

1.账户管理：账户列表，添加账户，编辑账户，删除账户，恢复账户

2.认证功能：登录退出，编辑信息，重置密码



用户表user

| name         | type                 | default             | comment          |
| ------------ | -------------------- | ------------------- | ---------------- |
| uid          | bigint(20)  unsigned | NULL                | 管理员id         |
| nickname     | varchar(100)         |                     | 用户名           |
| mobile       | varchar(20)          |                     | 手机号码         |
| email        | varchar(100)         |                     | 邮箱             |
| sex          | tinyint(1)           | 0                   | 性别 1男 2女     |
| avatar       | varchar(64)          |                     | 头像key          |
| login_name   | varchar(20)          |                     | 登录用户名       |
| login_pwd    | varchar(32)          |                     | 密码             |
| login_salt   | varchar(32)          |                     | 加密随机密钥     |
| status       | tinyint(4)           | 1                   | 1有效 0 无效     |
| updated_time | timestamp            | 0000-00-00 00:00:00 | 最后一次更新时间 |
| created_time | timestamp            | 0000-00-00 00:00:00 | 插入时间         |



![](/home/huhaidi/文档/订餐小程序/选区_001.png)



![](/home/huhaidi/文档/订餐小程序/选区_003.png)

![选区_004](/home/huhaidi/文档/订餐小程序/选区_004.png)

![](/home/huhaidi/文档/订餐小程序/选区_005.png)

![](/home/huhaidi/文档/订餐小程序/选区_006.png)



![](/home/huhaidi/文档/订餐小程序/选区_009.png)



![](/home/huhaidi/图片/选区_010.png)



![](/home/huhaidi/文档/订餐小程序/选区_011.png)

![](/home/huhaidi/文档/订餐小程序/选区_012.png)



微信支付流程：

**https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=7_4&index=3**

1:下单

2.调取支付框框

3.支付成功之后，微信回调我们，我们进行回调处理，将订单变为已支付的这样一个过程

向支付接口提交xml数据（注意数字签名），返回结果集，其中prepayid（用于发送微信消息模板），返回前台所需要的信息（签名），将数据返回前端进行渲染，  前端发起微信支付，然后进行微信支付回调的处理，如：将订单状态置为成功，快递状态置为已付款待发货，更新销售历史表，更新支付回调结果数据表内容，





商户系统和微信支付系统主要交互：

1、小程序内调用登录接口，获取到用户的openid,api参见公共api【[小程序登录API](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html)】

2、商户server调用支付统一下单，api参见公共api【[统一下单API](https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=9_1&index=1)】

3、商户server调用再次签名，api参见公共api【[再次签名](https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=7_7&index=3)】

4、商户server接收支付通知，api参见公共api【[支付结果通知API](https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=9_7)】

5、商户server查询支付结果，api参见公共api【[查询订单API](https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=9_2)】

![](/home/huhaidi/图片/选区_023.png)



模板消息：

### 步骤一：获取模板 ID

在微信公众平台手动配置获取模板 ID（[https://mp.weixin.qq.com](https://mp.weixin.qq.com/) ）

### 步骤二：获取下发权限

详见小程序端消息订阅接口 [wx.requestSubscribeMessage](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/subscribe-message/wx.requestSubscribeMessage.html)

### 步骤三：调用接口下发订阅消息

详见服务端消息发送接口 [subscribeMessage.send](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/subscribe-message/subscribeMessage.send.html)



微信支付四大金刚：

​    1.下单过程

2. 拉起支付过程
3. 支付异步回调过程
4. 通过异步job的方式给用户发送消息推送



确认收货：修改快递状态为1

取消订单： 归还库存







ssh hi137@139.9.246.116

Nfg8e1pe





