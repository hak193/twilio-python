r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Iam
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NewApiKeyInstance(InstanceResource):

    class Keytype(object):
        RESTRICTED = "restricted"

    """
    :ivar sid: The unique string that that we created to identify the NewKey resource. You will use this as the basic-auth `user` when authenticating to the API.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar date_created: The date and time in GMT that the API Key was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the new API Key was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar secret: The secret your application uses to sign Access Tokens and to authenticate to the REST API (you will use this as the basic-auth `password`).  **Note that for security reasons, this field is ONLY returned when the API Key is first created.**
    :ivar policy: Collection of allow assertions.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.secret: Optional[str] = payload.get("secret")
        self.policy: Optional[Dict[str, object]] = payload.get("policy")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Iam.V1.NewApiKeyInstance>"


class NewApiKeyList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the NewApiKeyList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Keys"

    def create(
        self,
        account_sid: str,
        friendly_name: Union[str, object] = values.unset,
        key_type: Union["NewApiKeyInstance.Keytype", object] = values.unset,
        policy: Union[object, object] = values.unset,
    ) -> NewApiKeyInstance:
        """
        Create the NewApiKeyInstance

        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Payments resource.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param key_type:
        :param policy: The \\\\`Policy\\\\` object is a collection that specifies the allowed Twilio permissions for the restricted key. For more information on the permissions available with restricted API keys, refer to the [Twilio documentation](https://www.twilio.com/docs/iam/api-keys/restricted-api-keys#permissions-available-with-restricted-api-keys).

        :returns: The created NewApiKeyInstance
        """

        data = values.of(
            {
                "AccountSid": account_sid,
                "FriendlyName": friendly_name,
                "KeyType": key_type,
                "Policy": serialize.object(policy),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return NewApiKeyInstance(self._version, payload)

    async def create_async(
        self,
        account_sid: str,
        friendly_name: Union[str, object] = values.unset,
        key_type: Union["NewApiKeyInstance.Keytype", object] = values.unset,
        policy: Union[object, object] = values.unset,
    ) -> NewApiKeyInstance:
        """
        Asynchronously create the NewApiKeyInstance

        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Payments resource.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param key_type:
        :param policy: The \\\\`Policy\\\\` object is a collection that specifies the allowed Twilio permissions for the restricted key. For more information on the permissions available with restricted API keys, refer to the [Twilio documentation](https://www.twilio.com/docs/iam/api-keys/restricted-api-keys#permissions-available-with-restricted-api-keys).

        :returns: The created NewApiKeyInstance
        """

        data = values.of(
            {
                "AccountSid": account_sid,
                "FriendlyName": friendly_name,
                "KeyType": key_type,
                "Policy": serialize.object(policy),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return NewApiKeyInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Iam.V1.NewApiKeyList>"
