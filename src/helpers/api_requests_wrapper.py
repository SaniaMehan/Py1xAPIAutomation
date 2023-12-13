# request wrapper is to make the post,put, patch, delete, get

#HTTPS methods = generic functions

import json

import requests


def get_requests(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_requests(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


def patch_requests(url, headers, auth, payload, in_json):
    patch_response_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def put_requests(url, headers, auth, payload, in_json):
    put_response_data = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data


def delete_requests(url, headers, auth, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data




# in get auth is not required
# data = get_request("https://restfulbooker.com/booking/1", in_json= False)
# data -> In return json response if in json is true, normal response if in json != True

# httpsapp.vwo.com , in this auth is required so that we are using auth
# Because these are generic functions we can use in any test cases.

# if XML data then convert into-> json Data
