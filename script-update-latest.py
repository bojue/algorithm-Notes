from bs4 import BeautifulSoup
import requests
import re
import os
import json

pattern = re.compile(r'^(\d+\..+?)\s-\s(.+)$', re.DOTALL)
md_page_content = """
# {title}

## 分类

## 问题描述 

{description}

## 题解

"""

def get_page_description_by_request(response, state):
    if response.status_code == 200 and state == 'description' :
        # 解析页面内容
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('meta', {
            'property':"og:description"
        })
        
        return content.get('content')    
    elif response.status_code == 200 and state == 'code' :
        # 解析页面内容
        soup = BeautifulSoup(response.text, 'html.parser')
        print('soup',soup)
        content = soup.find('meta', {
            'property':"og:description"
        })
        
        return content.get('content')    
    else :
        # 输出错误信息
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        
def get_md_content(content):
    md_content = ''
    matches = pattern.match(content)

    if matches:
       title = matches.group(1)
       description = matches.group()
       md_content = md_page_content.replace('{title}', title).replace('{description}',description)
       return md_content
    
def createFolderAndMdFile(folder, md_content):
    folder_path = 'src/hot-100/' + folder
    readme_path = os.path.join(folder_path, 'README.md')
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            with open(readme_path, 'w') as file:
                file.write(md_content)
                print('文件创建成功')
        else:
            print('文件已经存在', folder)
    except e:
        print('异常', e)

# 获取代码       
def get_code_post():
    url = 'https://leetcode.cn/graphql/'
    
    # csrftoken配置，可以读取配置，也可以独立设置
    cookies = {
        "csrftoken": 'hPx8BxZ8z17plp7uUZFw2AqPiicOyddKGtXCEFbTM9JCPPm9KAo3MxSSvNXxWy5p'
    }
    # Cookie配置，可以读取配置，也可以独立设置
    headers = {
        "Origin": "https://leetcode.cn",
        "content-type": "application/json",
        "Cookie": "gr_user_id=85be60a0-2c7e-4261-a8cf-7a7d977aca8d; a2873925c34ecbd2_gr_last_sent_cs1=bojue; _bl_uid=shlC5thelXd9k5cO1dmXrXIa0dan; csrftoken=hPx8BxZ8z17plp7uUZFw2AqPiicOyddKGtXCEFbTM9JCPPm9KAo3MxSSvNXxWy5p; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1710207219,1711026944; _gid=GA1.2.1149599486.1711026951; __appToken__=; Hm_lvt_f0faad39bcf8471e3ab3ef70125152c3=1710059613,1711026977; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1711127035; a2873925c34ecbd2_gr_session_id=a049ec7a-841b-4754-b571-9315b602a118; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=a049ec7a-841b-4754-b571-9315b602a118; a2873925c34ecbd2_gr_session_id_sent_vst=a049ec7a-841b-4754-b571-9315b602a118; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlx1NjBhOFx1NWRmMlx1N2VjZlx1NzY3Ylx1NTFmYSJdXQ:1rnkDb:00J5Odw-ay7hRCxzk1lx50zdlk_QxMFSWQ7C3GDX-KE; _gat=1; tfstk=fM0Jo42UZICRyxYRbDtmY9LvnFODS4hzHYl1-J2lAxHx3Anl-Lzu9wexLk2W4LyKpfDc-a4SKvBKEx2SpXRzOJMIpJmkmFcrayzBIvLMSb8hfbmnyy6nG3Cl42JMSFcSayzBIdAPiG2_bWaQNu_BlIFTtys5Vvwbc5NGFyaBVYrRlXyjo8QebdeSN-QKaqF72gl7Hw_IkNq8CwwARwgYwjsJnnbWW-ioA44jPKtLlfomFSU9J6FxXja7wv8NzzGsGDZ-JHfaLmhjjonVZQPxyf3L6otCKJqtl44rDdQgCmlIJoGyBGPmAf0ovgPKSVUmrO2TtgOvMMSUVSz6389X7a0IqSeMiYsFYoIaMRAv4MSUVSPYII4cYMrAb; github_state=8vG11WKw; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzE5NDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImI3MDU1NzliNGU1YjQ5ZmI2NTliMzFjOTM1OTI2ODE0ZTE1ZDY0ZWM5MmMyODA2OTI1OTY3Yjk5YTdhNGQ2ZjIiLCJpZCI6MTcxOTQ2LCJlbWFpbCI6IiIsInVzZXJuYW1lIjoiYm9qdWUiLCJ1c2VyX3NsdWciOiJib2p1ZSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNuL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvYm9qdWUvYXZhdGFyXzE1MzQ2Mzc0MjMucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsIl90aW1lc3RhbXAiOjE3MTExMzQzOTAuODQ2MzcyNCwiZXhwaXJlZF90aW1lXyI6MTcxMzcyNjAwMCwidmVyc2lvbl9rZXlfIjowfQ.vtnx0j046sX0_wd4BiEDa9VWVaa-osSRrAeDtLFqGaM; a2873925c34ecbd2_gr_cs1=bojue; _ga=GA1.1.895832374.1710059665; Hm_lpvt_f0faad39bcf8471e3ab3ef70125152c3=1711134427; _ga_PDVPZYN3CW=GS1.1.1711133664.34.1.1711134429.45.0.0"
    }
    # POST请求的数据
    data = {"query":"\n    query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!, $lang: String, $status: SubmissionStatusEnum) {\n  submissionList(\n    offset: $offset\n    limit: $limit\n    lastKey: $lastKey\n    questionSlug: $questionSlug\n    lang: $lang\n    status: $status\n  ) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      title\n      status\n      statusDisplay\n      lang\n      langName: langVerboseName\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      submissionComment {\n        comment\n        flagType\n      }\n    }\n  }\n}\n    ","variables":{"questionSlug":"two-sum","offset":0,"limit":20,"lastKey":'null',"status":"AC"},"operationName":"submissionList"}
    # 发送POST请求
    response = requests.post(url, data=json.dumps(data), headers=headers, cookies=cookies) 
    response_json = json.loads(response.text)
    submissions = response_json['data']['submissionList']['submissions']
    submission_list_success = [item for item in submissions if item['status'] == 'AC']
    print('submission==>\n', submission_list_success)

