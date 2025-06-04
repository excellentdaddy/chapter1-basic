# chapter1-basic
깃과 깃허브 첫 실급을 위한 원격 저장소

## OCR 스크립트 사용법

`ocr.py` 파일은 [Tesseract](https://github.com/tesseract-ocr/tesseract)와 `pytesseract`, `Pillow`를 이용해 이미지를 텍스트로 변환합니다. 의존성이 설치되어 있다면 다음과 같이 사용할 수 있습니다.

```bash
python ocr.py image.png -l eng -o output.txt
```

- `image.png` : 인식할 이미지 파일 경로
- `-l eng` : Tesseract 언어 코드(기본값은 `kor`)
- `-o output.txt` : 결과를 저장할 파일 경로(생략하면 표준 출력)
