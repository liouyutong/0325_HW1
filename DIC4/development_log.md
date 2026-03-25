# AIoT HW1 系統開發日誌 (Development Log)

**專案名稱**：溫濕度即時監控系統 (古風楊柳版)
**開發者**：liouyutong
**完成日期**：2026-03-25
**GitHub 連結**：[https://github.com/liouyutong/0325_HW1](https://github.com/liouyutong/0325_HW1)
**Live Demo**：[https://0325hw1-asdzfsjlaxuvvxncxyj6bm.streamlit.app/](https://0325hw1-asdzfsjlaxuvvxncxyj6bm.streamlit.app/)

---

## 🛠️ 技術棧 (Stack)
*   **硬體端/模擬端**：ESP32 (HW1.ino) / Python Simulator (sensor_simulator.py)
*   **傳輸協議**：HTTP POST
*   **後端/資料庫**：Flask API + SQLite3 (aiotdb.db)
*   **視覺化看板**：Streamlit + CSS + SVG Animation

---

## 📝 開發歷程摘要

### 第一階段：環境整理與檔案重構
*   分析了工作區內的文件結構，確認了 `DIC4` 為核心專案資料夾。
*   清理了過時的測試腳本 (`a.py`, `view_db.py`) 與冗餘資料庫。
*   保留關鍵檔案 `HW1.ino`（實體硬體端程式）與 `DIC4/` 資料夾。

### 第二階段：視覺美化 (素雅古風)
*   應要求將 Streamlit 看板進行風格改造。
*   **色彩配置**：採用「翠綠」主題，搭配淺綠絲綢質感背景與深綠宋體文字。
*   **動態特效**：使用 SVG 與 CSS `@keyframes` 製作了「楊柳依依」動畫，柳枝會在頁面兩側輕輕晃動，營造古風氛圍。

### 第三階段：GitHub 版本管理
*   在本地初始化 Git 儲存庫，並建立 `.gitignore`（排除資料庫與快取）。
*   將所有原始碼推送到 GitHub 儲存庫 `liouyutong/0325_HW1`。
*   擷取高品質看板截圖並更新至 README 檔案中。

### 第四階段：雲端部署與即時更新優化
*   協助將專案部署至 Streamlit Cloud。
*   **除錯與初始化**：針對雲端資料庫 `404` 或 `no such table` 錯誤，在 `streamlit_app.py` 內建了自動初始化功能 (init_db)。
*   **動態更新優化**：為了讓 Live Demo 也具備即時跳動感，修改了資料讀取邏輯，讓網頁在每次刷新時自動產生一筆隨機模擬數據。

---

## ✅ 最終成果清單
*   [x] 模擬感測數據流
*   [x] 實體 ESP32 程式碼備份
*   [x] 自動化資料庫初始化與模擬填充
*   [x] 高質感古風視覺設計
*   [x] GitHub 完整代碼上傳
*   [x] 成功部署並優化 Live Demo
*   [x] README 說明文件與截圖預覽

---
**開發工具**：Antigravity AI Coding Assistant (Google DeepMind)
