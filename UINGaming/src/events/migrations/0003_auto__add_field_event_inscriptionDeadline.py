# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.inscriptionDeadline'
        db.add_column(u'events_event', 'inscriptionDeadline',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.inscriptionDeadline'
        db.delete_column(u'events_event', 'inscriptionDeadline')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'game': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'head': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'inscriptionDeadline': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['events']