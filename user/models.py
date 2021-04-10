from django.db import models


# Create your models here.
class User(models.Model):
    # 用户名
    user = models.CharField(max_length=8, unique=True)
    # 手机号
    phone = models.CharField(max_length=16, unique=True)
    # 密码
    password = models.CharField(max_length=16, blank=False)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, blank=True)
    # 用户等级
    level = models.IntegerField(default=1)
    # 是否删除
    is_del = models.SmallIntegerField(default='0')
    # 扩展字段1~5
    ext1 = models.CharField(max_length=128)
    ext2 = models.CharField(max_length=128)
    ext3 = models.CharField(max_length=128)
    ext4 = models.CharField(max_length=128)
    ext5 = models.CharField(max_length=128)

    def to_dict(self):
        return {
            'user': self.user,
            'phone': self.phone,
            'level': self.level
        }
