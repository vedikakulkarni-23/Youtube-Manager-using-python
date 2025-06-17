
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_saver(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. ")

def add_video(videos):
    name = input("Name of video: ")
    time = input("time of video: ")
    videos.append({'name': name, 'time': time})
    save_data_saver(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("\n Youtube Manager ")
        print("\n1. List all Youtube Videos")
        print("\n2. Add Youtube Video")
        print("\n3. Update Youtube video details")
        print("\n4. Delete Youtube video")
        print("\n5. Exit")
        choice = input("Enter Your Choice")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("INVALID CHOICE")   
            
if __name__ == "__main__":
    main()