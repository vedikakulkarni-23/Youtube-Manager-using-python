import sqlite3

con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def Add_videos(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUE (?, ?)", (name, time))
    cursor.commit()

def Update_videos(vid_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, vid_id))
    cursor.commit()

def Delete_videos(vid_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (vid_id,))
    cursor.commit()



def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            Add_videos(name, time)

        elif choice == '3':
            vid_id = input("Enter video ID: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            Update_videos(vid_id, name, time)

        elif choice == '4':
            vid_id = input("Enter video ID: ")
            Delete_videos(vid_id)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid Choice")

    con.close()

if __name__ == "main":
    main()