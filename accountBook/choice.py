#지불방식
CASH = 'p001'
BANK = 'p002'
CREDIT = 'p003'
DEBIT = 'p004'

ACCOUNT_CHOICES = (
    (CASH, "현금"),
    (BANK, "은행"),
    (CREDIT, "신용카드"),
    (DEBIT, "체크카드"),
)


MEAL = 'c001'
Transportation = 'c002'
ENTERTAINMENT = 'c003'
GROCERY = 'c004'
SHOPPING = 'c005'
HEALTH = 'c006'
EDUCATION = 'c007'
ETC = 'c008'

CATEGORY_CHOICES = (
    (MEAL, "식비"),
    (Transportation, "교통비"),
    (ENTERTAINMENT, "문화생활"),
    (GROCERY, "마트/편의점"),
    (SHOPPING, "쇼핑"),
    (HEALTH, "건강"),
    (EDUCATION, "교육"),
    (ETC, "기타"),
)