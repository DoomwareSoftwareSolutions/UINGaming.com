# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'home_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('linkText', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('linkRef', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'home', ['Slide'])

        # Adding model 'Feature'
        db.create_table(u'home_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('subheading', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'home', ['Feature'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'home_slide')

        # Deleting model 'Feature'
        db.delete_table(u'home_feature')


    models = {
        u'home.feature': {
            'Meta': {'object_name': 'Feature'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'home.slide': {
            'Meta': {'object_name': 'Slide'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'linkRef': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'linkText': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['home']