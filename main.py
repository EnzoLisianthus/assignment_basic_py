import re

file_name = "07-02. 전주대 대동제 및 해커톤 통합운영 데이터 로그.txt"

with open(file_name, encoding="utf-8") as file:
    text = file.read()

emails = re.findall(
    r"(?<![\w.%+-])[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}(?![\w.-])",
    text
)
phones = re.findall(r"(?<![\w.-])010[-. ][0-9]{4}[-. ][0-9]{4}(?![\w.-])", text)
students = re.findall(
    r"\[(202[0-9]{6})[ \t]*/[ \t]*([^\s\]\r\n][^\]\r\n]*?)[ \t]*\]", text
)
github_urls = re.findall(
    r"https?://github\.com/[A-Za-z0-9-]+/[A-Za-z0-9._-]+", text
)
coupons = re.findall(r"(?<![\w-])FEST-2026-[A-Z0-9]{4}(?![\w-])", text)
sales = re.findall(
    r"(?m)^-[ \t]*([^\r\n]+?)[ \t]+매출:[ \t]*"
    r"([0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)원(?=$|[ \t(])",
    text
)

results = [
    ("1. 유효한 이메일", emails),
    ("2. 휴대폰 번호", phones),
    ("3. 재학생 학번과 학과", students),
    ("4-1. GitHub 저장소", github_urls),
    ("4-2. 2026년 쿠폰", coupons),
]

for title, values in results:
    print(f"\n{title} ({len(values)}개)")
    for value in values:
        print(value)

print(f"\n5. 부스별 매출 ({len(sales)}개)")
total_sales = 0
for booth, amount in sales:
    won = int(amount.replace(",", ""))
    total_sales += won
    print(f"{booth}: {won:,}원")
print(f"전체 매출 합계: {total_sales:,}원")
