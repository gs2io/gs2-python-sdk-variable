# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_variable_client.model import *


class SetMyVariableResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        
        self.__value = unicode(response['value']) if 'value' in response.keys() and response['value'] is not None else None
        
        self.__expire = int(response['expire']) if 'expire' in response.keys() and response['expire'] is not None else None

    def get_value(self):
        """
        値を取得
        :return: 値
        :rtype: unicode
        """
        return self.__value

    def get_expire(self):
        """
        有効期限(エポック秒)を取得
        :return: 有効期限(エポック秒)
        :rtype: int
        """
        return self.__expire

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return { 
            'value': self.__value,
        
            'expire': self.__expire,
        
        }