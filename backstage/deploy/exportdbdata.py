#coding: UTF-8

import os
import sys
from xml.etree.ElementTree import ElementTree, Element, SubElement
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append('/home/amaris/dev-mixxx/backstage/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'backstage.settings_dev'

RESOURCE_PATH = "/home/amaris/dev-mixxx/backstage/savefiles"

from backstage.gui.models import FileStorage, MappingPresetObject, FileTypeDict



def export_files(pid):
    file_objecs = FileStroge.objects.filter(pid=pid)
    for obj in file_objects:
        fname = os.path.join(RESOUCE_PATH)
        default_storage.save(fname, ContentFile(obj.file_obj.read()))
        

def export(path):
    root = Element('presets')
    xmlFiles = FileStorage.objects.filter(file_type.category='xml')
    for xml in xmlFiles:
        pid = xml.mapping_preset_id.pid
        try:
            status = MappingPresetObject.objects.get(pid=pid).preset_status.category
        except Exception,err:
            print err
            print "this pid is not exists in the database"
        else:
            preset = SubElement(root, 'preset')
            preset.set('filename', f.file_name)
            preset.set('pid', pid)
            preset.set('status', status)
            export_files(pid)
            
    tree = ElementTree(root)
    tree.write(os.path.join(path, 'mapScript.xml'), encoding='utf-8')

if __name__ == "__main__":
    export(path="./")
