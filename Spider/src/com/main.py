# coding=utf-8
'''
Created on 2010-7-19

@author: tyrone
'''
import sys
import sitecustomize

from optparse import OptionParser
from urlparse import urlparse


def main(args = None):
    """ 程序入口 """
    MSG_USAGE = "spider"
    optParser = OptionParser(MSG_USAGE)

    optParser.add_option("-u", "--url",
        type ="string",
        dest = "url",
        help = "set url"
        )
    optParser.add_option("-d", "--deep",
        type ="string",
        dest = "deep",
        help = "set deep"
        )

    options, _ = optParser.parse_args()
    url     = options.url
    deep    = options.deep
    

if __name__ == '__main__':
    main()
