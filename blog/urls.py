from django.conf import settings
from django.conf.urls import include, url
#from django.conf.urls.static import static
from django.views.static import serve
#from django.contrib.auth import authenticate
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^group/1/$', views.post_list_grp1, name='post_list_grp1'),
    url(r'^group/2/$', views.post_list_grp2, name='post_list_grp2'),
    url(r'^group/3/$', views.post_list_grp3, name='post_list_grp3'),
    url(r'^group/4/$', views.post_list_grp4, name='post_list_grp4'),
    url(r'^group/5/$', views.post_list_grp5, name='post_list_grp5'),
    #url(r'^newest$', views.post_list, name='post_list'),
    #url(r'^oldest$', views.post_list_rev, name='post_list_rev'),
    url(r'^index$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/document/$', views.add_document_to_post, name='add_document_to_post'),
    url(r'^document/(?P<pk>\d+)/remove/$', views.document_remove, name='document_remove'),
    url(r'^post/zapisy$', views.post_zapisy, name='post_zapisy'),
    url(r'^post/about$', views.post_about, name='post_about'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL )
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL )
#    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT )
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
#)
