from mutagen.easyid3 import EasyID3
from types import ListType

class TagContext(object):
    def __init__(self, file_path):
        self._tag = EasyID3(file_path)
        self.file_path = file_path
        #print 'Current tags:'
        #for frame in self._tag.frames:
        #print frame

    def set_tag_value(self, name, value):
        try:
            print 'setting tag %s on file %s to value %s' % \
                (name, self.file_path, str(value))

            if self._tag.has_key(name):
                curr = self._tag[name]
                if isinstance(curr, ListType):
                    new_value = []
                    new_value.append(str(value))
                else:
                    new_value = str(value)
            else: new_value = str(value)
            self._tag[name] = new_value
        except Exception, message:
            print "Invalid ID3 tag:", message
            raise

    def get_tag_value(self, name):
        if self._tag.has_key(name):
            curr = self._tag[name]
            if isinstance(curr, ListType):
                return curr[0]
            else: return curr
        else: return None

    def save(self):
        self._tag.save()

    def print_tags(self):
        for tag_key in self._tag.keys():
            print "%s: %s" % (tag_key, str(self._tag[tag_key]))

        
