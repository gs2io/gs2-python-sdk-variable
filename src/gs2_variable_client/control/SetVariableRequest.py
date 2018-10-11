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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_variable_client.Gs2Variable import Gs2Variable


class SetVariableRequest(Gs2BasicRequest):

    class Constant(Gs2Variable):
        FUNCTION = "SetVariable"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(SetVariableRequest, self).__init__(params)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__variable_name = None
        else:
            self.set_variable_name(params['variableName'] if 'variableName' in params.keys() else None)
        if params is None:
            self.__value = None
        else:
            self.set_value(params['value'] if 'value' in params.keys() else None)
        if params is None:
            self.__ttl = None
        else:
            self.set_ttl(params['ttl'] if 'ttl' in params.keys() else None)

    def get_user_id(self):
        """
        変数のスコープとなるユーザIDを取得
        :return: 変数のスコープとなるユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        変数のスコープとなるユーザIDを設定
        :param user_id: 変数のスコープとなるユーザID
        :type user_id: unicode
        """
        if user_id is not None and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        変数のスコープとなるユーザIDを設定
        :param user_id: 変数のスコープとなるユーザID
        :type user_id: unicode
        :return: this
        :rtype: SetVariableRequest
        """
        self.set_user_id(user_id)
        return self

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
        if variable_name is not None and not (isinstance(variable_name, str) or isinstance(variable_name, unicode)):
            raise TypeError(type(variable_name))
        self.__variable_name = variable_name

    def with_variable_name(self, variable_name):
        """
        変数名を設定
        :param variable_name: 変数名
        :type variable_name: unicode
        :return: this
        :rtype: SetVariableRequest
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
        if value is not None and not (isinstance(value, str) or isinstance(value, unicode)):
            raise TypeError(type(value))
        self.__value = value

    def with_value(self, value):
        """
        値を設定
        :param value: 値
        :type value: unicode
        :return: this
        :rtype: SetVariableRequest
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
        if ttl is not None and not isinstance(ttl, int):
            raise TypeError(type(ttl))
        self.__ttl = ttl

    def with_ttl(self, ttl):
        """
        変数の有効期間(秒)を設定
        :param ttl: 変数の有効期間(秒)
        :type ttl: int
        :return: this
        :rtype: SetVariableRequest
        """
        self.set_ttl(ttl)
        return self
