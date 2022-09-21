class WebDriverNotInitialisedException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self):
        return (
            "The custom webdriver is not initialised "
            "with the '.init_driver()' method"
        )
