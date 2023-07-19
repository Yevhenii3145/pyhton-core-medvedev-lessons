import collections

Movie = collections.namedtuple(
    "Movie", ["title", "year", "director", "genre"])

movie = Movie("Good Will Hunting", "1997", "Gus Van Sant", "Drama/Romance")
print(movie)  # Movie(title='Good Will Hunting', year='1997', director='Gus Van Sant', genre='Drama/Romance')
print(movie.title)  # Good Will Hunting
print(movie.genre)  # Drama/Romance
print(movie[0])  # Good Will Hunting

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut pharetra dui\
non bibendum malesuada. Vestibulum quis purus in nibh elementum varius. Praesent\
rutrum congue ex, nec varius nisi congue vel. Suspendisse ac lectus neque. Vestibulum\
dignissim mauris enim, ut molestie lorem fermentum sed. Sed aliquet tincidunt tellus,\
vitae fringilla elit suscipit at. Aenean rutrum dui in nisi blandit, id ultricies\
tortor laoreet. Fusce in auctor arcu. Aenean nec faucibus orci. Aenean elementum et\
urna ut feugiat. Morbi accumsan quam sit amet leo luctus, vitae aliquet ex posuere.\
Maecenas sit amet orci nec dolor fringilla vehicula id vitae massa. Nulla facilisi.\
Aliquam sagittis finibus lacinia. In sit amet urna mollis, tincidunt lorem eget,\
rutrum sapien. Fusce ante eros, placerat mattis diam id, elementum ultricies ipsum."

words = text.replace(".", "").replace(",", "").split()
print(words)

our_couner = collections.Counter(words)
print(our_couner)
print(text.count("amet"))  # 4

print(our_couner.most_common(3))  # [('sit', 4), ('amet', 4), ('in', 3)]


my_deque = collections.deque()
my_deque.append("1")
my_deque.appendleft("2")
first = my_deque.popleft()
print(first)  # 2
my_deque.insert(0, "3")
print(my_deque)  # deque(['3', '1'])
