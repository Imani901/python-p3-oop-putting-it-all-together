#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        if not isinstance(page_count, int):
            raise AssertionError("page_count must be an integer")
        self.title = title
        self.page_count = None
        self.current_page = 0
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value    

        
    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print("You have reached the end of the book.")    
    
        