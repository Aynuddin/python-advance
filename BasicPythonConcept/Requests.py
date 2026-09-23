import requests
import json
BASE_URL = "https://jsonplaceholder.typicode.com"
# call the get url using direct hard code path variable
end_points="/posts/2"
response= requests.get(f"{BASE_URL}/{end_points}")
#print(response.status_code)
json_response = response.json()
#print(json_response.get("id"))

# but if you want to pass as path param as runtime or calling time then below
#end_point = f"/post/{post_id}"

def get_Url_Call(post_id):
    end_point = f"/posts/{post_id}"
    endpoint_resp = requests.get(f"{BASE_URL}{end_point}")
    return endpoint_resp
res = get_Url_Call(1)
#print(res.status_code)
#print(res.json()["id"])

# post url
post_body= {
    "userId": 1,
    "id": 11,
    "title": "Python Learning",
    "body": "python using name"
  }
def post_call_url():
    p_end_points="/posts"
    post_response = requests.post(f"{BASE_URL}{p_end_points}", json=post_body, timeout=5)
    return post_response

resp_p = post_call_url()
#print(resp_p.status_code)
#print(resp_p.json())

# passing params in end points
def get_url(post_id):
    qparams = {
        "postId": post_id
    }
    end_p = "/comments"
    response_param = requests.get(f"{BASE_URL}{end_p}", params=qparams , timeout=5)
    return response_param
res_param = get_url(2)
print(res_param.status_code)
print(len(res_param.json()))


