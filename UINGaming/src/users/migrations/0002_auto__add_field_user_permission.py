# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.permission'
        db.add_column(u'users_user', 'permission',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.permission'
        db.delete_column(u'users_user', 'permission')


    models = {
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'hashedID': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'permission': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        }
    }

    complete_apps = ['users']