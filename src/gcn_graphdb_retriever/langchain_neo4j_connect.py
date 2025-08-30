from langchain_neo4j import GraphCypherQAChain
from langchain_openai import ChatOpenAI

import os
# from dotenv import load_dotenv


# load_dotenv()                    # 默认查找当前目录下的 .env

# url = os.getenv("url")
# name = os.getenv("user_name")
# password = os.getenv("password")

import argparse
from langchain_neo4j import Neo4jGraph


def langchain_neo4j_connect(url, name, password):
    
    graph = Neo4jGraph(
        url=url,
        username=name,
        password=password
    )
    graph.refresh_schema()  # 刷新图数据库的 schema 信息
    print(graph.schema)

    # 配置LLM
    llm = ChatOpenAI(
        base_url="https://api.deepseek.com/v1",
        api_key=os.environ["DEEPSEEK_API_KEY"],
        model="deepseek-chat",
        temperature=0,
    )

    chain = GraphCypherQAChain.from_llm(
        cypher_llm=llm,
        qa_llm=llm,
        graph=graph,
        verbose=True,
        allow_dangerous_requests=True,
    )

    result = chain.run("元嘉九年发生了几次天文事件")
    return result


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Quick view")
    parser.add_argument("-u", "--url", required=True, type=str, help="Neo4j's path")
    parser.add_argument("-n", "--name", required=True, type=str, help="User name")
    parser.add_argument("--password", required=True, type=str, help="Neo4j's password")
    args = parser.parse_args()

    url = args.url
    name = args.name
    password = args.password
    result = langchain_neo4j_connect(url, name, password)
    print(result)

if __name__ == "__main__":
    main()