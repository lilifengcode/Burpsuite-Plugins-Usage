## ![2019-03-26_163135.png](https://image.3001.net/images/20190326/1553589224_5c99e3e87cad9.png!small)

很久之前的，，，我懒得管了复制过来了

## 一.burp suite插件之xss Validator

### 1.安装xss Validator

安装xss Validator 最简单的方法就是通过burp---Extender模块---BApp Store菜单，找到xss Validator 插件单击”installing"进行安装

![1.png](https://image.3001.net/images/20190325/1553501604_5c988da400a89.png!small)

### 2.安装Phantom.js和xss-detector

### <span style="color: rgb(85, 85, 85);">xss Validator还需要Phantom.js和xss-detector脚本的配合使用来检测XSS漏洞</span>

phantom.js  下载地址：[http://phantomjs.org/download.html](http://phantomjs.org/download.html)

xss-detector 下载地址：[https://github.com/PortSwigger/xss-validator](https://github.com/PortSwigger/xss-validator)

![2019-03-25_163337.png](https://image.3001.net/images/20190325/1553504738_5c9899e25faf0.png!small)**配置phantom.js环境变量**

将解压好的phantomjs，位置路径复制---添加到PATH系统变量里 【<span style="color: rgb(239, 71, 71);">win 7前面加;</span>】

![2019-03-25_192709.png](https://image.3001.net/images/20190325/1553513951_5c98bddfdd0fb.png!small)![2019-03-25_194045.png](https://image.3001.net/images/20190325/1553514211_5c98bee3abc59.png!small)![2019-03-25_194500.png](https://image.3001.net/images/20190325/1553514405_5c98bfa5a7ca1.png!small)

### 3.使用方法

xss Validator此扩展将响应发送到本地运行的XSS-Detector服务器，由Phantom.js和/或Slimer.js提供支持

用法：

在开始攻击之前，必须启动XSS-Detector服务器。导航到xss-detector目录并执行以下命令：

$ phantomjs xss.js＆
$ slimerjs slimer.js＆

默认情况下，服务器将在端口8093上侦听。服务器期望通过http响应传递base64编码的页面响应，该响应将通过Burp扩展器传递。

导航到xssValidator选项卡，然后复制Grep Phrase的值。在Burp Intruder grep-match函数中输入此值。与此Grep Phrase匹配的有效负载表示成功执行XSS有效负载。

### 4.演示

**1）首先打开cmd界面进入到xss-detector目录，执行phantomjs xss.js
**

**![2019-03-25_195926.png](https://image.3001.net/images/20190325/1553515249_5c98c2f1f1d95.png!small)2）访问测试环境开始抓包**

**    大概步骤：请求包----发送到intruder---定义变量---设置playloads[playload sets] [playload options][playload processing]三个模块---设置options添加匹配规则
**

****发送到intruder**
**

**![2019-03-25_201606.png](https://image.3001.net/images/20190325/1553516276_5c98c6f45d5af.png!small)**定义变量**
**

![2019-03-25_201923.png](https://image.3001.net/images/20190325/1553516502_5c98c7d6016a6.png!small)![2019-03-25_202156.png](https://image.3001.net/images/20190325/1553516547_5c98c8035bdf0.png!small)

**设置playloads[playload sets] [playload options][playload processing]三个模块**

![2019-03-25_202415.png](https://image.3001.net/images/20190325/1553516831_5c98c91faeab3.png!small)![2019-03-25_202556.png](https://image.3001.net/images/20190325/1553516849_5c98c9311fac7.png!small)**设置options添加匹配规则**

![2019-03-25_203335.png](https://image.3001.net/images/20190325/1553517311_5c98caff120cd.png!small)![2019-03-26_121308.png](https://image.3001.net/images/20190326/1553575006_5c99ac5ee4f04.png!small)

**点击右上方start attack**

**![2019-03-26_125335.png](https://image.3001.net/images/20190326/1553576276_5c99b15452444.png!small)
**

**![2019-03-26_121508.png](https://image.3001.net/images/20190326/1553575076_5c99aca4eb600.png!small)
**

**3）测试**

**![2019-03-26_122120.png](https://image.3001.net/images/20190326/1553575144_5c99ace89e11d.png!small)
**

### **![2019-03-26_121805.png](https://image.3001.net/images/20190326/1553575113_5c99acc9ee201.png!small)![2019-03-26_121948.png](https://image.3001.net/images/20190326/1553575162_5c99acfaab76d.png!small)5.注意事项**

1）.***我上面最后成功使用的是burp  1.6  ,我在用2.0和1.7.37的时候，匹配的payload不对，能使用的payload无法匹配到。

_搞了n久2.0，要是有大佬2.0使用没有问题，请指点下。_

![2019-03-26_122507.png](https://image.3001.net/images/20190326/1553575358_5c99adbe74499.png!small)

2）一定要确保端口8093是开着的，你可以访问127.0.0.1:8093

![2019-03-26_122916.png](https://image.3001.net/images/20190326/1553575374_5c99adcea8cb1.png!small)

3）端口占用，请修改xss.js和xss validator 里面的端口

### ![2019-03-26_124518.png](https://image.3001.net/images/20190326/1553575569_5c99ae919078b.png!small)![2019-03-26_124626.png](https://image.3001.net/images/20190326/1553575640_5c99aed8940c0.png!small)