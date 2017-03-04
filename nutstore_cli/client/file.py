# coding: utf-8
from os import path as p
from dateutil.parser import parse as dt_parse


class PFile(object):
    def __init__(self, f):
        self._f = f

    @property
    def basename(self):
        return p.basename(self._f.name)

    @property
    def mtime(self):
        return dt_parse(self._f.mtime)

    @property
    def mtime_str(self):
        return self.mtime.strftime('%Y-%m-%d %H:%M')

    def __getattr__(self, item):
        return getattr(self._f, item)

    def __str__(self):
        return '<PFile {}>'.format(self.name)


class FileTable(object):
    def __init__(self, files):
        self.files = map(PFile, files)
        self.display_attrs = ['basename', 'mtime_str']

    def sort(self, key, reverse=False):
        self.files = sorted(self.files, key=key, reverse=reverse)

    def set_display_attrs(self, *attrs):
        """
        :type attrs: list[str]
        """
        self.display_attrs = attrs

    def get_format(self, extra_width):
        max_width = max([len(str(getattr(f, attr))) for attr in self.display_attrs for f in self.files]) + extra_width
        line_fmt = '{0._attr: <_width} '.replace('_width', str(max_width))
        fmt = ''
        for attr in self.display_attrs:
            fmt += line_fmt.replace('_attr', attr)
        return fmt

    def get_display(self, sep='\n', extra_with=2):
        fmt = self.get_format(extra_width=extra_with)
        return sep.join(map(fmt.format, self.files))