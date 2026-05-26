class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""                                       # ① 準備空字串裝答案
                                                       #    └ 因為要「累積」字元，所以從空的開始

        for i in range(len(strs[0])):                  # ② 一個位置一個位置往下檢查
                                                       #    └ 用第一個字串的長度當上限，
                                                       #      因為公共前綴不可能比它還長

            for s in strs:                             # ③ 每個位置上，比對所有字串
                                                       #    └ 確認「這個位置」每個字串是否都一樣

                if i == len(s) or s[i] != strs[0][i]:  # ④ 兩種停止情況，任一發生就停
                                                       #    ├ 左邊：i == len(s)
                                                       #    │   └ 某個字串「太短了，用完字元」
                                                       #    │     ⚠️ 必須先檢查，否則 s[i] 會炸
                                                       #    └ 右邊：s[i] != strs[0][i]
                                                       #        └ 某個字串「跟第一個對不上」
                                                       #    💡 用 or 的「短路」特性：
                                                       #       左邊 True 就不執行右邊，避免越界

                    return res                         # ⑤ 任一情況發生 → 立刻回傳目前答案
                                                       #    └ 用 return 直接結束函式，省略後面所有檢查

            res += strs[0][i]                          # ⑥ 內層迴圈跑完都沒 return → 全部對得上
                                                       #    └ 把這個字元加進答案，繼續下一個位置
                                                       #    💡 用 strs[0][i] 是因為大家都一樣，
                                                       #       拿哪個字串的字元都行，慣例用第 0 個

        return res                                     # ⑦ 外層迴圈跑完都沒 return
                                                       #    └ 代表第一個字串就是大家的公共前綴
                                                       #      例如 ["flow", "flower"] → 回傳 "flow"