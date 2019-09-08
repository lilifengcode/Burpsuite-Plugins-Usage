# Burpsuite插件之Hackvertor

​                                                                                                                                     by:裁决

## 0X01 Hackvertor介绍

Hackvertor是一个基于标签的转换工具，支持各种转义和编码，包括HTML5实体，十六进制，八进制，unicode，url编码等。

- 它使用类似XML的标记来指定使用的编码/转换类型。
- 您可以使用多个嵌套标记来执行转换。
- 标签也可以有参数，允许它们像函数一样运行。
- 它具有自动解码功能，可以猜测所需的转换类型并自动解码多次。
- 多个标签
- 字符集转换

## 0x02 Hackvertor安装

![nERSXQ.png](https://s2.ax1x.com/2019/09/04/nERSXQ.png)

## 0x03  Hackvertor使用

![nVGO9x.png](https://s2.ax1x.com/2019/09/04/nVGO9x.png)

### 1.简单base64加密

首先输入一个1

![nEON7V.png](https://s2.ax1x.com/2019/09/04/nEON7V.png)

选中1，选择base64加密

![nEOrc9.png](https://s2.ax1x.com/2019/09/04/nEOrc9.png)

### 2.多层加密base64+md5

![nEzuRO.png](https://s2.ax1x.com/2019/09/04/nEzuRO.png)

### 

![nEz8eA.png](https://s2.ax1x.com/2019/09/04/nEz8eA.png)

### 3.大致布局

![nVSIgS.png](https://s2.ax1x.com/2019/09/04/nVSIgS.png)

charset               字符集

compression     压缩 

encrypt               加密

HMACMD5         计算基于哈希值的消息验证代码



参考：https://portswigger.net/bappstore/65033cbd2c344fbabe57ac060b5dd100

​           https://portswigger.net/blog/bypassing-wafs-and-cracking-xor-with-hackvertor

