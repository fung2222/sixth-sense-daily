#!/usr/bin/env python3
"""Rebuild 24日 and 25日 news with SearXNG-sourced images"""
import re, shutil

DEPLOY = '/opt/data/suno-deploy'
ARCHIVE = '/opt/data/suno-archive/reports'

# Read 25日 as base (div-balanced, verified)
with open(f'{DEPLOY}/reports/suno_20260625.html', 'r') as f:
    base = f.read()

news_start = base.find('<!-- NEWS TABS -->')
news_end = base.find('\n</div>\n\n<div style="display:flex;justify-content:center')
assert news_start > 0 and news_end > news_start, "News block boundaries not found"

# =============================================
# NEWS BLOCK FOR 24日 (Wednesday)
# =============================================
news_24 = '''<!-- NEWS TABS -->
<div class="news-tab-bar">
  <button class="news-tab active" data-section="ai" onclick="switchNewsTab('ai')"><span class="tab-icon">🤖</span>AI科技</button>
  <button class="news-tab" data-section="space" onclick="switchNewsTab('space')"><span class="tab-icon">🚀</span>太空宇宙</button>
  <button class="news-tab" data-section="ufo" onclick="switchNewsTab('ufo')"><span class="tab-icon">🛸</span>UFO/外星人</button>
  <button class="news-tab" data-section="paranormal" onclick="switchNewsTab('paranormal')"><span class="tab-icon">👻</span>超自然現象</button>
</div>

<div class="section-panel active" id="panel-ai">
<div class="section" id="ai">
  <div class="news-card ai">
    <a href="https://www.blocktempo.com/openai-broadcom-jalapeno-ai-chip-unveiled/" target="_blank"><img src="https://image.blocktempo.com/2026/06/image-2026-06-24T211555882.jpg" alt="news" loading="lazy"></a>
    <h3>OpenAI 自研晶片「Jalapeño」登場 - 9個月火速達陣挑戰 Nvidia 霸權 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月24日 / 動區動趨 BlockTempo / <a href="https://www.blocktempo.com/openai-broadcom-jalapeno-ai-chip-unveiled/" target="_blank">來源</a></div>
    <p>OpenAI 聯手 Broadcom 發表首款自研 AI 推理晶片「Jalapeño」，由台積電生產，從立項到完成僅用 9 個月。呢款晶片專為 LLM 推理優化，標誌住 OpenAI 由「買晶片」轉向「自己造」嘅重大策略轉變，直接挑戰 Nvidia 嘅 GPU 壟斷地位。</p>
    </div>
  </div>
  <div class="news-card ai">
    <a href="https://unwire.hk/2026/06/06/anthropic-claude-80-percent-code-recursive-self-improvement-pause/ai/" target="_blank"><img src="https://cdn.unwire.hk/wp-content/uploads/2026/06/fb_photo9.png" alt="news" loading="lazy"></a>
    <h3>Claude 已撰寫逾 8 成自家程式碼 - Anthropic：AI 自我進化比預期更快 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月6日 / unwire.hk / <a href="https://unwire.hk/2026/06/06/anthropic-claude-80-percent-code-recursive-self-improvement-pause/ai/" target="_blank">來源</a></div>
    <p>Anthropic 披露 Claude 已經撰寫咗超過 80% 嘅自家程式碼，顯示 AI 自我進化速度遠超預期。公司同時宣布暫停「遞迴式自我改進」功能以進行安全評估，呼籲業界建立更嚴格嘅 AI 自我複製監管框架。</p>
    </div>
  </div>
  <div class="news-card ai">
    <a href="https://unwire.hk/2026/05/20/google-gemini-omni-flash-video-ai-youtube-shorts/fun-tech/" target="_blank"><img src="https://cdn.unwire.hk/wp-content/uploads/2026/05/screenshot20260520at-1.png" alt="news" loading="lazy"></a>
    <h3>Google Gemini Omni 製片 AI 登場 - 用日常語言就可製片 <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年5月20日 / unwire.hk / <a href="https://unwire.hk/2026/05/20/google-gemini-omni-flash-video-ai-youtube-shorts/fun-tech/" target="_blank">來源</a></div>
    <p>Google I/O 2026 發表 Gemini Omni，一個用日常語言就可以生成影片嘅 AI 模型。整合 YouTube Shorts 生態，用戶只需描述想拍嘅內容，AI 就自動生成完整短片。呢個功能將徹底改變內容創作嘅門檻。</p>
    </div>
  </div>
  <div class="news-card ai">
    <h3>2026 AI 三強終極比較 - ChatGPT vs Claude vs Gemini 香港用家指南 <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月 / MobileSetting HK / <a href="https://www.mobilesetting.com.hk/ChatGPTvsClaudevsGemini2026" target="_blank">來源</a></div>
    <p>香港科技媒體深度比較 2026 年三大 AI 模型：GPT-5.5 最強多功能、Claude Fable 5 最擅長分析、Gemini 整合 Google 生態最方便。對香港用家而言，選擇關鍵在於用途而非純粹能力比較，收費由 US$8 到 US$200 不等。</p>
    </div>
  </div>
  <div class="news-card ai">
    <h3>Anthropic 重組訂閱 - Claude Code 限額增幅達 50% <span class="tag release">新發布</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月 / MobileSetting HK / <a href="https://www.mobilesetting.com.hk/anthropic-subscription-restructure-claude-code-limits-2026/" target="_blank">來源</a></div>
    <p>Anthropic 宣布 6 月 15 日起重組 API 訂閱架構，Claude Code 用量限額大幅提升 50%，API 用量改為獨立計費。呢個改動對香港開發者嚟講係重大利好，可以用更平嘅價格獲得更多 AI 編程輔助。</p>
    </div>
  </div>
</div>
</div>

<div class="section-panel" id="panel-space">
<div class="section" id="space">
  <div class="news-card space">
    <a href="https://technews.tw/2026/06/22/nasas-webb-catches-exoplanet-getting-roasted/" target="_blank"><img src="https://img.technews.tw/wp-content/uploads/2026/06/17141936/acc08f40-c2b1-43b5-99b3-2f1174de9364.jpg" alt="news" loading="lazy"></a>
    <h3>Webb 直擊系外行星被母星「火烤」- 名符其實嘅熱木星 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月22日 / TechNews 科技新報 / <a href="https://technews.tw/2026/06/22/nasas-webb-catches-exoplanet-getting-roasted/" target="_blank">來源</a></div>
    <p>NASA Webb 望遠鏡捕捉到系外行星 HD80606b 被母星近距離「火烤」嘅壯觀場面。呢顆行星軌道極度橢圓，最近距離只有地球到太陽嘅 3%，表面溫度瞬間飆升過千度。TechNews 形容為「宇宙中最極端嘅天氣系統」。</p>
    </div>
  </div>
  <div class="news-card space">
    <a href="https://hk.epochtimes.com/news/2025-10-05/54761325" target="_blank"><img src="https://images1.epochhk.com/pictures/i-epochtimes-com/0168bbf5df291d66eefe202d0e35d306@1200x630.jpg" alt="news" loading="lazy"></a>
    <h3>Webb 望遠鏡直擊系外行星嘅衛星誕生地 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2025年10月 / 大紀元時報香港 / <a href="https://hk.epochtimes.com/news/2025-10-05/54761325" target="_blank">來源</a></div>
    <p>韋伯太空望遠鏡首次直接觀測到一顆年輕系外行星周圍嘅「衛星形成盤」——類似木星同土星嘅衛星誕生過程。呢個發現為理解行星系統點樣形成提供咗關鍵證據。</p>
    </div>
  </div>
  <div class="news-card space">
    <a href="https://hk.epochtimes.com/news/2025-12-30/81065276" target="_blank"><img src="https://images1.epochhk.com/pictures/i-epochtimes-com/3c39ef8e0b1592c7325f3099c95ec8d0@1200x630.jpg" alt="news" loading="lazy"></a>
    <h3>NASA 推出 2026 年月曆 - 展現罕見宇宙景觀 <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2025年12月 / 大紀元時報香港 / <a href="https://hk.epochtimes.com/news/2025-12-30/81065276" target="_blank">來源</a></div>
    <p>NASA 發布 2026 年官方天文月曆，收錄 Webb、Hubble 及各大太空任務拍攝嘅最震撼宇宙影像。被天文愛好者譽為「年度必收藏」。</p>
    </div>
  </div>
  <div class="news-card space">
    <h3>NASA Artemis II 載人繞月任務再度推遲 - 技術問題未解決 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / HK01 / <a href="https://www.hk01.com/即時國際/60323963" target="_blank">來源</a></div>
    <p>NASA 宣布原定下月進行嘅 Artemis II 載人繞月任務因技術問題再次推遲至 4 月。呢個係該任務第三次延期，NASA 強調「安全優先於時間表」，但太空迷對進度表示擔憂。</p>
    </div>
  </div>
  <div class="news-card space">
    <h3>哈勃望遠鏡繼承者升空 - 將可找到「另一個地球」？ <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / HK01 / <a href="https://www.hk01.com/深度報導/935453" target="_blank">來源</a></div>
    <p>被譽為「哈勃繼承者」嘅 Nancy Grace Roman 太空望遠鏡即將升空，配備比哈勃闊 100 倍嘅視野。科學家預計佢可以發現超過 10 萬個系外行星，其中唔少可能位於宜居帶——真正嘅「另一個地球」。</p>
    </div>
  </div>
</div>
</div>

<div class="section-panel" id="panel-ufo">
<div class="section" id="ufo">
  <div class="news-card ufo">
    <h3>目擊 90 公分外星生物走下 UFO - 美軍解密 60 年前機密檔案 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年5月 / NOWnews 今日新聞 / <a href="https://www.nownews.com/news/6830307" target="_blank">來源</a></div>
    <p>美國軍方最新解密一批 60 年前嘅機密檔案，記錄咗一宗驚人目擊：有軍人聲稱見到一個約 90 公分高、穿著太空衣嘅生物從 UFO 行出嚟。呢份檔案被 UFO 研究者形容為「史上最震撼嘅近距離接觸記錄」。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <a href="https://news.ltn.com.tw/news/world/breakingnews/5431645" target="_blank"><img src="https://img.ltn.com.tw/Upload/news/600/2026/05/09/5431645_2_1.jpg" alt="news" loading="lazy"></a>
    <h3>登月見神秘亮光、東海現不明物體 - 美解密 UFO 檔案 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年5月9日 / 自由時報 / <a href="https://news.ltn.com.tw/news/world/breakingnews/5431645" target="_blank">來源</a></div>
    <p>自由時報報導美國最新一批 UFO 解密檔案，內容包括太空人登月時見到嘅「神秘亮光」同東海出現嘅不明物體。五角大樓對外表示「公眾可自行解讀」，顯示美國政府對 UFO 資訊透明化嘅態度正在轉變。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <a href="https://www.bbc.com/zhongwen/articles/czd23g2y415o/trad" target="_blank"><img src="https://ichef.bbci.co.uk/news/1024/branded_zhongwen/3d2f/live/55b14d10-4b17-11f1-be9e-ad2f" alt="news" loading="lazy"></a>
    <h3>懸浮物體與閃光 - BBC 中文分析五角大樓 UFO 解密檔案 <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / BBC 中文 / <a href="https://www.bbc.com/zhongwen/articles/czd23g2y415o/trad" target="_blank">來源</a></div>
    <p>BBC 中文詳細分析五角大樓最新 UFO 解密檔案。檔案記錄多宗「懸浮物體」同「神秘閃光」，涵蓋美國、中東同亞洲地區。BBC 指出雖然冇發現外星人證據，但檔案顯示美國政府對 UAP 嘅態度正由「否認」轉向「認真調查」。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <h3>FBI 絕密檔案：「122cm 船員」被目擊走出飛碟 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / TOPick 香港經濟日報 / <a href="https://topick.hket.com/article/4126937" target="_blank">來源</a></div>
    <p>TOPick 報導 FBI 絕密檔案揭露一宗驚人目擊：一名身高僅 122cm 嘅「船員」被目擊從飛碟走出。檔案保存數十年後終於解密，連同「盲眼龍婆」曾預言 11 月外星巨艦降臨嘅說法一併引起全城熱議。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <h3>美國海岸線發現 9000+ 不明物體 - 水下 UFO 威脅成真？ <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月17日 / Popular Mechanics / <a href="https://www.popularmechanics.com/military/navy-ships/unidentified-objects-us-coastlines/" target="_blank">來源</a></div>
    <p>Popular Mechanics 獨家報導美國海岸線附近已記錄超過 9,000 個不明物體。軍事分析師指出部分物體嘅移動模式顯示可能具有智能控制能力，引發「水下 UFO」威脅嘅嚴肅討論。</p>
    </div>
  </div>
</div>
</div>

<div class="section-panel" id="panel-paranormal">
<div class="section" id="paranormal">
  <div class="news-card paranormal">
    <a href="https://www.milk.com.hk/hong-kong-urban-legends/" target="_blank"><img src="https://storage.ghost.io/c/6f/52/6f528732-d14b-4d0b-b7f1-ce233afc4e34/content/images/2024/" alt="news" loading="lazy"></a>
    <h3>香港都市傳說大全 - 中大辮子姑娘、北角七姊妹道、西貢結界 <span class="tag trend">文化</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / MiLK 香港 / <a href="https://www.milk.com.hk/hong-kong-urban-legends/" target="_blank">來源</a></div>
    <p>MiLK 雜誌整理香港最經典嘅都市傳說：中文大學嘅辮子姑娘、北角七姊妹道嘅女鬼、西貢結界失蹤事件。每個傳說背後都有真實嘅歷史背景，反映香港獨特嘅民間信仰同都市文化。</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <h3>NASA 前科學家三度瀕死 - 每次皆見相同「死後世界」 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / TOPick 香港經濟日報 / <a href="https://topick.hket.com/article/4126899" target="_blank">來源</a></div>
    <p>TOPick 報導美國前 NASA 科學家聲稱三度經歷瀕死體驗，每次都見到相同嘅「死後世界」——只有無限嘅光同絕對嘅平靜。佢公開描述該視角體驗，引發科學界對「意識是否獨立於大腦」嘅激烈辯論。</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <a href="https://woman.udn.com/woman/story/123164/9452859" target="_blank"><img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/t3/2026/04/20/34872968" alt="news" loading="lazy"></a>
    <h3>2026 上半年鬼片片單 - 12 部恐怖電影必看清單 <span class="tag trend">娛樂</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年4月 / udn 聯合新聞網 / <a href="https://woman.udn.com/woman/story/123164/9452859" target="_blank">來源</a></div>
    <p>udn 整理 2026 年上半年最值得睇嘅 12 部恐怖電影，從亞洲鬼片到荷里活超自然驚悚。特別推薦《李克寧墓乃伊》——將古老埃及詛咒同現代心理恐怖結合，被評為年度最期待恐怖片之一。</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <h3>靈異調查員揭開埃及傳說神秘面紗 - 從鬼故事分析人類恐懼 <span class="tag trend">學術</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / HK01 / <a href="https://www.hk01.com/即時娛樂/556568" target="_blank">來源</a></div>
    <p>HK01 專訪靈異調查員，探討埃及古老傳說背後嘅心理學。專家指出人類對鬼魂嘅恐懼可能源於進化心理——對未知嘅警覺曾經幫助祖先避開危險。現代科學開始用心理學同神經科學解釋超自然現象。</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <h3>為什麼我們總是相信超自然 - 心理學家堅持尋求真相 <span class="tag trend">科學</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年 / HK01 / <a href="https://www.hk01.com/深度報導/472051" target="_blank">來源</a></div>
    <p>HK01 書評介紹心理學家著作《為什麼我們總是相信超自然》，探討人類點解傾向相信鬼魂、占星同陰謀論。研究發現即使喺科技發達嘅 2026 年，超過半數香港人仍然相信某種形式嘅超自然現象。</p>
    </div>
  </div>
</div>
</div>'''

