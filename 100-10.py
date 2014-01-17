__author__ = 'rui'
#coding=utf-8

class Converter:
    convertMap = [["长度", [[25.4, "英寸", "毫米"],
                          [30.5, "英尺", "厘米"],
                          [1.61, "英里", "公里"],
                          [0.914, "码", "米"],
                          [201, "浪", "米"]]],

                  ["重量", [[28.3, "盎司", "克"],
                          [454, "磅", "克"],
                          [6.35, "石", "千克"],
                          [1.02, "吨", "公吨"]]],

                  ["力", [[4.45, "磅力", "牛顿"],
                         [0.100, "千牛", "吨力"]]],

                  ["面积", [[6.45, "平方英寸", "平方厘米"],
                          [929, "平方英尺", "平方厘米"],
                          [0.836, "平方码", "平方米"],
                          [2.59, "平方英里", "平方公里"],
                          [0.405, "英亩", "公顷"]]],

                  ["体积", [[16.4, "立方英寸", "立方厘米"],
                          [0.0283, "立方英尺", "立方米"],
                          [0.765, "立方码", "立方米"],
                          [0.34, "蒲式耳", "立方米"]]],

                  ["容积", [[28.4, "液体盎司", "毫升"],
                          [568, "品脱", "毫升"],
                          [4.55, "加仑", "升"]]], ]
    unitMap = {}
    """
    温度转换
    """

    def __init__(self):
        for k, v in enumerate(self.convertMap):
            for m, n in enumerate(v[1]):
                self.unitMap[n[1]] = [n[0], n[2]]
                self.unitMap[n[2]] = [1 / n[0], n[1]]

    def C2F(self, c):
        return (c * 9 / 5) + 32

    def F2C(self, f):
        return (f - 32) * 5 / 9

    def A2B(self, a, v):
        return self.unitMap[a][0] * v


if __name__ == "__main__":
    converter = Converter()
    print(converter.A2B("英尺", 123))
    print(converter.A2B("公里", 345))
    pass
