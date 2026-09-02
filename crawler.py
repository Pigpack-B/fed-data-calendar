import json
import datetime
import requests

# 數據核心字典
INDICATORS = [
    {
        "id": "ism_m",
        "name": "ISM 製造業",
        "icon": "🏭",
        "title": "ISM 製造業採購經理人指數 (PMI)",
        "desc": "景氣榮枯線 50，新訂單與庫存為科技股先行指標。",
        "impact": "科技硬體、半導體供應鏈、景氣循環類股。"
    },
    {
        "id": "nfp",
        "name": "非農 & 失業率",
        "icon": "👷",
        "title": "非農業就業人口 (NFP) & 失業率",
        "desc": "評估美國就業韌性與薪資通膨。",
        "impact": "大盤指數、美債殖利率、降息碼數預期。"
    },
    {
        "id": "cpi",
        "name": "CPI 通膨",
        "icon": "🔥",
        "title": "消費者物價指數 (CPI / 核心 CPI)",
        "desc": "消費端通膨走勢，核心指標決定估值折現率。",
        "impact": "高本益比科技股、美元指數、美債。"
    },
    {
        "id": "retail",
        "name": "零售銷售",
        "icon": "🛒",
        "title": "零售銷售月率 (恐怖數據)",
        "desc": "反映民間消費力道。",
        "impact": "消費電子拉貨、電商板塊。"
    },
    {
        "id": "fomc",
        "name": "FOMC 利率決策",
        "icon": "🏛️",
        "title": "FOMC 利率決策會議",
        "desc": "基準利率與貨幣政策基調。",
        "impact": "全球股債匯所有金融資產。"
    },
    {
        "id": "pce",
        "name": "Core PCE",
        "icon": "📈",
        "title": "核心 PCE 物價指數",
        "desc": "聯準會最看重的 2% 通膨錨定數據。",
        "impact": "確立中長期利率方向、指數評價面上限。"
    }
]

def fetch_latest_macro_data():
    """
    從開放財經日曆或 FRED 抓取已公布之實際數據
    此處以模擬 API 介接邏輯示範真實寫入格式
    """
    now = datetime.datetime.now()
    output_events = []

    # 產生 3 個月份行事曆清單
    for item in INDICATORS:
        # 範例邏輯：若官方已公布，更新真實值與多空判定
        event_entry = {
            "id": item["id"],
            "name": item["name"],
            "icon": item["icon"],
            "title": item["title"],
            "desc": item["desc"],
            "impact": item["impact"],
            "date": "待排定",
            "value": "等待官方公布",
            "status": "待發布",
            "reason": "官方尚未公布最新數據。"
        }
        output_events.append(event_entry)

    return {
        "last_updated": now.strftime("%Y-%m-%d %H:%M:%S"),
        "events": output_events
    }

if __name__ == "__main__":
    data = fetch_latest_macro_data()
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("data.json successfully generated.")
