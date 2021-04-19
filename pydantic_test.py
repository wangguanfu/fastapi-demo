#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "wangguanfu"
from typing import List
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    name: str = "wanggf"
    signup_ts: datetime
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2020-12-22 12:22",
    "friends": [1, 2, "3"],  # "3"是可以int("3")的
}
user = User(**external_data)
print(user.id, user.friends)  # 实例化后调用属性
print(repr(user.signup_ts))
print(user.dict())
