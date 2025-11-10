books= [101,102,103,104,105,106]
books.remove(101)
books.pop()
books.remove(103)
books.reverse()
print(books)



movies=["inception","Titanic","Avatar","Intestellar"]
movies.remove("Titanic")
movies.append("Avengers")
movies.insert(0,"up")
backup_movies=movies.copy()
movies.sort()
print(movies)
print(backup_movies)

goals=[5,12,36,47,56,80]
goals.append(90)
print(goals)
goals.remove(36)
print(goals)
if 47 in goals:
   
    print(goals)
goals[1]=15
print(goals)
goals.clear()
