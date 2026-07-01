#!/usr/bin/env python3
"""
搜尋指定日期嘅最新新聞
用法：python3 search_today_news.py "search query" "20260630"
輸出：JSON 格式嘅新聞列表
"""

import sys
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

SEARX_SCRIPT = Path("/opt/data/searx_html_search.py")

def search_today_news(query, target_date_str):
    """搜尋指定日期嘅新聞"""
    
    # 解析目標日期
    try:
        target_date = datetime.strptime(target_date_str, "%Y%m%d")
    except ValueError:
        print(json.dumps([]))
        return
    
    # 格式化日期用於搜尋同過濾
    date_cn = f"{target_date.month}月{target_date.day}日"
    date_en_short = target_date.strftime("%b %d")  # Jun 30
    date_en_long = target_date.strftime("%B %d")   # June 30
    
    # 搜尋關鍵詞加上日期
    search_query = f"{query} {date_en_long}"
    
    results = []
    
    try:
        cmd = ["python3", str(SEARX_SCRIPT), search_query]
        output = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if output.returncode == 0 and output.stdout.strip():
            items = json.loads(output.stdout)
            
            for item in items:
                title = item.get('title', '').strip()
                url = item.get('url', '')
                content = item.get('content', '')
                img = item.get('img', '')
                
                if not title or not url:
                    continue
                
                results.append({
                    'title': title,
                    'url': url,
                    'content': content[:300] if content else '',
                    'img': img if img else '',
                    'date': target_date_str
                })
                
                if len(results) >= 8:
                    break
                    
    except Exception as e:
        pass
    
    # 如果搵唔到結果，用普通搜尋
    if not results:
        try:
            cmd = ["python3", str(SEARX_SCRIPT), query]
            output = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if output.returncode == 0 and output.stdout.strip():
                items = json.loads(output.stdout)
                
                for item in items:
                    title = item.get('title', '').strip()
                    url = item.get('url', '')
                    content = item.get('content', '')
                    img = item.get('img', '')
                    
                    if not title or not url:
                        continue
                    
                    results.append({
                        'title': title,
                        'url': url,
                        'content': content[:300] if content else '',
                        'img': img if img else '',
                        'date': target_date_str
                    })
                    
                    if len(results) >= 8:
                        break
                        
        except Exception:
            pass
    
    print(json.dumps(results, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps([]))
        sys.exit(1)
    
    query = sys.argv[1]
    target_date = sys.argv[2]
    
    search_today_news(query, target_date)
