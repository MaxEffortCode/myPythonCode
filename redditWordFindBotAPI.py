"""
Praw API copyright: 

Copyright (c) 2016, Bryce Boe
All rights reserved.

My edition of this code:

Copyright 2019 Maxwell Bultman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""


import praw
import json
import datetime
import time
import operator

#bluefang9999
wordToFind = None
user = None
userToSearch = None
commentAuthor = ""
commentiD = ""
i = 0
i2 = 0
reply = ""
commentIDArray = []
commentStringArray = []
commentWordArray = []
UsedUserList = []
subRedditToSearchIn = ""
reddit = praw.Reddit(client_id='60pukh6GoGiSOQ',
                     client_secret='GwNICSY3vuoSBfSPlS087fT1om0',
                     user_agent='test',
                     username='N-Word-Alert',
                     password='maxandeva')

"""reddit = praw.Reddit(client_id='tb6ec6rnQLUJ1A',
                     client_secret='IRziIsJopbFkum38tjiQ9cybVNQ',
                     user_agent='test',
                     username='geekygamer1134',
                     password='Thatnewkid!234')"""

print(f"we are oneline = {(operator.__not__(reddit.read_only))}")  # Output: False
f = open('userComments.txt', 'w') #clears the file


def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False

def replyToCall():
	word = ""
	for mention in reddit.inbox.mentions(limit=25):
		comment_id = mention.id
		commentAuthor = str(mention.author)
		messageArray = mention.body.split()
		if check_if_string_in_file("inbox.txt", comment_id) == False:
			print(comment_id)
			inboxIdData = open("inbox.txt","a")
			try:
				userToFind = messageArray[1]
				wordToFind = messageArray[2]
				inboxIdData.write(f"{str(comment_id)}: {mention.body}\n")
				getRedditorComments(userToFind)
				searchUserComments(wordToFind)
				print(f"{commentAuthor} is requesting to search user: {userToFind} for the word: {wordToFind}\n")
				print(reply)
				replyToComment(comment_id)
			except IndexError:
				inboxIdData.write(f"{str(comment_id)}: {mention.body}\n")
				pass



def summonBot(subreddit):
	global userToSearch
	global commentAuthor
	global wordToFind
	global commentiD
	name = "N-Word-Alert"
	while(True):
		replyToCall()
		subReddit = reddit.subreddit(subreddit)
		for submission in subReddit.new(limit = 10):
			submission.comments.replace_more(limit=0)
			for comment in submission.comments:
				commentiD = comment.id
				if name.lower() in comment.body:
					if check_if_string_in_file("usedCommentFile.txt", commentiD) == False:#makes sure we havnt already replied to comment
						commentFoundArray = comment.body.split() #turns commentFoundArray into an array of the found comment
						print(20*"#")
						try:
							commentIdData = open("usedCommentFile.txt","a")
							commentIdData.write(f"commentID: {comment.id} \n    User: {str(comment.author)} \n    Comment: {comment.body}\n\n")
							userToSearch = commentFoundArray[1] #grabs the second word int he array
							wordToFind = commentFoundArray[2]
							commentAuthor = comment.author #gets the user instance of the comment containing geekygamer1134
							print(f"{commentAuthor.name} is requesting to search user: {userToSearch} for the word: {wordToFind}")
							return userToSearch #breaks te loop
						except IndexError:
							pass
	time.sleep(.4)
		



def deEmojify(inputString): #CMD does not like Emojis, and they are not relevent to what we are doing
    return inputString.encode('ascii', 'ignore').decode('ascii')

def getRedditorComments(user1): #need to apss the user(str), charLimit(int), leng(int)
	global user
	global userToSearch
	user = reddit.redditor(user1)
	for comment in user.comments.new(limit = None):
		deEmojiComment = deEmojify(comment.body)
		deEmojiCommentSplit = deEmojiComment.split()
		userComments = open("userComments.txt","a+") #same folder as program, and is read and write, hanlde is places at the end
		userComments.write(f"{user.name} said : {str(deEmojiCommentSplit)} \n\n ")
	return user
	time.sleep(.05)

def searchUserComments(word):
	global wordToFind
	global user
	global i2
	global reply
	word = word
	with open('userComments.txt') as f:
		for line in f:
			i2 += line.count(word)
	reply = (f"/u/{user.name} has: {i2} comments that contain the word: '{word}' \n\n*to request bot --> '/u/N-Word-Alert' 'user to search for' 'word to search for'* \n\n\n\n ^(If you have any complaints about this bot, please message: u/geekygamer134) \n\n")
	f = open('userComments.txt', 'w')
	i2 = 0


def replyToComment(commentID):
	global reply
	comment = reddit.comment(commentID)
	print(reply)
	comment.reply(reply)

def putCommentInlist(subreddit, limit):
	subreddit = reddit.subreddit(subreddit)
	for submission in subreddit.new(limit = limit): #gets the first 10 submissions in the subreddit
		submission.comments.replace_more(limit=0) #loads the "more" on each comment page
		commentIDArray.append(submission.comments.list()) #adds the comment ID to the array
		for comment in submission.comments: #will go through each comment ID and pull the comment string
			print(comment.body)
			commentStringArray.append(comment.body)

	print(f"This is the title: {submission.title}") #prints the submission title
	print(f"added these comment IDs: {commentIDArray}") #prints out all the comment ids
	print(f"added these Comment Bodies: {commentStringArray}") #prints out string IDs
	time.sleep(.05) #so reddit doesnt limit us

def searchWordInComments():
	global i
	word = input("Tell me the word to find: ") #request user to tell us the input
	print(f"Looking for the Word: {word}") #tells teh word to find
	for comment in commentStringArray:
		tempArray = comment.split() #splits the commments into words
		for tempWord in tempArray: #needed to break down the array into individual parts
			commentWordArray.append(tempWord)
		tempArray.clear()
	print(f"This is the comment word array: {commentWordArray}")
	try:
		if commentWordArray.index(word) >= 0: #if it finds the word in the index, it will equal its location in the index
			i+=1
	except ValueError:
		print("none Found")
	commentWordArray.clear()
	commentStringArray.clear()
	commentIDArray.clear()
	print(f"{word} found {i}")



while(True):
	bot = summonBot("test")
	getRedditorComments(userToSearch)
	searchUserComments(wordToFind)
	replyToComment(commentiD)


	
