import requests
import os
import concurrent.futures

# إذا تم تحديد API_BASE_URL يتم الاتصال بخادم FastAPI المنفصل،
# وإلا يتم تشغيل الوكلاء مباشرة داخل تطبيق Streamlit (وضع النشر الموحد)
API_BASE_URL = os.getenv("API_BASE_URL", "").rstrip("/")

def call_demographic_agent(record: dict) -> dict:
    try:
        response = requests.post(f"{API_BASE_URL}/agent/demographic", json=record, timeout=60)
        return response.json()
    except Exception as e:
        return {"status": "خطأ", "score": 0, "issues": [str(e)], "notes": "فشل الاتصال بالوكيل الديموغرافي", "agent": "الوكيل الديموغرافي"}

def call_financial_agent(record: dict) -> dict:
    try:
        response = requests.post(f"{API_BASE_URL}/agent/financial", json=record, timeout=60)
        return response.json()
    except Exception as e:
        return {"status": "خطأ", "score": 0, "issues": [str(e)], "notes": "فشل الاتصال بالوكيل المالي", "agent": "الوكيل المالي"}

def call_manager_agent(record: dict) -> dict:
    try:
        response = requests.post(f"{API_BASE_URL}/agent/manager", json=record, timeout=60)
        return response.json()
    except Exception as e:
        return {"status": "خطأ", "trust_score": 0, "issues": [str(e)], "recommendation": "فشل الاتصال بالوكيل القيادي", "agent": "الوكيل القيادي"}

def analyze_record_parallel(record: dict) -> dict:
    """يحلل السجل بتشغيل الوكيل الديموغرافي والمالي بالتوازي"""
    if not API_BASE_URL:
        from agents import analyze_record
        return analyze_record(record)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        demo_future = executor.submit(call_demographic_agent, record)
        fin_future = executor.submit(call_financial_agent, record)
        demo_result = demo_future.result()
        fin_result = fin_future.result()
    manager_result = call_manager_agent(record)
    return {"demographic": demo_result, "financial": fin_result, "manager": manager_result}