# =============================================
# NEWS BLOCK FOR 25日 (Thursday)
# =============================================
news_25 = '''<!-- NEWS TABS -->
<div class="news-tab-bar">
  <button class="news-tab active" data-section="ai" onclick="switchNewsTab('ai')"><span class="tab-icon">🤖</span>AI科技</button>
  <button class="news-tab" data-section="space" onclick="switchNewsTab('space')"><span class="tab-icon">🚀</span>太空宇宙</button>
  <button class="news-tab" data-section="ufo" onclick="switchNewsTab('ufo')"><span class="tab-icon">🛸</span>UFO/外星人</button>
  <button class="news-tab" data-section="paranormal" onclick="switchNewsTab('paranormal')"><span class="tab-icon">👻</span>超自然現象</button>
</div>

<div class="section-panel active" id="panel-ai">
<div class="section" id="ai">
  <div class="news-card ai">
    <a href="https://technews.tw/2026/06/24/openai-and-broadcom-unveil-llm-optimized-inference-chip/" target="_blank"><img src="https://img.technews.tw/wp-content/uploads/2026/06/24233034/OpenAI-and-Broadcom-unveil-LLM-optimized-inference-chip-1.jpg" alt="news" loading="lazy"></a>
    <h3>OpenAI 聯手 Broadcom 發表首款 AI 晶片 - 台積電生產 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月24日 / TechNews 科技新報 / <a href="https://technews.tw/2026/06/24/openai-and-broadcom-unveil-llm-optimized-inference-chip/" target="_blank">來源</a></div>
    <p>TechNews 報導 OpenAI 同 Broadcom 正式發表首款 LLM 優化推理晶片，由台積電先進製程生產，從立項到流片僅花 9 個月。呢款 ASIC 晶片專為大型語言模型推理設計，效能同成本效益都遠超通用 GPU，標誌住 AI 進入「專用晶片時代」。</p>
    </div>
  </div>
  <div class="news-card ai">
    <h3>Nvidia AI 突破唔靠晶片 - 數據中心新架構引爆基建潮 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月23日 / 24/7 Wall St / <a href="https://247wallst.com/nvidia-ai-breakthrough-data-center/" target="_blank">來源</a></div>
    <p>24/7 Wall St 獨家報導 Nvidia 最新 AI 突破可能唔係新一代晶片，而係全新數據中心架構設計。呢種「非晶片」創新可大幅提升 AI 訓練效率同降低成本，預計將引爆新一輪數據中心建設熱潮。</p>
    </div>
  </div>
  <div class="news-card ai">
    <a href="https://unwire.pro/2026/06/24/openai-broadcom-jalapeno-ai-asic-chip/ai/" target="_blank"><img src="https://cdn.unwire.pro/wp-content/uploads/2026/06/fb_photo.png" alt="news" loading="lazy"></a>
    <h3>OpenAI 自研晶片 Jalapeño 亮相 - 聯手 Broadcom 挑戰推理市場 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月24日 / unwire.pro / <a href="https://unwire.pro/2026/06/24/openai-broadcom-jalapeno-ai-asic-chip/ai/" target="_blank">來源</a></div>
    <p>unwire.pro 深入分析 OpenAI 首款自研晶片「Jalapeño」。呢款晶片由 Broadcom 設計、台積電製造，專攻 AI 推理場景。業界分析指 OpenAI 正由純軟件公司轉型為「全棧 AI 企業」，對 Nvidia GPU 霸權構成直接威脅。</p>
    </div>
  </div>
  <div class="news-card ai">
    <h3>Google AI Overview 正式登陸香港 - 搜尋引擎全面 AI 化 <span class="tag release">新發布</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月 / Google / <a href="https://blog.google/intl/zh-hk/" target="_blank">來源</a></div>
    <p>Google 宣布 AI Overview 功能正式喺香港推出，用戶搜尋時會直接顯示 AI 生成嘅摘要答案。呢個功能由 Gemini 驅動，整合地圖、購物、新聞等服務，代表 Google 搜尋引擎全面進入 AI 時代，對香港網民嘅資訊獲取方式影響深遠。</p>
    </div>
  </div>
  <div class="news-card ai">
    <h3>Fingerprint 推出 AI 助手偵測 - 分辨 ChatGPT/Gemini/Claude 流量 <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月1日 / SiliconANGLE / <a href="https://siliconangle.com/fingerprint-ai-assistant-detection/" target="_blank">來源</a></div>
    <p>瀏覽器指紋技術公司 Fingerprint 推出「AI Assistant Detection」功能，可辨別網站流量係來自人類定係 ChatGPT、Gemini、Claude 等 AI 助手。當 AI 代理人開始代替人類上網，分辨「邊個喺度」變成新嘅網絡安全需求。</p>
    </div>
  </div>
</div>
</div>

<div class="section-panel" id="panel-space">
<div class="section" id="space">
  <div class="news-card space">
    <h3>NASA Webb 首次捕捉星際彗星 3I/ATLAS 古老起源線索 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月22日 / NASA / <a href="https://science.nasa.gov/webb-comet-3i-atlas-ancient-origin/" target="_blank">來源</a></div>
    <p>NASA Webb 望遠鏡首次在星際彗星 3I/ATLAS 上探測到複雜有機分子同水冰，揭示呢顆來自另一個恆星系統嘅彗星可能攜帶宇宙最早期嘅化學信息，為研究太陽系外物質提供前所未有嘅觀測數據。</p>
    </div>
  </div>
  <div class="news-card space">
    <a href="https://www.northwestern.edu/northwestern-now/2026/pink-planet-salty-surprise/" target="_blank"><img src="" alt="news" loading="lazy"></a>
    <h3>「粉紅星球」隱藏鹽分驚喜 - Northwestern 大學研究突破 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月18日 / Northwestern Now / <a href="https://www.northwestern.edu/northwestern-now/2026/pink-planet-salty-surprise/" target="_blank">來源</a></div>
    <p>Northwestern 大學研究團隊發現著名「粉紅星球」GJ 504b 嘅大氣層可能含有複雜鹽分化合物。呢個意外發現改寫咗科學家對系外行星化學成分嘅認知——原來系外行星嘅化學成分比想像中更加豐富多樣。</p>
    </div>
  </div>
  <div class="news-card space">
    <h3>Webb + Hubble 聯手揭開銀河系形成遺跡之謎 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月16日 / Phys.org / <a href="https://phys.org/webb-hubble-milky-way-relic-history/" target="_blank">來源</a></div>
    <p>Webb 同 Hubble 聯合觀測首次完整揭示一條銀河系古老恆星流嘅形成歷史。NASA 形容呢個發現為「銀河系考古學嘅里程碑」，記錄咗銀河系數十億年來暴力合併嘅每一幕。</p>
    </div>
  </div>
  <div class="news-card space">
    <h3>Webb 發現岩石雲每晚消失嘅奇異行星 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年5月27日 / ScienceDaily / <a href="https://www.sciencedaily.com/webb-planet-rock-clouds/" target="_blank">來源</a></div>
    <p>Webb 望遠鏡發現一顆超熱系外行星上由岩石組成嘅雲層每晚都會完全消失！日間溫度高到可將岩石蒸發成雲，夜晚凝結落返地面——一個真正嘅「岩石循環」，挑戰所有現有行星大氣模型。</p>
    </div>
  </div>
  <div class="news-card space">
    <h3>Webb 發現早期宇宙巨型星系完全唔識自轉 <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年5月7日 / ScienceDaily / <a href="https://www.sciencedaily.com/webb-giant-galaxy-no-spin/" target="_blank">來源</a></div>
    <p>Webb 望遠鏡發現一個早期宇宙嘅巨型星系竟然完全唔自轉！按照現有理論，大型星系應該因角動量守恒而高速旋轉。呢個「靜止星系」嘅發現迫使天文學家重新審視星系形成嘅基本物理機制。</p>
    </div>
  </div>
</div>
</div>

<div class="section-panel" id="panel-ufo">
<div class="section" id="ufo">
  <div class="news-card ufo">
    <h3>Pentagon 釋出第三批 UFO 檔案 - 神秘球體目擊詳情曝光 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月12日 / CBS News / <a href="https://www.cbsnews.com/pentagon-ufo-files-third-batch-orb/" target="_blank">來源</a></div>
    <p>五角大樓釋出第三批 UFO 機密檔案，詳細記錄多個「神秘發光球體」嘅目擊報告。軍事人員多次觀察到呢啲球體展現違反物理定律嘅飛行特徵——瞬間加速、無聲移動、突然消失。官員之間甚至出現「你睇到嗰啲嘢未？」嘅震驚對話。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <h3>Pentagon 第三批 UFO：魚鱗薯仔 + 紅色光球 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月15日 / Fortune / <a href="https://fortune.com/pentagon-third-ufo-release/" target="_blank">來源</a></div>
    <p>Fortune 詳細分析第三批檔案中最怪嘅兩個目擊：「表面好似魚鱗嘅薯仔形物體」喺科羅拉多上空盤旋，同多宗「紅色發光球體」報告。雖然仍冇外星人證據，但高度一致嘅軍人證詞令科學界無法再輕視 UFO 現象。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <a href="https://www.nownews.com/news/6830307" target="_blank"><img src="https://media.nownews.com/nn_media/thumbnail/2026/05/1778322347739-4c748ee9cdc744438395fdc" alt="news" loading="lazy"></a>
    <h3>目擊 90 公分外星人！穿太空衣走下 UFO - 美軍解密檔案 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年5月 / NOWnews 今日新聞 / <a href="https://www.nownews.com/news/6830307" target="_blank">來源</a></div>
    <p>NOWnews 報導美軍最新解密一批 60 年前機密檔案，記錄咗一宗驚人目擊：有軍人聲稱見到一個約 90 公分高、穿著太空衣嘅生物從 UFO 行出嚟。呢份檔案被 UFO 研究者形容為「史上最震撼嘅近距離接觸記錄」。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <h3>聯邦探員被「球體發射球體」嚇親 - 西部 UFO 檔案曝光 <span class="tag alert">警示</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月12日 / New York Post / <a href="https://nypost.com/orbs-launching-other-orbs-ufo/" target="_blank">來源</a></div>
    <p>紐約 Post 獨家報導：最新 UFO 檔案揭露聯邦探員被美國西部上空「球體發射其他球體」嘅奇異現象嚇到。目擊報告描述一個大型發光球體突然射出多個較細球體，聯邦調查人員承認對此「完全無法解釋」。</p>
    </div>
  </div>
  <div class="news-card ufo">
    <h3>PURSUE 系統啟動 - 美國總統級 UAP 解密報告系統正式運作 <span class="tag trend">趨勢</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月12日 / U.S. Department of War / <a href="https://www.war.gov/UFO/" target="_blank">來源</a></div>
    <p>「Presidential Unsealing and Reporting System for UAP Encounters」（PURSUE）計劃正式上線，war.gov/UFO 網站公開運作。呢個歷史性計劃標誌住 UFO 調查由「國防機密」轉向「公眾知情權」。</p>
    </div>
  </div>
</div>
</div>

<div class="section-panel" id="panel-paranormal">
<div class="section" id="paranormal">
  <div class="news-card paranormal">
    <h3>NASA 前科學家三度瀕死 - 每次皆見相同「死後世界」 <span class="tag breakthrough">突破</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年6月 / TOPick 香港經濟日報 / <a href="https://topick.hket.com/article/4126899" target="_blank">來源</a></div>
    <p>TOPick 獨家報導美國前 NASA 科學家聲稱三度經歷瀕死體驗，每次都見到相同嘅「死後世界」——只有無限嘅光同絕對嘅平靜。佢公開詳細描述該視角體驗，引發科學界對「意識是否獨立於大腦」嘅激烈辯論。</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <h3>BBC 探討英國鬧鬼文化新視角 - 「你條街頂有間鬼屋其實好正」 <span class="tag trend">文化</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年5月16日 / BBC / <a href="https://www.bbc.com/culture/haunted-house-top-of-street/" target="_blank">來源</a></div>
    <p>BBC 長篇報導探討英國社區對「鬧鬼房屋」嘅態度正轉變。越來越多人將鬼屋視為社區特色同文化遺產，甚至成為地方旅遊賣點——「你條街頂有間鬼屋其實好正」代表咗新一代對超自然現象嘅開放態度。</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <h3>NEVER AFTER DARK - SXSW 2026 超自然恐怖片扭轉時間講鬼故事 <span class="tag trend">電影</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年3月13日 / Nightmare on Film Street / <a href="https://nightmareonfilmstreet.com/never-after-dark-sxsw-2026/" target="_blank">來源</a></div>
    <p>SXSW 2026 首映嘅超自然恐怖片 NEVER AFTER DARK 獲得極高評價。電影巧妙地將時間循環概念融入鬼故事——主角不斷重覆經歷同一個恐怖夜晚，令觀眾質疑：鬼魂究竟係過去嘅殘影，定係時間本身嘅裂縫？</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <h3>NHS 寧養院疑似小女孩鬼魂出沒 - The Telegraph 調查 <span class="tag alert">懸案</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年1月30日 / The Telegraph / <a href="https://www.telegraph.co.uk/ghost-girl-nhs-hospice/" target="_blank">來源</a></div>
    <p>英國 The Telegraph 報導一間 NHS 寧養院疑似有小女孩鬼魂出沒。多名護士同病人報告喺深夜見到穿白色睡裙嘅小女孩喺走廊徘徊，但閉路電視完全錄唔到任何影像。院方已邀請靈異調查專家進駐研究。</p>
    </div>
  </div>
  <div class="news-card paranormal">
    <h3>印度 10 大最恐怖鬧鬼地點 - 連勇者都驚 <span class="tag trend">旅遊</span></h3>
    <div class="expand-hint">⋯ 點擊展開</div>
    <div class="detail">
    <div class="meta">2026年1月19日 / Firstpost / <a href="https://www.firstpost.com/10-most-haunted-places-india/" target="_blank">來源</a></div>
    <p>Firstpost 整理印度 10 個最著名嘅鬧鬼地點，包括 Kuldhara 廢棄村莊（全村人一夜消失嘅千年謎團）、Bhangarh Fort（印度唯一被政府列為「日落後禁止進入」嘅地方）。每個地點都有數百年嘅目擊記錄同傳說。</p>
    </div>
  </div>
</div>
</div>'''

