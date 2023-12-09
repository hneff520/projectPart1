from logic01 import *

# This is the main file for the Lab 1 remake
def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()