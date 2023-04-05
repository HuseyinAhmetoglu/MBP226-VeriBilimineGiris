class BankaHesabi():
    def __init__(self, hesapNo, hesapSahibi, tutar):
        self.hesapNo = hesapNo
        self.hesapSahibi = hesapSahibi
        self.tutar = tutar

    def paraCek(self, cekilen):
        self.tutar -= cekilen

    def paraYatir(self, yatirilan):
        self.tutar += yatirilan


class KrediliHesap (BankaHesabi):
    def __init__(self, hesapNo, hesapSahibi, limit, tutar):
        super().__init__(hesapNo, hesapSahibi, tutar)
        self.limit = limit

    def paraCek(self, cekilen):
        if self.limit - cekilen > 0:
            self.tutar -= cekilen
            self.limit -= cekilen
        else:
            print("yeterli kredi limitniz yok!")
            print("kullanılabilir limitiniz: " + str(self.limit))
