#!/usr/bin/env python3
import optparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yt_dlp


def main():
    parser = optparse.OptionParser(usage='%prog OUTFILE.md')
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error('Expected an output filename')

    outfile, = args

    def gen_ies_md(ies):
        for ie in ies:
            ie_md = f'**{ie.IE_NAME}**'
            if ie.IE_DESC is False:
                continue
            if ie.IE_DESC is not None:
                ie_md += f': {ie.IE_DESC}'
            search_key = getattr(ie, 'SEARCH_KEY', None)
            if search_key is not None:
                ie_md += f'; "{ie.SEARCH_KEY}:" prefix'
            if not ie.working():
                ie_md += ' (Currently broken)'
            yield ie_md

    ies = sorted(yt_dlp.gen_extractors(), key=lambda i: i.IE_NAME.lower())
    out = '# Supported sites\n' + ''.join(
        ' - ' + md + '\n'
        for md in gen_ies_md(ies))

    with open(outfile, 'w', encoding='utf-8') as outf:
        outf.write(out)


if __name__ == '__main__':
    main()
