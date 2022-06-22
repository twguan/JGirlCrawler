# Judge Girl 成績html 爬蟲

## 步驟
1. 到ntu cool上的「成績」頁面取得標準檔案格式(.csv)
1. 將檔案轉為.xlsx (此檔案以下用**學生檔案**代稱)
1. 將**學生檔案**以學號順序作排序
1. 在`excel_path`、`save_path`分別輸入**學生檔案**位置和欲儲存的成績檔案位置
    ![](https://i.imgur.com/F0OYYlO.png)
1. 輸入judge girl分數版的檔案位置
    ![](https://i.imgur.com/K4spuWz.png)

即可得到excel版本的學生成績

## 注意事項
* 從cool上取得的標準檔案格式轉檔後應該會和下圖相似
![](https://i.imgur.com/mevEqIX.png)

* 請確保第一位學生由第4行開始
* 程式輸出後的excel並非符合cool的格式，請擷取成績的部分即可