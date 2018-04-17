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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_variable_client.Gs2Variable import Gs2Variable


class SetMyVariableRequest(Gs2UserRequest):

    class Constant(Gs2Variable):
        FUNCTION = "SetMyVariable"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(SetMyVariableRequest, self).__init__(params)
        if params is None:
            self.__variable_name = None
            self.__value = None
            self.__ttl = None
        else:
            self.set_variable_name(params['variableName'] if 'variableName' in params.keys() else None)
            self.set_value(params['value'] if 'value' in params.keys() else None)
            self.set_ttl(params['ttl'] if 'ttl' in params.keys() else None)

    def get_variable_name(self):
        """
        変数名を取得
        :return: 変数名
        :rtype: unicode
        """
        return self.__variable_name

    def set_variable_name(self, variable_name):
        """
        変数名を設定
        :param variable_name: 変数名
        :type variable_name: unicode
        """
        if _variable_name and not (isinstance(_variable_name, str) or isinstance(_variable_name, unicode)):
            raise TypeError(type(variable_name))
        self.__variable_name = variable_name

    def with_variable_name(self, variable_name):
        """
        変数名を設定
        :param variable_name: 変数名
        :type variable_name: unicode
        :return: this
        :rtype: SetMyVariableRequest
        """
        self.set_variable_name(variable_name)
        return self

    def get_value(self):
        """
        値を取得
        :return: 値
        :rtype: unicode
        """
        return self.__value

    def set_value(self, value):
        """
        値を設定
        :param value: 値
        :type value: unicode
        """
        if _value and not (isinstance(_value, str) or isinstance(_value, unicode)):
            raise TypeError(type(value))
        self.__value = value

    def with_value(self, value):
        """
        値を設定
        :param value: 値
        :type value: unicode
        :return: this
        :rtype: SetMyVariableRequest
        """
        self.set_value(value)
        return self

    def get_ttl(self):
        """
        変数の有効期間(秒)を取得
        :return: 変数の有効期間(秒)
        :rtype: int
        """
        return self.__ttl

    def set_ttl(self, ttl):
        """
        変数の有効期間(秒)を設定
        :param ttl: 変数の有効期間(秒)
        :type ttl: int
        """
        if _ttl and not isinstance(_ttl, int):
            raise TypeError(type(ttl))
        self.__ttl = ttl

    def with_ttl(self, ttl):
        """
        変数の有効期間(秒)を設定
        :param ttl: 変数の有効期間(秒)
        :type ttl: int
        :return: this
        :rtype: SetMyVariableRequest
        """
        self.set_ttl(ttl)
        return self
