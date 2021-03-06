#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

from sdk.card.BaseCard import BaseCard


class TextCard(BaseCard):
    """
    卡片形式展示
    """

    def __init__(self, content):
        '''
        文本卡片显示的content
        :param content:
        '''
        super(TextCard, self).__init__(['content'])
        self.data['type'] = "txt"
        self.data['content'] = "%s" % content

if __name__ == '__main__':

    textCard = TextCard('sdfasdfs')
    textCard.setContent('hehe')
    print(textCard.getData())
    pass