from ID3 import *

class TagContext(object):
    def __init__(self, file_path):
        print 'Current tags:'
        print self._id3_info
        self.file_path = file_path
        self._id3_info = ID3(file_path)

    def set_tag_value(self, name, value):
        try:
            print 'setting tag %s on file %s to value %s' % (name, self.file_path, value)
            self._id3_info[name] = str(value)
        except InvalidTagError, message:
            print "Invalid ID3 tag:", message
            raise

    def get_tag_value(self, name):
        return self._id3_info[name]
        
