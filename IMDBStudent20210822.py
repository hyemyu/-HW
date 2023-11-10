import sys

def count_genres(input_file, output_file):
    genre_count = {}


    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:

            parts = line.strip().split("::")
            if len(parts) >= 3:
                genres = parts[2].split('|')
                for genre in genres:
                    genre_count[genre] = genre_count.get(genre, 0) + 1


    with open(output_file, 'w', encoding='utf-8') as output:
        for genre, count in genre_count.items():
            output.write(f"{genre} {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("사용법: python IMDBStudent<학번>.py <입력파일> <출력파일>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    count_genres(input_file, output_file)

