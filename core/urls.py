from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^products/$', 'core.views.product_list', name='product_list'),
    url(r'^new_product/$', 'core.views.new_product', name='new_product'),
    url(r'^new_user/$', 'core.views.new_user', name='new_user'),
    url(r'^new_customer/$', 'core.views.new_customer', name='new_customer'),
    url(r'^customers/$', 'core.views.customer_list', name='customer_list'),
    url(r'^customer/(\d{1})$', 'core.views.customer', name='customer'),
    url(r'^new_order/$', 'core.views.new_order', name='new_order'),
    url(r'^orders/$', 'core.views.order_list', name='order_list'),
    url(r'^get_price/(\d{1})$', 'core.views.price_lookup', name='get_price'),
    url(r'^get_points/(\d{1})$', 'core.views.points_lookup', name='get_points'),
    url(r'^claim_backorder/(\d{1})$', 'core.views.claim_backorder', name='claim_backorder'),
)
