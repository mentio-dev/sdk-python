from enum import StrEnum


class SearchMentionsNotEmotionsItem(StrEnum):
    ANGER = "anger"
    ANTICIPATION = "anticipation"
    CONFUSION = "confusion"
    FEAR = "fear"
    FRUSTRATION = "frustration"
    JOY = "joy"
    NEUTRAL = "neutral"
    SADNESS = "sadness"
    SURPRISE = "surprise"
    TRUST = "trust"

    def __str__(self) -> str:
        return str(self.value)
