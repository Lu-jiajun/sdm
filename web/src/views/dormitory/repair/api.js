/*
 * @Description:
 * @Author: hongzai
 * @version:
 * @Date: 2022-04-08 12:44:55
 * @LastEditors: hongzai
 * @LastEditTime: 2022-04-08 12:44:55
 */

import { request } from '@/api/service'
export const urlPrefix = '/api/repair_application/'

export function GetList (query) {
  return request({
    url: urlPrefix,
    method: 'get',
    params: query
  })
}

export function AddObj (obj) {
  return request({
    url: urlPrefix,
    method: 'post',
    data: obj
  })
}

export function UpdateObj (obj) {
  return request({
    url: urlPrefix + obj.id + '/',
    method: 'put',
    data: obj
  })
}

export function DelObj (id) {
  return request({
    url: urlPrefix + id + '/',
    method: 'delete',
    data: { id }
  })
}
