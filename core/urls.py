from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^products/$', 'core.views.product_list', name='product_list'),
    url(r'^new_product/$', 'core.views.new_product', name='new_product'),
    url(r'^new_user/$', 'core.views.new_user', name='new_user'),
    url(r'^new_customer/$', 'core.views.new_customer', name='new_customer'),
    url(r'^customers/$', 'core.views.customer_list', name='customer_list'),
    url(r'^new_order/$', 'core.views.new_order', name='new_order'),
    url(r'^orders/$', 'core.views.order_list', name='order_list'),
)