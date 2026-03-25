# 專案開發對話紀錄總結 (AIoT DHT11 System)

本紀錄詳細記錄了從 2026-03-24 開始的所有開發對話與專案演進。

---

### 📝 2026-03-24 10:54 - 最初需求：Flask 與資料庫
**使用者請求：**  
> generate a flask web that insert a random number using pymysql library into SQL ite database every 3 second. Database has id, humid, temp and time as its fileds.

**實作內容：**  
- 建立了 `app.py` 搭配 Flask 與 `sqlite3`。
- 設計了第一個版本的儀表板。
- 設置了背景執行緒（Threading）每 3 秒自動插入模擬數據。

---

### 📝 2026-03-24 10:58 - 修改要求：MySQL 與資料表名稱
**使用者請求：**  
> create a mysql table names sensors, which has 4 fileds : id (auto increment, primary key) ... please also insert into the table with 30 random numbers

**實作內容：**  
- 準備了針對 MySQL 的 `test_mysql.py` 測試連線腳本。
- 嘗試整合 `pymysql`。

---

### 📝 2026-03-24 10:59 - 回歸 SQLite 與 30 筆預設數據
**使用者請求：**  
> create a sqlite table names sensors, which has 4 fileds : id (auto increment, primary key) ... please also insert into the table with 30 random numbers

**實作內容：**  
- 建立了 `setup_db.py` 腳本，手動預填 30 筆歷史數據以供展示圖表。
- 更新 `app.py` 支援 `sensors` 命名。

---

### 📝 2026-03-24 11:06 - 視覺強化：Highcharts 整合
**使用者請求：**  
> 1 give me flask web that generate 20 random numbers and use highcharts to show. 2 use python-highcharts library add. 3. add function show() that shows a pie chart example

**實作內容：**  
- 安裝 `python-highcharts` 並解決了 Python 3.10+ 的兼容性錯誤（ImportError: Iterable）。
- 建立了 `highcharts_app.py` 呈現柱狀圖與圓餅圖（Pie Chart）。

---

### 📝 2026-03-24 11:15 - 統一專案架構：Streamlit (HW1)
**使用者請求：**  
> 我統整一夏這次作業的內容吧，請統一修改程式，並更改成正確的檔名... 1. Generate DHT11 simulated sensor signals with random numbers every 2 seconds, insert into SQLite3 database aiotdb.db, in the table sensors. 2. Visualize temperature and humidity data using Streamlit.

**實作內容：**  
- 全面改用 **Streamlit** 架構（`streamlit_app.py`）。
- 建立專屬隨機生成器 `sensor_simulator.py` 每 2 秒寫入 `aiotdb.db`。
- 實現了動態監控儀表板。

---

### 📝 2026-03-24 11:18 - 藝術風格：素雅古風 (Zen Style)
**使用者請求：**  
> 現在要的資料都很完美的了，可以把版面設成素雅古風的感覺嗎

**實作內容：**  
- 在 `streamlit_app.py` 注入大量自訂 CSS。
- 背景改為米白色宣紙質感，字體改為襯線墨黑色體。
- 重新設計卡片外框呈現「雅致古樸」的東方美學風格。

---

### 📝 2026-03-24 11:21 - 檔案清理建議
**使用者請求：**  
> 我有哪些程式是不需要的嗎?有沒有可以刪掉的?

**實作內容：**  
- 協助分辨目前保留的最核心檔案（`streamlit_app.py`, `sensor_simulator.py`, `aiotdb.db`）。
- 提供清理名單（`app.py`, `highcharts_app.py`...等過渡期檔案）。

---

### 📝 2026-03-24 11:22 - 最終總結與內容回顧
**使用者請求：**  
> 請總結一下我們至今的對話 / 請稍微給我我們彼此對話的實際內容 / 將對話紀錄存成檔案。

**實作內容：**  
- 生成本紀錄檔。

---
*本系統由 AI 協助開發，已完成 2026-03-24 之 AIoT HW1 核心需求與進階風格美化任務。*
