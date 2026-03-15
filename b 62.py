st = input().lower()
a = st.count("a")
e = st.count("e")
i = st.count("i")
o = st.count("o")
u = st.count("u")
list = [a,e,i,o,u]
list2 = ["a","e","i","o","u"]
for i in range(5):
    if list[i] > 0:
        print(list2[i] + ": " + str(list[i]))
