# datarize 과제

1. 과제 내용 
- FastAPI 를 활용한 CRUD API 구현
- CRUD - MVP 패턴 구현
- 추가적으로 더 붙이고 싶은 기술 적용 (Optional)<aside>
```
💡 참고사항
- DB 및 구현환경은 원하는대로 사용 (e.g. mariadb, Docker)
- 유저에 대한 인증(Authentication)은 고려하지 않아도 됨
- 각 필드의 Type 이나 최대 길이 등은 개인이 자유롭게 정의해도 됨
- 과제제출은 소스코드와 간단한 설명문서를 깃헙에 업로드 한 뒤, 메일로 링크공유
- 과제에 대한 질문사항이 있을 경우, hello@datarize.ai 로 문의
```

2. 결과
- 유저 생성 성공
- 유저 로그인하여 토큰 발행 성공
- task CRUD는 구현하였으나 토큰으로 user_id값 조회 실패

3. 실패 이유 
- 첫째. 확장성을 고려하여 처음으로 oop 형태로 구현해 보려 하였으나 시간 부족으로 실패하였습니다.
- 둘째. token_helper활용 실패로 인한 user_id 받아오기 실패
- 셋째. 부족한 fastapi framework의 지식 (sqlalchemy, starlette 등)
- 넷째. oop에대한 이해도 부족 

4. 아쉬운점 
- 직장을 다니면서 코딩을 하기 때문에.. 시간이 하루만 더 있었다면 가능하지 않았을까라는 아쉬움이 있습니다.
  alembic, middleware, docker 등을 구현하지 못해서 아쉽습니다.
  물론 준비 부족으로 인한 제 탓이지만.. 코드라도 잘 봐주시면 감사하겠습니다. 감사합니다.