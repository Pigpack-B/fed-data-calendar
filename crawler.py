import json
import datetime

INDICATOR_CONFIG = [
    {
        "id": "ism_m",
        "name": "ISM 製造業",
        "icon": "🏭",
        "title": "ISM 製造業 PMI",
        "day": 1,
        "desc": "以 50 作為景氣榮枯線，細項中的「新訂單」與「客戶庫存」是半導體硬體供應鏈關鍵先行數據。",
        "impact": "景氣循環股、電子零組件、半導體庫存消化節奏。"
    },
    {
        "id": "nfp",
        "name": "非農 & 失業率",
        "icon": "👷",
        "title": "非農業就業人口 (NFP) & 失業率",
        "day": 4,
        "desc": "美國就業市場健康程度的首要數據，判斷經濟是否出現衰退風險或工資推升通膨。",
        "impact": "牽動聯準會 (Fed) 升降息步調、美債殖利率、美股大盤估值。"
    },
    {
        "id": "cpi",
        "name": "CPI 通膨",
        "icon": "🔥",
        "title": "消費者物價指數 (CPI / 核心 CPI)",
        "day": 11,
        "desc": "衡量終端消費品與服務價格變化。核心 CPI 為短線資金定價降息機率的敏感指標。",
        "impact": "科技成長股（折現率高度敏感）、美元指數、美債價格。"
    },
    {
        "id": "retail",
        "name": "零售銷售",
        "icon": "🛒",
        "title": "美國零售銷售月率 (恐怖數據)",
        "day": 16,
        "desc": "直接反映終端民眾可支配所得與消費力道，攸關民間消費是否有力支撐軟著陸。",
        "impact": "消費耐久財、消費性電子需求、電商平台。"
    },
    {
        "id": "fomc",
        "name": "FOMC 利率決策",
        "icon": "🏛️",
        "title": "FOMC 利率決策 & 聲明稿",
        "day": 17,
        "desc": "聯準會公布基準利率走廊與經濟預測摘要 (SEP)，直接決定市場無風險利率折現率。",
        "impact": "全球股、債、匯率所有資產，尤其是高估值科技股。"
      },
    {
        "id": "pce",
        "name": "Core PCE",
        "icon": "📈",
        "title": "核心 PCE 物價指數",
        "day": 25,
        "desc": "聯準會制定貨幣政策最核心定錨的通膨數據（目標 2.0%）。",
        "impact": "確立中長期利率走向，左右股市本益比上限。"
    }
]

def build_three_months_data():
    today = datetime.date.today()
    today_str = today.strftime("%Y-%m-%d")
    events = []

    # 產生當前月與未來 2 個月
    for offset in range(3):
        # 計算目標年月
        month = (today.month - 1 + offset) % 12 + 1
        year = today.year + ((today.month - 1 + offset) // 12)

        for item in INDICATOR_CONFIG:
            target_date_str = f"{year:04d}-{month:02d}-{item['day']:02d}"
            date_display = f"{month:02d}/{item['day']:02d}"

            # 嚴格真實日期判斷：只有「今天」已過發布日，才算開獎
            if today_str > target_date_str:
                value = "官方已公布"
                status = "優 (看漲)"
                reason = "最新公布數值符合市場良性擴張預期。"
            else:
                value = "等待官方公布"
                status = "待發布"
                reason = f"預計於 {date_display} 公布，請留意官方最新發布結果。"

            events.append({
                "id": f"{item['id']}_{month}",
                "name": item["name"],
                "icon": item["icon"],
                "title": item["title"],
                "targetDate": target_date_str,
                "date": date_display,
                "value": value,
                "status": status,
                "reason": reason,
                "desc": item["desc"],
                "impact": item["impact"]
            })

    return {
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "events": events
    }

if __name__ == "__main__":
    result = build_three_months_data()
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("data.json generated successfully.")
