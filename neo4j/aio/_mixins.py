#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2020 "Neo4j,"
# Neo4j Sweden AB [http://neo4j.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from neo4j.addressing import Address


class Addressable:
    """ Mixin for providing access to local and remote address
    properties via an asyncio.Transport object.
    """

    __transport = None

    def set_transport(self, transport):
        self.__transport = transport

    @property
    def local_address(self):
        return Address(self.__transport.get_extra_info("sockname"))

    @property
    def remote_address(self):
        return Address(self.__transport.get_extra_info("peername"))


class Breakable:
    """ Mixin for objects that can break, resulting in an unusable,
    unrecoverable state.
    """

    __broken = False

    def set_broken(self):
        self.__broken = True

    @property
    def broken(self):
        return self.__broken
