import math
import phrases
import coloredConsole
from datetime import datetime

colorDefault = coloredConsole.ANSI_DEFAULT

colorError   = coloredConsole.ANSI_BRIGHT_RED
colorErrorSign = colorError + coloredConsole.ANSI_BOLD
colorErrorText = colorDefault + colorError + coloredConsole.ANSI_ITALIC

colorWarning   = coloredConsole.ANSI_BRIGHT_PURPLE
colorWarningSign = colorWarning + coloredConsole.ANSI_BOLD
colorWarningText = colorDefault + colorWarning + coloredConsole.ANSI_ITALIC

colorSuccess = coloredConsole.ANSI_BRIGHT_GREEN
colorSuccessSign = colorSuccess + coloredConsole.ANSI_BOLD
colorSuccessText = colorDefault + colorSuccess + coloredConsole.ANSI_ITALIC

colorTitle   = coloredConsole.ANSI_YELLOW + coloredConsole.ANSI_BOLD
colorBorder  = coloredConsole.ANSI_BRIGHT_BLUE


def print_title(message): #┌─┐└─┘│
    print(colorBorder + "╓" + "─" * (len(message) + 2) + "╖")
    print("║ " + colorTitle + message + colorBorder + " ║")
    print("╙" + "─" * (len(message) + 2) + "╜" + colorDefault)

def print_error(message):
    print(colorErrorSign + "<< ! >>" + colorErrorText + " " + message + colorDefault)

def print_warning(message):
    print(colorWarningSign + "[ ! ] " + colorWarningText + message + colorDefault)

def print_message(message):
    print(colorSuccessSign + "[ √ ] " + colorSuccessText + message + colorDefault)

def cls():
    print(coloredConsole.ANSI_CLEARSCREEN)


# выбор из меню (принимает список - разные меню, печатает меню в 2 столбика)
def get_menu_choise(menu: list[str]) -> int:
    menuLength = len(menu)
    columnSize = math.ceil(menuLength / 2)
    for index in range(0, columnSize):
        print((f"[ {index + 1} ] {menu[index]:<30}"), end="")
        if index + columnSize < menuLength:
            print(f"[ {index + 1 + columnSize} ] {menu[index + columnSize]}")
        else:
            print("")
    while True:
        print("." * 70)
        select = input(phrases.selectMenu)
        if select.isdigit() and 0 < int(select) < menuLength + 1:
            return int(select)
        print_error(phrases.errorSelectMenu(menu))


# добавление новой заметки, защита от пустого ввода
def get_new_note() -> dict[str, str]:
    newNote = {}
    print_title(phrases.newNoteMessage)
    for field, message in phrases.inputNote.items():
        currentInput = input(message).strip()
        if len(currentInput) == 0:
            newNote[field] = "--"
        else:
            newNote[field] = currentInput
    currentTime = datetime.now().strftime('%Y.%m.%d, %H:%M:%S')
    newNote["createTime"] = currentTime
    newNote["editTime"] = currentTime
    cls()
    return newNote


# редактирование заметки, пустой ввод - оставить без изменений, коррекция только editTime
def get_edited_note(oldNote: dict[str, str]) -> dict[str, str]:
    editedNote = {}
    print_title(phrases.editNoteTitle)
    print(phrases.editNoteInstruction)
    for field, message in phrases.inputNote.items():
        currentInput = input(message).strip()
        if len(currentInput) == 0:
            editedNote[field] = oldNote[field]
        else:
            editedNote[field] = currentInput
    currentTime = datetime.now().strftime('%Y.%m.%d, %H:%M:%S')
    editedNote["createTime"] = oldNote["createTime"]
    editedNote["editTime"] = currentTime
    cls()
    return editedNote


# получение поискового запроса
def get_search_word():    
    while True:
        searchWord = input(phrases.searchMessage)
        if len(searchWord) == 0:
            print_warning(phrases.emptyRequest)
        else:
            return searchWord.lower()


# печать заметок (всех или из поискового запроса)
def print_notes(data: dict[int, dict[str: str]]):
    if len(data) != 0:
        idField         = max([len(str(item)) for item in data.keys()]) + 2
        titleField      = max([len(item['title']) for item in data.values()]) #максимальная из списка длин полей NAME
        textField       = max([len(item['text']) for item in data.values()])
        createTimeField = editTimeField = 20
        if titleField < len(phrases.titleTitle) + 1:
            titleField = len(phrases.titleTitle) + 2
        elif titleField > 25:
            titleField = 25

        if textField < len(phrases.titleText):
            textField = len(phrases.titleText) + 2
        elif textField > 35:
            textField = 35
        print("┌" + "─" * idField + "┬" + "─" * titleField + "┬" + "─" * textField + "┬" + "─" * createTimeField + "┬" + "─" * editTimeField + "┐")
        print("│" + phrases.titleID.center(idField) + "│" + phrases.titleTitle.center(titleField) + "│" + phrases.titleText.center(textField) +
               "│" + phrases.titleDateCreate.center(createTimeField) + "│"+ phrases.titleDateEdit.center(editTimeField) + "│")
        print("├" + "─" * idField + "┼" + "─" * titleField + "┼" + "─" * textField + "┼" + "─" * createTimeField + "┼" + "─" * editTimeField +"┤")
        for i, note in data.items():
            if len(note['title']) > titleField:
                title = note['title'][:22] + "..."
            else:
                title = note['title']
            if len(note['text']) > textField:
                text = note['text'][:32] + "..."
            else:
                text = note['text']
            print(f"│{i:^{idField}}│{title:<{titleField}}│{text:<{textField}}│{note['createTime']:<{createTimeField}}│{note['editTime']:<{editTimeField}}│")
        print("└" + "─" * idField + "┴" + "─" * titleField + "┴" +"─" * textField + "┴" + "─" * createTimeField + "┴" + "─" * editTimeField + "┘")
    else:
        print_error(phrases.errorEmptyList)


# печать единственной заметки без сокращений текста
def print_single_note(id: int, note: dict[str: str]):
    cardWidth = 40          
    title = note['title']
    text = note['text']
    editTime = note['editTime']

    titleLines = len(title) // cardWidth + int(len(title) % cardWidth > 0) # на случай многострочности заголовка
    textLines  = len(text) // cardWidth + int(len(text) % cardWidth > 0)   # на случай многострочности текста заметки
    
    print(phrases.noteTitle + id)
    # многострочный заголовок заметки
    print("╓" + "─" * (cardWidth + 2) + "╖")            
    for index in range(0, titleLines):
        print(f"║ {title[index * cardWidth : cardWidth * (index + 1)]:<{cardWidth}} ║")
    print("╟" + "─" * (cardWidth + 2) + "╢")

    # многострочный текст заметки
    for index in range(0, textLines):
        print(f"║ {text[index * cardWidth : cardWidth * (index + 1)]:<{cardWidth}} ║")
    print("║ " + " " * (cardWidth) + " ║")
    print("║ " + ("ред.: " + editTime).rjust(cardWidth) + " ║")
    print("╙" + "─" * (cardWidth + 2) + "╜")
########################


def get_note_id():
    while True:
        result = input(phrases.searchByID)
        if len(result) == 0:
            print_error(phrases.errorEmptyID)
        else:
            return result
    