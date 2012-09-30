# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('portfolio_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('portfolio', ['Category'])

        # Adding model 'Collection'
        db.create_table('portfolio_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('portfolio', ['Collection'])

        # Adding model 'Artwork'
        db.create_table('portfolio_artwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(related_name='artworks', to=orm['portfolio.Collection'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('portfolio', ['Artwork'])

        # Adding M2M table for field categories on 'Artwork'
        db.create_table('portfolio_artwork_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artwork', models.ForeignKey(orm['portfolio.artwork'], null=False)),
            ('category', models.ForeignKey(orm['portfolio.category'], null=False))
        ))
        db.create_unique('portfolio_artwork_categories', ['artwork_id', 'category_id'])

        # Adding model 'Picture'
        db.create_table('portfolio_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('artwork', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pictures', to=orm['portfolio.Artwork'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('portfolio', ['Picture'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('portfolio_category')

        # Deleting model 'Collection'
        db.delete_table('portfolio_collection')

        # Deleting model 'Artwork'
        db.delete_table('portfolio_artwork')

        # Removing M2M table for field categories on 'Artwork'
        db.delete_table('portfolio_artwork_categories')

        # Deleting model 'Picture'
        db.delete_table('portfolio_picture')


    models = {
        'portfolio.artwork': {
            'Meta': {'ordering': "['order']", 'object_name': 'Artwork'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'artworks'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['portfolio.Category']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artworks'", 'to': "orm['portfolio.Collection']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'portfolio.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'portfolio.collection': {
            'Meta': {'object_name': 'Collection'},
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