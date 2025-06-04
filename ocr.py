import argparse
from PIL import Image
import pytesseract


def run_ocr(image_path: str, lang: str = "kor") -> str:
    """Run OCR on the given image using Tesseract.

    Parameters
    ----------
    image_path : str
        Path to the image file.
    lang : str
        Language code for Tesseract. Default is "kor" (Korean).

    Returns
    -------
    str
        Extracted text.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)
    return text


def main():
    parser = argparse.ArgumentParser(description="Simple OCR tool using Tesseract")
    parser.add_argument("image", help="Path to image file")
    parser.add_argument("-l", "--lang", default="kor", help="Tesseract language code (default: kor)")
    parser.add_argument("-o", "--output", help="Output text file path")
    args = parser.parse_args()

    text = run_ocr(args.image, args.lang)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
