import easyocr
import cv2

# Загрузка изображения
img = cv2.imread("img.jpg")

# Инициализация модели EasyOCR
reader = easyocr.Reader(['en'])

# Распознавание текста
results = reader.readtext(img)
for (bbox, text, prob) in results:
   print(f"Текст: {text}, Вероятность: {prob:.2f}")

# Отображение обнаруженных областей с текстом
for (bbox, text, prob) in results:
   (top_left, bottom_right) = bbox[0], bbox[2]
   img = cv2.rectangle(img, tuple(map(int, top_left)), tuple(map(int, bottom_right)), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


def nums(*args):
   return sum(args)

# Ввод чисел через запятую
numbers = map(int, input("Введите числа через запятую: ").split(','))

print("Результат сложения:", nums(*numbers))


def mult(*args):
   return

# Ввод чисел через запятую
numbers = map(int, input("Введите числа через запятую: ").split(','))

print("Результат сложения:", nums(*numbers))







