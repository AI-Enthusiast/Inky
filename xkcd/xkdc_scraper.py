from bs4 import BeautifulSoup
# import pandas as pd
import requests
import os

root = os.path.dirname(os.path.realpath("xkcd_prototyping.ipynb"))
storage = os.path.join(root, "comics")


def get_comic(comic_index):
    url = "https://xkcd.com/" + str(comic_index)
    raw = requests.get(url)
    soup = BeautifulSoup(raw.text, "html.parser")
    try:
        image_url = soup.find(id="comic").find("img")["src"]  # get the image url
    except AttributeError:
        return
    title = soup.find(id="ctitle").get_text()  # get the title
    # strip the title of any characters that can't be in a file name
    bad_strs = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']
    title = ''.join(list(filter(lambda x: x not in bad_strs, title)))
    transcript = soup.find(id="transcript").get_text()  # get the transcript

    # download the image
    image_url = "https:" + image_url
    image_data = requests.get(image_url).content
    save_path = os.path.join(storage, title + '.' + str(image_url.split('.')[-1]))
    with open(save_path, 'wb') as handler:  # save the image
        handler.write(image_data)
    # save the title and transcript and number in a csv
    # try:
    #     # read in the csv xkcd.csv
    #     old_xkcd = pd.read_csv(os.path.join(root, 'comics', 'xkcd.csv'))
    #     # combine the result with the old results from hit_urls
    #     result_df = pd.concat(
    #         [old_xkcd, pd.DataFrame([[comic_index, title, transcript]], columns=['index', 'title', 'transcript'])])
    #     # drop duplicates
    #     result_df = result_df.drop_duplicates(subset=['index', 'title', 'transcript'])
    #     # save the results
    #     result_df.to_csv(os.path.join(root, 'comics', 'xkcd.csv'), index=False)
    # except FileNotFoundError:
    #     pd.DataFrame([[comic_index, title, transcript]], columns=['index', 'title', 'transcript']).to_csv(
    #         os.path.join(root, 'comics', 'xkcd.csv'), index=False)


def get_current_comic():
    url = "https://xkcd.com/"
    raw = requests.get(url)
    soup = BeautifulSoup(raw.text, "html.parser")
    comic_index = int(soup.find(id="middleContainer").find("a")["href"].split("/")[1])
    # get the image url
    image_url = soup.find(id="comic").find("img")["src"]
    title = soup.find(id="ctitle").get_text()  # get the title
    # strip the title of any characters that can't be in a file name
    bad_strs = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']
    title = ''.join(list(filter(lambda x: x not in bad_strs, title)))
    transcript = soup.find(id="transcript").get_text()  # get the transcript
    # download the image
    image_url = "https:" + image_url
    image_data = requests.get(image_url).content
    save_path = os.path.join(storage, title + '.' + str(image_url.split('.')[-1]))
    with open(save_path, 'wb') as handler:  # save the image
        handler.write(image_data)
    # save the title and transcript and number in a csv
    # try:
    #     # read in the csv xkcd.csv
    #     old_xkcd = pd.read_csv(os.path.join(root, 'comics', 'xkcd.csv'))
    #     # combine the result with the old results from hit_urls
    #     result_df = pd.concat(
    #         [old_xkcd, pd.DataFrame([[comic_index, title, transcript]], columns=['index', 'title', 'transcript'])])
    #     # drop duplicates
    #     result_df = result_df.drop_duplicates(subset=['index', 'title', 'transcript'])
    #     # save the results
    #     result_df.to_csv(os.path.join(root, 'comics', 'xkcd.csv'), index=False)
    # except FileNotFoundError:
    #     pd.DataFrame([[comic_index, title, transcript]], columns=['index', 'title', 'transcript']).to_csv(
    #         os.path.join(root, 'comics', 'xkcd.csv'), index=False)

if __name__ == "__main__":
    # for i in tqdm.tqdm(range(210 + 193, 2861)):
    #     get_comic(i)
    get_current_comic()