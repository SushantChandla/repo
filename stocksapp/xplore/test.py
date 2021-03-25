from pytezos import pytezos

pyte =pytezos.using(key='edskRsbSWHct7zNqpSgwEPbzYtLc3P3d3ygdHvWS7eYNd33hMobaiL2uhXecHkkcoXs6p9ov5UQRDkacFd7pmzKJUe1Pu8yTDc')
contrt=pyte.contract("KT1Vdz5CBaoYMZTP9AwZ4Y3EDPcdR5bsojwt")
# pyt = pytezos.using('florencenet').contract('KT1DgovASfdKtiDG33PQ6WKzksraXjvuqvdB')
print(contrt.storage()) 