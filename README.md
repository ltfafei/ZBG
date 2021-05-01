# ZBG
    ZBG（zoomeye batch gather），即：zoomeye批量搜集脚本(工具)。该脚本由afei00123编写，基于python3编写。
    
### 小项目结构：
├── ZBG

│   ├── checkToken.py	   检查token是否存在，不存在则登录获取

│   ├── config.py	       配置zoomeye邮箱和密码

│   ├── getToken.py	       登录获取token

│   └── zoomeyeQuery.py	   zoomeye查询批量获取资产

### 使用
python zoomeyeQuery.py -h

************************************************************
          Version：zoomeye_Batch_get v1.0
        github：https://github.com/ltfafei
          CSDN: afei00123.blog.csdn.net
               公众号：网络运维渗透

************************************************************

usage: zoomeyeQuery.py [-h] -q  [-p] [-n] [-F] [-o]

Zoomeye batch gather tools

optional arguments:
  -h, --help     show this help message and exit
  
  -q , --query   Please input query argument. eg: shiro
  
  -p , --page    Please input start page. eg: 2
  
  -n , --num     Please input max page. eg: 2
  
  -F , --facet   Please input covariance item. eg: server
  
  -o , --file    Please input output file path. eg: output.txt
  
![image](https://github.com/ltfafei/ZBG/blob/master/used.png)
