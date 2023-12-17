from collections import Counter
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# nltk에서 불용어 다운로드
nltk.download('stopwords')

# NLTK의 불용어 목록을 불러오기
stop_words = set(stopwords.words('english'))

# 중세 영어 불용어 추가
medieval_english_words = ["thou", "thy", "thee", "’t","th’","i’ll","’tis"]
stop_words.update(medieval_english_words)

# 대사를 담을 리스트
hamlet_lines = []

# XML 또는 HTML 문서를 파싱
with open('C:\\Users\\GY_Kim\\Desktop\\hamlet\\ham.xml', 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# Hamlet의 대사 추출
for speaker in soup.find_all("sp", attrs={"who": "#Hamlet_Ham"}):
    lines = [word.text.lower() for line in speaker.find_all("ab") for word in line.find_all("w")]
    hamlet_lines.extend(lines)

# 불용어 및 중세 영어 불용어 제거
filtered_lines = [' '.join([word for word in line.split() if word.lower() not in stop_words]) for line in hamlet_lines]

# 대소문자를 구분하지 않고 특정한 단어들을 대상으로 빈도 계산
target_words = ["mother", "horatio", "king","ophelia","polonius","laertes","rosencrantz","gyldensterne","claudius","fortinbras","madam"]  
word_counts = Counter([word for line in filtered_lines for word in line.split() if word.lower() in target_words])

# 특정한 단어들의 빈도수 출력
for word, count in word_counts.items():
    print(f"{word}: {count} times")

# 히스토그램 생성
plt.bar(word_counts.keys(), word_counts.values(), color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Frequency of names in Hamlet')
plt.xticks(rotation=45, ha='right')
plt.show()
