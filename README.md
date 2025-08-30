# 人工智能驱动的NASA GCN通告：GCN图数据库建设的前景
以下是关于GCN-graphdb-retriever的介绍
|方法|描述|
|:--:|:--:|
|subject_pipeline|提取GCN相关信息|
|gcn_graph_builder|构建知识图谱|
|langchain_neo4j_connect|根据提问访问知识图谱，并根据提问的自然语言对图谱进行检索反馈|

## 相关参数
### subject_pipeline参数简介
|参数|是否必须|参数描述|参数类型|
|:--:|:--:|:--:|:--:|
|input|true|GCN Circular file path|str|
|output|true|Write file|str|
|llm|false|Large Language Model|str|
|examples|false|Example file used for few shot|str|
|examples-num|false|Number of examples used for few shot|int|
|verbose|false|Use logging output|null|
|error|false|Error log file|str|
|silent-errors|false|Ignore errors|null|

### gcn_graph_builder参数简介
|参数|是否必须|参数描述|参数类型|
|:--:|:--:|:--:|:--:|
|input|true|GCN Circular file path|str|
|verbose|false|Use logging output|null|
|silent-errors|false|Ignore errors|null|

### langchain_neo4j_connect参数简介
|参数|是否必须|参数描述|参数类型|
|:--:|:--:|:--:|:--:|
|url|true|Neo4j's path|str|
|name|true|Neo4j_User name|str|
|password|true|Neo4j's password|str|



## 使用方法讲解
### 通过pip安装
<pre>
pip install GCN-Graphdb-Retriever
</pre>
### 1.直接在代码中进行应用
<pre>
from gcn_graphdb_retriever import subject_KEE_pipeline
from gcn_graphdb_retriever import gcn_graph_builder
from gcn_graphdb_retriever import langchain_neo4j_connect
import os
from dotenv import load_dotenv




def main():
    #subject_KEE_pipeline案例

    in_filepath = "tests/archive.txt.tar.gz"
    out_filepath = "tests/model_test.txt"
    examples_filepath = "tests/subject_parser_examples.json"
    model = "qwen3:14b"
    silent_errors = False
    examples_num = 1
    subject_KEE_pipeline.subject_pipeline(in_filepath, out_filepath, examples_filepath, model, silent_errors, examples_num)

    #gcn_graph_builder案例

    in_filepath = "tests/model_test.txt"
    silent_errors = False
    gcn_graph_builder(in_filepath, silent_errors)

    #langchain_neo4j_connect案例

    load_dotenv()                    # 默认查找当前目录下的 .env
    url = os.getenv("url")
    name = os.getenv("user_name")
    password = os.getenv("password")
    result = langchain_neo4j_connect(url, name, password)

if __name__ == "__main__":
    main()
</pre>

### 2.通过命令行调用
<pre>
ps@ps:~/桌面/Vscode_test/gcn-graphdb-retriever-main(1)/gcn-graphdb-retriever-main$ uv run subject_KEE_pipeline -i tests/archive.txt.tar.gz -o tests/model_test.txt --examples tests/subject_parser_examples.json
</pre>