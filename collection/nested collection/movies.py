movies=[
    ['lokah','malayalam',120,2025,9],
    ['spiderman bnd','english',180,2026,10],
    ['bahubali','telungu',190,2018,9],
    ['bangalore days','malayalam',200,2014,8],
    ['blast','tamil',120,2026,7]
]

print(movies[3][2:])

title=[m[0] for m in movies]
print(title)

language=[m[1] for m in movies]
print(language)

all_years=[m[-2] for m in movies]
print(all_years)