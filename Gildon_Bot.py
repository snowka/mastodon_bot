# This program is indebted to this example: https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/
# For scheduling, I'm using this explanation of the Schedule library: https://schedule.readthedocs.io/en/stable/

from mastodon import Mastodon
from database import dict
import schedule
import time

authors_and_quotes = dict

# Insert the number of quotes in your database in the "range" below.
def post():
    """A version of the function to post to Mastodon for testing purposes only.

    The post() function gathers values from the dict of quotes and authors to generate the post. This version of the
    function is for testing purposes. The visibility parameter is set to "direct" so that only named accounts can see
    it; in this case, my own handle "@snowka@scholar.social" (just before this) is the only account that can see it.

    Parameters
    ----------
    visibility: str, optional
        This parameter selects who can view your post. "Direct" limits the post to mentioned users. "Private" only goes
        to followers. "Public" is viewable to all.

    sensitive: bool, optional
        Choosing "True" will provide a content warning for your post. "False" will not.

    spoiler_text: str, optional
        The string you pass in for this parameter will be shown as part of a content warning.
    """
    #Change the number in the range function below to match the number of posts in database.
    for postNum in range(16):
        if authors_and_quotes[postNum][3] == False:
            mastodon.status_post(authors_and_quotes[postNum][0] + " on " + authors_and_quotes[postNum][1]+": " +
                         authors_and_quotes[postNum][2] + " @snowka@scholar.social", sensitive=True, visibility="direct",
                         spoiler_text="Eighteenth-Century Literary Snark")
            # This update the quote to True--it has been posted.
            authors_and_quotes[postNum][3] = True
            return
        else:
            continue


# def post():
#     """Function for posting to Mastodon.
#
#     The post() function gathers values from the dict of quotes and authors to generate the post.
#
#     Parameters
#     ----------
#     visibility: str, optional
#         This parameter selects who can view your post. "Direct" limits the post to mentioned users. "Private" only
#         goes to followers. "Public" is viewable to all.
#
#     sensitive: bool, optional
#         Choosing "True" will provide a content warning for your post. "False" will not.
#
#     spoiler_text: str, optional
#         The string you pass in for this parameter will be shown as part of a content warning.
#     """
#
#     for postNum in range(5):
#         if authors_and_quotes[postNum][3] == False:
#             mastodon.status_post(authors_and_quotes[postNum][0] + " on " + authors_and_quotes[postNum][1] + ": " +
#                                  authors_and_quotes[postNum][2], sensitive=True, visibility="public",
#                                  spoiler_text="Eighteenth-Century Literary Snark")
#             # This update the quote to True--it has been posted.
#             authors_and_quotes[postNum][3] = True
#             return
#         else:
#             continue


# Connects to Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)

# For testing purposes -- posts frequently to see if everything is working
schedule.every(2).days.do(post)
# For posting on a regular schedule
# schedule.every(2).days.at("11:00").do(post)


while True:
    schedule.run_pending()
    time.sleep(1)

