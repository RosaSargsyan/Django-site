from django.db import models

# Create your models here.
class Index(models.Model):
    name1 = models.CharField('Index first name', max_length=100)
    name2 = models.CharField('Index second name', max_length=100)
    text = models.TextField('Index text')
    img = models.ImageField('Index image', upload_to='pictures')

    def __str__(self):
        return self.name1

    
class IndexServices(models.Model):
    titl = models.CharField('Services title', max_length=100)
    name =  models.CharField('Services first name', max_length=100)
    text = models.TextField('Srvices first text')
    img = models.ImageField('Service image', upload_to='pictures')
    def __str__(self):
        return self.titl
    

class IndexPrice(models.Model):
    titl = models.CharField('Price name', max_length=100)
    text = models.TextField('Text')
    name = models.CharField('Price name', max_length=100)
    about= models.TextField('Text')
    price = models.PositiveIntegerField('Price')
    def __str__(self):
        return self.titl
    

class IndexBlog(models.Model):
    titl = models.CharField('Blog name', max_length=100)
    text = models.TextField('Blog')
    img = models.ImageField('Blog image', upload_to='pictures')
    name = models.CharField('Blog name', max_length=100)
    about= models.TextField('Blog')
    data = models.DateField('data')
    def __str__(self):
        return self.titl
    

class IndexAbout(models.Model):
    titl = models.CharField('About name', max_length=100)
    text = models.TextField('About')
    img = models.ImageField('About image', upload_to='pictures')
    def __str__(self):
        return self.titl
    

class IndexCustomers(models.Model):
    titl = models.CharField('Customers name', max_length=100)    
    text = models.TextField('About')
    img = models.ImageField('Customers image', upload_to='pictures')
    name = models.CharField('Customers name', max_length=100)
    about= models.TextField('Customers')
    def __str__(self):
        return self.titl


class Contact(models.Model):
    name = models.CharField('Contact name', max_length=100)
    text = models.TextField('Contact text')
    def __str__(self):
        return self.name