# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Customer.phone'
        db.delete_column(u'core_customer', 'phone')

        # Deleting field 'Customer.email'
        db.delete_column(u'core_customer', 'email')


    def backwards(self, orm):
        # Adding field 'Customer.phone'
        db.add_column(u'core_customer', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Customer.email'
        db.add_column(u'core_customer', 'email',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    models = {
        u'core.customer': {
            'Meta': {'object_name': 'Customer'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.order': {
            'Meta': {'object_name': 'Order'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Customer']"}),
            'order_number': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Product']", 'through': u"orm['core.ProductInOrder']", 'symmetrical': 'False'}),
            'update_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'core.product': {
            'Meta': {'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rr_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'sale_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'core.productinorder': {
            'Meta': {'object_name': 'ProductInOrder'},
            'order_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Order']"}),
            'pio_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        }
    }

    complete_apps = ['core']