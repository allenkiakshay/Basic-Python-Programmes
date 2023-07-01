import scrapetube
import pandas as pd
 
channelid = "UCp5mvCwXR-drTRyzNUUjdZg"
list1 = []
url = "https://www.youtube.com/watch?v="
dataframe = pd.DataFrame(columns=["url"])
videos = scrapetube.get_channel(channelid)
for vid in videos:
    url1 = url+str(vid['videoId'])
    # print(url1)
    list1.append(url1)

dataframe['URL'] = list1
dataframe.to_excel("youtube_urls.xlsx")
print("finish")