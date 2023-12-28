# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: gateway.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Optional

import betterproto
import grpclib


@dataclass
class AuthorizeRequest(betterproto.Message):
    pass


@dataclass
class AuthorizeResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    context_id: str = betterproto.string_field(2)
    new_token: str = betterproto.string_field(3)
    error_msg: str = betterproto.string_field(4)


@dataclass
class ObjectMetadata(betterproto.Message):
    name: str = betterproto.string_field(1)
    size: int = betterproto.int64_field(2)


@dataclass
class HeadObjectRequest(betterproto.Message):
    object_id: str = betterproto.string_field(1)


@dataclass
class HeadObjectResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    exists: bool = betterproto.bool_field(2)
    object_metadata: "ObjectMetadata" = betterproto.message_field(3)
    error_msg: str = betterproto.string_field(4)


@dataclass
class PutObjectRequest(betterproto.Message):
    object_content: bytes = betterproto.bytes_field(1)
    object_metadata: "ObjectMetadata" = betterproto.message_field(2)
    overwrite: bool = betterproto.bool_field(3)


@dataclass
class PutObjectResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    object_id: str = betterproto.string_field(2)
    error_msg: str = betterproto.string_field(3)


class GatewayServiceStub(betterproto.ServiceStub):
    async def authorize(self) -> AuthorizeResponse:
        request = AuthorizeRequest()

        return await self._unary_unary(
            "/gateway.GatewayService/Authorize",
            request,
            AuthorizeResponse,
        )

    async def head_object(self, *, object_id: str = "") -> HeadObjectResponse:
        request = HeadObjectRequest()
        request.object_id = object_id

        return await self._unary_unary(
            "/gateway.GatewayService/HeadObject",
            request,
            HeadObjectResponse,
        )

    async def put_object(
        self,
        *,
        object_content: bytes = b"",
        object_metadata: Optional["ObjectMetadata"] = None,
        overwrite: bool = False,
    ) -> PutObjectResponse:
        request = PutObjectRequest()
        request.object_content = object_content
        if object_metadata is not None:
            request.object_metadata = object_metadata
        request.overwrite = overwrite

        return await self._unary_unary(
            "/gateway.GatewayService/PutObject",
            request,
            PutObjectResponse,
        )
