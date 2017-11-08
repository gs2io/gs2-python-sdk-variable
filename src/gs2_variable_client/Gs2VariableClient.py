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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2VariableClient(AbstractGs2Client):

    ENDPOINT = "variable"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2VariableClient, self).__init__(credential, region)

    def delete_my_variable(self, request):
        """
        変数を削除する<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_variable_client.control.DeleteMyVariableRequest.DeleteMyVariableRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_variable_client.control.DeleteMyVariableRequest import DeleteMyVariableRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/variable/" + str(("null" if request.get_variable_name() is None else request.get_variable_name())) + "",
            service=self.ENDPOINT,
            module=DeleteMyVariableRequest.Constant.MODULE,
            function=DeleteMyVariableRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_variable(self, request):
        """
        変数を削除する<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_variable_client.control.DeleteVariableRequest.DeleteVariableRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_variable_client.control.DeleteVariableRequest import DeleteVariableRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "/variable/" + str(("null" if request.get_variable_name() is None else request.get_variable_name())) + "",
            service=self.ENDPOINT,
            module=DeleteVariableRequest.Constant.MODULE,
            function=DeleteVariableRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def get_my_variable(self, request):
        """
        変数を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_variable_client.control.GetMyVariableRequest.GetMyVariableRequest
        :return: 結果
        :rtype: gs2_variable_client.control.GetMyVariableResult.GetMyVariableResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_variable_client.control.GetMyVariableRequest import GetMyVariableRequest

        from gs2_variable_client.control.GetMyVariableResult import GetMyVariableResult
        return GetMyVariableResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/variable/" + str(("null" if request.get_variable_name() is None else request.get_variable_name())) + "",
            service=self.ENDPOINT,
            module=GetMyVariableRequest.Constant.MODULE,
            function=GetMyVariableRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_variable(self, request):
        """
        変数を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_variable_client.control.GetVariableRequest.GetVariableRequest
        :return: 結果
        :rtype: gs2_variable_client.control.GetVariableResult.GetVariableResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_variable_client.control.GetVariableRequest import GetVariableRequest

        from gs2_variable_client.control.GetVariableResult import GetVariableResult
        return GetVariableResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "/variable/" + str(("null" if request.get_variable_name() is None else request.get_variable_name())) + "",
            service=self.ENDPOINT,
            module=GetVariableRequest.Constant.MODULE,
            function=GetVariableRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def set_my_variable(self, request):
        """
        変数を格納する<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_variable_client.control.SetMyVariableRequest.SetMyVariableRequest
        :return: 結果
        :rtype: gs2_variable_client.control.SetMyVariableResult.SetMyVariableResult
        """
        body = { 
            "value": request.get_value(),
            "ttl": request.get_ttl(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_variable_client.control.SetMyVariableRequest import SetMyVariableRequest

        from gs2_variable_client.control.SetMyVariableResult import SetMyVariableResult
        return SetMyVariableResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/variable/" + str(("null" if request.get_variable_name() is None else request.get_variable_name())) + "",
            service=self.ENDPOINT,
            module=SetMyVariableRequest.Constant.MODULE,
            function=SetMyVariableRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def set_variable(self, request):
        """
        変数を格納する<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_variable_client.control.SetVariableRequest.SetVariableRequest
        :return: 結果
        :rtype: gs2_variable_client.control.SetVariableResult.SetVariableResult
        """
        body = { 
            "value": request.get_value(),
            "ttl": request.get_ttl(),
        }

        headers = { 
        }
        from gs2_variable_client.control.SetVariableRequest import SetVariableRequest

        from gs2_variable_client.control.SetVariableResult import SetVariableResult
        return SetVariableResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "/variable/" + str(("null" if request.get_variable_name() is None else request.get_variable_name())) + "",
            service=self.ENDPOINT,
            module=SetVariableRequest.Constant.MODULE,
            function=SetVariableRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


