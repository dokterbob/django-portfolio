# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoryTranslation'
        db.create_table(u'portfolio_categorytranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['portfolio.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'portfolio', ['CategoryTranslation'])

        # Adding unique constraint on 'CategoryTranslation', fields ['parent', 'language_code']
        db.create_unique(u'portfolio_categorytranslation', ['parent_id', 'language_code'])

        # Adding model 'CollectionTranslation'
        db.create_table(u'portfolio_collectiontranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['portfolio.Collection'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'portfolio', ['CollectionTranslation'])

        # Adding unique constraint on 'CollectionTranslation', fields ['parent', 'language_code']
        db.create_unique(u'portfolio_collectiontranslation', ['parent_id', 'language_code'])

        # Adding model 'ArtworkTranslation'
        db.create_table(u'portfolio_artworktranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['portfolio.Artwork'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'portfolio', ['ArtworkTranslation'])

        # Adding unique constraint on 'ArtworkTranslation', fields ['parent', 'language_code']
        db.create_unique(u'portfolio_artworktranslation', ['parent_id', 'language_code'])

        # Deleting field 'Collection.description'
        db.delete_column(u'portfolio_collection', 'description')

        # Deleting field 'Collection.title'
        db.delete_column(u'portfolio_collection', 'title')

        # Deleting field 'Category.title'
        db.delete_column(u'portfolio_category', 'title')

        # Deleting field 'Artwork.title'
        db.delete_column(u'portfolio_artwork', 'title')

        # Deleting field 'Artwork.description'
        db.delete_column(u'portfolio_artwork', 'description')


    def backwards(self, orm):
        # Removing unique constraint on 'ArtworkTranslation', fields ['parent', 'language_code']
        db.delete_unique(u'portfolio_artworktranslation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'CollectionTranslation', fields ['parent', 'language_code']
        db.delete_unique(u'portfolio_collectiontranslation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'CategoryTranslation', fields ['parent', 'language_code']
        db.delete_unique(u'portfolio_categorytranslation', ['parent_id', 'language_code'])

        # Deleting model 'CategoryTranslation'
        db.delete_table(u'portfolio_categorytranslation')

        # Deleting model 'CollectionTranslation'
        db.delete_table(u'portfolio_collectiontranslation')

        # Deleting model 'ArtworkTranslation'
        db.delete_table(u'portfolio_artworktranslation')

        # Adding field 'Collection.description'
        db.add_column(u'portfolio_collection', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Collection.title'
        raise RuntimeError("Cannot reverse this migration. 'Collection.title' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Category.title'
        raise RuntimeError("Cannot reverse this migration. 'Category.title' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Artwork.title'
        raise RuntimeError("Cannot reverse this migration. 'Artwork.title' and its values cannot be restored.")
        # Adding field 'Artwork.description'
        db.add_column(u'portfolio_artwork', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    models = {
        u'portfolio.artwork': {
            'Meta': {'ordering': "['order']", 'object_name': 'Artwork'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'artworks'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['portfolio.Category']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artworks'", 'to': u"orm['portfolio.Collection']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        u'portfolio.artworktranslation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'ArtworkTranslation'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': u"orm['portfolio.Artwork']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'portfolio.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'portfolio.categorytranslation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'CategoryTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': u"orm['portfolio.Category']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'portfolio.collection': {
            'Meta': {'ordering': "['order']", 'object_name': 'Collection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'portfolio.collectiontranslation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'CollectionTranslation'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': u"orm['portfolio.Collection']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'portfolio.picture': {
            'Meta': {'ordering': "['order']", 'object_name': 'Picture'},
            'artwork': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pictures'", 'to': u"orm['portfolio.Artwork']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']