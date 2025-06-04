# chapter1-basic
깃과 깃허브 첫 실급을 위한 원격 저장소

## 의존성 설치

이 스크립트를 실행하려면 Tesseract 엔진과 파이썬 라이브러리 `pytesseract`, `Pillow`가 필요합니다.

1. `pytesseract`, `Pillow` 설치:
   ```bash
   pip install pytesseract pillow
   ```
2. Tesseract 설치:
   - Debian/Ubuntu: `sudo apt install tesseract-ocr`
   - macOS(Homebrew): `brew install tesseract`

Tesseract의 다른 설치 방법은 [Tesseract 프로젝트](https://github.com/tesseract-ocr/tesseract)에서도 확인할 수 있습니다.


## OCR 스크립트 사용법

`ocr.py` 파일은 [Tesseract](https://github.com/tesseract-ocr/tesseract)와 `pytesseract`, `Pillow`를 이용해 이미지를 텍스트로 변환합니다. 의존성이 설치되어 있다면 다음과 같이 사용할 수 있습니다.

```bash
python ocr.py image.png -l eng -o output.txt
```

- `image.png` : 인식할 이미지 파일 경로
- `-l eng` : Tesseract 언어 코드(기본값은 `kor`)
- `-o output.txt` : 결과를 저장할 파일 경로(생략하면 표준 출력)
