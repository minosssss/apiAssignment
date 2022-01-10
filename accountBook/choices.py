#지불방식
CASH = 'P001'
BANK = 'P002'
CREDIT = 'P003'
DEBIT = 'P004'

ACCOUNT_CHOICES = (
    (CASH, "현금"),
    (BANK, "은행"),
    (CREDIT, "신용카드"),
    (DEBIT, "체크카드"),
)

#사용구분
MEAL = 'C001'
Transportation = 'C002'
ENTERTAINMENT = 'C003'
GROCERY = 'C004'
SHOPPING = 'C005'
HEALTH = 'C006'
EDUCATION = 'C007'
ETC = 'C008'

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

CLASSIFICATION_CHOICES = (
    ('INCM', '수입'),
    ('EXPND', '지출'),
    #('ACTRSF', "이체"),
)