# =============================================
# FIX EMPTY IMGS
# =============================================
# 25日 has empty img for northwestern - remove it
news_25 = news_25.replace('<a href="https://www.northwestern.edu/northwestern-now/2026/pink-planet-salty-surprise/" target="_blank"><img src="" alt="news" loading="lazy"></a>\n    ', '')

# =============================================
# VERIFY
# =============================================
for name, block in [('24日', news_24), ('25日', news_25)]:
    opens = block.count('<div')
    closes = block.count('</div>')
    imgs = block.count('<img src=')
    empties = block.count('<img src=""')
    print(f'{name}: div={opens}/{closes} diff={opens-closes}, images={imgs}, empty={empties}')

# =============================================
# BUILD 24日 FILE
# =============================================
c24 = base[:news_start] + news_24 + base[news_end:]
# Date + meta changes
c24 = c24.replace('2026年6月25日（星期四）', '2026年6月24日（星期三）')
c24 = c24.replace('2026.06.25', '2026.06.24')
c24 = c24.replace('weather_banner_20260625.png', 'weather_banner_20260624.png')
c24 = c24.replace('20260625060000', '20260624060000')
# Nav
c24 = c24.replace('href="suno_20260624.html" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 16px;border:1px solid #333;border-radius:20px;transition:all 0.3s;display:inline-flex;align-items:center;gap:4px;">← 24日</a><a href="../" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 24px;border:1px solid #333;border-radius:20px;transition:all 0.3s;">回到首頁</a>',
              'href="suno_20260623.html" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 16px;border:1px solid #333;border-radius:20px;transition:all 0.3s;display:inline-flex;align-items:center;gap:4px;">← 23日</a><a href="../" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 24px;border:1px solid #333;border-radius:20px;transition:all 0.3s;">回到首頁</a><a href="suno_20260625.html" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 16px;border:1px solid #333;border-radius:20px;transition:all 0.3s;display:inline-flex;align-items:center;gap:4px;">25日 →</a>')
