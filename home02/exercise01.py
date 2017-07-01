class Editor:
    def view_doc(self):
        print('Content of the document.')

    def edit_doc(self):
        print('You do not have permissions to edit documents.')


class ProEditor(Editor):
    def edit_doc(self):
        print('Key is valid! Now you can edit the document.')


def main():
    user_input = str(input('Please fill in the Licence Key: '))
    secret_key = '32Df#44'
    if user_input == secret_key:
        my_edit = ProEditor()
    else:
        my_edit = Editor()

    my_edit.view_doc()
    my_edit.edit_doc()

if __name__ == '__main__':
    main()