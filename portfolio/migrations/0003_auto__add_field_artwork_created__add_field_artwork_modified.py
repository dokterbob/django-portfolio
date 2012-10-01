# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artwork.created'
        db.add_column('portfolio_artwork', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 1, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Artwork.modified'
        db.add_column('portfolio_artwork', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 1, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artwork.created'
        db.delete_column('portfolio_artwork', 'created')

        # Deleting field 'Artwork.modified'
        db.delete_column('portfolio_artwork', 'modified')


    models = {
        'portfolio.artwork': {
            'Meta': {'ordering': "['order']", 'object_name': 'Artwork'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'artworks'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['portfolio.Category']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artworks'", 'to': "orm['portfolio.Collection']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'portfolio.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'portfolio.collection': {
            'Meta': {'ordering': "['order']", 'object_name': 'Collection'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'portfolio.picture': {
            'Meta': {'ordering': "['order']", 'object_name': 'Picture'},
            'artwork': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pictures'", 'to': "orm['portfolio.Artwork']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']