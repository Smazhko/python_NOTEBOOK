import json
import os


path = "notes.json"
fieldToSort = 4
notes = {} # dict[int, dict[str, str]]


# попытка открыть файл. при неудаче - проверяет, есть ли файл в принципе, 
# а если его нет, то создаёт пустой
def open_file() -> int:
    global notes # пометка GLOBAL внутри метода перед переменной в случае, если она будет этим методом изменена
    try:
        with open(path, 'r', encoding="UTF-8") as notes_file:
            notes = json.load(notes_file)
        return 1
    except:
        if os.path.exists(path):
            return 0
        else:
            notes_file = open(path, 'w+', encoding="UTF-8")
            notes_file.close()
            return 2


def save_file() -> bool:
    global notes
    try:
        with open(path, 'w', encoding='UTF-8') as notes_file:
            json.dump(notes, notes_file, ensure_ascii=False)
        return True
    except:
        return False


# поиск по словарю - возвращает словарь такой же структуры с записями, подходящими под поиск
# поиск соответствия запросу происходит по полям ID, ЗАГОЛОВОК, ТЕКСТ заметки
def search_notes(requestWord = ''):
    result = {}
    for i, note in notes.items():
        if requestWord in (i + note['title'] + note['text']).lower():
            result[i] = note
    return result


# добавляет новую заметку - запись в словаре и возвращает её заголовок
def add_new_note(newNote: dict[str: str]):
    # формирование нового ID
    if len(notes) != 0:
        newID = max(list(map(int, notes.keys()))) + 1
    else:
        newID = 1
    notes.update({str(newID): newNote})
    return newNote['title']


# обновлят заметку с конкретным индексом новыми данными и возвращает заголовок отредактированной заметки
def edit_note(currentID: str, editedNote: dict[str, str]):
    notes[currentID] = editedNote
    return notes[currentID]['title']


# удаляет запись в словаре и возвращает заголовок удалённой заметки
def remove_note(idToRemove) -> str:
    global notes
    removedNoteTitle = notes[idToRemove]['title']
    notes.pop(idToRemove) 
    return removedNoteTitle

# СОРТИРОВКА ГЛАВНОГО СЛОВАРЯ по всем полям
def sort_notes_by(fieldNumber: int):
    global fieldToSort
    global notes
    # обновляем глобальную переменную, чтобы сортировки в последующем были такими же
    fieldToSort = fieldNumber
    if len(notes) != 0:
        match fieldNumber:
            case 1: # 1 и по умолчанию - ID. объяснение по оформуле - ниже
                sortedNotes = dict(sorted(notes.items(), key=lambda i: int(i[0])))
            case 2: # title
                sortField = 'title'
            case 3: # text
                sortField = 'text'
            case 4: # createTime
                sortField = 'createTime'
            case 5: # editTime
                sortField = 'editTime'
        if 2 <= fieldNumber <= 5:
        # для сортировки применяем метод SORTED, который сортирует с учётом ЛЯМБДЫ 
        # и возвращает СПИСОК КОРТЕЖЕЙ, который снова превращаем в СЛОВАРЬ.
        # ЛЯМБДА указывает, что сортировать надо по каждому второму члену каждого из кортежей (индекс 1).
        # каждое второе поле - это словарь - содержимое заметки.
        # указываем на необходимое поле внутреннего словаря (заголовок, текст и т.д.) для сортировки
        # upper() - приведение к верхнему регистру - даёт возможность сортировки ВНЕ зависимости от регистра символов
            sortedNotes = dict(sorted(notes.items(), key = lambda i: i[1][sortField].upper())) 
        
        # обновляем глобальный словарь. теперь он отсортирован
        notes = sortedNotes
