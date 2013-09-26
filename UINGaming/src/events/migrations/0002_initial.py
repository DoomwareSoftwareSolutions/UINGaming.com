# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('head', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('game', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('inscriptionDeadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding model 'EventMembership'
        db.create_table(u'events_eventmembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('teamName', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('teamTag', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('teamMembers', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['EventMembership'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Deleting model 'EventMembership'
        db.delete_table(u'events_eventmembership')


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
            'teamTag': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
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

    complete_apps = ['events']