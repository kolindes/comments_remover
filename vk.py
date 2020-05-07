try:
    from vk_api import VkApi, ApiError

except ImportError as err:
    raise err



class User:
    def __init__(self, login, password):

        try:
            print('VK Logging in...')
            self.vk = VkApi(login=login, password=password)
            self.vk.auth(token_only=True)
            self.api = self.vk.get_api()
            self.info = self._get_user_info()
            print('VK Successfully logged in.')

        except Exception as e:
            raise e

    def _get_user_info(self):
        return self.api.users.get()[0]

    def comment_info(self, source_id, comment_id):
        try:
            self.api.wall.getComment(source_id=source_id, comment_id=comment_id, extended=True)

        except ApiError as e:
            print("Couldn't get comment info: %s" % e)

    def remove_comment(self, source_id, comment_id):
        try:
            self.api.wall.deleteComment(owner_id=source_id, comment_id=comment_id)
            print('Comment removed.')
            return True

        except ApiError as e:
            print('Warning! Comment was not removed: %s | %s %s' % (e, source_id, comment_id))
            return False
