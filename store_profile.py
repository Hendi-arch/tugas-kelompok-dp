from store_utils import lines


class StoreProfile:
    def __init__(self):
        self.__store_name = "toko kelompok 2".title().center(len(lines()))
        self.__address = "Jl. Gatot Subroto No.8, Cimone, Kec. Karawaci, Kota Tangerang, Banten 15114".center(
            len(lines()))
        self.__npwp = "NPWP : 347934383912345".center(len(lines()))

    def show_profile(self):
        print(lines())
        print(self.__store_name)
        print(self.__address)
        print(self.__npwp)
        print(lines())
