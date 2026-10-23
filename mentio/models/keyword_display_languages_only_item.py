from enum import StrEnum


class KeywordDisplayLanguagesOnlyItem(StrEnum):
    AR = "ar"
    CA = "ca"
    DA = "da"
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    HI = "hi"
    ID = "id"
    IT = "it"
    JA = "ja"
    KO = "ko"
    NL = "nl"
    PL = "pl"
    PT = "pt"
    RU = "ru"
    SV = "sv"
    TR = "tr"
    UK = "uk"
    ZH = "zh"

    def __str__(self) -> str:
        return str(self.value)
