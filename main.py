import re

file_name = "07-02. 전주대 대동제 및 해커톤 통합운영 데이터 로그.txt"

with open(file_name, "r", encoding="utf-8") as file:
    text = file.read()

emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}",
    text
)

phones = re.findall(r"\b010[-. ]\d{4}[-. ]\d{4}\b", text)

students = re.findall(r"\[(202\d{6})\s*/\s*([^\]\r\n]+?)\s*\]", text)

github_urls = re.findall(
    r"https?://github\.com/[A-Za-z0-9-]+/[A-Za-z0-9._-]+",
    text
)
coupons = re.findall(r"\bFEST-2026-[A-Z0-9]{4}\b", text)

sales = re.findall(r"- (.+?) 매출:\s*([\d,]+)원", text)

print("=== 대동제 및 해커톤 정규표현식 추출 결과 ===")

print(f"\n1. 유효한 이메일 ({len(emails)}개)")
for email in emails:
    print(email)

print(f"\n2. 휴대폰 번호 ({len(phones)}개)")
for phone in phones:
    print(phone)

print(f"\n3. 재학생 학번과 학과 ({len(students)}개)")
for student_id, department in students:
    print((student_id, department.strip()))

print(f"\n4-1. GitHub 저장소 ({len(github_urls)}개)")
for url in github_urls:
    print(url)

print(f"\n4-2. 2026년 쿠폰 ({len(coupons)}개)")
for coupon in coupons:
    print(coupon)

print(f"\n5. 부스별 매출 ({len(sales)}개)")
total_sales = 0
for booth, amount in sales:
    won = int(amount.replace(",", ""))
    total_sales += won
    print(f"{booth}: {won:,}원")

print(f"전체 매출 합계: {total_sales:,}원")