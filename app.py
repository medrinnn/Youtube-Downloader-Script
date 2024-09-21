import os
import yt_dlp

def main():
    print("Welcome To The Youtube Downloader Script Made By medrinnn")
    
    # Default download folder
    videofolder = "./YDS Downloads"

    while True:
        print("\nOptions:")
        print("1 - Download YouTube Video")
        print("2 - Change Download Directory")
        print("3 - Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            ytlink = input("Enter Your YouTube Video Link: ").strip()

            # Validate the URL format
            if not ytlink.startswith("https://") and not ytlink.startswith("http://"):
                print("Please enter a valid YouTube URL starting with 'https://' or 'http://'.")
                continue
            
            # Download type selection
            download_type = input("Enter 1 for MP3 or 2 for MP4: ")

            if download_type == '2':
                # Fetch available resolutions
                with yt_dlp.YoutubeDL() as ydl:
                    info_dict = ydl.extract_info(ytlink, download=False)
                    formats = info_dict['formats']
                    resolutions = sorted(set(f['height'] for f in formats if f.get('height') is not None))

                print("Available video resolutions:")
                for res in resolutions:
                    print(f"- {res}p")

                resolution_choice = input("Choose the resolution (e.g., 144, 240, 360, etc.): ")

                # Validate resolution choice
                if resolution_choice.isdigit() and int(resolution_choice) in resolutions:
                    resolution = f"{resolution_choice}p"
                else:
                    print("Invalid resolution choice. Downloading the best available.")
                    resolution = 'bestvideo'

            # Download options
            ydl_opts = {
                'format': 'bestaudio/best' if download_type == '1' else f'bestvideo[height<={resolution_choice}]+bestaudio/best',
                'outtmpl': os.path.join(videofolder, '%(title)s.%(ext)s'),
            }

            # Download the video or audio
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([ytlink])
                print("Download completed!")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == '2':
            new_folder = input("Enter the new folder where you want to download videos: ").strip()
            if new_folder:
                videofolder = new_folder
                # Create the new directory if it doesn't exist
                if not os.path.exists(videofolder):
                    os.makedirs(videofolder)
                print(f"Download directory changed to: {videofolder}")
            else:
                print("No folder specified. Keeping the current folder.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

