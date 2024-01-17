from django.contrib import admin
from graduateapp.models import student, st_class, course

class studentAdmin(admin.ModelAdmin):   #學生資料
    list_display = ('st_number','st_name','st_password','sch_transfer','dep_transfer','exchange','early','postpone','preparation','repeat','HK')
    list_filter = ('st_number','st_name')
    search_fields = ('st_number',)
    odering = ('st_number')

admin.site.register(student,studentAdmin)

class st_classAdmin(admin.ModelAdmin):  #學生修課資料
    list_display = ('st_number','class_number','class_name','grade','credit','year_in_school','classify1','classify2')
    list_filter = ('class_number','class_name')
    search_fields = ('class_name',)
    odering = ('class_number')

admin.site.register(st_class,st_classAdmin)

class courseAdmin(admin.ModelAdmin):  #課程
    list_display = ('class_number','class_name','credit','year_in_school','time','classify1','classify2','english','compolsory')
    list_filter = ('class_number','class_name')
    search_fields = ('class_name',)
    odering = ('class_number')

admin.site.register(course,courseAdmin)
