# coding: utf-8
import re

from .common import InfoExtractor


class KnownDRMIE(InfoExtractor):
    IE_DESC = False
    UNSUPPORTED_SITES = (
        'play.hbomax.com',
    )
    _VALID_URL = r'https?://(%s)' % '|'.join(map(re.escape, UNSUPPORTED_SITES))

    def _real_extract(self, url):
        self.report_warning('TEMPLATE')
        return self.url_result(url, 'Generic')
