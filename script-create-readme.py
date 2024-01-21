from bs4 import BeautifulSoup
import requests
import re
import os


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
        
    

def get_page(page):
    url = 'https://leetcode.cn/problems/{page}/description/?envType=study-plan-v2&envId=top-100-liked'
    page_url = url.replace('{page}', page)
    # 根据页面url获取页面内容
    request_page_response = requests.get(page_url)
    
    print(page_url)
    # 获取页面描述部分
    md_content_description = get_page_description_by_request(request_page_response, 'description')
    
    print(md_content_description, md_content_description)
    # 获取 Markdown 内容部分
    md_content = get_md_content(md_content_description) 

    createFolderAndMdFile(page, md_content)

def run(page_array): 
    for page in page_array:
        get_page(page)
        

page_array = ['lowest-common-ancestor-of-a-binary-tree']      
run(page_array)