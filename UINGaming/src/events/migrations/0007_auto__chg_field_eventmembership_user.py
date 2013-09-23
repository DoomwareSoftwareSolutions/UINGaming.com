# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EventMembership.user'
        db.alter_column(u'events_eventmembership', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User']))

    def backwards(self, orm):

        # Changing field 'EventMembership.user'
        db.alter_column(u'events_eventmembership', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authentication.User']))

    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'enrolledUsers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.User']", 'through': u"orm['events.EventMembership']", 'symmetrical': 'False'}),
            'game': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'head': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'inscriptionDeadline': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'events.eventmembership': {
            'Meta': {'object_name': 'EventMembership'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'teamMembers': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'teamName': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'hashedID': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['events']