from pytrends.request import TrendReq
import random

pytrend_request = TrendReq(hl="ja-jp", tz=540)

#後々データベースから取得
words = ["アニメ","映画","旅行","カフェ","アーティスト","PS4"]
word =  random.choice(words)


# キーワード一覧
keywords = [word]

# 検索範囲の日付
start_date, end_date = "2022-2-10T00", "2022-2-17T00"

# 検索リクエストのビルド
pytrend_request.build_payload(kw_list=keywords, timeframe=f"{start_date} {end_date}", geo="JP")

# 指定したキーワードの関連キーワード情報を取得する
related_keywords_info = pytrend_request.related_queries()

# に関連するトップキーワードの情報を取得する
related_top_keywords_table = related_keywords_info[word]["rising"]

print("検索ワード"+str(keywords))
print("検索結果は")
print(related_top_keywords_table.values)
print("トップトレンドは")
print(related_top_keywords_table.values[0][0])
print("↓がgoogle検索url")
print("https://www.google.com/search?q="+related_top_keywords_table.values[0][0]+"&rlz=1C1FQRR_jaJP938JP938&oq="+related_top_keywords_table.values[0][0]+"&aqs=chrome..69i57j0i4i131i433i512j0i67i131i433j0i4i131i433i512j0i67l2j0i131i433i512l2j0i4i131i433i512j0i67.748j0j15&sourceid=chrome&ie=UTF-8")