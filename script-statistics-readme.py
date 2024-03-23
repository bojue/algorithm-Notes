import os
import re

# 算法分类目录
folder_path = "src/hot-100"
# 题目总数
total = 100
# 输出MD文件名称
output_path = './README.md'
# 文件标题
md_header = 'Algorithm'
# 文件标题描述
md_header_description = """

## 构建脚本

`Bojue` 前端算法笔记

### 1. 根据题目自动创建题目（手动更新）

场景：完成题目，根据题目名称创建对应的题目笔记


```shell

# mac上执行
# window要自测

python3 script-create-readme.py
```


### 2. 更新最新的数据（自动更新）

场景：习题题解更新，可以执行全部更新算法笔记，获取全部的最新笔记内容，题解只获取最新通过的题目


1. 配置config.json，统计leetcode接口需要

```shell

{
  "csrftoken": "",
  "Cookie": ""
}
```


2. 执行统计脚本


```shell

# mac上执行
# window要自测

python3 script-update-latest.py
```



### 3. 更新统计README

场景：更新完毕题目笔记，更新最新的统计数据

```shell

# mac上执行
# window要自测

python3 script-statistics-readme.py
```

## 题目统计

"""


files = os.listdir(folder_path)

def get_md_first_header(content):
  pattern = r'^#\s+(.*)$'
  match = re.search(pattern, content, re.MULTILINE)
  if match:
    return match.group(1)
  else:
    return None

# 获取文档动态内容
def get_md_dy_content_by_path(folder_path, files):
  # MD文档动态内如生成
  md_content = '\n'
  for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    isDir = os.path.isdir(file_path)
    isFile = os.path.isfile(file_path)
  
    if isDir:
      file = folder_path +'/'+ file_name +'/'+"README.md"
      isExists = os.path.exists(file)
      if not isExists:
        continue
      md_file_path = os.path.join(file)
      md_file = open(md_file_path, 'r') 
      md_line = md_file.read()
      md_content_line = '[' + get_md_first_header(md_line)  +'](' + md_file_path+ ')\n\n'
      md_content += md_content_line
  
  return md_content

# 获取统计数据
def get_statistical_data(): 
  data = ''
  dir_len = len(files)
  data = '\n\n统计数据 => 总数量：<font color="#336df4" >'+ str(total)+'</font>  , 已经完成 <font color="#1dddae" >'+ str(dir_len) + '</font> , 百分比例 <font color="#1dddae" >' + str(dir_len % total) + '%</font>\n\n'
  data += '## 题目列表'
  return data
  
  
# 获取md文档内容
def get_md_content(): 
  # md文档内容
  md_content = ''
  md_header_content = "# " + md_header + '\n' + md_header_description + '\n'
  md_statistical = get_statistical_data()
  md_dy_content = get_md_dy_content_by_path(folder_path, files)
  
  # 完成内容拼装
  md_content = md_header_content + md_statistical +  md_dy_content
  
  return md_content


# 更新markdown内容 
def update_readme_md(file_path, content):
  if os.path.isfile(file_path):
    with open(file_path, 'w') as file:
          file.write(content)
  else:
      with open(file_path, 'x') as file:
          file.write(content)
  
def run():
  content = get_md_content()
  update_readme_md(output_path, content)
  
run()


