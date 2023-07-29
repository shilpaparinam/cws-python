def marks(phy, che, maths, sst):
    total = phy + che + maths + sst
    percent = (total / 400) * 100
    print(f"Total=  {total}")
    print(f"Percentage= {percent}")


# marks(94, 86, 78, 89) #
marks(sst=89, maths=78, phy=86, che=94)
