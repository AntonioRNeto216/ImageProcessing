from src.application_gui import ApplicationGUI


def main() -> None:
    """
    The main function of the code.\n
    Create an ApplicationGUI object and call init_gui.
    """
    application_gui = ApplicationGUI()
    application_gui.init_gui()


if __name__ == '__main__':
    main()
