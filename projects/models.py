from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile/' ,blank=True, default='media/profile/male.png')
    bio=models.TextField(blank=True,default='*No Bio*')
    phone_no=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=10,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username 
    @classmethod
    def get_profile(cls,username):
        userd=cls.objects.get(user=username)
        return userd
        
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class webapps(models.Model):
    title=models.CharField(max_length=100)
    main_picture=models.ImageField(upload_to='webapps/',default='webapps/internet.png')
    screenshot1=models.ImageField(upload_to='webapps/',blank=True,default='webapps/internet.png')
    screenshot2=models.ImageField(upload_to='webapps/',blank=True,default='webapps/internet.png')
    screenshot3=models.ImageField(upload_to='webapps/',blank=True,default='webapps/internet.png')
    link=models.CharField(max_length=200)
    description=models.TextField()
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-pub_date']

    @classmethod
    def get_all(cls):
        webapp=cls.objects.all()
        return webapp

    @classmethod
    def getlatest(cls):
        latestprojects=cls.objects.all()[:6]
        return latestprojects
    @classmethod
    def getspecificproject(cls,webapp_id):
        specificprojects=cls.objects.get(id=webapp_id)
        return specificprojects


class ratings(models.Model):
    RATE=[
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
    ]
    rate_by_design=models.IntegerField(choices=RATE,default=0,)
    rate_by_usability=models.IntegerField(choices=RATE,default=0,)
    rate_by_content=models.IntegerField(choices=RATE,default=0,)
    rate_by_creativity=models.IntegerField(choices=RATE,default=0,)
    average= models.IntegerField(default=0,)
    webapp=models.OneToOneField(webapps,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    def avg(self):
       
        print(self.rate_by_creativity)
        aver=(self.rate_by_creativity+self.rate_by_design+self.rate_by_usability+self.rate_by_content)/2
        
        return aver

    @classmethod
    def getinstance(cls,webapp_id):
        webaaps=cls.objects.filter(webapp=webapp_id).first()
        return webaaps

    @classmethod
    def getall(cls,webapp_id):
        weball=cls.objects.filter(webapp=webapp_id)
        return weball
    @classmethod
    def getuserrating(cls,currentuser):
        user=cls.objects.filter(user=currentuser)
        return user
    @classmethod
    def averageOfuser(cls,userratedarray,webappid):
    # sumOfNumbers=0
        num=cls.objects.filter(user__in=userratedarray,webapp=webappid).all()
        numsums=[]
        
        for no in num:
            numsum=no.rate_by_design+no.rate_by_usability+no.rate_by_content+no.rate_by_creativity
            numsums.append(numsum)
        lengthofratings=len(userratedarray)*40
        if lengthofratings:
            percentagevalue=((sum(numsums)*100))/lengthofratings
            return percentagevalue
        else:
            return numsums
    @ classmethod
    def average(cls,webapp_id):
        print(webapp_id)
        av=cls.objects.filter(webapp=webapp_id).first()
        return av
class comment(models.Model):
    comment=models.CharField(max_length=80,blank=True)
    webapp=models.ForeignKey(webapps,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def get_all(cls,webapp_id):
        comments=cls.objects.filter(webapp=webapp_id)
        return comments


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


