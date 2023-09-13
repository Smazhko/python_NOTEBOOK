import view
import model
import phrases


def start_menu():
    view.cls()
    opening_file()
    while True:
        view.print_title(phrases.menuTitle)
        select = view.get_menu_choise(phrases.mainMenu)
        match select:
            case 1: # показать все заметки
                show_all_notes()
            case 2:
                one_note_working(model.notes)
            case 3: # добавить новую заметку
                view.cls()                
                newNote = view.get_new_note()
                view.print_message(phrases.successAddNote(model.add_new_note(newNote)))
                saving_file()
            case 4: # найти по содержимому
                view.cls()
                searchResult = searching_note()
                if len(searchResult) != 0:
                    view.print_notes(searchResult)
                    one_note_working(searchResult)
            case 5: # настройки сортировки
                view.cls()                
                view.print_title(phrases.sortTitle)
                model.fieldToSort = view.get_menu_choise(phrases.sortOptions)
                show_all_notes()
            case 6: # выход из программы
                saving_file()
                view.print_title(phrases.exitMessage)
                break # прерывает цикл WHILE


def saving_file():
    if model.save_file():
        view.print_message(phrases.successSaveFile)
    else:
        view.print_error(phrases.errorSaveFile)


def opening_file():
    match model.open_file():
        case 0:
            view.print_error(phrases.errorOpenFile)
        case 1:
            view.print_message(phrases.successOpenFile)
        case 2:
            view.print_message(phrases.successCreateFile)


def show_all_notes():
    view.cls()
    print(phrases.sortMode(model.fieldToSort - 1).rjust(109))
    model.sort_notes_by(model.fieldToSort)
    view.print_notes(model.notes)


def searching_note():
    repeatSearchFlag = True
    answer = {}
    view.print_title(phrases.searchTitle)
    while repeatSearchFlag:
        request = view.get_search_word()
        answer = model.search_notes(request)
        if len(answer) == 0:
            view.print_warning(phrases.emptySearch)
            if input(phrases.searchRepeat) != "+":
                repeatSearchFlag = False
                view.cls()
                return answer
        else:
            repeatSearchFlag = False
            return answer
        

def one_note_working(noteDict: dict[int, dict[str, str]]):
    continueFlag = True
    while(continueFlag):
        currentNoteID = view.get_note_id() # получить ID заметки для печати
        if currentNoteID in noteDict.keys():
            view.cls()
            continueFlag = False
            note_menu(currentNoteID)
        elif currentNoteID == "-":
            view.cls()
            continueFlag = False
        else: 
            view.print_warning(phrases.warningWrongID)


def note_menu(currentNoteID: int):
    view.print_title(phrases.editNoteTitle)
    view.print_single_note(currentNoteID, model.notes[currentNoteID])
    select = view.get_menu_choise(phrases.noteMenu)
    match select:
        case 1: # изменить заметку
            editedNote = view.get_edited_note(model.notes[currentNoteID]) 
            view.cls()               
            view.print_message(phrases.successEditNote(model.edit_note(currentNoteID, editedNote)))
            model.sort_notes_by(model.fieldToSort)
            model.save_file()
        case 2: # удалить заметку
            view.cls()
            view.print_message(phrases.successRemoveNote(model.remove_note(currentNoteID)))
            model.save_file()
        case _: # вернуться в главное меню
            view.cls()

