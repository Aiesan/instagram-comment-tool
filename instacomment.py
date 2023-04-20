import requests

def post_comment(post_id, comment_text, csrf_token, session_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-CSRFToken': csrf_token,
        'X-Instagram-AJAX': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': f'https://www.instagram.com/p/{post_id}/',
        'Cookie': f'sessionid={session_id};'
    }
    cookies = {
        'sessionid': session_id
    }
    data = {
        'comment_text': comment_text
    }
    response = requests.post(f'https://www.instagram.com/web/comments/{post_id}/add/', headers=headers, cookies=cookies, data=data)
    if response.status_code == 200:
        return True
    else:
        return False

# Customize the following variables:
post_id = 'POST_ID_HERE'   # Replace with the ID of the Instagram post you want to comment on
comment_text = 'COMMENT_TEXT_HERE'   # Replace with the text of the comment you want to post
csrf_token = 'YOUR_CSRF_TOKEN_HERE'   # Replace with your own CSRF token
session_id = 'YOUR_SESSION_ID_HERE'   # Replace with your own session ID

# Call the post_comment function to post the comment
result = post_comment(post_id, comment_text, csrf_token, session_id)

# Check the result to see if the comment was successfully posted
if result:
    print('Comment posted successfully!')
else:
    print('Failed to post comment.')
