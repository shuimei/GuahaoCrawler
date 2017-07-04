# GuahaoCrawler
一个通用的单页网页数据抓取脚本

## 脚本结构
+ main.py 程序运行入口
+ PageTemplate.py 页面模板
+ rules.py 页面提取规则
+ hospitals/ 数据文件夹

## 使用说明
本例是在进行[微医（挂号网）](https://www.guahao.com/)抓取实践中总结而成的。
PageTemplate.py 使用一个类定义了目标网页的元数据，包括url结构，请求方式，需求字段，和解析方式
rules.py 使用xpath语法定义了目标网页需要抓取数据的节点信息
main.py 由用户自己编写数据读取方式

可以很方便地按照实际需求扩展PageTemplate.py中的元数据类和rules.py中的抓取规则实现抓取不同的网页数据。

