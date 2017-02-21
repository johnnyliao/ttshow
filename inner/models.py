#-*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from django.contrib.auth.models import AbstractUser
from mezzanine.core.fields import RichTextField
from django.utils import timezone

from django.contrib.contenttypes import generic

from django.core.exceptions import ObjectDoesNotExist
from account.models import User
from django.contrib.sites.models import Site
import urlparse, settings

TYPE_CHOICES = (
	("fun_news", u'趣味新聞'),
	("video", u'影音'),
	("picture", u'插畫'),
	("love", u'星座愛情'),
	("pet", u'寵物'),
    ("link_out", u'聯合出品'),
	("millon", u'百萬經典'),
)


class Inner(models.Model):
    user = models.ForeignKey(User, related_name='user_inners')
    title = models.CharField(_(u"標題"), max_length=100)
    content = RichTextField(_(u"簡介"), max_length=2000)
    inner_type = models.CharField(_(u"分類"), max_length=100, choices=TYPE_CHOICES)
    photo = models.ImageField(_(u"縮圖"), upload_to='inner/pre_image')
    date = models.DateTimeField(_(u"時間"), auto_now=True)
    count = models.IntegerField(_(u"點擊數"))

    class Meta:
        verbose_name = _(u'文章')
        verbose_name_plural = _(u'文章列表')

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.photo.url + '" />'

    image_tag.allow_tags = True
