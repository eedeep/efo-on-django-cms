# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Programme.spiele'
        db.delete_column('programmes_programme', 'spiele')

        # Adding field 'Programme.needs'
        db.add_column('programmes_programme', 'needs', self.gf('django.db.models.fields.TextField')(default='needs'), keep_default=False)

        # Adding field 'Programme.objectives'
        db.add_column('programmes_programme', 'objectives', self.gf('django.db.models.fields.TextField')(default='objectives'), keep_default=False)

        # Adding field 'Programme.activities'
        db.add_column('programmes_programme', 'activities', self.gf('django.db.models.fields.TextField')(default='activities'), keep_default=False)

        # Adding field 'Programme.long_term_impact'
        db.add_column('programmes_programme', 'long_term_impact', self.gf('django.db.models.fields.TextField')(default='long term impact'), keep_default=False)

        # Adding field 'Programme.funding_info'
        db.add_column('programmes_programme', 'funding_info', self.gf('django.db.models.fields.TextField')(default='funding info'), keep_default=False)

        # Adding field 'Programme.how_to_help'
        db.add_column('programmes_programme', 'how_to_help', self.gf('django.db.models.fields.TextField')(default='how to help'), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Programme.spiele'
        db.add_column('programmes_programme', 'spiele', self.gf('django.db.models.fields.TextField')(default='spiele'), keep_default=False)

        # Deleting field 'Programme.needs'
        db.delete_column('programmes_programme', 'needs')

        # Deleting field 'Programme.objectives'
        db.delete_column('programmes_programme', 'objectives')

        # Deleting field 'Programme.activities'
        db.delete_column('programmes_programme', 'activities')

        # Deleting field 'Programme.long_term_impact'
        db.delete_column('programmes_programme', 'long_term_impact')

        # Deleting field 'Programme.funding_info'
        db.delete_column('programmes_programme', 'funding_info')

        # Deleting field 'Programme.how_to_help'
        db.delete_column('programmes_programme', 'how_to_help')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'features.featureset': {
            'Meta': {'object_name': 'FeatureSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_feature_area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['features.SiteFeatureArea']", 'null': 'True'})
        },
        'features.sitefeaturearea': {
            'Meta': {'unique_together': "(('site', 'area'),)", 'object_name': 'SiteFeatureArea'},
            'area': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'null': 'True'})
        },
        'images.image': {
            'Meta': {'ordering': "['order']", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'images_image_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'feature': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'images_image_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'photographer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slide_show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'programmes.programme': {
            'Meta': {'object_name': 'Programme'},
            'activities': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'programmes_programme_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'feature_sets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['features.FeatureSet']", 'null': 'True', 'blank': 'True'}),
            'funding_info': ('django.db.models.fields.TextField', [], {}),
            'how_to_help': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_term_impact': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'programmes_programme_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'needs': ('django.db.models.fields.TextField', [], {}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'programmes_programme_tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['taggit.Tag']"})
        },
        'programmes.programmeimage': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProgrammeImage', '_ormbases': ['images.Image']},
            'image_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['images.Image']", 'unique': 'True', 'primary_key': 'True'}),
            'programme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programmes.Programme']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['programmes']
