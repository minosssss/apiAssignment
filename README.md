# apiAssignment (payhere)

> REST API Reference
- Django Rest framework 활용
- Vesion : 1.0.0
- Servers:
  - `http://localhost:8000/api/v1/user/`
  - `http://localhost:8000/api/asset/payments/`
  - `http://localhost:8000/api/asset/records/`

# User API
### 유저목록
유저의 전체 리스트를 가져오는 API 입니다.
- 오직 관리자에게만 허용됩니다.
```
GET http://localhost:8000/api/v1/user/
```
### 회원가입, 로그인, 로그아웃
- `email`과 `password`로 가입을 진행합니다. 
- 로그인 후 `token` 을 발행합니다.
```
@회원가입
POST http://localhost:8000/api/v1/user/
        
@로그인
POST http://localhost:8000/api/v1/user/login/
        
✔요구항목
{
    "email":"email"
    "password":"string"
}

@로그아웃
GET http://localhost:8000/api/v1/user/logout/
```
### 사용자 정보 조회
- 사용자의 아이디`{user_id}`로 사용자의 정보만 조회 가능하며, 관리자도 허용되지 않습니다.
```
GET http://localhost:8000/api/v1/user/{user_id}/

@user_id 1번이 1번과 2번을 조회 할 경우 응답값
GET http://localhost:8000/api/v1/user/1/
{
    "id": 1,
    "email": "admin@django.com"
}

GET http://localhost:8000/api/v1/user/2/
{
    "detail": "You do not have permission to perform this action."
}
```

### 사용자 정보 변경
- 사용자의 이메일과 비밀번호를 변경할 수 있습니다.
```
PUT http://localhost:8000/api/v1/user/{user_id}/
        
✔요구항목
{
    "email":"email"
    "password":"string"
}
```

# Asset API
## 자산 및 지불방식
### 조회 및 추가
- 사용자의 자산항목을 조회 및 추가 할 수 있습니다.
  - `group` [^1] 은 `Choice`항목으로 대분류에 속합니다.
  - `name`은 실제 결제되는 지불방식 입니다.
  
[^1]: CASH, BANK, CREDIT, DEBIT
 
```
GET http://localhost:8000/api/v1/payments/

✔응답값
{
    "id": 1,
    "name": "현대카드",
    "group": "CREDIT"
}
POST http://localhost:8000/api/v1/payments/
        
✔요구항목
{
    "group":""
    "name":""
}
```

### 수정 및 삭제
- 사용자의 자산항목을 수정,삭제 할 수 있습니다.
 
```
PUT http://localhost:8000/api/v1/payments/{payment_id}/
DELETE http://localhost:8000/api/v1/payments/{payment_id}/
        
✔요구항목
{
    "group":"choice"
    "name":"string"
}
```

## 사용내역
### 전체조회
- 로그인 된 사용자의 사용내역을 조회 및 추가 할 수 있습니다.
```
GET http://127.0.0.1:8000/api/v1/asset/records/
```
### 응답 item
- count: 전체 핳목 개수
- next: `pagination` 다음 항목
- previous: `pagination` 이전 항목
- result: 내역
  - id: 사용내역 ID
  - payment: 지불방식
    - id: 지불 ID
    - name: 지불 세부 정보
    - group: 자산 세부 정보
  - category: 사용구분
    - type: 세부 항목
    - 식비, 교통비, 문화생활, 마트/편의점, 쇼핑, 건강, 교육, 기타 중 택1
  - classfication: 수입, 지출 구분 (1=수입, 2=지출)
  - date: 날짜(YYYY-mm-dd)
  - amout: 금액
  - note: 메모
  - status: 삭제여부 (true=보관 ,false=삭제)
  - user: 요청 유저 ID

### 응답값 예
```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "payment": {
                "id": 5,
                "name": "국민카드",
                "group": "CREDIT"
            },
            "category": {
                "type": "교통비"
            },
            "classification": 2,
            "date": "2022-01-01",
            "amout": 30000,
            "note": "주유비",
            "status": true,
            "user": 3
        }
    ]
}
```
```
POST http://127.0.0.1:8000/api/v1/asset/records/
✔요구항목
{
    "payment": {
        "name": "string",
        "group": "choice"
    },
    "category": {
        "type": "choice"
    },
    "classification": "choice(integer_1(수입) or 2(지출))",
    "date": "date(YYYY-mm-dd)",
    "amout": "integer", #0미만은 입력되지 않습니다.
    "note": "string",
    "status": "boolean"
}
```

### 수정 기능
- 사용자는 결과의 세부항목을 변경할 수 있습니다.
- 필요로하는 항목만 수정도 가능합니다.
- `status`는 단순 제외기능이며, 물리적인 삭제는 관리자만 가능합니다.
- `payment와 category 항목은 업데이트 예정`
```
PUT http://127.0.0.1:8000/api/v1/asset/records/{record_id}

✔요구항목
{
    "classification": "choice(integer_1(수입) or 2(지출))",
    "date": "date(YYYY-mm-dd)",
    "amout": "integer", 
    "note": "string",
    "status": "boolean"
}
```

### 검색 기능
- 사용 내역을 검색할 수 있는 API 입니다.
```
GET http://127.0.0.1:8000/api/v1/asset/records/search?
  payment={payment}
  category={category}
  classification={classification}
  date={date}
  date_from={date}&date_to={date}
  amout_lte={amout}
  amout_gte={amout}
  note={note}
  status={status}

```
- 매개변수는 다음과 같습니다.
  - payment: 지불방식
  - category: 사용구분
  - classification: 수입/지출 구분
  - date: 날짜
  - date_from={date}&date_to={date}: 기간 검색
  - amout_lte: 해당 금액보다 적은
  - amout_gte: 해당 금액보다 많은
  - note: 포함된 내용 검색 
  - status: 보관 여부 검색
