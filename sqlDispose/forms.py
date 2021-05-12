from django import forms

from .models import SqlDispose


class SqlDisposeForm(forms.ModelForm):
    class Meta:
        model = SqlDispose
        fields = ['host', 'user', 'password', 'dbName', 'sqlType', 'mark', 'founder', 'port', 'encoding', 'linkTest']


class UpdateSqlDisposeForm(forms.ModelForm):
    class Meta:
        model = SqlDispose
        fields = ['password', 'user', 'host', 'mark', 'encoding', 'update_person', 'dbName', 'sqlType', 'founder',
                  'port', 'id']


class DeleteSqlDisposeForm(forms.ModelForm):
    class Meta:
        model = SqlDispose
        exclude = ()


class NewSqlDisposeForm(forms.Form):
    host = forms.CharField(max_length=32,
                           label='主机名',
                           error_messages={
                               "required": "不能为空",
                               "invalid": "格式错误",
                               "min_length": "用户名最短7位"
                           })
    port = forms.CharField(max_length=8,
                           label='端口号',
                           error_messages={
                               "required": "不能为空",
                               "invalid": "格式错误",
                               "min_length": "用户名最短7位"
                           })
    # 数据库用户名
    user = forms.CharField(max_length=16)
    # 数据库密码
    password = forms.CharField(max_length=16)
    # 数据库名称
    dbName = forms.CharField(max_length=16)
    # 数据库类型
    sqlType = forms.CharField(max_length=8)
    # 引用标识
    mark = forms.CharField(max_length=8)
    # 连接编号
    encoding = forms.CharField(max_length=8)
    # 连接情况
    linkTest = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )
    # 创建人
    founder = forms.CharField(max_length=8)
    # 创建时间
    # create_time = forms.DateTimeField(auto_now_add=True, blank=True)
    # 更新人
    # update_person = forms.CharField(max_length=8)
    # 更新时间
    # update_time = forms.DateTimeField(auto_now=True, blank=True)
