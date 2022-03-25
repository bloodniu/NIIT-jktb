# **NIIT-健康填报自动化**  
基于python，通过代码模拟运行打卡过程，实现一键自动化健康打卡。

# **特别声明**  
- 本仓库发布的项目中涉及的任何脚本，仅用于测试和python学习研究，禁止用于任何商业用途,虚假上报等，请勿开展以此为目的的任何盈利和违法行为，违法必究！  
- 在任何情况下，本程序作者与你决定运行本程序无关，不为你运行此程序所造成的任何损失、受到的处罚以及造成的法律后果等负任何责任。原则上不提供任何形式的技术支持。<code>tanglaoban</code> 保留随时更改或补充与删除项目的权利。  
**您一旦使用并复制了本仓库且本人制作的任何代码或项目，则视为<code>已接受</code>此声明，请仔细阅读**  

# **更新记录**  
邮箱通知功能，修改jktb.py文件对应参数   
2022/3/25  表单更新，新增是否在校，疫苗，核酸 
# **使用方法**  
**1.环境要求**  
- windows操作系统，Linux操作系统，Ubuntu操作系统，ios操作系统（Pythonista）
- Python 3.x以上，安装有 requests，Pyyaml 库  
 
**2.数据填写**  
- 打开config.yaml，填写学号，姓名，高德API,Cookie，X_CSRF_Token，定位地址  
- 打开jktb.py 填写空缺内容   个人识别码，班级识别码，学院识别码 

**3.数据获取**  
- 高德开放平台，Web服务API  
- Cookie,X_CSRF_Token
- 自行通过抓包软件获取最后的create，涉及隐私，请勿泄露，测试后及时删除。  

**4.运行脚本**  
python3 jktb.py  
<pre><span class="pl-k">~</span> python3 jktb.py
INFO:root: <span class="pl-k">**</span> Get ready <span class="pl-k">**</span>
INFO:root: <span class="pl-k">**</span> 详细位置获取经纬度开始 <span class="pl-k">**</span>
 当前经度（通过详细地址获取）：xxx.xxxxxx00000001
 当前纬度（通过详细地址获取）：xxx.xxxxxx000000001
200
200
200
200
200
200
200
 get <span class="pl-k">if</span> seccess 200
200
INFO:root: all ready to start <span class="pl-k">!</span>
 get id xxxxx
 get Class xxx
 get email xxx
 get sex x
 get telephone 189<span class="pl-k">****</span>6699
 get sdept xxxx
 get specialty 网络xxxxx
 get address 江苏省xxxxxxxxxxxxxxxx
INFO:root: 信息全部获取完毕
INFO:root: <span class="pl-k">**</span> Wait five seconds <span class="pl-k">**</span>
 push data {<span class="pl-s"><span class="pl-pds">"</span>code<span class="pl-pds">"</span></span>:4402,<span class="pl-s"><span class="pl-pds">"</span>msg<span class="pl-pds">"</span></span>:<span class="pl-s"><span class="pl-pds">"</span>今日健康信息已上报，请勿重复提交!!<span class="pl-pds">"</span></span>,<span class="pl-s"><span class="pl-pds">"</span>meta<span class="pl-pds">"</span></span>:{<span class="pl-s"><span class="pl-pds">"</span>repeatFields<span class="pl-pds">"</span></span>}}</pre>

# **end**  
仅限个人测试学习python，请在下载后24小时内删除。本人不提供任何形式的技术支持!
