#!/usr/bin/env python3
"""
This module is used to validate the arguments
"""
from pydantic import BaseModel, IPvAnyInterface


class IPAddressModel(BaseModel):
    """IP address Model class"""

    address: IPvAnyInterface
