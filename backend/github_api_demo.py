"""
第一周 后端丁 任务：
- 调用 GitHub API 获取仓库信息
- 发送 POST 请求到 httpbin.org
运行方式：python github_api_demo.py
"""
import requests
import json


def get_github_info():
    url = "https://api.github.com/repos/python/cpython"
    print(f"正在请求: {url}")

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None


def send_post_request():
    url = "https://httpbin.org/post"

    post_data = {
        "name": "王晨宁",
        "task": "Python模块学习",
        "language": "Python",
        "framework": "requests",
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "PythonLearningScript",
    }

    print(f"正在发送 POST 请求到: {url}")
    response = requests.post(url, json=post_data, headers=headers, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"POST 请求失败，状态码: {response.status_code}")
        return None


def main():
    print("=" * 50)
    print("Python 模块学习 - API 调用示例")
    print("=" * 50)

    github_data = get_github_info()
    if github_data:
        print("\n[OK] GitHub API 返回数据：")
        print(f"   - 仓库名: {github_data.get('full_name')}")
        print(f"   - 描述: {github_data.get('description', '无')}")
        print(f"   - Stars: {github_data.get('stargazers_count')}")
        print(f"   - 语言: {github_data.get('language')}")

    post_result = send_post_request()
    if post_result:
        print("\n[OK] POST 请求返回数据：")
        print(json.dumps(post_result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