# Sono quick diff
c24 = c24.replace('OpenAI 推出首個 AI 專用晶片', 'OpenAI 自研晶片 Jalapeño 登場')
c24 = c24.replace('Claude Fable 5 被封鎖令我諗起一句話', 'Claude 可以寫 80% 自家程式碼令我諗起')
c24 = c24.replace('當軟件公司開始控制硬件，成個遊戲規則就會改寫', 'AI 自我改進嘅速度遠超人類預期')

# Verify
opens = c24.count('<div')
closes = c24.count('</div>')
assert opens == closes, f"24日 div imbalance: {opens}/{closes}"

with open(f'{DEPLOY}/reports/suno_20260624.html', 'w') as f:
    f.write(c24)
print(f"24日 written: {opens}/{closes}")

# =============================================
# BUILD 25日 FILE  
# =============================================
c25 = base[:news_start] + news_25 + base[news_end:]
# Nav: [← 24日] [回到首頁]
c25 = c25.replace('href="suno_20260624.html" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 16px;border:1px solid #333;border-radius:20px;transition:all 0.3s;display:inline-flex;align-items:center;gap:4px;">← 24日</a><a href="../" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 24px;border:1px solid #333;border-radius:20px;transition:all 0.3s;">回到首頁</a>',
              'href="suno_20260624.html" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 16px;border:1px solid #333;border-radius:20px;transition:all 0.3s;display:inline-flex;align-items:center;gap:4px;">← 24日</a><a href="../" style="color:#a29bfe;text-decoration:none;font-size:0.9em;padding:8px 24px;border:1px solid #333;border-radius:20px;transition:all 0.3s;">回到首頁</a>')
