# coding=utf-8
from utils.def_ import *
import pyautogui
import pyperclip


def 扫描上传程序():
    pyautogui.PAUSE = 1.5
    # 打开客户端
    pyautogui.hotkey('winleft', 'r')
    sleep(2)
    pyperclip.copy(r'D:\扫描客户端\IntegrationScan.exe')
    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(10)

    # 客户端登录
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(15)

    # 模板制作
    pyautogui.click(x=1100, y=530)
    sleep(1)

    # 科目一
    pyautogui.click(x=675, y=336)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.click(x=1340, y=405)
    pyautogui.click(x=1450, y=455)
    pyautogui.press('enter')
    sleep(3)

    # 双面试卷
    pyautogui.press('shiftleft')
    pyautogui.typewrite(
        r'D:\PyCharm\File\Template\Chinese\"IMdl_4812_1.tif" "IMdl_4812_2.tif" ')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(x=1440, y=560)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(x=1440, y=605)
    sleep(2)

    # 模板编辑
    # 定位文字
    pyautogui.moveTo(730, 240)
    pyautogui.dragTo(755, 255, 0.5, button='left')
    pyautogui.moveTo(727, 359)
    pyautogui.dragTo(777, 373, 0.5, button='left')
    pyautogui.moveTo(1130, 605)
    pyautogui.dragTo(1200, 618, 0.5, button='left')
    sleep(2)
    pyautogui.moveTo(1135, 415)
    pyautogui.dragTo(1200, 428, 0.5, button='left')
    pyautogui.moveTo(1148, 440)
    pyautogui.dragTo(1165, 471, 0.5, button='left')
    pyautogui.moveTo(1285, 710)
    pyautogui.dragTo(1354, 722, 0.5, button='left')
    sleep(2)
    # 准考证识别
    pyautogui.click(x=485, y=168)
    pyautogui.moveTo(900, 205)
    pyautogui.dragTo(1130, 370, 0.5, button='left')
    sleep(1)

    # 客观题填涂区
    pyautogui.moveTo(759, 382)
    pyautogui.dragTo(806, 435, 0.5, button='left')
    pyautogui.moveTo(824, 382)
    pyautogui.dragTo(850, 435, 0.5, button='left')
    pyautogui.moveTo(868, 382)
    pyautogui.dragTo(913, 435, 0.5, button='left')
    pyautogui.moveTo(932, 382)
    pyautogui.dragTo(980, 435, 0.5, button='left')
    pyautogui.moveTo(760, 468)
    pyautogui.dragTo(818, 521, 0.5, button='left')
    pyautogui.moveTo(759, 382)
    pyautogui.dragTo(806, 426, 0.5, button='left')
    pyautogui.moveTo(824, 382)
    pyautogui.dragTo(850, 406, 0.5, button='left')

    # 客观题题目区
    pyautogui.moveTo(736, 375)
    pyautogui.dragTo(1083, 525, 0.5, button='left')

    # 主观题
    pyautogui.moveTo(735, 461)
    pyautogui.dragTo(1083, 605, 0.5, button='left')
    pyautogui.moveTo(735, 627)
    pyautogui.dragTo(1083, 695, 0.5, button='left')
    pyautogui.moveTo(1143, 197)
    pyautogui.dragTo(1490, 327, 0.5, button='left')
    pyautogui.moveTo(1142, 331)
    pyautogui.dragTo(1490, 683, 0.5, button='left')
    pyautogui.click(x=620, y=170)
    pyautogui.moveTo(735, 198)
    pyautogui.dragTo(1086, 675, 0.5, button='left')
    pyautogui.moveTo(1142, 198)
    pyautogui.dragTo(1490, 409, 0.5, button='left')
    pyautogui.moveTo(1140, 415)
    pyautogui.dragTo(1490, 623, 0.5, button='left')
    # 保存模板
    pyautogui.click(x=490, y=510)
    sleep(5)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(x=914, y=190)
    pyautogui.press('down')
    pyautogui.press('enter')

    # 科目二
    pyautogui.click(x=1450, y=455)
    pyautogui.press('enter')
    sleep(3)

    # 双面试卷
    pyautogui.typewrite(
        r'D:\PyCharm\File\Template\Math\"IMdl_4956_1.tif" "IMdl_4956_2.tif" ')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(x=1440, y=560)
    pyautogui.press('enter')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(x=1440, y=605)
    sleep(2)

    # 模板编辑
    pyautogui.click(x=456, y=285)
    # 定位文字
    pyautogui.moveTo(890, 205)
    pyautogui.dragTo(917, 227, 0.5, button='left')
    pyautogui.moveTo(800, 300)
    pyautogui.dragTo(844, 317, 0.5, button='left')
    pyautogui.moveTo(730, 391)
    pyautogui.dragTo(777, 405, 0.5, button='left')
    sleep(2)
    pyautogui.moveTo(722, 197)
    pyautogui.dragTo(751, 253, 0.5, button='left')
    pyautogui.moveTo(723, 430)
    pyautogui.dragTo(800, 451, 0.5, button='left')
    pyautogui.moveTo(1100, 560)
    pyautogui.dragTo(1140, 595, 0.5, button='left')
    sleep(2)
    # 准考证识别
    pyautogui.click(x=485, y=168)
    pyautogui.moveTo(930, 235)
    pyautogui.dragTo(1165, 383, 0.5, button='left')
    sleep(1)

    # 客观题
    pyautogui.moveTo(761, 415)
    pyautogui.dragTo(813, 476, 0.5, button='left')
    pyautogui.moveTo(834, 415)
    pyautogui.dragTo(863, 476, 0.5, button='left')
    pyautogui.moveTo(884, 415)
    pyautogui.dragTo(938, 476, 0.5, button='left')
    pyautogui.moveTo(957, 415)
    pyautogui.dragTo(1010, 476, 0.5, button='left')
    pyautogui.moveTo(760, 512)
    pyautogui.dragTo(798, 573, 0.5, button='left')
    pyautogui.moveTo(736, 409)
    pyautogui.dragTo(1130, 575, 0.5, button='left')

    # 主观题
    pyautogui.moveTo(735, 601)
    pyautogui.dragTo(1130, 650, 0.5, button='left')
    pyautogui.moveTo(735, 675)
    pyautogui.dragTo(1130, 771, 0.5, button='left')
    pyautogui.click(x=620, y=170)
    pyautogui.moveTo(733, 450)
    pyautogui.dragTo(1130, 590, 0.5, button='left')
    pyautogui.moveTo(732, 609)
    pyautogui.dragTo(928, 633, 0.5, button='left')
    pyautogui.moveTo(920, 609)
    pyautogui.dragTo(1127, 631, 0.5, button='left')
    pyautogui.moveTo(732, 630)
    pyautogui.dragTo(927, 659, 0.5, button='left')
    pyautogui.moveTo(923, 629)
    pyautogui.dragTo(1128, 661, 0.5, button='left')
    # 保存模板
    pyautogui.click(x=490, y=510)
    sleep(5)
    pyautogui.press('enter')
    pyautogui.click(x=1525, y=150)
    pyautogui.click(x=1484, y=281)
    print('模板制作完毕')

    # 答题卷扫描
    pyautogui.click(x=747, y=535)

    # 扫描科目一
    pyautogui.doubleClick(x=625, y=353)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.doubleClick(x=747, y=394)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.doubleClick(x=955, y=471)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(x=978, y=252)
    pyautogui.click(x=880, y=605)
    pyautogui.click(x=880, y=640)
    pyautogui.click(x=900, y=655)
    pyautogui.click(x=900, y=690)
    pyautogui.press('enter')
    pyautogui.press('enter')
    sleep(210)
    pyautogui.click(x=1297, y=265)
    pyautogui.click(x=967, y=218)

    # 扫描科目二
    pyautogui.doubleClick(x=950, y=490)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(x=978, y=252)
    pyautogui.click(x=900, y=675)
    pyautogui.press('enter')
    pyautogui.press('enter')
    sleep(120)
    pyautogui.click(x=1297, y=265)

    # 上传试卷
    pyautogui.click(x=800, y=238)
    sleep(3)
    pyautogui.click(x=1252, y=256)
    pyautogui.click(x=1185, y=372)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.rightClick(x=1185, y=372)
    pyautogui.click(x=1220, y=384)
    pyautogui.click(x=562, y=250)
    sleep(1)
    pyautogui.doubleClick(x=1253, y=252)
    pyautogui.click(x=1185, y=372)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.rightClick(x=1185, y=372)
    pyautogui.click(x=1220, y=384)
    pyautogui.click(x=562, y=250)
    pyautogui.click(x=845, y=270)
    pyautogui.press('enter')
    sleep(50)
    pyautogui.click(x=1540, y=145)
    sleep(2)
    pyautogui.click(x=1514, y=177)
    sleep(2)
    pyautogui.click(x=1350, y=335)
    pyautogui.press('enter')
    print('扫描上传完毕')


if __name__ == '__main__':
    扫描上传程序()
