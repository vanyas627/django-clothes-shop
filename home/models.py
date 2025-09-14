from django.db import models


class Peculiarities(models.Model):

    title = models.CharField(max_length=50)
    description1 = models.TextField(max_length=100)
    description2 = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'


    class Meta:
        ordering = ['-created']
        verbose_name = 'Peculiarities'
        verbose_name_plural = 'Peculiarities'


class AboutUs(models.Model):

    description1 = models.TextField(max_length=200)
    image = models.ImageField(upload_to='about/')
    services_title = models.CharField(max_length=50)
    services_description = models.TextField(max_length=200)


    def __str__(self):
        return f'{self.services_title}'


    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'



class Services(models.Model):

    SERVICES_CHOICES_SIGN = [('fa fa-truck fa-lg','Car'),
                              ('fa fa-percent', 'Percent'),
                              ('fa fa-user', 'User'),
                              ('fa fa-comment', 'Comments'),
                              ('fa fa-phone', 'Phone'),
                              ('fa fa-shopping-cart','ShoppingCart'),
                              ('fa fa-home', 'Home'),
                             ('fa fa-search', 'Search')]


    service = models.CharField(max_length=50)
    service_sign = models.CharField(choices=SERVICES_CHOICES_SIGN, max_length=50)


    def __str__(self):
        return f'{self.service}'


    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'