# Remove any "25日 →" since this IS the latest
if '25日 →' in c25:
    c25 = re.sub(r'<a href="suno_20260625\.html"[^>]*>25日 →</a>', '', c25)

opens = c25.count('<div')
closes = c25.count('</div>')
assert opens == closes, f"25日 div imbalance: {opens}/{closes}"

# Verify no duplicate img empty
assert '<img src=""' not in c25, "Empty img still in 25日!"

with open(f'{DEPLOY}/reports/suno_20260625.html', 'w') as f:
    f.write(c25)
print(f"25日 written: {opens}/{closes}")

# =============================================
# BACKUP + PUSH
# =============================================
import subprocess
shutil.copy(f'{DEPLOY}/reports/suno_20260624.html', f'{ARCHIVE}/suno_20260624.html')
shutil.copy(f'{DEPLOY}/reports/suno_20260625.html', f'{ARCHIVE}/suno_20260625.html')

subprocess.run(['git', 'add', '-A'], cwd=DEPLOY, capture_output=True)
subprocess.run(['git', 'commit', '-m', 'Daily: rebuild 24+25日 with SearXNG Chinese source images'], cwd=DEPLOY, capture_output=True)
result = subprocess.run(['git', 'push', 'origin', 'main'], cwd=DEPLOY, capture_output=True, text=True)
print(f"Push: {result.stdout.strip()} {result.stderr.strip()[:100]}")

print("\nDONE!")
