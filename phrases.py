from model import path

menuTitle = "ЗАПИСНАЯ КНИЖКА (заметки)"

mainMenu = ["показать все заметки", 
            "открыть заметку по ID",
            "добавить новую заметку",
            "найти заметку по содержимому",
            "настройки сортировки заметок",
            "выйти из программы"]

noteMenu = ["изменить заметку",
            "удалить заметку",
            "вернуться в главное меню"]

sortOptions = ["по идентификатору ID",
               "по заголовкам",
               "по тексту",
               "по дате создания",
               "по дате изменения"]

selectMenu      = "Выберите пункт меню... >> "
newNoteMessage  = "СОЗДАНИЕ НОВОЙ ЗАМЕТКИ"
inputNote       = {"title": "Заголовок >> ",
                   "text" : "Текст     >> "}

sortTitle          = "ВАРИАНТЫ СОРТИРОВКИ"
def sortMode(field):
    return "Сортировка " + sortOptions[field]

searchTitle        = "ПОИСК ЗАМЕТКИ по содержимому"
searchMessage      = "Введите поисковый запрос >> "
searchRepeat       = "Повторить поиск ? (Введите \"+\", если ДА, и \"-\", если НЕТ) >> "
readNoneTitle      = "ПРОСМОТР ЗАМЕТКИ"
searchByID         = "Введите ID заметки (или '-' для выхода) >> "


editNoteTitle       = "РЕДАКТИРОВАНИЕ ЗАМЕТКИ"
noteTitle           = "Заметка #"
editNoteInstruction = "Введите новые данные (Enter - оставить как было)"

errorOpenFile   = "Ошибка открытия файла с заметками. Вероятно, файл занят другим процессом."
errorSaveFile   = "Ошибка сохранения заметок."
def errorSelectMenu(menu: list):
    return f"Ошибка ввода (необходимо ввести цифры от 1 до {len(menu)}). Попробуйте ещё раз."
errorEmptyList  = "Список пуст. Выводить нечего."
errorEmptyID    = "Пустого ID не бывает! "

emptyRequest    = "Не могу найти пустоту. Попробуйте снова."
emptySearch     = "Ничего не найдено..."
warningWrongID  = "Заметки с таким ID среди найденных не обнаружено"

successOpenFile   = "Заметки успешно загружены."
successCreateFile = "Файл для заметок успешно создан."
successSaveFile   = f"Заметки успешно сохранены в файл."

def successAddNote(title):
    return f"Заметка \"{title}\" успешно ДОБАВЛЕНА."

def successRemoveNote(title):
    return f"Заметка \"{title}\" успешно УДАЛЕНА."

def successEditNote(title):
    return f"Заметка \"{title}\" успешно ИЗМЕНЕНА."

titleID         = "ID"
titleTitle      = "ЗАГОЛОВОК"
titleText       = "ТЕКСТ" 
titleDateCreate = "ДАТА СОЗДАНИЯ"
titleDateEdit   = "ДАТА ИЗМЕНЕНИЯ"


exitMessage = "ВОТ и ВСЁ! Приходите ещё (^_^)"

