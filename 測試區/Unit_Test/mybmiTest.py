import unittest # 匯入測試框架套件
#import coverage # 匯入涵蓋度紀錄套件
import mybmi # 匯入 mybmi.py 內的程式
class TestBMI(unittest.TestCase): # 設計測試驅動程式類別
    def test_computeBMIOK(self): # 設計測試主程式功能的方法，self 是物件本身
        self.assertEqual(mybmi.computeBMI(52, 1.55), 21.64) # assertEqual(執行結果, 期望結果)

        self.assertEqual(mybmi.computeBMI(52, 0.05), -1)
        self.assertEqual(mybmi.computeBMI(2, 1.55), -1)
        self.assertEqual(mybmi.computeBMI(500, 5), -1)

        # self.assertEqual(mybmi.computeBMI(500, 1.55), -1)

# 撰寫測試 驅動程式