from django.db import models


# Create your models here.
class SqlDispose(models.Model):
    # 主机名
    host = models.CharField(max_length=32)
    # 端口号
    port = models.CharField(max_length=8, blank=True, null=True)
    # 数据库用户名
    user = models.CharField(max_length=16)
    # 数据库密码
    password = models.CharField(max_length=16)
    # 数据库名称
    dbName = models.CharField(max_length=16)
    # 数据库类型
    sqlType = models.CharField(max_length=8)
    # 引用标识
    mark = models.CharField(max_length=8, unique=True)
    # 连接编号
    encoding = models.CharField(max_length=8, blank=True, null=True)
    # 连接情况
    linkTest = models.SmallIntegerField(default=0, blank=True, null=True)
    # 创建人
    founder = models.CharField(max_length=8)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # 更新人
    update_person = models.CharField(max_length=8, blank=True, null=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True)
    # 是否删除
    is_del = models.SmallIntegerField(default='0')
    # 扩展字段1~5
    ext1 = models.CharField(max_length=128, blank=True, null=True)
    ext2 = models.CharField(max_length=128, blank=True, null=True)
    ext3 = models.CharField(max_length=128, blank=True, null=True)
    ext4 = models.CharField(max_length=128, blank=True, null=True)
    ext5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ['-update_time', '-create_time']

    def to_dict(self):
        return {
            'host': self.host,
            'port': self.port,
            'user': self.user,
            'password': self.password,
            'dbName': self.dbName,
            'sqlType': self.sqlType,
            'mark': self.mark,
            'encoding': self.encoding,
            'linkTest': self.linkTest,
            'founder': self.founder,
            'create_time': self.create_time,
            'update_person': self.update_person
        }
