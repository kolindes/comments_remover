import datetime

import vk
import comments


def main():
    login = input('login: ')
    password = input('password: ')
    user = vk.User(login, password)

    all_comments_ids = comments.collect_comments_ids()
    count_found = len(all_comments_ids)
    print('Comments found: %d' % count_found)
    print('Estimated time: %s' % str(datetime.timedelta(seconds=0.34 * count_found)))  # 0.34 - api requests per second

    comments_was_not_removed = []

    for i in all_comments_ids:
        src_id, comment_id = i[0], i[1]
        is_removed = user.remove_comment(src_id, comment_id)

        if is_removed is False:
            comments_was_not_removed.append('source_id: %s comment_id: %s' % (src_id, comment_id))

    with open('failed.txt', 'w+', encoding='utf-8') as failed_comments_file_txt:
        failed_comments_file_txt.write('\n'.join(comments_was_not_removed))

    count_failed = len(comments_was_not_removed)
    count_removed = count_found - count_failed

    print(45 * '_')
    print('Comments removed: %d' % count_removed)
    print('Comments failed: %d' % count_failed)
    print('\n', 'Comments that was not removed are saved in "failed.txt"')


if __name__ == '__main__':
    main()
