class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun nimi on {self.name}")


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja on {self.editor}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Kirjailija on {self.author}")
        print(f"Sivuja on {self.page_count}")


pub1 = Magazine("Aku Ankka", "Aki Hyyppä")
pub1.print_info()

pub2 = Book("Hytti nro 6", "Rosa Liksom", 220)
pub2.print_info()
