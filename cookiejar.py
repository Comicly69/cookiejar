import os
import http.cookies

def get_cookies():
    cookie_dict = {}
    cookie_string = os.environ.get('HTTP_COOKIE')
    if cookie_string:
        cookies = http.cookies.SimpleCookie()
        cookies.load(cookie_string)
        for key, morsel in cookies.items():
            cookie_dict[key] = morsel.value
    return cookie_dict

def write_cookies_to_file(cookie_dict):
    file_path = os.path.join(os.path.expanduser('~'), 'cookies.txt')
    with open(file_path, 'w') as f:
        for key, value in cookie_dict.items():
            f.write(f'{key}: {value}\n') 

def main():
    cookie_dict = get_cookies()
    write_cookies_to_file(cookie_dict)

if __name__ == '__main__':
    main()