def getPageUrl(page, type):
    url = 'https://leetcode.cn/problems/{page}/{type}/?envType=study-plan-v2&envId=top-100-liked'
    url = url.replace('{page}', page)
    url = url.replace('{type}', type)
    return url    

def get_page(question):
    print(question['translatedTitle'], question['titleSlug'], question)
    page = question['titleSlug']
    page_description_url = getPageUrl(page, 'description')
    # 根据页面url获取页面描述内容
    request_page_response = requests.get(page_description_url)
    # 获取页面描述部分
    md_content_description = get_page_description_by_request(request_page_response, 'description')
    soup = BeautifulSoup(request_page_response.text, 'html.parser')
    # 查找代码编辑区域的元素
    code_editor = get_code_post()
    md_content = get_md_content(md_content_description) 
    createFolderAndMdFile(page, md_content)


def getQuestions(questions_url): 
  # 问题列表
  questions_list = []
  request_page_response = requests.get(questions_url)
  html_content = request_page_response.text
  # 使用BeautifulSoup解析HTML内容
  soup = BeautifulSoup(html_content, 'html.parser')
  script_tag = soup.find('script', id='__NEXT_DATA__')
  # 提取script标签的内容
  if script_tag:
      script_content = script_tag.string
      json_content = json.loads(script_content)
      planSubGroups = json_content['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['studyPlanV2Detail']['planSubGroups']
      for subGroup in planSubGroups:
        questions = subGroup['questions']
        for question in questions:
          questions_list.append(question)
    
  else:
    print('未找到id为"__NEXT_DATA__"的script标签')
#   for question in questions_list:
  question = questions_list[0]
  get_page(question)  

  
questions_url = 'https://leetcode.cn/studyplan/top-100-liked/' 

# 获取所有的问题
getQuestions(questions_url)
