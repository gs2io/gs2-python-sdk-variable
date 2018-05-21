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


class GetMyVariableRequest(Gs2UserRequest):

    class Constant(Gs2Variable):
        FUNCTION = "GetMyVariable"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetMyVariableRequest, self).__init__(params)
        if params is None:
            self.__variable_name = None
        else:
            self.set_variable_name(params['variableName'] if 'variableName' in params.keys() else None)

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
        if variable_name and not (isinstance(variable_name, str) or isinstance(variable_name, unicode)):
            raise TypeError(type(variable_name))
        self.__variable_name = variable_name

    def with_variable_name(self, variable_name):
        """
        変数名を設定
        :param variable_name: 変数名
        :type variable_name: unicode
        :return: this
        :rtype: GetMyVariableRequest
        """
        self.set_variable_name(variable_name)
        return self
