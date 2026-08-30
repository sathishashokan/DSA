# OPTIMAL(BINARY SEARCH)
def book_allocation(books, students):
    if students > len(books):
        return -1
    low = max(books)
    high = sum(books)
    while low <= high:
        mid = (low+high)//2
        pages, student_count = 0, 1
        for book in books:
            if pages + book <= mid:
                pages += book
            else:
                student_count += 1
                pages = book
        if student_count <= students:
            high = mid - 1
        else:
            low = mid + 1
    return low

# Driver code
a = [12,34,67,90]
b = [25, 46, 28, 49, 24]
print(book_allocation(a,2))
