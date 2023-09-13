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


# редактирует запись в словаре и возвращает заголовок отредактированной заметки
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
    if len(notes) == 0:
        return {}
    match fieldNumber:
        case 1: # ID
            return dict(sorted(notes.items()))
        case 2: # title
            sortField = 'title'
        case 3: # text
            sortField = 'text'
        case 4: # createTime
            sortField = 'createTime'
        case 5: # editTime
            sortField = 'editTime'
        case _: # по умолчанию ID
            return dict(sorted(notes.items()))
    # создаём временный словарь
    tempDict = {}
    # наполняем его парами ID-сортируемое поле
    for i, note in notes.items():
        tempDict[i] = note[sortField]
    # для сортировки применяем метод SORTED, который сортирует с учётом ЛЯМБДЫ 
    # (она указывает, что сортировать надо по каждому второму полю и ВНЕ зависимости от регистра символов upper())
    # и возвращает СПИСОК КОРТЕЖЕЙ, который снова превращаем в СЛОВАРЬ
    tempDict = dict(sorted(tempDict.items(), key=lambda i: i[1].upper())) 
    # формируем новый отсортированный словарь на основании ID из tempDict и данных их словаря-источника NOTES
    sortedNotes = {}
    for i, field in tempDict.items():
        sortedNotes[i] = notes[i]
    # обновляем глобальную переменную, чтобы сортировки в последующем были такими же
    fieldToSort = fieldNumber
    # обновляем глобальный словарь. теперь он отсортирован
    notes = sortedNotes
            
