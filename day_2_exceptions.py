def errorsTestSUM (a:int, b:int):
    try:
        result = a/b     
    except:
        print("Деление на 0")
        print("Исключение было обработано")
    return result