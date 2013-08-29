# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'core_product', (
            ('product_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sale_price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('rr_price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Product'])

        # Adding model 'Customer'
        db.create_table(u'core_customer', (
            ('customer_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('address_3', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Customer'])

        # Adding model 'Order'
        db.create_table(u'core_order', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order_number', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Customer'])),
            ('order_total', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Order'])

        # Adding model 'ProductInOrder'
        db.create_table(u'core_productinorder', (
            ('pio_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Order'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('total_price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'core', ['ProductInOrder'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'core_product')

        # Deleting model 'Customer'
        db.delete_table(u'core_customer')

        # Deleting model 'Order'
        db.delete_table(u'core_order')

        # Deleting model 'ProductInOrder'
        db.delete_table(u'core_productinorder')


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