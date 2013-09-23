# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event.created'
        db.alter_column(u'events_event', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Event.date'
        db.alter_column(u'events_event', 'date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Event.created'
        db.alter_column(u'events_event', 'created', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'Event.date'
        db.alter_column(u'events_event', 'date', self.gf('django.db.models.fields.DateField')())

    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'game': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'head': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['events']