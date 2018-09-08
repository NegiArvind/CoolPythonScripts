from pytube import YouTube
from datetime import datetime


def completionMessage(stream, fileHandle):
    print("Video Downloaded")


def downloadVideoWithSound(stringUrl, path):
    # youTubeVariable = YouTube("https://www.youtube.com/watch?v=aNEnzS_um9U")

    print("Fetching Data...")

    try:

        youTubeVariable = YouTube(stringUrl)
        # video=video.get("mp4","480")

        myTitle = youTubeVariable.title
        print(myTitle)  # title of you tube video
        # print(youTubeVariable.thumbnail_url)  # png image used on you tube video
        # print(youTubeVariable.streams.all())  # it will return all the streams available for this video
        # stream = youTubeVariable.streams.filter(res="480p").first()  # get that stream whose resolution is 480p
        # print("first stream", stream)

        stream = youTubeVariable.streams.first()

        # stream.download('/home/arvind/Downloads/Video',myTitle+" "+datetime.now().ctime())  # downloading video and saved into specific folder

        print("Downloading...")
        stream.download(path,
                        myTitle + " " + datetime.now().ctime())  # downloading video and saved into specific folder
        # second argument is the filename or video name
        youTubeVariable.register_on_complete_callback(
            completionMessage(stream, None))  # Whenever video will be completed
        # then this method will invoke

        # some of the stream contains only audio or only video .We can also download them

    except:
        print("Please enter valid url")


def downloadOnlyAudio(url, path):
    print("Fetching Data...")

    try:
        youTubeVariable = YouTube(url)
        # Below code is used to download only audio

        myTitle = youTubeVariable.title
        print(myTitle)
        stream1 = youTubeVariable.streams.filter(only_audio=True).first()
        # print(stream1)
        # stream1.download('/home/arvind/Downloads/Video')  # downloading only audio of you tube video and
        # #  then save into specific folder
        #
        print("Downloading...")
        stream1.download(path, myTitle + " " + datetime.now().ctime())  # downloading only audio of you tube video and
        #  then save into specific folder
        youTubeVariable.register_on_complete_callback(completionMessage(stream1, None))

    except:
        print("Please enter a valid url")


url = str(input("Enter the you tube url\n"))
path = input("Enter the path where you want to save this video\n")
downloadVideoWithSound(url, path)
# downloadOnlyAudio(url,path)
