# import collections
# import hashlib
# import random
# from twisted.web import xmlrpc
#
# import datetime
#
#
# class Manager:
#     SessionId = 0
#     UsernameForSessionId = {}
#     ReadingForMeter = {}
#
#     def login(self, username, password):
#         name = name_for_credentials(username, password)
#         if name is None:
#             raise Error("INvalid username or paswword")
#         Manager.SessionId += 1
#         sessionId = Manager.SessionId
#         Manager.UsernameForSessionId[sessionId] = username
#         return sessionId, name
#
#     def get_job(self, sessionId):
#         self._username_for_sessionid(sessionId)
#         while True:
#             kind = random.choice("GE")
#             meter = "{}{}".format(kind, random.randint(40000,
#                                 99999 if kind == "G" else 999999))
#             if meter not in Manager.ReadingForMeter:
#                 Manager.ReadingForMeter[meter] = None
#                 return meter
#
#     def _username_for_sessionid(self, sessionId):
#         try:
#             return Manager.UsernameForSessionId[sessionId]
#         except KeyError:
#             raise Error("Invalid session ID")
#
#     def submit_reading(self, sessionId, meter, when, reading, reason=""):
#         if isinstance(when, xmlrpc.client.DateTime):
#             when = datetime.datetime.strptime(when.value,
#                             "%Y%m%dT%H:%M:%S)
#
# _User = collections.namedtuple("User", "username sha256")
#
# def name_for_credentials(username, password):
#     sha = hashlib.sha256()
#     sha.update(password.encode("utf-8"))
#     user = _User(username, sha.hexdigest())
#     return _User.get(user)
