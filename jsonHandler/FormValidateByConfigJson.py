#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from enum import Enum

# from main.interfaces.impl.formValidateImpl import FormValidateImpl

REGEXP={
    'date':'([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))'
}

class FormValidateByConfigJson(object):

    jsonData = ''
    formData = ''
    status = False

    def __init__(self, formData, jsonDateName):
        path = os.path.dirname(__file__) + '/../../ticket_template/{0}.json'.format(jsonDateName)
        f = file(path)
        self.jsonData = json.load(f)
        self.formData = formData

    def doValidate(self):
        pass

    def initJsonData(self):
        initDate = {}
        keys = self.jsonData.get('data').keys()
        for key in keys:
            objectJson = self.findJsonObjectByName(key)
            objectJson.get()
        pass


    def findJsonObjectByName(self, name):
        sections = self.jsonData.get('sections')
        for section in sections:
            fields = section.get('fields')
            for field in fields:
                if field.get('name') is None or field.get('name') == '':
                    groups = field.get('groups')
                    for group in groups:
                        if group.get('name') == name:
                            return group

                if field.get('name') == name:
                    return field


class ValidateDomain(object):
    # 如果提交的是一个数组，那么这个数组理论上应该是有长度限制的
    maxSize = 1
    # 非数组情况下值为‘normal’
    objectsType = ObjectTypeEnum.NORMAL
    # 校验的主体
    objects = ''


class ValidateRules(object):
    # 这个type是为了标识我要使用什么样的正则
    type = ''
    # 是否为必须的，是，说明不能为空，否且有数据则需要使用校验规则
    required = False
    # 正则表达式
    regexp = None

    # def __init__(self, type, required = False, regexp = None):



class ObjectTypeEnum(Enum):
    NORMAL = 'normal'
    ARRAY = 'array'




if __name__ == '__main__':
    # fv = FormValidateImpl()
    # fv.isFormAvailabe()
    path = os.path.dirname(__file__) + '/iot_test.json'
    f = file(path)
    jsonData = json.load(f)
    print jsonData.get('data').keys()
    print jsonData.get('sections')[0].get('fields')[1]
