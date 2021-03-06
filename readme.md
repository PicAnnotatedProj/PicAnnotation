--------------
**通用图片文字标注软件设计**
---

**一、要求：**
> ①设计一个标注软件，可以显示图片，可以将图片中的文字框位置显示出来，可以将图片中的文字记录下来；
> 
>②图片中的文字每行相关的内容组成一个框，框的位置和框内文字的内容需要手工生成，软件只负责记录；

>③软件可以通过手动修改框的位置，并记录下修改以后的位置；

> ④软件可以通过手动修改框内标注文字的内容，并记录下修改后的内容；

> ⑤采用xml格式记录以上信息，要求软件能解析xml格式文件，并能生成xml格式的文件；

>  ⑥Xml格式会记录框的坐标，同时可以记录框的内容。

***
**二、框架结构设计：**

1.软件窗口gui实现
>1)工具栏：

* ①打开文件（open）；②放大镜； ③缩小；④创造标记图形（create label，默认矩形）；⑤修改标记图形（edit label）；⑥撤销（undo）；⑦保存（save）；

>2)文件显示区域（file list）：

* 要求点击相应文件名显示图片和标记

>3)操作显示界面：

* 显示当前文件的图片以及所有标注，标注框生成时自动跳出输入框（进行用户标注显示）

>4)功能显示区：

* ①labellist：标注框排列显示所有已标注的内容（点击自动高亮）

* ②ploygon labels:标注区域显示选项表	


2.软件功能实现
>1)工具栏：

>①open（打开文件）：

* 软件在打开图片的时候，要判断是否有同名的xml文件，如果存在，则读取该文件，并将标注信息显示在图片上，如果没有，保持图片原状；
>②save（保存文件）：
* 软件需要有保存按钮，在保存按钮按下的时候要判断是否对标注信息进行过修改，如果修改过，则需要修改对应的xml文件；* 软件中退出的时候要保存最新的结果到xml文件，以免标注信息丢失；>③放大镜：

* 图片可以在视图区域中使用鼠标滚轮进行中心缩放、拖动平移
>④创造标记图形（create label，默认矩形）：

* 矩形框在显示区域操作

>⑤修改标记图形（edit label）

* 可移动和修改标记图形位置

>2)文件显示区域（file list）：

* 相应文件名显示

>3)操作显示界面：

* ①图片显示:
>>
* 显示当且文件对应图片并且解析xml文件
* 显示标记矩形框、和移动操作的矩形框
* 每次标记矩形框确定自动弹出文本输入框，进行输入

>4)功能显示区：

* labellist：标注框排列显示所有已标注的内容（点击自动高亮）

* ploygon labels:标注区域显示选项表

###三、总结所有功能：
>1)基本功能：

* 读取选定文件夹下的所有jpg，png等格式的图片，具有可以显示文件列表的区域，可以通过点击相应文件名打开相应图片，具有显示图片的区域。
* 读取选定文件夹下的图片对应的xml文件（xml文件名前缀与图片文件名前缀相同），xml文件中存储有标注框相对于图片的坐标，以及框内文本的识别内容
* 将xml中的识别内容解析出来并显示在列表区域中，根据标注框的坐标将标注框绘制在图片上
* 将标注框绘制在图片上，要求可以选中标注框，对标注框的位置、大小进行调整，可以对框内识别内容进行修改，将以上调整信息存储到对应的xml文件中。

>2)拓展功能：

* 图片可以在视图区域中使用鼠标滚轮进行中心缩放、拖动平移。
* 设计一个固定位置的工作区，用于放大显示当前选中的标注框以及标注框中的文字内容。
* 注意选中标注框时，内容列表焦点也跳到相应部位，工作区内容也更改为相应框
* 更多人性化设计
