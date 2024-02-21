class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"{song} ditambahkan ke playlist.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} dihapus dari playlist.")
        else:
            print(f"{song} tidak ditemukan dalam playlist.")

    def display_playlist(self):
        if self.songs:
            print("Daftar Lagu:")
            for index, song in enumerate(self.songs, start=1):
                print(f"{index}. {song}")
        else:
            print("Playlist kosong.")

    def save_playlist(self, file_name):
        with open(file_name, 'w') as file:
            for song in self.songs:
                file.write(song + '\n')
        print("Playlist disimpan.")

    def load_playlist(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.songs = [line.strip() for line in file]
            print("Playlist dimuat.")
        except FileNotFoundError:
            print("File playlist tidak ditemukan. Membuat playlist baru.")


def main():
    playlist = Playlist()
    playlist_file = "playlist.txt"
    playlist.load_playlist(playlist_file)

    while True:
        print("\nPilih operasi yang ingin Anda lakukan:")
        print("1. Tambah lagu ke playlist")
        print("2. Hapus lagu dari playlist")
        print("3. Tampilkan playlist")
        print("4. Simpan playlist")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == "1":
            song = input("Masukkan nama lagu: ")
            playlist.add_song(song)
        elif choice == "2":
            song = input("Masukkan nama lagu yang ingin dihapus: ")
            playlist.remove_song(song)
        elif choice == "3":
            playlist.display_playlist()
        elif choice == "4":
            playlist.save_playlist(playlist_file)
        elif choice == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()