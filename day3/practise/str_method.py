class Book:
    def __init__(self,book,author):
        self.book=book
        self.author=author

    def __str__(self):
        return f"Book:{self.book} written by {self.author}"
    
book1=Book(" Atomic Habits","James Clear")
book2=Book(" For a smile","GV")

print(book1)
print(book2)