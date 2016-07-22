# OCR Image Processing 
## Read out the captcha

Author: Lin Dong

Date: July 22nd, 2016

## Prerequisites

OS: Mac

```
brew install imagemagick
brew install tesseract --all-languages

brew install python2
pip install Pillow
pip install pytesseract
```

## Instructions

Just run: `python main.py`

* `iteration.py`: iterate multiple times of original image
* `convert_to_text.py`: read out the string from white-gray image,

## Screenshots

Progressive Iterations: 

Iteration 1: ![](./screenshots/iteration_0.jpeg)

Iteration 2: ![](./screenshots/iteration_1.jpeg)

Iteration 3: ![](./screenshots/iteration_2.jpeg)

# References
1. [python 识别验证码](https://segmentfault.com/q/1010000005686388)
2. [OCR on OS X with tesseract Raw](https://gist.github.com/henrik/1967035)

