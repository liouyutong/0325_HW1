# HW1 AIoT System: 溫濕度即時監控系統

這是一個整合「實體感測器」與「模擬感測器」的 AIoT 數據流系統。本專案透過 Flask API 接收數據，並使用 SQLite 存儲，最後透過 Streamlit 打造一個具備「素雅古風」風格的即時數據監測看板。

## 🌟 專案特色
*   **雙重數據源**：支持實體 ESP32 (DHT11) 與 Python 模擬腳本數據上傳。
*   **素雅古風看板**：以「翠綠、楊柳、古風」為核心視覺設計，讓數據展現人文氣息。
*   **即時監控**：自動每 2 秒更新一次數據，並提供完整的歷史趨勢圖表。
*   **數據持久化**：使用輕量級 SQLite 資料庫存儲所有歷史感測紀錄。

## 📂 資料夾結構說明
*   `HW1.ino`: 實體 ESP32 硬體讀取 DHT11 數據並上傳的原始碼。
*   `DIC4/`: 系統核心資料夾
    *   `app.py`: Flask 後端伺服器 (接收感測器資料)。
    *   `streamlit_app.py`: 素雅古風 Streamlit 即時看板。
    *   `sensor_simulator.py`: 本端數據模擬器 (模擬傳送溫濕度資料)。
    *   `aiotdb.db`: 感測數據保存庫 (SQLite)。

## 🚀 如何運行 (模擬環境)
1.  **安裝依賴**：
    ```bash
    pip install flask streamlit pandas
    ```
2.  **啟動模擬器** (開啟一個終端機)：
    ```bash
    python DIC4/sensor_simulator.py
    ```
3.  **啟動看板** (開啟另一個終端機)：
    ```bash
    streamlit run DIC4/streamlit_app.py
    ```
4.  **訪問看板**：瀏覽器開啟 `http://localhost:8501`。

## 👤 開發者
*   **GitHub**: [liouyutong](https://github.com/liouyutong)
