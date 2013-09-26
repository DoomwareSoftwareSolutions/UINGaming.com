# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'users_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('hashedID', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal(u'users', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'users_user')


    models = {
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'hashedID': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        }
    }

    complete_apps = ['users']