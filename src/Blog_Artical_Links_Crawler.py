#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_user_blog_url():
    """Get user's blog URL and ensure it ends with /archives/
    获取用户输入的博客地址并确保以/archives/结尾"""
    user_url = input("Please enter your blog URL (e.g. https://example.com/): \n请输入您的博客地址(例如 https://example.com/): ").strip()
    
    # Ensure URL ends with /
    # 确保URL以/结尾
    if not user_url.endswith('/'):
        user_url += '/'
    
    # Check if archives path already exists
    # 检查是否已有archives路径
    if not user_url.endswith('archives/'):
        user_url += 'archives/'
    
    return user_url

def get_output_filename():
    """Get output filename from user or use default
    获取用户指定的输出文件名或使用默认值"""
    default_name = "blog_articles.md"
    user_input = input(f"Enter output filename (default: {default_name}): \n请输入输出文件名(默认: {default_name}): ").strip()
    return user_input if user_input else default_name

def fetch_archive_links(url):
    """Fetch all article links from archive page
    从归档页面获取所有文章链接"""
    try:
        print("Fetching blog content...\n正在获取博客内容...")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Match URLs containing dates (for articles)
            # 匹配包含日期的URL(文章链接)
            if '/20' in href and href.count('/') >= 5:
                full_url = urljoin(url, href)
                title = link.get_text(strip=True)
                if title:
                    results.append((title, full_url))
        
        # Remove duplicates
        # 去重处理
        return list({v[1]:v for v in results}.values())
        
    except requests.RequestException as e:
        print(f"Failed to fetch blog content: {e}\n获取博客内容失败: {e}")
        return []

def save_to_markdown(data, filename):
    """Save links to markdown file
    将链接保存为Markdown文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Blog Archive Links\n# 博客文章链接\n\n")
        for title, link in data:
            f.write(f"- [{title}]({link})\n")
    print(f"Saved to {filename}\n已保存到 {filename}")

if __name__ == "__main__":
    print("Blog Article Links Crawler\n博客文章链接爬取工具")
    blog_url = get_user_blog_url()
    output_file = get_output_filename()
    print(f"Processing: {blog_url}\n正在处理: {blog_url}")
    
    links = fetch_archive_links(blog_url)
    
    if links:
        save_to_markdown(links, output_file)
        print("Done! Check the output file.\n处理完成! 请查看输出文件。")
    else:
        print("No article links found. Please check the URL or site structure.\n没有找到文章链接，请检查博客地址或网站结构。")
