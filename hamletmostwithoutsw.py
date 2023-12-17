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

#사라지지 않은 일부 조동사 추가
auxiliary_verbs = ["shall", "will", "should", "would", "may", "might", "can", "could"]
stop_words.update(auxiliary_verbs)

# 단어 빈도를 계산하는 함수
def word_counts(lines, top_n):
    words = [word for line in lines for word in line.split()]
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

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

# 불용어 제거
filtered_lines = [' '.join([word for word in line.split() if word.lower() not in stop_words]) for line in hamlet_lines]

# 가장 많이 사용된 단어 상위 25개 출력
top_filtered_words = word_counts(filtered_lines, 25)

# 히스토그램 생성
plt.figure(figsize=(10, 5))
plt.bar([word[0] for word in top_filtered_words], [word[1] for word in top_filtered_words], color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 25 Most Frequent Words in Hamlet')
plt.xticks(rotation=45, ha='right')
plt.show()
