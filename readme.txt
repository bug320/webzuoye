# 猜数字游戏
----
## 结构:
### 后台
1. 数据库模块 ---- DBM
 1.1 用户信息 ---- UserInfo
    获取用户信息 --- getUserInfo() --- 不超过10 位数
        用户id   ---- User.id    
        用户名   ---- User.name
        用户密码 ---- User.passwd
        最好成绩 ---- User.best
        全球排名 ---- User.reportId
    修改用户信息 --- chageUserInfo()
        插入用户 ---- Insert()
        更新用户 ---- Update()
        删除用户 ---- Delete()
 1.2 系统信息 --- SysInfo
    游戏难度  --- GameLevel
        回合数 --- GameLevel.loopSize  --- 不超过2位数
        猜测数长度 ---GameLevel.lengthSize  --- 不超过2位数

2. 游戏模块 --- GPM
 2.1 设置函数
    2.1.1 生成随机数 ---- getAim()
 2.2 交互函数 
    2.2.1 获取用户输入 ---- User.Input()
    2.2.2 提交         ---- User.Post()
    2.2.3 重置         ---- User.Reset()
    2.2.4 撤销         ---- User.Back()
 2.3 后台处理
    2.3.1 保存游戏信息到数据库 --- GPM.SaveGameSnap()
### 前端
3. 网站版面:
 1.母版：layout.htm
    页面分为 5 个部分，左右导航条，上下信息栏，中间主控区
 2. 登录和注册界面：signin.html sigout.html
 3. 游戏页面 play.html
 4. 设置页面 setting.html
 5. 排行页面 report.html

