from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField, TextAreaField, IntegerField
from wtforms.validators import DataRequired
from hashlib import md5


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={
                           'placeholder': 'Username'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
                             'placeholder': 'Password'})
    submit = SubmitField('Login', render_kw={
                         'class': 'ui fluid large teal submit button'})


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={
                           'placeholder': 'Username'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
                             'placeholder': 'Password'})
    repassword = PasswordField('Repeat password', validators=[
                               DataRequired()], render_kw={'placeholder': 'Repeat password'})
    student_id = IntegerField('Your student ID', validators=[
                      DataRequired()], render_kw={'placeholder': 'Student ID'})
    nation = StringField('Nation', validators=[
                      DataRequired()], render_kw={'placeholder': 'Your nation'})
    qq = IntegerField('Your QQ number', validators=[
                      DataRequired()], render_kw={'placeholder': 'QQ number'})
    submit = SubmitField('Register', render_kw={
                         'class': 'ui fluid large teal submit button'})


class AnswerForm(FlaskForm):

    def generate_form(self):
        for select in select_data:
            setattr(AnswerForm, 'select_' + md5(select[0].encode('utf-8')).hexdigest(),
                    RadioField(select[0], choices=[('A', select[1][0]), ('B', select[1][1]), ('C', select[1][2]), ('D', select[1][3])],
                               validators=[DataRequired()]))
        for judge in judge_data:
            setattr(AnswerForm, 'judge_'+md5(judge[0].encode('utf-8')).hexdigest(),
                    RadioField(judge[0], choices=[('T', 'T'), ('F', 'F')], validators=[DataRequired()]))
        setattr(AnswerForm, 'text_1', TextAreaField('描述计算机相关经历'))
        setattr(AnswerForm, 'text_2', TextAreaField('为什么想要加入计算机兴趣小组，加入后的学习方向'))
        setattr(AnswerForm, 'submit', SubmitField('Submit', render_kw={
            'class': 'ui fluid medium teal submit button'}))


select_data = [
    ['下列设备中，属于输出设备的是', ['显示器', '键盘', '鼠标', '手写板'], 'A'],
    ['组成计算机的CPU两大部件是', ['运算器和控制器', '控制器和寄存器', '运算器和内存', '控制器和内存'], 'A'],
    ['微型计算机的内存容量主要指', ['RAM', 'ROM', 'CMOS', 'Cache'], 'A'],
    ['可被计算机直接执行的程序由', ['机器', '汇编', '高级', '网络'], 'A'],
    ['从本质上讲，计算机病毒是一种', ['细菌', '文本', '程序', '微生物'], 'C'],
    ['在Internet上用于收发电子邮件的协议是', ['TCP/IP', 'IPX/SPX', 'POP3/SMTP', 'NetBEUI'], 'C'],
    ['算法的基本结构中不包括', ['逻辑结构', '选择结构', '循环结构', '顺序结构'], 'A'],
    ['Windows的剪贴板是用于临时存放信息的', ['一个窗口', '一个文件夹', '一块内存区间', '一块磁盘区间'], 'C'],
    ['操作系统按其功能关系分为系统层、管理层和（）三个层次', ['数据层', '逻辑层', '用户层', '应用层'], 'D'],
    ['完整的计算机系统由（）组成', ['运算器、控制器、存储器、输入设备和输出设备', '主机和外部设备',
                       '硬件系统和软件系统', '主机箱、显示器、键盘、鼠标、打印机'], 'C'],
    ['Windows的目录结构采用的是', ['树形结构', '线形结构', '层次结构', '网状结构'], 'A'],
    ['第一次保存Word文档时，系统将打开（）对话框', ['保存', '另存为', '新建', '关闭'], 'B'],
    ['在Excel工作表的单元格中计算一组数据后出现########', [
        '单元格显示宽度不够', '计算数据出错', '计算机公式出错', '数据格式出错'], 'A'],
    ['用C语言编写的程序需要用（）程序翻译后计算机才能识别。', ['汇编', '编译', '解释', '连接'], 'B'],
    ['用以太网形式构成的局域网，其拓扑结构为', ['环形', '总线型', '星型', '树形'], 'B'],
    ['对同一幅照片采用以下格式存储时，占用存储空间最大的格式是', ['JPG', 'TIF', 'BMP', 'GIF'], 'C'],
    ['世界上第一台电子计算机诞生于', ['1941年', '1946年', '1949年', '1950年'], 'B'],
    ['“Pentium Ⅱ350”和“Pentium Ⅲ450”中的“350”和“450”的含义是', [
        '最大内存容量', '最大运算速度', '最大运算精度', 'CPU的时钟频率'], 'D'],
    ['下列四条叙述中，属RAM特点的是', ['可随机读写数据，且断电后数据不会丢失', '可随机读写数据，断电后数据将全部丢失',
                          '只能顺序读写数据，断电后数据将部分丢失', '只能顺序读写数据，且断电后数据将全部丢失'], 'B'],
    ['32位微机中的32是指该微机', ['能同时处理32位二进制数', '能同时处理32位十进制数',
                        '具有32根地址总线', '运算精度可达小数点后32位'], 'A'],
]

judge_data = [
    ['内存储器按读写方式的不同分为两种，一种叫随机存储器（简称ROM），另一种叫只读存储器（简称RAM）。', 'F'],
    ['计算机内部使用二进制的根本原因在于，计算机的主要部件是由仅具有两个稳定状态的物理元件--电子开关线路组成的', 'T'],
    ['第四代电子计算机主要元件为大规模、超大规模集成电路。', 'T'],
    ['运算器的作用是完成各种算术运算和逻辑运算。', 'T'],
    ['微型计算机系统按传输信息的类型分为数据、控制、和地址三种总线，其中地址总线决定了CPU的最大寻址能力。', 'T'],
    ['人工智能技术能使计算机取代人的思维和行为。', 'F'],
    ['根据计算机的工作原理，计算机由系统软件和应用软件两部分组成。', 'F'],
    ['信息处理包括信息输入、信息加工和信息输出。', 'T'],
    ['1GB的确切表示为1024*1024*1024个Byte。', 'T'],
    ['操作系统是充当人与计算机之间的接口，使人们能通过一些简单的命令方便地使用计算机的一种软件。', 'T']
]
