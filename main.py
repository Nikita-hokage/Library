import re


class Library:
    def add_book(self):
        with open('lib.txt', 'a+', encoding='utf-8') as f:
            title = input('title: ').strip()
            author = input('author: ').strip()
            year = int(input('year: '))
            book_id = 1 + sum(1 for line in open('lib.txt', 'r'))
            book = f'{book_id} {title} {author} {year} в наличии'
            f.write(book + '\n')
        print('книга добавлена')

    def dell_book(self):
        book_id = int(input('Введите id книги для удаления')) - 1
        with open('lib.txt', 'r', encoding='utf-8') as f:
            lines = [line for line in f]

        with open('lib.txt', 'w', encoding='utf-8') as f:
            for number, line in enumerate(lines):
                if number != book_id:
                    if number > book_id:
                        f.write(str(int(line[0]) - 1) + line[1::])
                    else:
                        f.write(line)
        print(f'Книга с id {book_id} удалена')

    def find_book(self):
        word = input('Введите слово для поиска: ').strip()
        bool = False
        with open('lib.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if word in line:
                    print(line.strip())
                    bool = True
        if bool == False:
            print('Книга не найдена')

    def whole_lib(self):
        with open('lib.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
            else:
                print('Библиотека пуста')

    def change_status(self):
        book_id = int(input('Введите id книги '))
        new_status = input('Статус на который хотите поменять [в наличии/выдано] ').lower().strip()
        updated = False
        if new_status not in ['в наличии', 'выдано']:
            print("Некорректный статус.")
            return

        with open('lib.txt', 'r', encoding='utf-8') as f:
            lines = [line for line in f]

        with open('lib.txt', 'w', encoding='utf-8') as f:
            for number, line in enumerate(lines):
                if number == book_id - 1:
                    stat = re.findall("\D+$", line)
                    f.write(line.replace(stat[0], ' ' + new_status + '\n'))
                    updated = True
                else:
                    f.write(line)
        if updated:
            print(f"Статус книги с id {book_id} изменён на '{new_status}'.")
        else:
            print(f"Книга с id {book_id} не найдена.")

    def menu(self):
        f = open('lib.txt', 'a+')
        f.close()
        while True:
            try:
                inp = int(input(
                    "Что хотите сделать?\n"
                    "1. Добавить книгу\n"
                    "2. Удалить книгу\n"
                    "3. Найти книгу\n"
                    "4. Посмотреть библиотеку\n"
                    "5. Изменить статус книги\n"
                    "0. Выйти\n"
                    "Ваш выбор: "
                ))
                if inp == 1:
                    self.add_book()
                elif inp == 2:
                    self.dell_book()
                elif inp == 3:
                    self.find_book()
                elif inp == 4:
                    self.whole_lib()
                elif inp == 5:
                    self.change_status()
                elif inp == 0:
                    print("Выход из программы.")

                    break
                else:
                    print("Некорректный ввод. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите номер действия.")


prog = Library()
prog.menu()
