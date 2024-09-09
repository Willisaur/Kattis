a=int(input())
[print((" ".join(b.split()[2:]))if (b:=input()).startswith("simon says")else "")for i in range(a)]