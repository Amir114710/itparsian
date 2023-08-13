from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.


class Mainmenu(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['position']

    title = models.CharField(max_length=50, verbose_name='نام دسته بندی')
    parent = models.ForeignKey('self', blank=True, null=True, max_length=100, related_name="children",
                               default=None, on_delete=models.SET_NULL, verbose_name="زیر دسته")
    status = models.BooleanField(
        default=True, blank=True, null=True, verbose_name="آیا نمایش داده شود؟")
    link = models.CharField(max_length=500, verbose_name='لینک صفحه', blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.title
    objects = CategoryManager()

    class Meta:
        ordering = ['-created']
        verbose_name = 'منو های سایت'
        verbose_name_plural = 'منو های سایت'


class ProjectDone(models.Model):
    title = RichTextUploadingField(blank=True)
    mainimg = models.ImageField(blank=True, upload_to='Projects')
    respornsive = models.ImageField(blank=True, upload_to='Projects')
    logo = models.ImageField(blank=True, upload_to='Projects')
    discription1 = RichTextUploadingField(max_length=70)
    discription2 = RichTextUploadingField(max_length=70)
    link = models.TextField(max_length=120)
    created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'نمونه کار های سایت'
        verbose_name_plural = 'نمونه کار های سایت'


class ContentBox(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'کانتنت باکس های سایت'
        verbose_name_plural = 'کانتنت باکس های سایت'

class Services(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField()
    icon = models.ImageField(upload_to='ServicesLogo')
    created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'سرویس های سایت'
        verbose_name_plural = 'سرویس های سایت'
    
class TipsAbout(models.Model):
    title = models.CharField(max_length=200 , null=True , blank=True , verbose_name='نکته :')
    first_col = models.BooleanField(default=False , verbose_name='ایا در ستون اول باشد ؟')
    seconde_col = models.BooleanField(default=False , verbose_name='ایا در ستون دوم باشد ؟')
    created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'نکاتی درباره ی سایت'
        verbose_name_plural = 'نکاتی درباره ی سایت'

class Attribute(models.Model):
    title = models.CharField(max_length=250 , verbose_name='نام ویژگی')
    address = models.TextField(verbose_name='لینک' , null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'ویژگی ها'
        verbose_name_plural = 'ویژگی های سایت'

class Footer(models.Model):
    address = RichTextUploadingField(verbose_name='ادرس')
    phone_number = models.IntegerField(default=0 , verbose_name='شماره تلفن')
    whatsappphone_number = models.CharField(max_length=50 , verbose_name='شماره تلفن واتساپ')
    email = models.EmailField(verbose_name='ایمیل')
    attribute = models.ManyToManyField(Attribute , related_name='footers' , verbose_name='ویژگی')
    discription = RichTextUploadingField(verbose_name='توضیحات')
    instagram = models.TextField(verbose_name='ادرس اینستاگرام' , null=True)
    telegram = models.TextField(verbose_name='ادرس تلگرام' , null=True)
    whatsapp = models.TextField(verbose_name='ادرس واتساپ' , null=True)
    linkdin = models.TextField(verbose_name='ادرس لینک دین' , null=True)
    youtube = models.TextField(verbose_name='ادرس یوتیوب' , null=True)
    twwiter = models.TextField(verbose_name='ادرس توییتر' , null=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.address
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'فوتر'
        verbose_name_plural = 'فوتر'

class Question(models.Model):
    question = RichTextUploadingField(verbose_name='سوال')
    answer = RichTextUploadingField(verbose_name='جواب')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        ordering = ['-created']
        verbose_name = ' سوال متداول'
        verbose_name_plural = 'سوالات متداول'
