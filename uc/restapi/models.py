# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    adminid = models.AutoField(db_column='adminId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chat(models.Model):
    chatid = models.BigAutoField(db_column='chatId', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    searchid = models.BigIntegerField(db_column='searchId')  # Field name made lowercase.
    chattext = models.TextField(db_column='chatText', blank=True, null=True)  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='deleteFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chat'


class Comments(models.Model):
    commentid = models.BigAutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    searchid = models.BigIntegerField(db_column='searchId')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    shortlistedid = models.BigIntegerField(db_column='shortlistedId')  # Field name made lowercase.
    roomtype = models.CharField(db_column='roomType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commenttext = models.TextField(db_column='commentText', blank=True, null=True)  # Field name made lowercase.
    filetype = models.CharField(db_column='fileType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commentfile = models.CharField(db_column='commentFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    video_thumbnail = models.CharField(max_length=255, blank=True, null=True)
    deleteflag = models.IntegerField(db_column='deleteFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comments'


class Commentsread(models.Model):
    readid = models.BigAutoField(db_column='readId', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    commentid = models.BigIntegerField(db_column='commentId')  # Field name made lowercase.
    shortlistedid = models.BigIntegerField(db_column='shortlistedId')  # Field name made lowercase.
    roomtype = models.CharField(db_column='roomType', max_length=255)  # Field name made lowercase.
    readflag = models.IntegerField(db_column='readFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commentsread'


class Commute(models.Model):
    commuteid = models.BigAutoField(db_column='commuteId', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    searchid = models.BigIntegerField(db_column='searchId')  # Field name made lowercase.
    commutename = models.CharField(db_column='commuteName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(max_length=255, blank=True, null=True)
    timeofcommuting = models.IntegerField(db_column='timeofCommuting', blank=True, null=True)  # Field name made lowercase.
    modeofcommute = models.CharField(db_column='modeOfCommute', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maxcommutetime = models.IntegerField(db_column='maxCommuteTime', blank=True, null=True)  # Field name made lowercase.
    destlatitude = models.CharField(db_column='destLatitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destlongitude = models.CharField(db_column='destLongitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primarycommute = models.IntegerField(db_column='primaryCommute')  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='deleteFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commute'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Properties(models.Model):
    id = models.BigAutoField(primary_key=True)
    propertyid = models.BigIntegerField(db_column='propertyId')  # Field name made lowercase.
    propertyname = models.CharField(db_column='propertyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    propertyurl = models.CharField(db_column='propertyUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commutetime = models.IntegerField(db_column='commuteTime', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    availabledate = models.DateField(db_column='availableDate', blank=True, null=True)  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='deleteFlag', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'properties'


class Rating(models.Model):
    ratingid = models.BigAutoField(db_column='ratingId', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    shortlistedid = models.BigIntegerField(db_column='shortlistedId')  # Field name made lowercase.
    searchid = models.BigIntegerField(db_column='searchId')  # Field name made lowercase.
    propertyname = models.CharField(db_column='propertyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ratecriteria1 = models.FloatField(db_column='rateCriteria1', blank=True, null=True)  # Field name made lowercase.
    ratecriteria2 = models.FloatField(db_column='rateCriteria2', blank=True, null=True)  # Field name made lowercase.
    ratecriteria3 = models.FloatField(db_column='rateCriteria3', blank=True, null=True)  # Field name made lowercase.
    average = models.FloatField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rating'


class Searchcriteria(models.Model):
    searchid = models.BigAutoField(db_column='searchId', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    searchname = models.CharField(db_column='searchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idealmovingdate = models.DateField(db_column='idealMovingDate', blank=True, null=True)  # Field name made lowercase.
    housetype = models.CharField(db_column='houseType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    minprice = models.BigIntegerField(db_column='minPrice', blank=True, null=True)  # Field name made lowercase.
    maxprice = models.BigIntegerField(db_column='maxPrice', blank=True, null=True)  # Field name made lowercase.
    minbedroom = models.CharField(db_column='minBedroom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maxbedroom = models.CharField(db_column='maxBedroom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commute = models.CharField(max_length=255, blank=True, null=True)
    criteria1 = models.TextField(blank=True, null=True)
    criteria2 = models.TextField(blank=True, null=True)
    criteria3 = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    proximity = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    likeflag = models.IntegerField(blank=True, null=True)
    avoid_proximity = models.CharField(max_length=255, blank=True, null=True)
    avoid_keywords = models.CharField(max_length=255, blank=True, null=True)
    avoid_area = models.CharField(max_length=255, blank=True, null=True)
    sherpainterest = models.IntegerField(db_column='sherpaInterest', blank=True, null=True)  # Field name made lowercase.
    travelapidata = models.TextField(db_column='travelApiData', blank=True, null=True)  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='deleteFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'searchcriteria'


class Shortlistedproperty(models.Model):
    shortlistedid = models.BigAutoField(db_column='shortlistedId', primary_key=True)  # Field name made lowercase.
    searchid = models.BigIntegerField(db_column='searchId')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    propertyid = models.BigIntegerField(db_column='propertyId')  # Field name made lowercase.
    propertyname = models.CharField(db_column='propertyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    propertyurl = models.CharField(db_column='propertyUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commutetime = models.IntegerField(db_column='commuteTime', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    availabledate = models.DateField(db_column='availableDate', blank=True, null=True)  # Field name made lowercase.
    avgpropertyrating = models.FloatField(db_column='avgPropertyRating', blank=True, null=True)  # Field name made lowercase.
    avgratecriteria1 = models.FloatField(db_column='avgRateCriteria1', blank=True, null=True)  # Field name made lowercase.
    avgratecriteria2 = models.FloatField(db_column='avgRateCriteria2', blank=True, null=True)  # Field name made lowercase.
    avgratecriteria3 = models.FloatField(db_column='avgRateCriteria3', blank=True, null=True)  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='deleteFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shortlistedproperty'


class Tribe(models.Model):
    inviteid = models.BigAutoField(db_column='inviteId', primary_key=True)  # Field name made lowercase.
    searchid = models.BigIntegerField(db_column='searchId')  # Field name made lowercase.
    fromuserid = models.BigIntegerField(db_column='fromuserId')  # Field name made lowercase.
    touserid = models.BigIntegerField(db_column='touserId', blank=True, null=True)  # Field name made lowercase.
    inviteemail = models.CharField(db_column='inviteEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    deleteflag = models.IntegerField(db_column='deleteFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tribe'


class Users(models.Model):
    userid = models.BigAutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    contactnumber = models.CharField(db_column='contactNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    workeducation = models.CharField(db_column='workEducation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255, blank=True, null=True)
    devicetoken = models.CharField(db_column='deviceToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='deviceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    facebookid = models.CharField(db_column='facebookId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=255, blank=True, null=True)
    tokenexpiry = models.BigIntegerField(db_column='tokenExpiry', blank=True, null=True)  # Field name made lowercase.
    refreshtoken = models.CharField(db_column='refreshToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refreshtokenexpiry = models.CharField(db_column='refreshTokenExpiry', max_length=20, blank=True, null=True)  # Field name made lowercase.
    forgottoken = models.CharField(db_column='forgotToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    forgottokenexpiry = models.CharField(db_column='forgotTokenExpiry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    deleteflag = models.IntegerField(db_column='deleteFlag', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='lastLogin', blank=True, null=True)  # Field name made lowercase.
    connectsherpaflag = models.IntegerField(db_column='connectSherpaFlag', blank=True, null=True)  # Field name made lowercase.
    testflag = models.CharField(db_column='testFlag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    sherpasignedup = models.DateTimeField(db_column='sherpaSignedup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

# Custom function in models

    # def get_my_password(self):
    #     return self.password

class Viewproperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    searchid = models.BigIntegerField(db_column='searchId')  # Field name made lowercase.
    propertyid = models.BigIntegerField(db_column='propertyId')  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='viewCount')  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='deleteFlag')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'viewproperties'
