from django.db import models

class student(models.Model):    #學生資料
    st_number = models.CharField(max_length=8, null=False)  #學號
    st_name = models.CharField(max_length=20, null=False)   #姓名
    st_password = models.CharField(max_length=50, null=False)   #密碼
    sch_transfer = models.BooleanField(default='False', null=False)  #是否為轉學生
    dep_transfer = models.BooleanField(default='False', null=False)  #是否為轉系生
    exchange = models.BooleanField(default='False', null=False)  #是否為留學生
    early = models.BooleanField(default='False', null=False)  #是否為提前畢業
    postpone = models.BooleanField(default='False', null=False)  #是否為延畢生
    preparation = models.BooleanField(default='False', null=False)  #是否為預備研究生
    repeat = models.BooleanField(default='False', null=False)  #是否為復學生
    HK = models.BooleanField(default='False', null=False)  #是否為境外生(中五生)

    def __str__(self):
        return self.st_number

class st_class(models.Model):   #學生修課資料
    st_number = models.CharField(max_length=8, null=False)  #學號
    class_number = models.CharField(max_length=8, null=False)   #課程編號
    class_name = models.CharField(max_length=20, null=False)    #課程名稱
    grade = models.IntegerField(default=60, null=False)     #成績
    c_items = (('1','1'),('2','2'),('3','3'),('4','4'),)
    credit = models.CharField(choices=c_items, default='2', max_length=10)  #學分數
    y_items = (('1','1'),('2','2'),('3','3'),('4','4'),)
    year_in_school = models.CharField(choices=y_items, default='1', max_length=10)   #學期
    items1 = (('必修','必修'),('選修','選修'),)
    classify1 = models.CharField(choices=items1, default='必修', max_length=10)   #分類(必/選)
    items2 = (('系上','系上'),('通識','通識'),)
    classify2 = models.CharField(choices=items2, default='系上', max_length=10)   #分類(系上/通識)

    def __str__(self):
        return self.st_number

class course(models.Model):  #課程
    class_number = models.CharField(max_length=8, null=False)   #課程編號
    class_name = models.CharField(max_length=20, null=False)    #課程名稱
    c_items = (('1','1'),('2','2'),('3','3'),('4','4'),)
    credit = models.CharField(choices=c_items, default='2', max_length=10)  #學分數
    y_items = (('1','1'),('2','2'),('3','3'),('4','4'),)
    year_in_school = models.CharField(choices=y_items, default='1', max_length=10)  #學期
    time = models.CharField(max_length=100, null=False)     #上課時間
    items1 = (('必修','必修'),('選修','選修'),)
    classify1 = models.CharField(choices=items1, default='必修', max_length=10)   #分類(必/選)
    items2 = (('系上','系上'),('通識','通識'),)
    classify2 = models.CharField(choices=items2, default='系上', max_length=10)   #分類(系上/通識)
    english = models.BooleanField(default='True', null=False)  #全英語授課
    compolsory = models.BooleanField(default='True', null=False) #畢業應修科目

    def __str__(self):
        return self.class_name
